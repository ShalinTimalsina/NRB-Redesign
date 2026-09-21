import os
from bs4 import BeautifulSoup

def add_redirects():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')

    mapping = {
        'Card-Economic-Overview': ('View Statistics Hub', 'pages/statistics/index.html'),
        'Card-Foreign-Exchange-Snapshot': ('View Daily Exchange Rates', 'pages/forex-management/index.html'),
        'Card-Featured-Publications': ('View All Publications', 'pages/publications/index.html'),
        'Card-Latest-Media & Speeches-Circulars': ('View Media & Speeches', 'pages/media-speeches/index.html'),
        'Card-Media-Centre': ('View Media Hub', 'pages/media-speeches/index.html'),
        'Card-Consumer-Services': ('View Consumer Services', 'pages/consumer-services/index.html'),
        'Card-Institutional-Network': ('About the Bank', 'pages/about/index.html')
    }

    for card_id, (label, link) in mapping.items():
        card = soup.find('article', id=card_id)
        if not card:
            continue
        
        header_row = card.find('div', class_=lambda c: c and 'mb-7 flex items-end justify-between' in c)
        
        if header_row:
            existing_link = header_row.find('a', href=True)
            if not existing_link:
                new_btn = soup.new_tag('a', href=link, attrs={'class': 'inline-flex items-center gap-2 rounded-full bg-[#138496] px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-[#0f6c7a] shrink-0'})
                new_btn.string = label
                
                icon_svg = BeautifulSoup('''<svg aria-hidden="true" class="h-4 w-4" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>''', 'html.parser')
                new_btn.append(icon_svg)
                
                right_div = header_row.find('div', class_=lambda c: c and 'rounded-full border' in c)
                if right_div and right_div.name != 'a':
                    right_div.replace_with(new_btn)
                else:
                    header_row.append(new_btn)

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Added redirects successfully.")

if __name__ == '__main__':
    add_redirects()
