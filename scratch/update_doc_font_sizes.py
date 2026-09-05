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
    
    # Update document titles (from text-sm to text-base for better readability)
    content = content.replace(
        'class="font-semibold text-sm text-slate-900 group-hover:text-[#138496] transition-colors leading-snug"',
        'class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug"'
    )
    
    # Update metadata chips (from text-[10px] to text-xs for legibility)
    content = content.replace(
        'class="inline-flex items-center rounded-md bg-slate-100 px-2 py-0.5 text-[10px] font-medium text-slate-600"',
        'class="inline-flex items-center rounded-md bg-slate-100 px-2.5 py-1 text-xs font-medium text-slate-600"'
    )
    
    if original != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {file_path}")
