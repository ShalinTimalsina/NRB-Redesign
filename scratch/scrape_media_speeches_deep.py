import requests
from bs4 import BeautifulSoup
import sys
import json
import re
sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# ======= SCRAPE THE OFG DEPARTMENT PAGE (main source of truth) =======
print("=== Scraping OFG Department Page (full content) ===\n")
url = 'https://www.nrb.org.np/departments/ofg/'
resp = requests.get(url, headers=headers, timeout=30)
soup = BeautifulSoup(resp.text, 'html.parser')

# Get ALL text content structured
sections = {}
current_section = "General"

# Look for content divs that contain the actual data
for el in soup.find_all(['h2', 'h3', 'h4', 'h5', 'a', 'p', 'span', 'div', 'li', 'table']):
    text = el.get_text(strip=True)
    if not text or len(text) < 3:
        continue
    
    # Detect section headers
    if el.name in ['h2', 'h3', 'h4', 'h5']:
        current_section = text
        if current_section not in sections:
            sections[current_section] = []
        continue
    
    # Collect content items
    if el.name == 'a':
        href = el.get('href', '')
        if href and text and len(text) > 5:
            if current_section not in sections:
                sections[current_section] = []
            sections[current_section].append({
                'text': text,
                'href': href,
                'type': 'link'
            })
    elif el.name in ['p', 'span', 'li']:
        if len(text) > 15 and not text.startswith('{') and not text.startswith('var '):
            if current_section not in sections:
                sections[current_section] = []
            sections[current_section].append({
                'text': text,
                'type': 'text'
            })

# Print structured content
for section, items in sections.items():
    if not items or len(section) > 200:
        continue
    # Filter out JS/CSS noise
    if any(x in section.lower() for x in ['script', 'style', 'cookie', 'google', 'analytics']):
        continue
    print(f"\n## {section}")
    seen = set()
    for item in items:
        key = item['text'][:60]
        if key in seen:
            continue
        seen.add(key)
        if 'href' in item:
            print(f"  - [{item['text'][:100]}]({item['href']})")
        else:
            if len(item['text']) > 15 and not any(x in item['text'].lower() for x in ['cookie', 'google', 'script', '{', 'function', 'var ', 'const ']):
                print(f"  - {item['text'][:150]}")

# ======= SCRAPE MEDIA RELEASES PAGE (multiple pages if needed) =======
print("\n\n=== Scraping Media Releases (with date extraction) ===\n")

for page_num in range(1, 4):  # Get first 3 pages
    if page_num == 1:
        url_mr = 'https://www.nrb.org.np/category/media-releases/?department=ofg'
    else:
        url_mr = f'https://www.nrb.org.np/category/media-releases/page/{page_num}/?department=ofg'
    
    try:
        resp_mr = requests.get(url_mr, headers=headers, timeout=30)
        if resp_mr.status_code != 200:
            break
        soup_mr = BeautifulSoup(resp_mr.text, 'html.parser')
        
        # NRB uses table-based listings
        items_found = 0
        for tr in soup_mr.find_all('tr'):
            cells = tr.find_all(['td', 'th'])
            if cells:
                row_text = ' | '.join([c.get_text(strip=True) for c in cells])
                links = tr.find_all('a')
                link_info = [(a.get_text(strip=True), a.get('href', '')) for a in links if a.get('href')]
                if row_text and len(row_text) > 10:
                    print(f"  Page {page_num}: {row_text[:120]}")
                    for lt, lh in link_info:
                        if lh and '.pdf' in lh.lower():
                            print(f"    PDF: {lh}")
                    items_found += 1
        
        # Also check for list-based format
        for li in soup_mr.find_all('li'):
            a = li.find('a')
            if a:
                text = a.get_text(strip=True)
                href = a.get('href', '')
                date_el = li.find('span', class_=lambda x: x and 'date' in str(x).lower()) or li.find('time')
                date = date_el.get_text(strip=True) if date_el else ''
                if text and len(text) > 15 and ('pdf' in href.lower() or 'media' in href.lower() or 'nrb.org' in href.lower()):
                    print(f"  Page {page_num}: {text[:100]} | Date: {date} | {href}")
                    items_found += 1
        
        # Try div-based cards
        for div in soup_mr.find_all('div', class_=lambda x: x and any(k in str(x).lower() for k in ['card', 'item', 'post', 'entry'])):
            a = div.find('a')
            if a:
                text = a.get_text(strip=True)
                href = a.get('href', '')
                if text and len(text) > 10:
                    print(f"  Page {page_num} (card): {text[:100]} | {href}")
                    items_found += 1
        
        if items_found == 0:
            print(f"  Page {page_num}: No structured items found, checking raw links...")
            for a in soup_mr.find_all('a'):
                text = a.get_text(strip=True)
                href = a.get('href', '')
                if text and len(text) > 20 and '.pdf' in href.lower():
                    print(f"    PDF Link: {text[:100]} -> {href}")
                    items_found += 1
        
        print(f"  (Total items on page {page_num}: {items_found})")
        
    except Exception as e:
        print(f"  Error on page {page_num}: {e}")
        break

# ======= SCRAPE SPEECHES PAGE =======
print("\n\n=== Scraping Speeches ===\n")
url_sp = 'https://www.nrb.org.np/category/governors-speech/?department=ofg'
resp_sp = requests.get(url_sp, headers=headers, timeout=30)
soup_sp = BeautifulSoup(resp_sp.text, 'html.parser')

# Same approach
items_found = 0
for tr in soup_sp.find_all('tr'):
    cells = tr.find_all(['td', 'th'])
    if cells:
        row_text = ' | '.join([c.get_text(strip=True) for c in cells])
        links = tr.find_all('a')
        if row_text and len(row_text) > 10:
            print(f"  {row_text[:150]}")
            items_found += 1

for a in soup_sp.find_all('a'):
    text = a.get_text(strip=True)
    href = a.get('href', '')
    if text and len(text) > 20 and ('speech' in href.lower() or '.pdf' in href.lower()):
        print(f"  Speech: {text[:120]} -> {href}")
        items_found += 1

print(f"\n(Total speech items found: {items_found})")

# Save raw HTML for deeper analysis
with open('scratch/media_releases_raw.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)  # OFG page

with open('scratch/speeches_raw.html', 'w', encoding='utf-8') as f:
    f.write(resp_sp.text)

print("\nSaved raw HTML for deeper analysis.")
