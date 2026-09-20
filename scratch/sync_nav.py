import re

filepath = 'pages/monetary-policy/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Global Nav Dropdown for Monetary Policy
nav_dropdown_old = '''<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#overview">
<span class="block">Overview</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy stance, objectives, and current rates.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#monetary-operations">
<span class="block">Monetary Operations</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Open market operations and liquidity management.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#data-reports">
<span class="block">Data &amp; Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy documents, bulletins, and data series.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#circulars">
<span class="block">Circulars</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Official circulars issued to regulated institutions.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#notices">
<span class="block">Notices</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Public notices related to monetary policy.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#policies-procedures">
<span class="block">Policies &amp; Procedures</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Operational frameworks and procedural guidelines.</span>
</a>'''

nav_dropdown_new = '''<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/index.html#overview">
<span class="block">Overview</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy stance, objectives, and current rates.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/monetary-operations/index.html">
<span class="block">Monetary Operations</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Open market operations and liquidity management.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/data-reports/index.html">
<span class="block">Data &amp; Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy documents, bulletins, and data series.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/circulars/index.html">
<span class="block">Circulars</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Official circulars issued to regulated institutions.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/notices/index.html">
<span class="block">Notices</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Public notices related to monetary policy.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="../../pages/monetary-policy/policies-procedures/index.html">
<span class="block">Policies &amp; Procedures</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Operational frameworks and procedural guidelines.</span>
</a>'''

content = content.replace(nav_dropdown_old, nav_dropdown_new)

# 2. Update Quick Access Section
quick_access_old_pattern = r'<div class="grid grid-cols-2 gap-6">\n<!-- Card 1: Monetary Operations -->.*?</a>\n</div>\n</div>\n</section>'

# Define semantic SVG icons
icon_overview = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>'
icon_monetary = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>'
icon_data = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/></svg>'
icon_circulars = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>'
icon_notices = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>'
icon_policies = '<svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>'

arrow_svg = '<svg class="dir-row-arrow h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>'

def create_card(title, desc, icon, link):
    return f'''<a class="hub-card nrb-elevated-card group flex flex-col rounded-[20px] bg-white border border-slate-200 p-8 hover:border-[#25295B]/20 transition-all" href="{link}">
<div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] mb-5 group-hover:bg-[#25295B] group-hover:text-white transition-colors">
{icon}
</div>
<h3 class="font-semibold text-lg text-slate-900 mb-2 group-hover:text-[#138496] transition-colors">{title}</h3>
<p class="text-sm text-slate-600 leading-6 flex-grow">{desc}</p>
<span class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496]">Explore {arrow_svg}</span>
</a>'''

cards = [
    create_card("Overview", "Policy stance, objectives, and current rates.", icon_overview, "#overview"),
    create_card("Monetary Operations", "Open market operations and liquidity management.", icon_monetary, "monetary-operations/index.html"),
    create_card("Data & Reports", "Policy documents, bulletins, and data series.", icon_data, "data-reports/index.html"),
    create_card("Circulars", "Official circulars issued to regulated institutions.", icon_circulars, "circulars/index.html"),
    create_card("Notices", "Public notices related to monetary policy.", icon_notices, "notices/index.html"),
    create_card("Policies & Procedures", "Operational frameworks and procedural guidelines.", icon_policies, "policies-procedures/index.html")
]

quick_access_new = f'''<div class="grid grid-cols-3 gap-6">
{chr(10).join(cards)}
</div>
</div>
</section>'''

content = re.sub(quick_access_old_pattern, quick_access_new, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Nav and Quick Access synced.")
