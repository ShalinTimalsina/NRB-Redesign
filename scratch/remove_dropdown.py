import os
import glob
from bs4 import BeautifulSoup

html_files = glob.glob(r"c:\Users\LOQ\Desktop\NRB Redesign\**\*.html", recursive=True)

for file_path in html_files:
    if "node_modules" in file_path or ".gemini" in file_path or "scratch" in file_path:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    reg_link = soup.find('a', id='Nav-Regulations')
    
    if reg_link:
        parent_div = reg_link.parent
        # Verify parent is the dropdown container we added
        if parent_div and parent_div.name == 'div' and 'relative' in parent_div.get('class', []):
            href = reg_link.get('href')
            # Create a simple replacement anchor tag
            new_a = soup.new_tag('a', id='Nav-Regulations', href=href, **{'class': 'text-slate-100 transition hover:text-[#138496]'})
            new_a.string = 'Regulations'
            parent_div.replace_with(new_a)
            
            # Write back
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"Updated nav in {file_path}")
