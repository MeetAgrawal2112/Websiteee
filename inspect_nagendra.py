import requests
from bs4 import BeautifulSoup

url = "https://www.iiitp.ac.in/page/dr-nagendra-kushwaha"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

fp = soup.find('div', class_='faculty-profile')
print("Divs inside faculty-profile:", len(fp.find_all('div', recursive=False)))
for i, d in enumerate(fp.find_all('div', recursive=False)):
    print(f"Child {i} classes: {d.get('class')} - Length: {len(d.text)}")
