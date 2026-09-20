import re

def reformat_meta_string(meta_str):
    # E.g. "September 19, 2026 · 26.79 kb"
    # We want it to be: DOC • 26.79 kb • September 19, 2026
    
    parts = meta_str.split('·')
    if len(parts) == 2:
        date_str = parts[0].strip()
        size_str = parts[1].strip()
        # capitalize KB if it's kb
        size_str = size_str.upper() if size_str.endswith('kb') else size_str
        
        return f'<div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">DOC</span><span class="text-slate-300 px-1.5">•</span><span>{size_str}</span><span class="text-slate-300 px-1.5">•</span><span>{date_str}</span></div>'
    return meta_str

def update_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the document rows
    # The structure starts with: <a class="hub-card nrb-elevated-card...
    
    def replacer(match):
        doc = match.group(0)
        
        # 1. Update the title text styles
        doc = re.sub(
            r'<div>\s*<p class="text-sm font-semibold text-slate-900 group-hover:text-\[#138496\] transition-colors">(.*?)</p>\s*<p class="text-xs text-slate-500 mt-1">(.*?)</p>\s*</div>',
            lambda m: f'<div class="flex flex-col gap-1.5">\n<p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">{m.group(1)}</p>\n{reformat_meta_string(m.group(2))}\n</div>',
            doc,
            flags=re.DOTALL
        )
        
        # 2. Update the left icon
        doc = re.sub(
            r'<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24">.*?</svg>',
            r'<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>',
            doc,
            flags=re.DOTALL
        )
        
        # 3. Update the trailing right arrow
        doc = re.sub(
            r'<svg class="dir-row-arrow h-5 w-5 text-slate-400 group-hover:text-\[#138496\] shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24">.*?</svg>',
            r'<div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>',
            doc,
            flags=re.DOTALL
        )
        
        return doc
        
    pattern = r'<a class="hub-card nrb-elevated-card flex items-center justify-between.*?</a>'
    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Updated document layout in {filepath}')

update_cards('pages/monetary-policy/monetary-operations/index.html')
update_cards('pages/monetary-policy/notices/index.html')
