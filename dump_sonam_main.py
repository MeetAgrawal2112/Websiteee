import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

url = "https://www.iiitp.ac.in/page/dr-sonam-maurya"
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.content, 'html.parser')
    
faculty_main = soup.find('div', class_='faculty-main')
if faculty_main:
    print(faculty_main.prettify())
