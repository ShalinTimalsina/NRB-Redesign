import os
import re

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

# The regex to find the existing Publications link. It varies slightly based on indentation and href depth.
nav_pattern = re.compile(
    r'<a[^>]*?id="Nav-Publications"[^>]*>Publications</a>',
    re.IGNORECASE
)

new_mega_menu_template = """<div class="relative group">
<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{depth}pages/publications/index.html" id="Nav-Publications">
Publications
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
</a>
<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-5 px-6 w-[1080px] grid grid-cols-4 gap-x-6 text-left">
<!-- Column 1: Research & Analysis -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Research & Analysis</div>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/economic-review/index.html">
<span class="block">Economic Review</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Periodic reviews of economic trends.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/macroeconomic-reports/index.html">
<span class="block">Macroeconomic Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Monthly and annual economic data.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/working-papers/index.html">
<span class="block">NRB Working Papers</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Research papers from NRB economists.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/publications/study-reports/index.html">
<span class="block">Study Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">In-depth research and study findings.</span>
</a>
</div>

<!-- Column 2: Institutional Reports -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Institutional Reports</div>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/annual-reports/index.html">
<span class="block">Annual Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Comprehensive yearly performance reports.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/financial-stability/index.html">
<span class="block">Financial Stability Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Assessments of financial system health.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/publications/economic-activities/index.html">
<span class="block">Economic Activities Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Regional and national economic activity.</span>
</a>
</div>

<!-- Column 3: Special Publications -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Special Publications</div>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/special-publications/index.html">
<span class="block">Special Publications</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Ad-hoc reports and special releases.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/golden-jubilee/index.html">
<span class="block">Golden Jubilee Publications</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">50th anniversary commemorative releases.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="{depth}pages/publications/arthabodh/index.html">
<span class="block">Arthabodh</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Financial literacy and awareness.</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/publications/know-your-bank-notes/index.html">
<span class="block">Know Your Bank Notes</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Security features and banknote guides.</span>
</a>
</div>

<!-- Column 4: Featured Publications -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Featured Publications</div>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="#">
<span class="block text-xs font-semibold text-[#138496] mb-1 uppercase tracking-wider">Latest Publication</span>
<span class="block font-bold">Q1 2026 Macroeconomic Report</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg mb-1" href="#">
<span class="block text-xs font-semibold text-[#138496] mb-1 uppercase tracking-wider">Latest Report</span>
<span class="block font-bold">Annual Report 2025/26</span>
</a>
<a class="px-2 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="#">
<span class="block text-xs font-semibold text-[#138496] mb-1 uppercase tracking-wider">Latest Working Paper</span>
<span class="block font-bold">Digital Currency Impact Study</span>
</a>
</div>
</div>
</div>
</div>"""

count = 0
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            # Determine depth
            rel_path = os.path.relpath(filepath, base_dir)
            depth_count = rel_path.count(os.sep)
            depth = '../' * depth_count
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # If the mega menu is already injected, skip
            if 'Research & Analysis' in content and 'Know Your Bank Notes' in content and 'Nav-Publications' in content:
                continue
            
            # Search for the existing single link
            if nav_pattern.search(content):
                replacement = new_mega_menu_template.format(depth=depth)
                new_content = nav_pattern.sub(replacement, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Updated {count} HTML files with the new Publications Mega Menu.")
