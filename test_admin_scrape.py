import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

urls = {
    "Chairperson": "https://www.iiitp.ac.in/page/chairperson",
    "Director": "https://www.iiitp.ac.in/page/director",
    "Registrar": "https://www.iiitp.ac.in/page/registrar",
    "Board of Governors": "https://www.iiitp.ac.in/page/board-governors",
    "Finance Committee": "https://www.iiitp.ac.in/page/finance-committee",
    "Building and Works Committee": "https://www.iiitp.ac.in/page/building-and-works-committee",
    "Senate": "https://www.iiitp.ac.in/page/senate",
    "Board of Studies (CSE)": "https://www.iiitp.ac.in/page/board-studies-cse",
    "Board of Studies (ECE)": "https://www.iiitp.ac.in/page/board-studies-ece",
    "Board of Studies (AS&H)": "https://www.iiitp.ac.in/page/board-studies-ash"
}

for name, url in urls.items():
    try:
        res = requests.get(url, verify=False, timeout=10)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # usually it's in node__content
        content_root = soup.find('div', class_='node__content')
        if content_root:
            print(f"{name}: Found node__content, length: {len(content_root.text)}")
        else:
            region_content = soup.find('div', class_='region-content')
            print(f"{name}: No node__content. region-content length: {len(region_content.text) if region_content else 'None'}")
    except Exception as e:
        print(f"Failed {name}: {e}")
