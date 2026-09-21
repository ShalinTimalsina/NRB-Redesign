import os
from bs4 import BeautifulSoup

def sync_reg_nav_bs4(filepath):
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
    # It might have id="Nav-Bank-Supervision" or "Nav-Regulation-Supervision"
    reg_link = soup.find('a', id='Nav-Bank-Supervision') or soup.find('a', id='Nav-Regulation-Supervision')
    if not reg_link:
        # Fallback to finding by text
        for a in soup.find_all('a'):
            if 'Regulation &' in a.get_text():
                reg_link = a
                break

    if not reg_link:
        return False

    parent_div = reg_link.find_parent('div', class_='relative group')
    if not parent_div:
        return False
        
    new_html = f"""
<div class="relative group">
<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{prefix}pages/regulation-and-supervision/index.html" id="Nav-Regulation-Supervision">
Regulation &amp; Supervision
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
</a>
<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-5 px-6 w-[720px] grid grid-cols-2 gap-x-6">
<!-- Column 1: Regulations -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Regulations</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bfr/index.html">Banks &amp; Financial Institutions</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/fxm/index.html">Foreign Exchange Management</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/psd/index.html">Payment Systems</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bkd/index.html">Banking Department</a>
</div>
<!-- Column 2: Supervisions -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Supervisions</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bsd/index.html">Bank Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/fisd/index.html">Financial Institutions Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/mfd/index.html">Microfinance Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/nbfisd/index.html">Non-Bank Entities Supervision</a>
</div>
</div>
</div>
</div>
"""
    new_soup_element = BeautifulSoup(new_html, 'html.parser')
    parent_div.replace_with(new_soup_element)
    
    # Write back without changing formatting
    # BS4 prettify might mess up formatting, so we just use string replacement based on str() of original vs new if possible
    # But since BS4 modifies the tree, we convert it back to string. We'll use the unformatted version to preserve spaces as best as possible.
    result = str(soup)
    
    # BS4 sometimes encodes HTML entities poorly, fix common ones
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
                if sync_reg_nav_bs4(filepath):
                    print(f"Synced global nav in {filepath}")
                    count += 1
            except Exception as e:
                pass

print(f"Total files synced safely: {count}")
