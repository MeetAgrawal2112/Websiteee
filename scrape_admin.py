import os
import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings()

urls = {
    "Chairperson": ("admin_chairperson.html", "https://www.iiitp.ac.in/page/chairperson"),
    "Director": ("admin_director.html", "https://www.iiitp.ac.in/page/director"),
    "Registrar": ("admin_registrar.html", "https://www.iiitp.ac.in/page/registrar"),
    "Board of Governors": ("admin_board-of-governors.html", "https://www.iiitp.ac.in/page/board-governors"),
    "Finance Committee": ("admin_finance-committee.html", "https://www.iiitp.ac.in/page/finance-committee"),
    "Building and Works Committee": ("admin_building-and-works-committee.html", "https://www.iiitp.ac.in/page/building-and-works-committee"),
    "Senate": ("admin_senate.html", "https://www.iiitp.ac.in/page/senate"),
    "Board of Studies (CSE)": ("admin_board-of-studies-cse.html", "https://www.iiitp.ac.in/page/board-studies-cse"),
    "Board of Studies (ECE)": ("admin_board-of-studies-ece.html", "https://www.iiitp.ac.in/page/board-studies-ece"),
    "Board of Studies (AS&H)": ("admin_board-of-studies-ash.html", "https://www.iiitp.ac.in/page/board-studies-ash")
}

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

    for name, (filename, url) in urls.items():
        print(f"Processing {name} - {url}")
        try:
            res = requests.get(url, verify=False, timeout=15)
            res.raise_for_status()
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
            continue
            
        soup = BeautifulSoup(res.content, 'html.parser')
        content_root = soup.find('div', class_='node__content')
        
        if not content_root:
            print(f"Could not find node__content in {url}")
            continue

        # Fix image paths and links
        for img in content_root.find_all('img'):
            src = img.get('src')
            if src and src.startswith('/'):
                img['src'] = 'https://www.iiitp.ac.in' + src

        for a in content_root.find_all('a'):
            href = a.get('href')
            if href and href.startswith('/'):
                a['href'] = 'https://www.iiitp.ac.in' + href
                
        # Remove any unwanted empty elements or scripts if needed
        # Mostly just take the inner HTML
        inner_html = content_root.decode_contents()

        page_html = header
        page_html += f'<div class="page-content">\n'
        page_html += f'<div class="admin-page-container">\n'
        page_html += f'<h1>{name}</h1>\n'
        page_html += inner_html
        page_html += f'\n</div>\n</div>\n'
        page_html += footer

        # Since we copied header from faculty.html, we need to update the title
        page_html = re.sub(r'<title>.*?</title>', f'<title>{name} | IIITP Pune</title>', page_html)

        # Update the active class in nav
        page_html = page_html.replace('class="active" href="faculty.html"', 'href="faculty.html"')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
    print("Done generating administration pages.")

if __name__ == '__main__':
    main()
