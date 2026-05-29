import os
import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings()

def get_all_page_urls():
    print("Fetching main page to discover links...")
    try:
        res = requests.get('https://www.iiitp.ac.in', verify=False, timeout=15)
        res.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch main site: {e}")
        return []
    
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', href=True)
    menu_links = set([a['href'] for a in links if a['href'].startswith('/page/')])
    return list(menu_links)

def main():
    with open('faculty.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split to get header and footer
    page_content_start = content.find('<div class="page-content')
    if page_content_start == -1:
        print("Could not find page-content")
        return
    
    header = content[:page_content_start]
    
    footer_start = content.find('<!-- Footer -->')
    if footer_start == -1:
        # fallback for footer
        footer_start = content.rfind('<footer')
        if footer_start == -1:
            print("Could not find footer")
            return
            
    footer = content[footer_start:]

    admin_styles = """
    <style>
    .page-content {
        padding: 40px 22px;
        max-width: 1100px;
        margin: 0 auto;
    }
    .admin-page-container {
        font-family: 'Montserrat', sans-serif;
        background: #fff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-top: 5px solid #174873;
        margin-bottom: 40px;
    }
    .admin-page-container h2, .admin-page-container h3, .admin-page-container h1 {
        color: #174873;
        font-weight: 700;
        margin-bottom: 25px;
    }
    .admin-page-container p {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #444;
        margin-bottom: 20px;
    }
    .admin-page-container img {
        max-width: 100%;
        height: auto;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .admin-page-container table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 30px;
        font-size: 1rem;
    }
    .admin-page-container th, .admin-page-container td {
        padding: 15px;
        border: 1px solid #e0e0e0;
        text-align: left;
    }
    .admin-page-container th {
        background-color: #f4f6fb;
        color: #174873;
        font-weight: 700;
    }
    .admin-page-container tr:nth-child(even) {
        background-color: #fafafa;
    }
    .admin-page-container tr:hover {
        background-color: #f1f1f1;
    }
    .admin-page-container ul, .admin-page-container ol {
        margin-bottom: 20px;
        padding-left: 20px;
    }
    .admin-page-container li {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #444;
        margin-bottom: 10px;
    }
    </style>
    """
    
    header = header.replace('</head>', admin_styles + '\n</head>')

    urls_to_scrape = get_all_page_urls()
    
    # Also let's check for links inside those pages to discover more?
    # No, just the ones in the main nav / main page is a good start.
    print(f"Found {len(urls_to_scrape)} pages to scrape.")

    for path in urls_to_scrape:
        url = 'https://www.iiitp.ac.in' + path
        slug = path.replace('/page/', '')
        
        # Check if we already have it mapped (like admin pages)
        # We will just generate page_<slug>.html for all of them
        filename = f'page_{slug}.html'
        
        print(f"Processing {url} -> {filename}")
        try:
            res = requests.get(url, verify=False, timeout=15)
            res.raise_for_status()
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            continue
            
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # find the title
        title_tag = soup.find('h1', class_='page-header')
        if title_tag:
            page_title = title_tag.get_text(strip=True)
        else:
            page_title = slug.replace('-', ' ').title()

        content_root = soup.find('div', class_='node__content')
        
        if not content_root:
            # Let's try region-content if node__content is not found
            content_root = soup.find('div', class_='region-content')
            if not content_root:
                print(f"Could not find node__content or region-content in {url}")
                continue

        # Fix image paths and links
        for img in content_root.find_all('img'):
            src = img.get('src')
            if src and src.startswith('/'):
                img['src'] = 'https://www.iiitp.ac.in' + src

        for a in content_root.find_all('a'):
            href = a.get('href')
            if href and href.startswith('/'):
                if href.startswith('/page/'):
                    new_slug = href.replace('/page/', '')
                    a['href'] = f'page_{new_slug}.html'
                else:
                    a['href'] = 'https://www.iiitp.ac.in' + href
                
        # Remove any unwanted empty elements or scripts if needed
        # Mostly just take the inner HTML
        inner_html = content_root.decode_contents()

        page_html = header
        page_html += f'<div class="page-content">\n'
        page_html += f'<div class="admin-page-container">\n'
        page_html += f'<h1>{page_title}</h1>\n'
        page_html += inner_html
        page_html += f'\n</div>\n</div>\n'
        page_html += footer

        # Since we copied header from faculty.html, we need to update the title
        page_html = re.sub(r'<title>.*?</title>', f'<title>{page_title} | IIITP Pune</title>', page_html)

        # Update the active class in nav
        page_html = page_html.replace('class="active" href="faculty.html"', 'href="faculty.html"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    print("Done generating pages.")

if __name__ == '__main__':
    main()
