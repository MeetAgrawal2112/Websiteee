import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

region = soup.find('div', class_='region-content')
if region:
    # Print the direct children of region-content
    for i, child in enumerate(region.find_all(recursive=False)):
        print(f"Region Child {i}: {child.name} - classes: {child.get('class')} - Length: {len(child.text)}")
