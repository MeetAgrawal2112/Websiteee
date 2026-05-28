import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

article = soup.find('article')
if article:
    content = article.find('div', class_='node__content')
    if content:
        for i, child in enumerate(content.find_all(recursive=False)):
            print(f"Content Child {i}: {child.name} - classes: {child.get('class')} - Length: {len(child.text)}")
