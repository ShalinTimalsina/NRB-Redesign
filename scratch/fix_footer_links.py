from pathlib import Path

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix spokesperson link: external nrb.org.np -> internal about page
    old_spokes = 'href="https://www.nrb.org.np/spokesperson/"'
    old_info = 'href="https://www.nrb.org.np/information-officer/"'

    if old_spokes in html or old_info in html:
        # Determine the correct relative prefix
        depth = len(p.parts) - 1
        prefix = "../" * depth if depth > 0 else ""

        new_spokes = f'href="{prefix}pages/about/index.html#leadership"'
        new_info = f'href="{prefix}pages/about/index.html#leadership"'

        html = html.replace(old_spokes, new_spokes)
        html = html.replace(old_info, new_info)
        
        # Also remove target="_blank" for these internal links
        html = html.replace('href="' + prefix + 'pages/about/index.html#leadership" target="_blank" rel="noopener"',
                            'href="' + prefix + 'pages/about/index.html#leadership"')

        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed {count} files — links now point to internal About page.')
