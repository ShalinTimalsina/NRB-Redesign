import os
import re

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

nav_pattern = re.compile(
    r'<a[^>]*?id="Nav-Statistics"[^>]*>Statistics</a>',
    re.IGNORECASE
)

new_mega_menu_template = """<div class="relative group">
<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{depth}pages/statistics/index.html" id="Nav-Statistics">
Statistics
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
</a>
<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-5 px-6 w-[1080px] grid grid-cols-4 gap-x-6 text-left">
<!-- Column 1: Macroeconomic -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Macroeconomic Statistics</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/statistics/macroeconomic/index.html">
<span class="block">Macroeconomic Statistics</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5 leading-relaxed">Inflation, economic activity, surveys and macroeconomic indicators.</span>
</a>
</div>

<!-- Column 2: Financial Sector -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Financial Sector Statistics</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/statistics/financial-sector/index.html">
<span class="block">Financial Sector Statistics</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5 leading-relaxed">Banking, microfinance and financial sector performance data.</span>
</a>
</div>

<!-- Column 3: Monetary & Forex -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Monetary & Forex Statistics</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/statistics/monetary-forex/index.html">
<span class="block">Monetary & Forex Statistics</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5 leading-relaxed">Monetary operations, interest rates and foreign exchange information.</span>
</a>
</div>

<!-- Column 4: Financial Inclusion -->
<div class="flex flex-col">
<div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-3">Financial Inclusion & Payments</div>
<a class="px-2 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{depth}pages/statistics/financial-inclusion/index.html">
<span class="block">Financial Inclusion & Payments</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5 leading-relaxed">Financial inclusion indicators, payment systems and access metrics.</span>
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
            
            rel_path = os.path.relpath(filepath, base_dir)
            depth_count = rel_path.count(os.sep)
            depth = '../' * depth_count
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'Financial Inclusion & Payments' in content and 'Macroeconomic Statistics' in content and 'Nav-Statistics' in content:
                continue
            
            if nav_pattern.search(content):
                replacement = new_mega_menu_template.format(depth=depth)
                new_content = nav_pattern.sub(replacement, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Updated {count} HTML files with the new Statistics Mega Menu.")
