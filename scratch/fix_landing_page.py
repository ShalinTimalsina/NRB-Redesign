import re

filepath = 'pages/monetary-policy/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Data & Reports
data_reports_old = '''<div class="w-full rounded-[20px] bg-white border border-slate-200 p-6 shadow-sm flex flex-col justify-between">
<div class="flex items-center justify-between border-b border-slate-100 pb-3 mb-4">
<span class="text-xs font-semibold uppercase tracking-wider text-[#138496]">Recent Documents</span>
<span class="text-xs bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md font-semibold">FY 2083/84</span>
</div>
<div class="space-y-3 text-sm text-slate-600">
<a class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100 hover:border-[#138496]/30 transition-colors" href="https://www.nrb.org.np/pdm/monetary-operation-summary-fy-2083-084-up-to-2083-06-03/" target="_blank">
<span class="font-semibold text-slate-900">Monetary Operation Summary FY 2083-084</span>
<span class="text-xs font-medium text-[#138496]">Sep 19, 2026</span>
</a>
<a class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100 hover:border-[#138496]/30 transition-colors" href="https://www.nrb.org.np/pdm/deposit-collection-result-update-f-y-2083-84-up-to-2083-06-02/" target="_blank">
<span class="font-semibold text-slate-900">Deposit Collection Result Update</span>
<span class="text-xs font-medium text-[#138496]">Sep 18, 2026</span>
</a>
<a class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100 hover:border-[#138496]/30 transition-colors" href="https://www.nrb.org.np/pdm/standing-deposit-facility-update-2083-06-02/" target="_blank">
<span class="font-semibold text-slate-900">Standing Deposit Facility Update</span>
<span class="text-xs font-medium text-[#138496]">Sep 18, 2026</span>
</a>
</div>
</div>'''

hub_card_template = '''<a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#" target="_blank">
<div class="flex items-start gap-4">
<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
</div>
<div class="flex flex-col gap-1.5">
<p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">{title}</p>
<div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">DOC</span><span class="text-slate-300 px-1.5">•</span><span>{size}</span><span class="text-slate-300 px-1.5">•</span><span>{date}</span></div>
</div>
</div>
<div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
</a>'''

data_reports_new = '<div class="flex flex-col gap-3 w-full">\n' + \
    hub_card_template.format(title='Monetary Operation Summary FY 2083-084', size='110 KB', date='Sep 19, 2026') + '\n' + \
    hub_card_template.format(title='Deposit Collection Result Update', size='158 KB', date='Sep 18, 2026') + '\n' + \
    hub_card_template.format(title='Standing Deposit Facility Update', size='51 KB', date='Sep 18, 2026') + '\n</div>'

content = content.replace(data_reports_old, data_reports_new)


# 2. Fix Circulars
circulars_old_pattern = r'<div class="grid grid-cols-3 gap-6">\n<div class="nrb-elevated-card.*?</div>\n</div>\n</div>\n</section>\n<!-- 5. NOTICES -->'
circulars_new = '<div class="flex flex-col gap-3">\n' + \
    hub_card_template.format(title='Interest Rate Corridor Adjustment', size='1.2 MB', date='Shrawan 2081') + '\n' + \
    hub_card_template.format(title='Open Market Operations Schedule', size='850 KB', date='Bhadra 2081') + '\n' + \
    hub_card_template.format(title='Cash Reserve Ratio Compliance', size='540 KB', date='Ashadh 2081') + '\n</div>\n</div>\n</section>\n<!-- 5. NOTICES -->'

content = re.sub(circulars_old_pattern, circulars_new, content, flags=re.DOTALL)

# 3. Fix Notices
notices_old_pattern = r'<div class="grid grid-cols-3 gap-6">\n<a class="nrb-elevated-card.*?</a>\n</div>\n</div>\n</section>\n<!-- 6. POLICIES & PROCEDURES -->'
notices_new = '<div class="flex flex-col gap-3">\n' + \
    hub_card_template.format(title='असोज २ गते रु.३० अर्बको १ महिने निक्षेप संकलन बोलकबोल सम्बन्धी सूचना', size='230 KB', date='September 18, 2026') + '\n' + \
    hub_card_template.format(title='भदौ ३१ गते रु.६० अर्बको १ महिने निक्षेप संकलन बोलकबोल सम्बन्धी सूचना', size='220 KB', date='September 16, 2026') + '\n' + \
    hub_card_template.format(title='ब्याजदरसम्बन्धी विवरण उपलब्ध गराउने सम्बन्धमा', size='150 KB', date='August 24, 2026') + '\n</div>\n</div>\n</section>\n<!-- 6. POLICIES & PROCEDURES -->'

content = re.sub(notices_old_pattern, notices_new, content, flags=re.DOTALL)

# 4. Fix Policies & Procedures
policies_old_pattern = r'<a class="block nrb-elevated-card bg-\[#25295B\].*?</a>\n</div>\n</div>\n</section>'

policies_new = '''<a class="hub-card nrb-elevated-card group flex flex-col rounded-[20px] bg-[#25295B] border border-[#25295B] p-8 hover:border-[#138496] transition-colors" href="#">
<p class="text-xs font-semibold uppercase tracking-[0.22em] text-[#138496] mb-3">Key Framework</p>
<h3 class="font-semibold text-xl text-white mb-2 group-hover:text-[#138496] transition-colors">Monetary Policy for FY 2083/84</h3>
<p class="text-sm text-slate-300 leading-6 flex-grow">Full monetary policy statement for fiscal year 2083/84 including policy stance, projections, and implementation measures.</p>
<span class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496]">Open Document <svg class="dir-row-arrow h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></span>
</a>
</div>
</div>
</section>'''

content = re.sub(policies_old_pattern, policies_new, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated monetary-policy/index.html layout components.')
