import os
from bs4 import BeautifulSoup

def update_homepage():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Add "Contact Us" to Popular Services grid
    pop_services = soup.find('section', id='Popular-Services')
    if pop_services:
        grid = pop_services.find('div', class_=lambda c: c and 'grid-cols-3' in c)
        if grid:
            # Create a new quick link card for Contact
            contact_card = soup.new_tag('a', href='pages/contact/index.html', id='Service-Contact', attrs={'class': 'nrb-elevated-card group rounded-[20px] bg-white p-6 transition hover:-translate-y-0.5 hover:shadow-md'})
            
            header_div = soup.new_tag('div', attrs={'class': 'flex items-center justify-between'})
            
            icon_container = soup.new_tag('div', attrs={'class': 'flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white'})
            
            # Contact icon SVG
            svg_html = '''<svg aria-hidden="true" class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'''
            icon_svg = BeautifulSoup(svg_html, 'html.parser').svg
            icon_container.append(icon_svg)
            
            label_span = soup.new_tag('span', attrs={'class': 'text-xs font-semibold uppercase tracking-[0.18em] text-slate-400'})
            label_span.string = "Connect"
            
            header_div.append(icon_container)
            header_div.append(label_span)
            
            title = soup.new_tag('h3', attrs={'class': 'mt-8 text-xl font-semibold text-slate-900'})
            title.string = "Contact & Locations"
            
            desc = soup.new_tag('p', attrs={'class': 'mt-3 text-sm leading-6 text-slate-600'})
            desc.string = "Official contact channels, routing, and public inquiry paths."
            
            contact_card.append(header_div)
            contact_card.append(title)
            contact_card.append(desc)
            
            grid.append(contact_card)

    # 2. Delete the massive Dashboard section completely
    dashboard = soup.find('section', id='Homepage-Dashboard')
    if dashboard:
        dashboard.decompose()

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Homepage updated successfully.")

if __name__ == '__main__':
    update_homepage()
