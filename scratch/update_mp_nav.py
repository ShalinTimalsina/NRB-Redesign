"""
Replace the plain Monetary Policy <a> nav entry with a dropdown <div class="relative group">
across all HTML files, preserving each file's specific href depth.
"""
import os, glob, re

# The old pattern (href varies per file depth)
OLD_PATTERN = re.compile(
    r'<a class="text-slate-100 transition hover:text-\[#138496\]" '
    r'href="([^"]*monetary-policy/index\.html)" '
    r'id="Nav-Monetary-Policy">Monetary Policy</a>'
)

def make_new_block(href):
    return (
        '<div class="relative group">\n'
        f'<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{href}" id="Nav-Monetary-Policy">\n'
        'Monetary Policy\n'
        '<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>\n'
        '</a>\n'
        '<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">\n'
        '<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-3 px-2 w-72 flex flex-col">\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#overview">\n'
        '<span class="block">Overview</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy stance, objectives, and current rates.</span>\n'
        '</a>\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#monetary-operations">\n'
        '<span class="block">Monetary Operations</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Open market operations and liquidity management.</span>\n'
        '</a>\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#data-reports">\n'
        '<span class="block">Data &amp; Reports</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Policy documents, bulletins, and data series.</span>\n'
        '</a>\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#circulars">\n'
        '<span class="block">Circulars</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Official circulars issued to regulated institutions.</span>\n'
        '</a>\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#notices">\n'
        '<span class="block">Notices</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Public notices related to monetary policy.</span>\n'
        '</a>\n'
        f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{href}#policies-procedures">\n'
        '<span class="block">Policies &amp; Procedures</span>\n'
        '<span class="block text-xs text-slate-400 font-normal mt-0.5">Operational frameworks and procedural guidelines.</span>\n'
        '</a>\n'
        '</div>\n'
        '</div>\n'
        '</div>'
    )

updated = []
for path in glob.glob('**/*.html', recursive=True):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = OLD_PATTERN.search(content)
    if not m:
        continue
    
    href = m.group(1)
    new_block = make_new_block(href)
    new_content = OLD_PATTERN.sub(new_block, content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    updated.append(path)

print(f"Updated {len(updated)} files:")
for p in updated:
    print(f"  {p}")
