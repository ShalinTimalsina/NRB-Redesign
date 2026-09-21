import os
from pathlib import Path

def fix_contact_dropdown():
    # We want to replace 'pages/about/index.html#contact' with 'pages/contact/index.html'
    target_pattern = 'pages/about/index.html#contact'
    replacement = 'pages/contact/index.html'
    
    # Check root nrb.html
    root_file = Path('nrb.html')
    if root_file.exists():
        content = root_file.read_text(encoding='utf-8')
        if target_pattern in content:
            content = content.replace(target_pattern, replacement)
            root_file.write_text(content, encoding='utf-8')
            print("Fixed nrb.html")

    # Check all files in pages/
    count = 0
    for p in Path('pages').rglob('*.html'):
        content = p.read_text(encoding='utf-8')
        if target_pattern in content:
            content = content.replace(target_pattern, replacement)
            p.write_text(content, encoding='utf-8')
            count += 1
            
    print(f"Fixed {count} files in pages directory.")

if __name__ == '__main__':
    fix_contact_dropdown()
