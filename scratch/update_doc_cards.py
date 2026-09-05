import os
from bs4 import BeautifulSoup
import re

files_to_process = [
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\annual-financial-statements.html",
    r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\investment-related-notices.html"
]

for file_path in files_to_process:
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    changed = False
    for a_tag in soup.find_all("a", class_=lambda c: c and "hub-card" in c and "nrb-elevated-card" in c):
        span_action = a_tag.find("span", text=lambda t: t and "Open Document" in t)
        if not span_action:
            continue
            
        div_container = a_tag.find("div", class_="flex items-center gap-4")
        if not div_container:
            continue
            
        changed = True
        
        # update div_container class to items-start
        div_container["class"] = "flex items-start gap-4"
        
        # update icon div class
        icon_div = div_container.find("div", class_="shrink-0")
        if icon_div:
            icon_div["class"] = "flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5"
            
        text_div = icon_div.find_next_sibling("div")
        if text_div:
            text_div["class"] = "flex flex-col gap-1.5"
            p_title = text_div.find("p", class_=lambda c: c and "font-semibold" in c)
            if p_title:
                p_title["class"] = "font-semibold text-sm text-slate-900 group-hover:text-[#138496] transition-colors leading-snug"
                
            p_meta = text_div.find("p", class_=lambda c: c and "text-xs" in c)
            if p_meta:
                meta_text = p_meta.get_text().strip()
                chips = [chip.strip() for chip in meta_text.split("·")]
                
                chip_container = soup.new_tag("div")
                chip_container["class"] = "flex items-center gap-2 flex-wrap"
                
                for chip in chips:
                    span_chip = soup.new_tag("span")
                    span_chip["class"] = "inline-flex items-center rounded-md bg-slate-100 px-2 py-0.5 text-[10px] font-medium text-slate-600"
                    span_chip.string = chip
                    chip_container.append(span_chip)
                
                p_meta.replace_with(chip_container)
                
        # replace action span with arrow icon div
        action_div = soup.new_tag("div")
        action_div["class"] = "flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"
        
        svg_code = '<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>'
        svg_tag = BeautifulSoup(svg_code, "html.parser").svg
        action_div.append(svg_tag)
        
        span_action.replace_with(action_div)
        
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Updated {file_path}")
