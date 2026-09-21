import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('scratch/media_releases_raw.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== ALL PDF LINKS ON OFG PAGE ===\n")
pdf_count = 0
for a in soup.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True)
    if '.pdf' in href.lower() and text:
        print(f"  {text[:120]}")
        print(f"    -> {href}")
        pdf_count += 1
print(f"\nTotal PDFs: {pdf_count}")

print("\n\n=== DOCUMENT SECTIONS (h2/h3/h4 followed by links) ===\n")
current_heading = "Unknown"
for el in soup.find_all(['h2', 'h3', 'h4', 'h5', 'a']):
    if el.name in ['h2', 'h3', 'h4', 'h5']:
        text = el.get_text(strip=True)
        if text and len(text) > 2 and len(text) < 200:
            current_heading = text
            print(f"\n--- {current_heading} ---")
    elif el.name == 'a':
        href = el.get('href', '')
        text = el.get_text(strip=True)
        if text and len(text) > 5 and href and ('nrb.org' in href or '.pdf' in href):
            # Skip nav links
            if any(skip in href for skip in ['#', 'facebook', 'twitter', 'youtube']):
                continue
            print(f"  [{text[:100]}]({href})")

print("\n\n=== LOOKING FOR TAB CONTENT SECTIONS ===\n")
for div in soup.find_all('div', id=True):
    div_id = div.get('id', '')
    if any(k in div_id.lower() for k in ['tab', 'panel', 'content', 'media', 'speech', 'release']):
        text = div.get_text(strip=True)[:200]
        if text:
            print(f"div#{div_id}: {text}")

print("\n\n=== LOOKING AT SPECIFIC NRB WIDGET CLASSES ===\n")
for div in soup.find_all('div', class_=True):
    classes = ' '.join(div.get('class', []))
    if any(k in classes.lower() for k in ['dept-', 'nrb-', 'post-listing', 'archive-list', 'document-list']):
        text = div.get_text(strip=True)[:150]
        links_count = len(div.find_all('a'))
        if text and links_count > 0:
            print(f"  .{classes}: {links_count} links, text: {text[:80]}")
