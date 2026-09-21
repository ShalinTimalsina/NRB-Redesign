from pathlib import Path

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacing Spokesperson name
    old_spokes = '>Dr. Ram Sharan Kharel<'
    new_spokes = '>Mr. Guru Prasad Paudel<'
    
    # Replacing Info Officer name
    old_info = '>Narayan Prasad Pokhrel<'
    new_info = '>Dr. Sanjay Prasad Mishra<'

    if old_spokes in html or old_info in html:
        html = html.replace(old_spokes, new_spokes)
        html = html.replace(old_info, new_info)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed names in {count} footers.')
