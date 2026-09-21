import os
from bs4 import BeautifulSoup

def insert_bkd_link(filepath):
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

    # Check if Banking Department already exists
    exists = False
    for a in parent_div.find_all('a'):
        if 'Banking Department' in a.get_text(strip=True):
            exists = True
            break
            
    if exists:
        return False

    # Find the Payment Systems link, which is the last one in the Regulated Sectors column
    psd_link = None
    for a in parent_div.find_all('a'):
        if 'Payment Systems' in a.get_text(strip=True):
            psd_link = a
            break
            
    if not psd_link:
        return False
        
    # Create the new link
    new_a = soup.new_tag('a', href=f"{prefix}pages/regulation-and-supervision/bkd/index.html", **{'class': 'px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg'})
    new_a.string = "Banking Department"
    
    psd_link.insert_after(new_a)
    
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
                if insert_bkd_link(filepath):
                    print(f"Added Banking Department link in {filepath}")
                    count += 1
            except Exception as e:
                pass

print(f"Total files updated safely: {count}")
