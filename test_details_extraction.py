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
    faculty_main = soup.find('div', class_='faculty-main')
    if faculty_main:
        info_divs = faculty_main.find_all('div', recursive=False)
        if info_divs:
            info_div = info_divs[-1]
            for div in info_div.find_all('div', recursive=False):
                print(div.get_text(strip=True))
