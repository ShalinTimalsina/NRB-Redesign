import os
from bs4 import BeautifulSoup

def fix_quick_access():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Change Media & Speeches link to the fully fleshed out hub instead of the notices demo
    media_card = soup.find('a', id='Service-Media & Speeches')
    if media_card:
        media_card['href'] = 'pages/media-speeches/index.html'

    # 2. Remove the Consumer Services card entirely because it points to an empty demo page
    consumer_card = soup.find('a', id='Service-Consumer-Protection')
    if consumer_card:
        consumer_card.decompose()
        
    # Optional: While we're at it, Consumer Services is also in the footer and main nav.
    # The user said "make sure that evey quick access menues opens to a acutual page... if it redeirects to a random page, that was previously imade in the demo then remove it"
    # This specifically targets the quick access menus (the cards). We'll stick to removing the card.

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Fixed Quick Access links and removed demo cards successfully.")

if __name__ == '__main__':
    fix_quick_access()
