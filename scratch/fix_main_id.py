from pathlib import Path

count = 0
for p in sorted(Path('.').rglob('*.html')):
    if 'scratch' in p.parts or '.git' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html
    
    html = html.replace('<main class="flex-1">', '<main class="flex-1" id="Main-Content">')
    html = html.replace('<main>', '<main id="Main-Content">')
    html = html.replace('<main id="Main-Content" id="Main-Content">', '<main id="Main-Content">')
    
    if html != original:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed missing main IDs in {count} files.')
