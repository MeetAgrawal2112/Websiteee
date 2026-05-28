import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

fp = soup.find('div', class_='faculty-profile')
if fp:
    parent = fp.parent
    for i, child in enumerate(parent.find_all(recursive=False)):
        print(f"Parent Child {i}: {child.name} - classes: {child.get('class')} - text length: {len(child.text)}")
