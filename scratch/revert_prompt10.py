import re

# 1. Revert organogram.html to prompt 8 version (remove injected sub-nav and restore gold badge)
def restore_organogram():
    fpath = 'pages/about/organogram.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Restore gold badge if modified
    html = re.sub(
        r'<span class="inline-flex items-center gap-1\.5 rounded-full bg-\[#25295B\]/10 px-3\.5 py-1 text-xs font-semibold uppercase tracking-wider text-\[#25295B\] mb-4">About NRB</span>',
        r'<span class="inline-block rounded-full border border-[#C59D5F]/25 bg-[#C59D5F]/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-[#8B6A30] mb-5">About NRB</span>',
        html
    )
    # Remove injected subnav
    html = re.sub(r'\s*<!-- SUB NAVIGATION BAR -->\s*<div id="Local-Navigation".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("organogram.html restored to final prompt 8 state.")

# 2. Revert departments.html to initial prompt 9 version (remove injected sub-nav and restore gold badge)
def restore_departments():
    fpath = 'pages/about/departments.html'
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = re.sub(
        r'<span class="inline-flex items-center gap-1\.5 rounded-full bg-\[#25295B\]/10 px-3\.5 py-1 text-xs font-semibold uppercase tracking-wider text-\[#25295B\] mb-4">About NRB</span>',
        r'<span class="inline-block rounded-full border border-[#C59D5F]/25 bg-[#C59D5F]/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-[#8B6A30] mb-5">About NRB</span>',
        html
    )
    html = re.sub(r'\s*<!-- SUB NAVIGATION BAR -->\s*<div id="Local-Navigation".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("departments.html restored to initial prompt 9 state.")

# 3. Revert prompt 10 modifications on board-of-directors, governors-history, principal-officers, information-officers, financial-statements, provincial-offices, index
def restore_other_pages():
    other_pages = [
        'board-of-directors.html',
        'governors-history.html',
        'principal-officers.html',
        'information-officers.html',
        'financial-statements.html',
        'provincial-offices.html',
        'index.html'
    ]
    for fname in other_pages:
        fpath = f'pages/about/{fname}'
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Restore gold badge
        html = re.sub(
            r'<span class="inline-flex items-center gap-1\.5 rounded-full bg-\[#25295B\]/10 px-3\.5 py-1 text-xs font-semibold uppercase tracking-wider text-\[#25295B\] mb-4">About NRB</span>',
            r'<span class="inline-block rounded-full border border-[#C59D5F]/25 bg-[#C59D5F]/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-[#8B6A30] mb-5">About NRB</span>',
            html
        )
        # Remove injected subnav if it was newly added (except on index where Local-Navigation was already native)
        if fname != 'index.html':
            html = re.sub(r'\s*<!-- SUB NAVIGATION BAR -->\s*<div id="Local-Navigation".*?</div>\s*</div>', '', html, flags=re.DOTALL)
            
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Restored {fname}.")

restore_organogram()
restore_departments()
restore_other_pages()
