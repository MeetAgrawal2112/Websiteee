import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.iiitp.ac.in/page/dr-sanjeev-sharma",
    "https://www.iiitp.ac.in/page/dr-habila-basumatary",
    "https://www.iiitp.ac.in/page/dr-mohammad-akhlaqur-rahman"
]

for url in urls:
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    fp = soup.find('div', class_='faculty-profile')
    if fp:
        print(f"Found faculty-profile for {url}")
    else:
        print(f"MISSING faculty-profile for {url}")
