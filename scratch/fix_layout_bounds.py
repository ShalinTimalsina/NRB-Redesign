from pathlib import Path

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to make the body a slightly darker neutral color on ultra-wide screens, 
    # and give the page frame a perfect 1440px wrapper with a border and shadow so it looks like a Figma canvas.
    
    old_body = 'body class="min-w-[1440px] bg-[#F8FAFC] text-slate-900 antialiased"'
    new_body = 'body class="bg-[#E2E8F0] text-slate-900 antialiased flex flex-col items-center min-h-screen"'
    
    # Also handle pages that might have bg-slate-50
    old_body2 = 'body class="min-w-[1440px] bg-slate-50 text-slate-900 antialiased"'
    
    # The page frame should be strictly 1440px max, with a white/f8 background and shadow/border
    old_frame = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC]" id="Page-Frame"'
    new_frame = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC] min-h-screen shadow-2xl border-x border-slate-300 relative overflow-hidden" id="Page-Frame"'
    
    old_frame2 = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px]"'
    new_frame2 = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC] min-h-screen shadow-2xl border-x border-slate-300 relative overflow-hidden"'

    changed = False
    
    if old_body in html:
        html = html.replace(old_body, new_body)
        changed = True
    elif old_body2 in html:
        html = html.replace(old_body2, new_body)
        changed = True
        
    if old_frame in html:
        html = html.replace(old_frame, new_frame)
        changed = True
    elif old_frame2 in html:
        html = html.replace(old_frame2, new_frame2)
        changed = True
        
    if changed:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Fixed layout bounds in {count} files.')
