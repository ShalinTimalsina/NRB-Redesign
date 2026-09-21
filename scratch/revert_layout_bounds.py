from pathlib import Path

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # The current body that we changed it to
    current_body = 'body class="bg-[#E2E8F0] text-slate-900 antialiased flex flex-col items-center min-h-screen"'
    # We will revert to the standard one. The safest is to revert to the old_body 
    # since we can't tell if it was bg-slate-50 or bg-[#F8FAFC] originally for all files, 
    # but bg-[#F8FAFC] is the global standard we've been using in nrb.html.
    revert_body = 'body class="min-w-[1440px] bg-[#F8FAFC] text-slate-900 antialiased"'

    # The current frame that we changed it to
    current_frame = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC] min-h-screen shadow-2xl border-x border-slate-300 relative overflow-hidden" id="Page-Frame"'
    revert_frame = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC]" id="Page-Frame"'
    
    current_frame2 = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px] bg-[#F8FAFC] min-h-screen shadow-2xl border-x border-slate-300 relative overflow-hidden"'
    revert_frame2 = 'div class="nrb-page-frame mx-auto w-full max-w-[1440px]"'

    if current_body in html:
        html = html.replace(current_body, revert_body)
        changed = True
        
    if current_frame in html:
        html = html.replace(current_frame, revert_frame)
        changed = True
    elif current_frame2 in html:
        html = html.replace(current_frame2, revert_frame2)
        changed = True

    if changed:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Reverted layout bounds in {count} files.')
