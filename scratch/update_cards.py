import re

def update_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the document count text
    content = content.replace('10 Documents', '4 Documents')
    content = content.replace('10 Notices', '4 Notices')

    # 2. Extract the first 4 documents and discard the rest
    # Find the start of the document list
    list_match = re.search(r'<div class="flex flex-col gap-3">', content)
    list_start = list_match.end()
    
    # Find the end of the document list
    list_end = content.find('</div>\n<div class="mt-10 pt-6 border-t border-slate-100">')
    
    documents_html = content[list_start:list_end]
    
    # Split documents by comment
    docs = re.split(r'<!-- Document \d+ -->|<!-- Notice \d+ -->', documents_html)
    docs = [d for d in docs if d.strip()]
    
    # Keep only the first 4
    first_4 = docs[:4]
    
    # Process each document
    processed_docs = []
    for i, doc in enumerate(first_4):
        # 1. Update main link tag classes
        doc = re.sub(
            r'<a class="dir-row group flex items-center justify-between p-5 bg-white border border-slate-200 rounded-\[16px\] hover:border-\[#25295B\]/30 hover:shadow-sm transition-all"',
            r'<a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors"',
            doc
        )
        # 2. Update icon container
        doc = re.sub(
            r'<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-\[12px\] bg-slate-100 text-\[#25295B\] border border-slate-100 group-hover:bg-\[#25295B\] group-hover:text-white transition-colors">',
            r'<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">',
            doc
        )
        # 3. Update inner SVG icon (replace whatever it is with the document icon)
        doc = re.sub(
            r'<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24">.*?</svg>',
            r'<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>',
            doc,
            flags=re.DOTALL
        )
        # 4. Update trailing arrow SVG
        doc = re.sub(
            r'<svg class="dir-row-arrow h-5 w-5 text-slate-400 group-hover:text-\[#138496\] shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"><path d="M5 12h14" stroke-linecap="round" stroke-linejoin="round"></path><path d="m12 5 7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
            r'<svg class="dir-row-arrow h-5 w-5 text-slate-400 group-hover:text-[#138496] shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>',
            doc
        )
        # 5. Fix margin on the meta text
        doc = doc.replace('class="text-xs text-slate-500 mt-0.5"', 'class="text-xs text-slate-500 mt-1"')
        
        prefix = 'Document' if 'monetary' in filepath else 'Notice'
        processed_docs.append(f'\n<!-- {prefix} {i+1} -->{doc}')
        
    # Reassemble
    new_documents_html = ''.join(processed_docs) + '\n'
    
    # Replace in main content
    new_content = content[:list_start] + new_documents_html + content[list_end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Updated cards in {filepath}')

update_cards('pages/monetary-policy/monetary-operations/index.html')
update_cards('pages/monetary-policy/notices/index.html')
