import requests
from bs4 import BeautifulSoup
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# ======= 1. MEDIA RELEASES =======
print("=== Scraping Media Releases ===")
url1 = 'https://www.nrb.org.np/category/media-releases/?department=ofg'
resp = requests.get(url1, headers=headers, timeout=30)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find all article/post items
media_releases = []
# Look for typical WordPress post listing
for article in soup.find_all(['article', 'div'], class_=lambda x: x and ('post' in str(x).lower() or 'entry' in str(x).lower() or 'listing' in str(x).lower())):
    title_el = article.find(['h2', 'h3', 'h4', 'a'])
    if title_el:
        title = title_el.get_text(strip=True)
        link = title_el.get('href', '') or (title_el.find('a') or {}).get('href', '')
        if title and len(title) > 5:
            media_releases.append({'title': title, 'link': link})

# Also try the common NRB pattern of <a> tags with PDF links
if not media_releases:
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        if '.pdf' in href.lower() and text and len(text) > 10:
            media_releases.append({'title': text, 'link': href})

# Try finding the main content area
content_area = soup.find('div', class_='content-area') or soup.find('main') or soup.find('div', id='content')
if content_area:
    print(f"Found content area with tag: {content_area.name}")
    # Look for list items or document links
    for item in content_area.find_all(['li', 'tr', 'div']):
        links = item.find_all('a')
        for a in links:
            text = a.get_text(strip=True)
            href = a.get('href', '')
            if text and len(text) > 10 and href and ('pdf' in href.lower() or 'media' in href.lower() or 'nrb.org' in href.lower()):
                media_releases.append({'title': text, 'link': href})

# Deduplicate
seen = set()
unique_releases = []
for item in media_releases:
    key = item['title'][:50]
    if key not in seen:
        seen.add(key)
        unique_releases.append(item)

print(f"Found {len(unique_releases)} media releases")
for item in unique_releases[:10]:
    print(f"  - {item['title'][:80]}")
    print(f"    {item['link']}")

# ======= 2. SPEECHES =======
print("\n=== Scraping Speeches ===")
url2 = 'https://www.nrb.org.np/category/governors-speech/?department=ofg'
resp2 = requests.get(url2, headers=headers, timeout=30)
soup2 = BeautifulSoup(resp2.text, 'html.parser')

speeches = []
content_area2 = soup2.find('div', class_='content-area') or soup2.find('main') or soup2.find('div', id='content')
if content_area2:
    for a in content_area2.find_all('a'):
        text = a.get_text(strip=True)
        href = a.get('href', '')
        if text and len(text) > 10 and href and ('pdf' in href.lower() or 'speech' in href.lower() or 'nrb.org' in href.lower()):
            speeches.append({'title': text, 'link': href})

# Also try finding dates
for item in soup2.find_all(['li', 'tr', 'div']):
    links = item.find_all('a')
    for a in links:
        text = a.get_text(strip=True)
        href = a.get('href', '')
        if text and len(text) > 10 and href and ('pdf' in href.lower() or 'speech' in href.lower()):
            speeches.append({'title': text, 'link': href})

# Deduplicate
seen2 = set()
unique_speeches = []
for item in speeches:
    key = item['title'][:50]
    if key not in seen2:
        seen2.add(key)
        unique_speeches.append(item)

print(f"Found {len(unique_speeches)} speeches")
for item in unique_speeches[:10]:
    print(f"  - {item['title'][:80]}")
    print(f"    {item['link']}")

# ======= 3. Also scrape the OFG department page directly =======
print("\n=== Scraping Office of the Governor (OFG) Department Page ===")
url3 = 'https://www.nrb.org.np/departments/ofg/'
resp3 = requests.get(url3, headers=headers, timeout=30)
soup3 = BeautifulSoup(resp3.text, 'html.parser')

# Get all text content from main body
body = soup3.find('body')
all_links = []
if body:
    for a in body.find_all('a'):
        text = a.get_text(strip=True)
        href = a.get('href', '')
        if text and len(text) > 5 and href and ('media' in text.lower() or 'speech' in text.lower() or 'release' in text.lower() or 'press' in text.lower() or 'pdf' in href.lower()):
            all_links.append({'title': text, 'link': href})

print(f"Found {len(all_links)} relevant links on OFG page")
for item in all_links[:15]:
    print(f"  - {item['title'][:80]}")
    print(f"    {item['link']}")

# Dump everything to a consolidated JSON
import json
result = {
    'media_releases': unique_releases,
    'speeches': unique_speeches,
    'ofg_links': all_links
}
with open('scratch/media_speeches_content.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print("\nSaved all scraped content to scratch/media_speeches_content.json")
