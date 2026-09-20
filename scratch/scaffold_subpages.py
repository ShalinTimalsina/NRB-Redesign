import os
import re

template_path = 'pages/monetary-policy/notices/index.html'

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

def generate_subpage(folder_name, title, desc, breadcrumb, md_file, card_icon_svg, section_title):
    os.makedirs(f'pages/monetary-policy/{folder_name}', exist_ok=True)
    out_path = f'pages/monetary-policy/{folder_name}/index.html'
    
    # Extract first 4 items from MD file
    documents = []
    if md_file and os.path.exists(md_file):
        with open(md_file, 'r', encoding='utf-8') as mf:
            lines = mf.readlines()
            for line in lines:
                if line.startswith('- ['):
                    # Parse: - [Title](url) Date Size
                    match = re.match(r'- \[([^\]]+)\]\(([^)]+)\) (.+) (\d+\.\d+ [A-Za-z]+)', line.strip())
                    if match:
                        title_str, url, date, size = match.groups()
                    else:
                        match2 = re.match(r'- \[([^\]]+)\]\(([^)]+)\) (.+)', line.strip())
                        if match2:
                            title_str, url, rest = match2.groups()
                            # Try to split rest into Date and Size
                            parts = rest.rsplit(' ', 2)
                            if len(parts) == 3:
                                date = parts[0]
                                size = parts[1] + ' ' + parts[2]
                            else:
                                date = rest
                                size = "100 KB"
                        else:
                            continue
                            
                    documents.append({
                        'title': title_str,
                        'url': url,
                        'date': date,
                        'size': size.upper()
                    })
                if len(documents) >= 4:
                    break
    
    # Build HTML for documents
    docs_html = ""
    for doc in documents:
        docs_html += f'''<a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="{doc['url']}" target="_blank">
<div class="flex items-start gap-4">
<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
{card_icon_svg}
</div>
<div class="flex flex-col gap-1.5">
<p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">{doc['title']}</p>
<div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">DOC</span><span class="text-slate-300 px-1.5">•</span><span>{doc['size']}</span><span class="text-slate-300 px-1.5">•</span><span>{doc['date']}</span></div>
</div>
</div>
<div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
</a>\n'''
        
    # Replace content in template
    # 1. Update Title and Breadcrumb
    new_content = template
    new_content = re.sub(r'<span class="text-slate-700">Public Debt Notices</span>', f'<span class="text-slate-700">{breadcrumb}</span>', new_content)
    new_content = re.sub(r'<h1 class="text-2xl font-bold text-slate-900 mb-3">Public Debt – Notices</h1>', f'<h1 class="text-2xl font-bold text-slate-900 mb-3">{title}</h1>', new_content)
    new_content = re.sub(r'<p class="text-base text-slate-600 leading-relaxed max-w-2xl">.*?</p>', f'<p class="text-base text-slate-600 leading-relaxed max-w-2xl">{desc}</p>', new_content)
    
    # 2. Update list header
    new_content = re.sub(r'<p class="text-xs font-semibold uppercase tracking-\[0\.18em\] text-slate-500">4 Notices</p>', f'<p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">{len(documents)} Documents</p>', new_content)
    # Remove the "Public Debt Management" pill completely
    new_content = re.sub(r'<span class="text-xs bg-slate-100 text-slate-700 px-3 py-1\.5 rounded-full font-semibold">Public Debt Management</span>', '', new_content)
    
    # 3. Replace document list
    docs_pattern = r'<div class="flex flex-col gap-3">.*?</div>\n</div>\n</section>'
    new_list_html = f'<div class="flex flex-col gap-3">\n{docs_html}</div>\n</div>\n</section>'
    new_content = re.sub(docs_pattern, new_list_html, new_content, flags=re.DOTALL)
    
    # 4. Make sure hrefs back to root are correct if nesting is same (it is, pages/monetary-policy/folder/index.html)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Generated {out_path}")

doc_svg = '<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>'

# 1. Monetary Operations
generate_subpage(
    'monetary-operations', 
    'Monetary Operations', 
    'Daily operation summaries, deposit collection results, and standing deposit facility updates.',
    'Monetary Operations',
    'NRB Page md files/Monetory Management/monetary-operations-archives-the-official-site-of-the-central-bank-of-nepal-20260920184632.md',
    doc_svg,
    'Operations'
)

# 2. Notices
generate_subpage(
    'notices', 
    'Monetary Policy Notices', 
    'Public notices, announcements, and key communications regarding monetary policy.',
    'Notices',
    'NRB Page md files/laws-policies/notices-archives-the-official-site-of-the-central-bank-of-nepal-20260906003107.md',
    doc_svg,
    'Notices'
)

# 3. Policies & Procedures
generate_subpage(
    'policies-procedures', 
    'Policies & Procedures', 
    'Annual monetary policy statements, periodic reviews, and comprehensive macroeconomic reports.',
    'Policies & Procedures',
    'NRB Page md files/laws-policies/monetary-policy-archives-the-official-site-of-the-central-bank-of-nepal-20260906003136.md',
    doc_svg,
    'Policies'
)

# 4. Circulars
generate_subpage(
    'circulars', 
    'Circulars', 
    'Official circulars and directives issued to banks and financial institutions.',
    'Circulars',
    'NRB Page md files/laws-policies/rules-&-by-laws-archives-the-official-site-of-the-central-bank-of-nepal-20260906002803.md',
    doc_svg,
    'Circulars'
)

# 5. Data & Reports
generate_subpage(
    'data-reports', 
    'Data & Reports', 
    'Macroeconomic data, interest rate bulletins, and detailed financial reports.',
    'Data & Reports',
    'NRB Page md files/laws-policies/other-policies-archives-the-official-site-of-the-central-bank-of-nepal-20260906003129.md',
    doc_svg,
    'Data & Reports'
)

