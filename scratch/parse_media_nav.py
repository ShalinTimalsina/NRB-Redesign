import requests
from bs4 import BeautifulSoup
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.nrb.org.np/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("Fetching NRB homepage...")
resp = requests.get(url, headers=headers, timeout=30)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find the "Media Speeches" menu item
print("\n=== MEDIA & SPEECHES DROPDOWN STRUCTURE ===\n")

for li in soup.find_all('li', class_=lambda x: x and 'menu-item' in str(x)):
    a = li.find('a', recursive=False)
    if not a:
        continue
    text = a.get_text(strip=True)
    
    if 'media' in text.lower() or 'speech' in text.lower():
        href = a.get('href', '')
        print(f"TOP LEVEL: '{text}' -> {href}")
        
        # Get sub-menu
        sub = li.find('ul')
        if sub:
            for sub_li in sub.find_all('li', recursive=False):
                sub_a = sub_li.find('a', recursive=False)
                if sub_a:
                    sub_text = sub_a.get_text(strip=True)
                    sub_href = sub_a.get('href', '')
                    print(f"  L2: '{sub_text}' -> {sub_href}")
                    
                    # Check for sub-sub menu
                    sub_sub = sub_li.find('ul')
                    if sub_sub:
                        for ss_li in sub_sub.find_all('li', recursive=False):
                            ss_a = ss_li.find('a', recursive=False)
                            if ss_a:
                                ss_text = ss_a.get_text(strip=True)
                                ss_href = ss_a.get('href', '')
                                print(f"    L3: '{ss_text}' -> {ss_href}")
                                
                                # Check for L4
                                sub_sub_sub = ss_li.find('ul')
                                if sub_sub_sub:
                                    for sss_li in sub_sub_sub.find_all('li', recursive=False):
                                        sss_a = sss_li.find('a', recursive=False)
                                        if sss_a:
                                            sss_text = sss_a.get_text(strip=True)
                                            sss_href = sss_a.get('href', '')
                                            print(f"      L4: '{sss_text}' -> {sss_href}")

# Also dump the full nav tree to JSON for reference
print("\n\n=== FULL NAV TREE (for reference) ===\n")

nav_tree = {}
for li in soup.find_all('li', class_=lambda x: x and 'menu-item' in str(x)):
    a = li.find('a', recursive=False)
    if not a:
        continue
    text = a.get_text(strip=True)
    href = a.get('href', '')
    
    # Only top-level items (direct children of the main nav ul)
    parent_ul = li.parent
    if parent_ul and parent_ul.parent:
        grandparent = parent_ul.parent
        # Check if this is the main nav
        if grandparent.name == 'nav' or (grandparent.get('class') and any('navbar' in c for c in grandparent.get('class', []))):
            nav_tree[text] = {'href': href, 'children': []}
            sub = li.find('ul')
            if sub:
                for sub_li in sub.find_all('li', recursive=False):
                    sub_a = sub_li.find('a', recursive=False)
                    if sub_a:
                        child = {
                            'text': sub_a.get_text(strip=True),
                            'href': sub_a.get('href', ''),
                            'children': []
                        }
                        sub_sub = sub_li.find('ul')
                        if sub_sub:
                            for ss_li in sub_sub.find_all('li', recursive=False):
                                ss_a = ss_li.find('a', recursive=False)
                                if ss_a:
                                    grandchild = {
                                        'text': ss_a.get_text(strip=True),
                                        'href': ss_a.get('href', '')
                                    }
                                    child['children'].append(grandchild)
                        nav_tree[text]['children'].append(child)

# Save the Media & Speeches portion
with open('scratch/media_speeches_nav.json', 'w', encoding='utf-8') as f:
    json.dump(nav_tree, f, indent=2, ensure_ascii=False)

print("Saved full nav tree to scratch/media_speeches_nav.json")
