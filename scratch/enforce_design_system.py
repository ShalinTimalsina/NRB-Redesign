import os
import re
import glob

html_files = glob.glob(r"c:\Users\LOQ\Desktop\NRB Redesign\**\*.html", recursive=True)

for file_path in html_files:
    if "node_modules" in file_path or ".gemini" in file_path or "scratch" in file_path:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    
    # 1. Remove IBM Plex Sans Google Font link
    content = re.sub(r'<link[^>]+family=IBM\+Plex\+Sans[^>]+>\s*', '', content)
    
    # 2. Normalize h1 tags
    # We want to replace the class attribute of h1 tags to "text-2xl font-bold text-slate-900 mb-4"
    # But keep other attributes like id.
    def replace_h1(match):
        attrs = match.group(1)
        inner = match.group(2)
        # Remove existing class attribute
        attrs = re.sub(r'\s*class="[^"]*"', '', attrs)
        return f'<h1{attrs} class="text-2xl font-bold text-slate-900 mb-4">{inner}</h1>'
        
    content = re.sub(r'<h1([^>]*)>(.*?)</h1>', replace_h1, content, flags=re.DOTALL)
    
    # 3. Replace text-[#1E3A5F] with text-[#25295B]
    content = content.replace("text-[#1E3A5F]", "text-[#25295B]")
    
    # 4. Replace border-[#1E3A5F] with border-[#25295B]
    content = content.replace("border-[#1E3A5F]", "border-[#25295B]")
    
    # 5. Replace arbitrary gold badges with slate badges
    # Old: border border-[#C59D5F]/25 bg-[#C59D5F]/10 px-4 py-2 text-xs font-semibold uppercase tracking-[0.2em] text-[#8B6A30]
    # We can just string replace the color hex codes in those badges
    content = content.replace("border-[#C59D5F]/25", "border-slate-200")
    content = content.replace("bg-[#C59D5F]/10", "bg-slate-100")
    content = content.replace("text-[#8B6A30]", "text-slate-600")

    if original != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {file_path}")
