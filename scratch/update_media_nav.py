import os

old_nav = '<a class="text-slate-100 transition hover:text-[#138496]" href="../pages/notices/index.html" id="Nav-Media &amp; Speeches">Media &amp; Speeches</a>'
old_nav_root = '<a class="text-slate-100 transition hover:text-[#138496]" href="pages/notices/index.html" id="Nav-Media &amp; Speeches">Media &amp; Speeches</a>'
old_nav_depth3 = '<a class="text-slate-100 transition hover:text-[#138496]" href="../../pages/notices/index.html" id="Nav-Media &amp; Speeches">Media &amp; Speeches</a>'

def get_new_nav(depth):
    prefix = '../' * depth
    if depth == 0:
        prefix = ''
    
    return f"""<div class="relative group">
<a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="{prefix}pages/media-speeches/index.html" id="Nav-Media-Speeches">
Media &amp; Speeches
<svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
</a>
<div class="absolute left-1/2 -translate-x-1/2 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
<div class="bg-white rounded-[16px] shadow-lg border border-slate-200 py-3 px-2 w-72 flex flex-col">
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/media-speeches/media-releases/index.html">
<span class="block">Media Releases</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Official press statements.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/media-speeches/speeches/index.html">
<span class="block">Speeches</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Governor's official speeches.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/media-speeches/notices/index.html">
<span class="block">Notices</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Public notices from the Governor's office.</span>
</a>
<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/media-speeches/bok-kpp/index.html">
<span class="block">BOK-KPP Reports</span>
<span class="block text-xs text-slate-400 font-normal mt-0.5">Joint study reports.</span>
</a>
</div>
</div>
</div>"""

count = 0
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig = content
            # Determine depth
            rel_path = os.path.relpath(filepath, 'c:/Users/LOQ/Desktop/NRB Redesign')
            depth = len(rel_path.split(os.sep)) - 1
            
            new_nav = get_new_nav(depth)
            
            if old_nav in content:
                content = content.replace(old_nav, new_nav)
            elif old_nav_root in content:
                content = content.replace(old_nav_root, new_nav)
            elif old_nav_depth3 in content:
                content = content.replace(old_nav_depth3, new_nav)
                
            if content != orig:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Updated Media & Speeches nav in {count} files.")
