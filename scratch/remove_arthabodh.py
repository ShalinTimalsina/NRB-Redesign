import os
import re
import shutil

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

count_mega = 0
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Remove from Mega Menu
            mega_menu_pattern = r'<a[^>]*href="[^"]*pages/publications/arthabodh/index.html"[^>]*>.*?</a>\s*'
            content = re.sub(mega_menu_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
            
            # Remove from local navigation
            local_nav_pattern = r'<a[^>]*href="\.\./arthabodh/index\.html"[^>]*>.*?</a>\s*'
            content = re.sub(local_nav_pattern, '', content, flags=re.IGNORECASE)
            
            # Remove from publications hub grid
            hub_grid_pattern = r'<!-- Arthabodh -->\s*<a href="arthabodh/index\.html".*?</a>\s*'
            content = re.sub(hub_grid_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count_mega += 1

print(f"Removed Arthabodh links from {count_mega} files.")

arthabodh_dir = os.path.join(base_dir, 'pages', 'publications', 'arthabodh')
if os.path.exists(arthabodh_dir):
    shutil.rmtree(arthabodh_dir)
    print("Deleted arthabodh folder.")
