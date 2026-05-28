import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sanjeev-sharma"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

region = soup.find('div', class_='region-content')
if region:
    # Let's count direct children of faculty-profile
    fp = region.find('div', class_='faculty-profile')
    if fp:
        print("faculty-profile children count:", len(fp.find_all('div', recursive=False)))
        for i, child in enumerate(fp.find_all('div', recursive=False)):
            print(f"Child {i}: length {len(child.text)}")
    
    # Are there other things outside faculty-profile but inside node__content?
    node = region.find('div', class_='node__content')
    if node:
        print("\nnode__content children count:", len(node.find_all('div', recursive=False)))
        for i, child in enumerate(node.find_all('div', recursive=False)):
            print(f"Node Child {i}: {child.get('class')}")
            
    print("\nTotal text length in node__content:", len(node.text))
    print("Total text length in faculty-profile:", len(fp.text) if fp else 0)
