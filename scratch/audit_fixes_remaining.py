"""Fix remaining violations after the main audit sweep."""
from pathlib import Path

# Fix 1: components/footer.html and components/header.html
# These are component fragments, they don't have full head sections.
# Nothing to do for Inter font import on these.

# Fix 2: Know Your Bank Notes page - remove shadow-lg, drop-shadow, hover:scale
p = Path('pages/publications/know-your-bank-notes/index.html')
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# Remove drop-shadow-lg and drop-shadow-xl
html = html.replace('drop-shadow-lg', '')
html = html.replace('drop-shadow-xl', '')

# Remove hover:scale-[1.02]
html = html.replace('hover:scale-[1.02]', '')

# Remove shadow-lg (remaining in this file)
html = html.replace('shadow-lg', 'shadow-md')

# Fix the #16A34A third accent -> use #138496 instead
html = html.replace('#16A34A', '#138496')

# Clean up any double spaces from removals
import re
html = re.sub(r'  +', ' ', html)

if html != original:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Fixed: {p}')

# Fix 3: pages/about/index.html - remove hover:scale
p2 = Path('pages/about/index.html')
with open(p2, 'r', encoding='utf-8') as f:
    html2 = f.read()
original2 = html2
html2 = html2.replace('hover:scale-[1.02]', '')
html2 = html2.replace('hover:scale-105', '')
html2 = re.sub(r'  +', ' ', html2)
if html2 != original2:
    with open(p2, 'w', encoding='utf-8') as f:
        f.write(html2)
    print(f'Fixed: {p2}')

# Fix 4: pages/regulation-and-supervision/index.html - remove hover:scale
p3 = Path('pages/regulation-and-supervision/index.html')
with open(p3, 'r', encoding='utf-8') as f:
    html3 = f.read()
original3 = html3
html3 = html3.replace('hover:scale-[1.02]', '')
html3 = html3.replace('hover:scale-105', '')
html3 = re.sub(r'  +', ' ', html3)
if html3 != original3:
    with open(p3, 'w', encoding='utf-8') as f:
        f.write(html3)
    print(f'Fixed: {p3}')

print('Done fixing remaining violations.')
