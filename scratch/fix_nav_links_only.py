import os
from bs4 import BeautifulSoup

# Map of existing text in the dropdown to their new relative paths
# We will match the text exactly as it appears in the a tag
link_map = {
    'Banks & Financial Institutions': 'pages/regulation-and-supervision/bfr/index.html',
    'Foreign Exchange': 'pages/regulation-and-supervision/fxm/index.html',
    'Payment Systems': 'pages/regulation-and-supervision/psd/index.html',
    'Bank Supervision': 'pages/regulation-and-supervision/bsd/index.html',
    'Financial Institutions': 'pages/regulation-and-supervision/fisd/index.html',
    'Microfinance': 'pages/regulation-and-supervision/mfd/index.html',
    'Non-Bank Entities': 'pages/regulation-and-supervision/nbfisd/index.html',
    'Circulars': 'pages/regulation-and-supervision/bfr/index.html#circulars',
    'Notices': 'pages/regulation-and-supervision/bfr/index.html#notices',
    'Policies & Guidelines': 'pages/regulation-and-supervision/psd/index.html#policiesguidelines',
    'Consumer Protection': 'pages/regulation-and-supervision/bfr/index.html#financialconsumerprotection'
}

def sync_reg_nav_links(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Determine depth prefix based on another known link
    prefix = ""
    pub_link = soup.find('a', id='Nav-Publications')
    if pub_link and pub_link.has_attr('href'):
        href = pub_link['href']
        if href.endswith('pages/publications/index.html'):
            prefix = href.replace('pages/publications/index.html', '')
            
    # Find the Regulation & Supervision nav
    reg_link = soup.find('a', id='Nav-Bank-Supervision') or soup.find('a', id='Nav-Regulation-Supervision')
    if not reg_link:
        for a in soup.find_all('a'):
            if 'Regulation &' in a.get_text():
                reg_link = a
                break

    if not reg_link:
        return False

    parent_div = reg_link.find_parent('div', class_='relative group')
    if not parent_div:
        return False

    # ONLY update the hrefs of the 'a' tags inside this parent_div based on text
    changed = False
    for a in parent_div.find_all('a'):
        text = a.get_text(strip=True)
        if text in link_map:
            new_href = prefix + link_map[text]
            if a.get('href') != new_href:
                a['href'] = new_href
                changed = True
                
    if not changed:
        return False
        
    # Write back without changing formatting
    result = str(soup)
    result = result.replace('&amp;amp;', '&amp;')
    
    if result != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False

count = 0
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                if sync_reg_nav_links(filepath):
                    print(f"Updated nav links in {filepath}")
                    count += 1
            except Exception as e:
                pass

print(f"Total files where links were securely updated: {count}")
