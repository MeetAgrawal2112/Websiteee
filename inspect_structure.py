import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-bhupendra-singh"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

node_content = soup.find('div', class_='node__content')
if node_content:
    # let's look for the main text container
    inner = node_content.find('div', class_='content_layout') or node_content
    print("Found content length:", len(inner.text))
    # print the first few tags inside it to understand the structure
    for child in inner.find_all(['h2', 'h3', 'p', 'div', 'ul'], recursive=False)[:10]:
        print(child.name, child.get('class'))
else:
    print("node__content not found")
