import os
import glob
import re

html_files = glob.glob(r"c:\Users\LOQ\Desktop\NRB Redesign\**\*.html", recursive=True)

nav_template = """<div class="relative group">
<a id="Nav-Regulations" href="{prefix}pages/regulations/index.html" class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]">
Regulations
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path></svg>
</a>
<div class="absolute left-0 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-3 w-64 flex flex-col">
<div class="px-5 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Laws &amp; Legislation</div>
<a href="{prefix}pages/regulations/acts.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Acts</a>
<a href="{prefix}pages/regulations/rules-and-bylaws.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors mb-1">Rules and Bylaws</a>
<div class="px-5 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-t border-slate-100 mb-1 mt-1">Policies &amp; Guidelines</div>
<a href="{prefix}pages/regulations/notices.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Notices</a>
<a href="{prefix}pages/regulations/guidelines-and-manuals.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Guidelines &amp; Manuals</a>
<a href="{prefix}pages/regulations/other-policies.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Other Policies</a>
<a href="{prefix}pages/regulations/monetary-policy.html" class="px-5 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Monetary Policy</a>
</div>
</div>
</div>
"""

for file_path in html_files:
    if "node_modules" in file_path or ".gemini" in file_path or "scratch" in file_path:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if 'id="Nav-Regulations"' in content:
        continue
        
    # More robust regex: find the monetary policy link and extract the prefix
    match = re.search(r'<a[^>]*href="([^"]*)pages/monetary-policy/index.html"[^>]*id="Nav-Monetary-Policy"[^>]*>', content)
    if not match:
        # Check if id is before href
        match = re.search(r'<a[^>]*id="Nav-Monetary-Policy"[^>]*href="([^"]*)pages/monetary-policy/index.html"[^>]*>', content)
        if not match:
            # Maybe the order is different, let's just search for the href and ID anywhere in the tag
            match = re.search(r'<a(?=.*?id="Nav-Monetary-Policy")(?=.*?href="([^"]*)pages/monetary-policy/index.html")[^>]*>', content)

    if not match:
        print(f"Could not find Nav-Monetary-Policy in {file_path}")
        continue
            
    prefix = match.group(1)
    
    # We replace the entire matched tag with the template + the tag itself
    full_tag = match.group(0)
    replacement = nav_template.replace('{prefix}', prefix) + full_tag
    
    # We must replace only the first occurrence of full_tag
    new_content = content.replace(full_tag, replacement, 1)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated nav in {file_path}")
    else:
        print(f"Failed to replace in {file_path}")
