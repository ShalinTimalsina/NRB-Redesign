import os
from bs4 import BeautifulSoup

def transform_nrb_html():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    main_content = soup.find('main', id='Main-Content')
    if not main_content:
        print("Could not find Main-Content")
        return

    target_section_ids = [
        'Economic-Overview',
        'Foreign-Exchange-Snapshot',
        'Featured-Publications',
        'Latest-Media & Speeches-Circulars',
        'Media-Centre',
        'Consumer-Services',
        'Institutional-Network'
    ]

    sections_to_wrap = []
    for sid in target_section_ids:
        sec = soup.find('section', id=sid)
        if sec:
            sections_to_wrap.append(sec)
    
    if not sections_to_wrap:
        print("No sections to wrap found.")
        return

    # Create the new unified wrapper
    new_wrapper = soup.new_tag('section', id='Homepage-Dashboard', attrs={'class': 'bg-slate-50 py-16 border-b border-slate-200'})
    inner_shell = soup.new_tag('div', attrs={'class': 'nrb-section-shell flex flex-col gap-12'})
    new_wrapper.append(inner_shell)

    for sec in sections_to_wrap:
        shell_div = sec.find('div', class_='nrb-section-shell')
        if not shell_div:
            children = list(sec.children)
        else:
            children = list(shell_div.children)

        # Create the new card tag
        card = soup.new_tag('article', id=f"Card-{sec.get('id')}", attrs={'class': 'nrb-elevated-card rounded-[24px] bg-white border border-slate-200 overflow-hidden'})
        card_inner = soup.new_tag('div', attrs={'class': 'p-8 lg:p-12'})
        
        for child in children:
            if type(child).__name__ == 'NavigableString' and not str(child).strip():
                continue
            card_inner.append(child.extract())
        
        card.append(card_inner)
        inner_shell.append(card)
        
        sec.decompose()
        
    pop_services = soup.find('section', id='Popular-Services')
    if pop_services:
        pop_services.insert_after(new_wrapper)
    else:
        main_content.append(new_wrapper)
    
    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Transformed nrb.html successfully.")

if __name__ == '__main__':
    transform_nrb_html()
