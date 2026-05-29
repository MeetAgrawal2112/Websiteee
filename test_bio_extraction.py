import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

urls = [
    "https://www.iiitp.ac.in/page/dr-chandrakant-narayan-guled",
    "https://www.iiitp.ac.in/page/dr-sonam-maurya",
    "https://www.iiitp.ac.in/page/dr-nagendra-kushwaha"
]

for url in urls:
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    print(f"\n--- {url} ---")
    bio = soup.find('div', class_='faculty-bio')
    if bio:
        print("Found faculty-bio, length:", len(bio.text))
        # print excerpt
        print(bio.text.strip()[:100])
    else:
        print("No faculty-bio found")
        # Try to find node__content
        nc = soup.find('div', class_='node__content')
        if nc:
            print("Found node__content instead, length:", len(nc.text))
