import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

content_root = soup.find('div', class_='node__content')

# Remove faculty-main
fm = content_root.find('div', class_='faculty-main')
if fm: fm.decompose()

# Remove link divs
for cls in ['google-scholar', 'orcid', 'scopus', 'resume']:
    link = content_root.find('div', class_=cls)
    if link: link.decompose()

bio_html = ""
for tag in content_root.find_all(['p', 'ul', 'ol', 'table']):
    # Skip breadcrumbs or nav
    if tag.find_parent('nav') or tag.find_parent(class_='breadcrumb'):
        continue
    
    if not tag.text.strip():
        continue
        
    if tag.name == 'p' and 'Biography' in tag.text.strip() and len(tag.text.strip()) < 15:
        continue
        
    # Clean up attributes
    for child in tag.find_all(True):
        child.attrs = {k: v for k, v in child.attrs.items() if k not in ['style', 'class', 'id']}
    tag.attrs = {k: v for k, v in tag.attrs.items() if k not in ['style', 'class', 'id']}
    
    bio_html += str(tag) + "\n"

print(bio_html)
