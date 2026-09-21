import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://www.nrb.org.np/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the menu item that contains 'Regulations & Supervisions'
    # It might be 'Regulations & <br> Supervisions' or similar
    reg_menu = None
    for a in soup.find_all('a', class_='dropdown-toggle'):
        if 'Regulation' in a.get_text() or 'Supervision' in a.get_text():
            reg_menu = a.find_next_sibling('div', class_='dropdown-menu')
            break
            
    if not reg_menu:
        print("Could not find the dropdown menu.")
        exit(1)
        
    # Build a tree of the dropdown
    def parse_ul(ul_element):
        items = []
        for li in ul_element.find_all('li', recursive=False):
            title_elem = li.find('span') or li.find('a')
            title = title_elem.get_text(strip=True) if title_elem else "Unknown"
            
            sub_ul = li.find('ul')
            if sub_ul:
                children = parse_ul(sub_ul)
                items.append({title: children})
            else:
                items.append(title)
        return items

    top_ul = reg_menu.find('ul')
    tree = parse_ul(top_ul) if top_ul else []
    
    print(json.dumps(tree, indent=2))
    
    with open('scratch/nav_tree.json', 'w') as f:
        json.dumps(tree, indent=2)

except Exception as e:
    print(f"Error: {e}")
