import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

region = soup.find('div', class_='region-content')
print(region.text if region else "No region-content found")
