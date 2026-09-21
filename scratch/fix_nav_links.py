from pathlib import Path
import re

count = 0
for p in sorted(Path('.').rglob('*.html')):
    if 'scratch' in p.parts or '.git' in p.parts:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # Need to handle paths correctly based on depth.
    # The links in the header are usually relative, e.g., "pages/..." or "../../pages/..." depending on the depth.
    # But wait, in the header, the links are already set up with some relative path for others (like "pages/about/index.html" or "index.html" for home).
    # Let's see how "About" is linked in the mega menu to copy the prefix.
    
    # Find the prefix used for 'pages/about'
    match = re.search(r'href="([^"]*)pages/about[^"]*"', html)
    prefix = ""
    if match:
        prefix = match.group(1)
        
    def replace_link(text, target_url):
        # We need to find href="#" where the anchor text matches `text`
        # Using a regex to match the anchor tag wrapping the text
        pattern = r'href="#"([^>]*)>' + re.escape(text) + r'</a>'
        replacement = r'href="' + prefix + target_url + r'"\1>' + text + r'</a>'
        return re.sub(pattern, replacement, html)
        
    html = replace_link('Banks &amp; Financial Institutions', 'pages/regulation-and-supervision/bfr/index.html')
    html = replace_link('Foreign Exchange', 'pages/regulation-and-supervision/fxm/index.html')
    html = replace_link('Payment Systems', 'pages/regulation-and-supervision/psd/index.html')
    html = replace_link('Bank Supervision', 'pages/regulation-and-supervision/bsd/index.html')
    html = replace_link('Financial Institutions', 'pages/regulation-and-supervision/fisd/index.html')
    html = replace_link('Microfinance', 'pages/regulation-and-supervision/mfd/index.html')
    html = replace_link('Non-Bank Entities', 'pages/regulation-and-supervision/nbfisd/index.html')
    
    if html != original:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed nav placeholder links in {count} files.')
