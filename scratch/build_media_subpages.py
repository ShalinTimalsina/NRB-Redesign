import os
import re

# 1. Base template structure
def get_header_and_footer(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = re.split(r'<main[^>]*>', content)
    header_part = parts[0] + '<main id="Main-Content">\n'
    footer_part = '\n</main>\n' + re.split(r'</main>', parts[1])[-1]
    return header_part, footer_part

# We extract header and footer from procurement/domestic-tenders/index.html (depth 3)
header, footer = get_header_and_footer('pages/procurement/domestic-tenders/index.html')

sections = [
    {
        'id': 'media-releases',
        'title': 'Media Releases',
        'desc': 'Official press statements and communications issued by the Office of the Governor.',
        'md_file': 'NRB Page md files/Media and Speeches/Media_Releases.md'
    },
    {
        'id': 'speeches',
        'title': 'Speeches',
        'desc': 'Official speeches delivered by the Governor of Nepal Rastra Bank.',
        'md_file': 'NRB Page md files/Media and Speeches/Governors_Speeches.md'
    },
    {
        'id': 'notices',
        'title': 'Notices',
        'desc': 'Official notices issued by the Office of the Governor.',
        'md_file': 'NRB Page md files/Media and Speeches/Notices_OFG.md'
    },
    {
        'id': 'bok-kpp',
        'title': 'BOK-KPP Study Reports',
        'desc': 'Joint study reports under the Bank of Korea – Knowledge Partnership Program.',
        'md_file': 'NRB Page md files/Media and Speeches/BOK_KPP_Study_Reports.md'
    }
]

def extract_list_items(md_path):
    items = []
    if not os.path.exists(md_path):
        return items
        
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_item = None
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # New item (e.g., ### 1. Title)
        if line.startswith('###') and line[4].isdigit():
            if current_item: items.append(current_item)
            title = line.split('.', 1)[-1].strip()
            current_item = {'title': title, 'meta': []}
        elif current_item and line.startswith('- '):
            meta_text = line[2:].strip()
            clean_meta = meta_text.replace('**', '')
            if clean_meta.startswith('Verified'):
                continue
            
            if 'Source:' in meta_text or 'PDF Link:' in meta_text:
                link = meta_text.split(':', 1)[-1].strip()
                if link.startswith('http'):
                    current_item['href'] = link
                elif link.startswith('['):
                    # Markdown link: [Text](URL)
                    m = re.search(r'\[(.*?)\]\((.*?)\)', link)
                    if m: current_item['href'] = m.group(2)
            else:
                current_item['meta'].append(meta_text.replace('**', ''))
                
    if current_item: items.append(current_item)
    return items

for sec in sections:
    sec_header = header.replace('<title>Domestic Tenders | Procurement | Nepal Rastra Bank</title>', f'<title>{sec["title"]} | Media & Speeches | Nepal Rastra Bank</title>')
    
    # Hero Banner
    hero = f"""
<section class="border-b border-slate-200 bg-white" id="Hero-Banner">
    <div class="nrb-section-shell py-10 lg:py-14">
        <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
            <a class="transition hover:text-[#25295B]" href="../../../nrb.html">Home</a>
            <span class="text-slate-300">/</span>
            <a class="transition hover:text-[#25295B]" href="../../media-speeches/index.html">Media & Speeches</a>
            <span class="text-slate-300">/</span>
            <span class="text-slate-700">{sec['title']}</span>
        </nav>
        <h1 class="text-2xl font-bold text-slate-900 mb-3">{sec['title']}</h1>
        <p class="text-base text-slate-600 leading-relaxed max-w-2xl">{sec['desc']}</p>
    </div>
</section>
"""

    items = extract_list_items(sec['md_file'])
    
    content_html = f"""
<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">
    <div class="nrb-section-shell">
        <div class="flex flex-col gap-3">
"""
    
    for item in items:
        href = item.get('href', '#')
        meta_html = ''
        for m in item['meta']:
            meta_html += f'<span class="px-1.5">•</span><span>{m}</span>'
            
        content_html += f"""
            <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="{href}" target="_blank">
                <div class="flex items-start gap-4">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                    </div>
                    <div class="flex flex-col gap-1.5">
                        <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">{item['title']}</p>
                        <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">Document</span>{meta_html}</div>
                    </div>
                </div>
                <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
            </a>
"""

    content_html += """
        </div>
    </div>
</section>
"""

    full_html = sec_header + hero + content_html + footer
    
    out_dir = f'pages/media-speeches/{sec["id"]}'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print(f"Scaffolded {out_path}")
