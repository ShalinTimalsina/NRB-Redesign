import re

for filepath in [
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/media-releases/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/speeches/index.html',
]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'href="(.*?)"', content)
    print(f"\n--- {filepath} ---")
    for link in links:
        if 'http' in link or '#' in link:
            print(link)
