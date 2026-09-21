import os
from bs4 import BeautifulSoup

def clean_homepage():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Strip the heavy cards, keep only Institutional Network (Locations/Contact)
    cards_to_remove = [
        'Card-Economic-Overview',
        'Card-Foreign-Exchange-Snapshot',
        'Card-Featured-Publications',
        'Card-Latest-Media & Speeches-Circulars',
        'Card-Media-Centre',
        'Card-Consumer-Services'
    ]

    for cid in cards_to_remove:
        c = soup.find('article', id=cid)
        if c:
            c.decompose()

    # 2. Update the remaining 'Card-Institutional-Network' to be about Contact & Locations
    net_card = soup.find('article', id='Card-Institutional-Network')
    if net_card:
        title = net_card.find('h2')
        if title:
            title.string = "Contact & Locations"
        
        btn = net_card.find('a', attrs={'href': 'pages/about/index.html'})
        if btn:
            btn['href'] = 'pages/contact/index.html'
            btn_texts = btn.find_all(string=True)
            for t in btn_texts:
                if 'About the Bank' in t:
                    t.replace_with('Contact Us')

    # 3. Fix broken mega menu links
    # Regulation & Supervision dropdown
    reg_sup_nav = soup.find('a', id='Nav-Bank-Supervision')
    if reg_sup_nav:
        reg_dropdown = reg_sup_nav.find_next_sibling('div')
        if reg_dropdown:
            broken_links = reg_dropdown.find_all('a', href='#')
            for a in broken_links:
                a['href'] = 'pages/regulation-and-supervision/index.html'
                
    # Footer broken links
    footer = soup.find('footer', id='Footer')
    if footer:
        footer_links = footer.find_all('a', href='#')
        for a in footer_links:
            # Point to a safe generic page based on context, or just the top level hub.
            parent_col = a.find_parent('div', class_='flex flex-col gap-4')
            if parent_col:
                header = parent_col.find('h3')
                if header:
                    text = header.get_text(strip=True).lower()
                    if 'statistics' in text:
                        a['href'] = 'pages/statistics/index.html'
                    elif 'publications' in text:
                        a['href'] = 'pages/publications/index.html'
                    elif 'consumer' in text:
                        a['href'] = 'pages/consumer-services/index.html'
            
            # Bottom footer links like Privacy Policy, etc.
            if 'Policy' in a.get_text() or 'Terms' in a.get_text() or 'Accessibility' in a.get_text():
                a['href'] = 'pages/about/index.html'

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Homepage cleaned and links fixed successfully.")

if __name__ == '__main__':
    clean_homepage()
