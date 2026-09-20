import os
import glob
import re
import bs4

nav_order = [
    'About',
    'Laws & Policies',
    'Regulation & Supervision',
    'Publications',
    'Statistics',
    'Procurement',
    'Careers',
    'Monetary Policy',
    'Media & Speeches'
]

def get_child_name(c):
    if isinstance(c, bs4.NavigableString):
        return ""
    if c.name == 'a':
        return c.get_text(strip=True)
    elif c.name == 'div':
        a = c.find('a')
        if a: return a.get_text(strip=True)
    return ""

def child_sort_key(c):
    name = get_child_name(c)
    for i, n in enumerate(nav_order):
        if n in name: 
            return i
    return 999

def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'(<nav\s+[^>]*id=\"Primary-Navigation\"[^>]*>)(.*?)(</nav>)', re.DOTALL)
    
    def repl(m):
        start = m.group(1)
        inner = m.group(2)
        end = m.group(3)
        
        soup = bs4.BeautifulSoup(start + inner + end, 'html.parser')
        nav_tag = soup.find('nav')
        
        element_children = [c for c in nav_tag.children if not isinstance(c, bs4.NavigableString)]
        element_children.sort(key=child_sort_key)
        
        new_inner = "\n"
        for c in element_children:
            new_inner += str(c) + "\n"
            
        return start + new_inner + end

    new_content = pattern.sub(repl, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {path}")

for path in glob.glob('**/*.html', recursive=True):
    process_file(path)

print('Done reordering.')
