import os
import requests
from bs4 import BeautifulSoup
import urllib3

def main():
    urllib3.disable_warnings()

    with open('faculty.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split to get header and footer
    page_content_start = content.find('<div class="page-content">')
    if page_content_start == -1:
        print("Could not find page-content")
        return
    
    header = content[:page_content_start]
    
    footer_start = content.find('<!-- Footer -->')
    if footer_start == -1:
        print("Could not find footer")
        return
        
    footer = content[footer_start:]
    
    soup = BeautifulSoup(content, 'html.parser')
    
    cards = soup.find_all('div', class_='card')
    print(f"Found {len(cards)} cards")
    
    premium_styles = """
    <style>
    .page-content {
        padding: 40px 22px;
        max-width: 1100px;
        margin: 0 auto;
    }
    .premium-profile-page {
        font-family: 'Montserrat', sans-serif;
    }
    .profile-header-card {
        display: flex;
        gap: 40px;
        align-items: flex-start;
        background: #fff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-top: 5px solid #174873;
        margin-bottom: 40px;
    }
    .profile-image-container img {
        width: 250px;
        height: 250px;
        object-fit: cover;
        border-radius: 50%;
        border: 5px solid #f4f6fb;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .profile-info-container {
        flex: 1;
    }
    .profile-info-container h1 {
        color: #174873;
        font-weight: 700;
        margin-bottom: 25px;
        font-size: 2.2rem;
    }
    .profile-details-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .profile-details-list li {
        font-size: 1.05rem;
        color: #444;
        margin-bottom: 15px;
        line-height: 1.6;
        position: relative;
        padding-left: 30px;
    }
    .profile-details-list li::before {
        content: "\\f058"; /* Check circle */
        font-family: 'Font Awesome 5 Free';
        font-weight: 900;
        position: absolute;
        left: 0;
        top: 2px;
        color: #e85d04;
        font-size: 1.1rem;
    }
    .profile-details-list li strong {
        color: #174873;
        font-weight: 600;
        display: inline-block;
        min-width: 140px;
    }
    .profile-details-list a {
        color: #e85d04;
        text-decoration: none;
        word-break: break-all;
    }
    .profile-details-list a:hover {
        text-decoration: underline;
    }
    
    .profile-body-card {
        background: #fff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        margin-bottom: 50px;
    }
    .profile-body-card h2 {
        color: #174873;
        border-bottom: 2px solid #f4f6fb;
        padding-bottom: 15px;
        margin-bottom: 25px;
        margin-top: 35px;
        font-weight: 700;
        font-size: 1.6rem;
    }
    .profile-body-card h2:first-child {
        margin-top: 0;
    }
    .profile-body-card h2 i {
        color: #e85d04;
        margin-right: 10px;
    }
    .biography-text {
        font-size: 1.05rem;
        line-height: 1.8;
        color: #444;
    }
    .biography-text p {
        margin-bottom: 20px;
    }
    
    .profile-links-list {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    .profile-links-list li {
        background: #f4f6fb;
        padding: 15px 20px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        border-left: 4px solid #174873;
        transition: transform 0.3s;
    }
    .profile-links-list li:hover {
        transform: translateX(5px);
        border-left-color: #e85d04;
    }
    .profile-links-list li i {
        font-size: 1.5rem;
        color: #174873;
        margin-right: 20px;
        width: 30px;
        text-align: center;
    }
    .profile-links-list li .link-label {
        font-weight: 600;
        color: #333;
        font-size: 1.1rem;
        width: 150px;
    }
    .profile-links-list li a {
        color: #e85d04;
        text-decoration: none;
        font-weight: 500;
        word-break: break-all;
    }
    .profile-links-list li a:hover {
        text-decoration: underline;
    }

    @media(max-width: 768px) {
        .profile-header-card {
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .profile-details-list li {
            text-align: left;
        }
        .profile-links-list li {
            flex-direction: column;
            text-align: center;
            align-items: center;
        }
        .profile-links-list li i {
            margin-right: 0;
            margin-bottom: 10px;
        }
        .profile-links-list li .link-label {
            width: auto;
            margin-bottom: 10px;
        }
    }
    </style>
    """
    
    modified = False

    for card in cards:
        a_tags = card.find_all('a')
        if not a_tags: continue
        
        # Get LOCAL data to guarantee 100% accurate Name and Image
        img_tag_local = card.find('img')
        local_img_src = img_tag_local.get('src') if img_tag_local else ""
        if local_img_src and local_img_src.startswith('/'):
            local_img_src = "https://www.iiitp.ac.in" + local_img_src
            
        h3_tag_local = card.find('h3')
        local_name = h3_tag_local.text.strip() if h3_tag_local else "Faculty Member"
        
        profile_url = None
        for a in a_tags:
            href = a.get('href')
            if href and ('/page/' in href or 'profile_' in href) and (href.startswith('http') or href.endswith('.html')):
                if href.startswith('profile_'):
                    slug = href.replace('profile_', '').replace('.html', '')
                    profile_url = f"https://www.iiitp.ac.in/page/{slug}"
                else:
                    profile_url = href
                break
                
        if not profile_url:
            continue
            
        print(f"Processing {local_name} - {profile_url}")
        try:
            res = requests.get(profile_url, verify=False, timeout=15)
            res.raise_for_status()
        except Exception as e:
            print(f"Failed to fetch {profile_url}: {e}")
            continue
            
        remote_soup = BeautifulSoup(res.content, 'html.parser')
        
        # WE MUST USE node__content AS ROOT, NOT faculty-profile! 
        # Because in some pages like Dr. Sonam Maurya, the bio is OUTSIDE the faculty-profile div.
        content_root = remote_soup.find('div', class_='node__content')
        if not content_root:
            # Fallback to region-content if node__content is somehow missing
            content_root = remote_soup.find('div', class_='region-content')
            
        if not content_root:
            print(f"Could not find root content container in {profile_url}")
            continue
            
        # Extractor Phase - 100% Structural Agnostic
        try:
            img_src = local_img_src
            name = local_name
            
            # Remove any remote images since we have the local one
            for img in content_root.find_all('img'):
                img.decompose()
            
            # 2. Details
            faculty_main = content_root.find('div', class_='faculty-main')
            details_html = ""
            
            if faculty_main:
                # Remove headings as we already have the local name
                for heading in faculty_main.find_all(['h1', 'h2', 'h3']):
                    heading.decompose()
                title = faculty_main.find(class_='faculty-left-title')
                if title: title.decompose()
                    
                faculty_right = faculty_main.find('div', class_='faculty-right')
                if faculty_right:
                    container_for_details = faculty_right
                else:
                    info_divs = faculty_main.find_all('div', recursive=False)
                    container_for_details = info_divs[-1] if info_divs else faculty_main
                    
                raw_texts = []
                for elem in container_for_details.children:
                    if elem.name in ['p', 'div'] and elem.get('class') != ['faculty-left-title']:
                        for br in elem.find_all('br'):
                            br.replace_with('\n')
                        text = elem.get_text().strip()
                        if text:
                            raw_texts.extend([t.strip() for t in text.split('\n') if t.strip()])
                
                for text in raw_texts:
                    if not text: continue
                    text = text.replace('\xa0', ' ')
                    if ':' in text:
                        parts = text.split(':', 1)
                        details_html += f"<li><strong>{parts[0].strip()}:</strong> {parts[1].strip()}</li>\n"
                    else:
                        if text.lower().startswith("designation"):
                            details_html += f"<li><strong>Designation:</strong> {text[11:].strip()}</li>\n"
                        elif text.lower().startswith("email"):
                            details_html += f"<li><strong>Email:</strong> {text[5:].strip()}</li>\n"
                        elif text.lower().startswith("phone"):
                            details_html += f"<li><strong>Phone:</strong> {text[5:].strip()}</li>\n"
                        else:
                            # It might be a continuation of education or a bullet point
                            details_html += f"<li>{text}</li>\n"
                            
                # Remove faculty_main from DOM so we can extract biography from the rest
                faculty_main.decompose()

            # 3. Links
            links_html = ""
            def extract_link(class_name, icon_html, label):
                nonlocal links_html
                container = content_root.find('div', class_=class_name)
                if container:
                    a_tag = container.find('a')
                    if a_tag and a_tag.get('href'):
                        href = a_tag.get('href')
                        links_html += f'<li>{icon_html} <span class="link-label">{label}:</span> <a href="{href}" target="_blank">{href}</a></li>\n'
                    container.decompose()

            extract_link('google-scholar', '<i class="fab fa-google"></i>', 'Google Scholar')
            extract_link('orcid', '<i class="fab fa-orcid"></i>', 'ORCID')
            extract_link('scopus', '<i class="fas fa-book"></i>', 'Scopus')
            extract_link('resume', '<i class="fas fa-file-pdf"></i>', 'Resume')

            # 4. Biography
            # Remove hidden elements
            for hidden in content_root.find_all(class_='hidden'):
                hidden.decompose()
                
            # Remove empty paragraphs and H3 headers like "Biography"
            for h3 in content_root.find_all('h3'):
                if 'Biography' in h3.text or not h3.text.strip():
                    h3.decompose()
                    
            for p in content_root.find_all('p'):
                if not p.text.strip():
                    p.decompose()
                else:
                    p.attrs = {key: value for key, value in p.attrs.items() if key != 'style'}
                    
            faculty_bio = content_root.find('div', class_='faculty-bio')
            if faculty_bio:
                biography_html = faculty_bio.decode_contents().strip()
            else:
                biography_html = content_root.decode_contents().strip()

        except Exception as e:
            print(f"Extraction error on {profile_url}: {e}")
            continue
            
        # Builder Phase
        slug = profile_url.rstrip('/').split('/')[-1]
        local_filename = f"profile_{slug}.html"
        
        new_page_html = header.replace('</head>', premium_styles + '\n</head>')
        new_page_html += f'<div class="page-content premium-profile-page">\n'
        
        new_page_html += f'''
        <div class="profile-header-card">
            <div class="profile-image-container">
                <img src="{img_src}" alt="{name}">
            </div>
            <div class="profile-info-container">
                <h1>{name}</h1>
                <ul class="profile-details-list">
                    {details_html}
                </ul>
            </div>
        </div>
        
        <div class="profile-body-card">
        '''
        
        if biography_html.strip() and biography_html.strip() != '<div></div>':
            new_page_html += f'''
            <h2><i class="fas fa-user-tie"></i> Biography & Research</h2>
            <div class="biography-text">
                {biography_html}
            </div>
            '''
            
        if links_html.strip():
            new_page_html += f'''
            <h2><i class="fas fa-link"></i> Academic Profiles & Links</h2>
            <ul class="profile-links-list">
                {links_html}
            </ul>
            '''
            
        new_page_html += f'''
        </div>
        </div>
        '''
        
        new_page_html += footer
        
        with open(local_filename, 'w', encoding='utf-8') as pf:
            pf.write(new_page_html)
            
        # Update the links in the card
        for a in a_tags:
            href = a.get('href')
            if href == profile_url or href == local_filename:
                a['href'] = local_filename
                modified = True
                
    if modified:
        with open('faculty.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print("Updated faculty.html with local links.")

if __name__ == '__main__':
    main()
