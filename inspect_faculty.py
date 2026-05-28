import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-bhupendra-singh"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

content = soup.find('div', class_='region-content')
if content:
    print(content.prettify()[:2000])
else:
    print("Content not found")
