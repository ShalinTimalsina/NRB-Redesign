from pathlib import Path

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Determine the correct relative prefix
    depth = len(p.parts) - 1
    prefix = "../" * depth if depth > 0 else ""

    # Replace the leadership link with the information-officers link
    old_link = f'href="{prefix}pages/about/index.html#leadership"'
    new_link = f'href="{prefix}pages/about/information-officers.html"'

    # Only replace it within the Spokesperson and Info Officer paragraphs
    # To be safe, we can just look for the specific lines.
    
    # Spokesperson line
    spokes_old = f'<span class="text-slate-300">Spokesperson:</span> <a href="{prefix}pages/about/index.html#leadership" class="hover:text-white transition">Dr. Ram Sharan Kharel</a>'
    spokes_new = f'<span class="text-slate-300">Spokesperson:</span> <a href="{prefix}pages/about/information-officers.html" class="hover:text-white transition">Dr. Ram Sharan Kharel</a>'
    
    info_old = f'<span class="text-slate-300">Info Officer:</span> <a href="{prefix}pages/about/index.html#leadership" class="hover:text-white transition">Narayan Prasad Pokhrel</a>'
    info_new = f'<span class="text-slate-300">Info Officer:</span> <a href="{prefix}pages/about/information-officers.html" class="hover:text-white transition">Narayan Prasad Pokhrel</a>'

    if spokes_old in html or info_old in html:
        html = html.replace(spokes_old, spokes_new)
        html = html.replace(info_old, info_new)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed {count} files — links now point to information-officers.html.')
