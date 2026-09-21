import os
import re

def sync_reg_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to determine the correct relative depth to root

    # Let's just find an existing known link to anchor our relative path
    # 'href=".*?/pages/publications/index.html"'
    prefix_match = re.search(r'href="([^"]*)pages/publications/index.html"', content)
    prefix = prefix_match.group(1) if prefix_match else ""

    # The block we are replacing is the "Regulation & Supervision" nav block.
    # We will use regex to find the start of `<div class="relative group">\s*<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="[^"]*pages/regulation-and-supervision/index.html"`
    # And we replace the entire div.
    
    # Let's match the block accurately
    pattern = re.compile(r'<div class="relative group">\s*<a class="flex items-center gap-1\.5 text-slate-100 transition hover:text-\[#138496\]" href="[^"]*pages/regulation-and-supervision/index\.html" id="Nav-[^"]*">\s*Regulation &amp; Supervision\s*<svg[^>]*>.*?</svg>\s*</a>\s*<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">\s*<div class="bg-white rounded-\[16px\] shadow-lg border border-slate-200 py-5 px-6 w-\[720px\] grid grid-cols-3 gap-x-6">.*?</div>\s*</div>\s*</div>', re.DOTALL)
    
    new_block = f"""<div class="relative group">
<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{prefix}pages/regulation-and-supervision/index.html" id="Nav-Regulation-Supervision">
Regulation &amp; Supervision
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
</a>
<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-5 px-6 w-[720px] grid grid-cols-2 gap-x-6">
<!-- Column 1: Regulations -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Regulations</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bfr/index.html">Banks &amp; Financial Institutions</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/fxm/index.html">Foreign Exchange Management</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/psd/index.html">Payment Systems</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bkd/index.html">Banking Department</a>
</div>
<!-- Column 2: Supervisions -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Supervisions</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/bsd/index.html">Bank Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/fisd/index.html">Financial Institutions Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/mfd/index.html">Microfinance Supervision</a>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/regulation-and-supervision/nbfisd/index.html">Non-Bank Entities Supervision</a>
</div>
</div>
</div>
</div>"""

    new_content = pattern.sub(new_block, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

count = 0
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if sync_reg_nav(filepath):
                print(f"Synced global nav in {filepath}")
                count += 1

print(f"Total files synced: {count}")
