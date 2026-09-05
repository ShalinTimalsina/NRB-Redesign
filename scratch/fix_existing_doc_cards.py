import os
import re
from datetime import datetime

files_to_check = [
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\annual-financial-statements.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\financial-statements.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\investment-related-notices.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\publications\index.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\notices\index.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\monetary-policy\index.html"
]

def format_size(size_str):
    if not size_str:
        return ""
    try:
        match = re.match(r'([\d.]+)\s*([a-zA-Z]+)', size_str.strip())
        if match:
            val = float(match.group(1))
            unit = match.group(2).upper()
            
            bytes_val = val
            if unit == "KB": bytes_val *= 1024
            elif unit == "MB": bytes_val *= 1024*1024
            elif unit == "GB": bytes_val *= 1024*1024*1024
            
            mb = bytes_val / (1024 * 1024)
            if mb >= 1.0:
                formatted = f"{mb:.1f}".rstrip('0').rstrip('.')
                return f"{formatted} MB"
            else:
                kb = bytes_val / 1024
                formatted = str(int(round(kb)))
                return f"{formatted} KB"
    except Exception:
        pass
    return size_str

def format_date(date_str):
    if not date_str:
        return ""
    try:
        d = datetime.strptime(date_str.strip(), "%B %d, %Y")
        return d.strftime("%d %b %Y").lstrip("0")
    except Exception:
        pass
    try:
        # Fallback for already formatted dates
        d = datetime.strptime(date_str.strip(), "%d %b %Y")
        return d.strftime("%d %b %Y").lstrip("0")
    except:
        pass
    return date_str.strip()

for filepath in files_to_check:
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # We are looking for: <div class="flex items-center gap-2 flex-wrap"><span ...>Date</span><span ...>Type</span><span ...>Size</span></div>
    # But since some files might have different structures, let's use a regex that matches the entire chip container block
    # and extracts the text from the spans.
    
    def replacer(match):
        full_div = match.group(0)
        
        # Extract span texts
        spans = re.findall(r'<span[^>]*>(.*?)</span>', full_div)
        if len(spans) < 2:
            return full_div # Skip if it doesn't look like our metadata
            
        date = ""
        ftype = ""
        size = ""
        
        for text in spans:
            if text in ["PDF", "DOC", "XLS"]:
                ftype = text
            elif "MB" in text or "KB" in text:
                size = text
            else:
                date = text
                
        if not ftype:
            ftype = "PDF" # Default fallback
            
        date_f = format_date(date)
        size_f = format_size(size)
        
        meta_parts = []
        meta_parts.append(f'<span class="font-medium text-slate-700">{ftype}</span>')
        if size_f:
            meta_parts.append(f'<span class="text-slate-300 px-1.5">•</span><span>{size_f}</span>')
        if date_f:
            meta_parts.append(f'<span class="text-slate-300 px-1.5">•</span><span>{date_f}</span>')
            
        meta_html = "".join(meta_parts)
        # We need to change the parent div class too since we aren't using chips anymore
        return f'<div class="flex items-center text-[13px] text-slate-500">{meta_html}</div>'

    # The regex targets the container that has flex-wrap and gap-2 which was the chip container
    new_html = re.sub(r'<div class="flex items-center gap-2 flex-wrap">.*?</div>', replacer, html, flags=re.DOTALL)
    
    # Also handle the older format if it exists (e.g., in other pages) 
    # Just in case other pages have the exact old "chip-less" format but wrong order
    
    if new_html != html:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Updated metadata formatting in {filepath}")
