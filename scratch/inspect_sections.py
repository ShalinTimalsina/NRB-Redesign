import re
from bs4 import BeautifulSoup

with open('nrb.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

sections = soup.find_all('section')
for s in sections:
    print(f"{s.get('id', 'NO-ID')}: {len(str(s))} bytes")
