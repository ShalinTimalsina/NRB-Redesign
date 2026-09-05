import glob
import re

files = glob.glob('pages/about/*.html') + ['nrb.html']

old_style = r'\.hub-card\s*\{\s*transition:\s*transform\s+150ms\s+ease,\s*box-shadow\s+150ms\s+ease(?:,\s*border-color\s+150ms\s+ease)?;?\s*\}\s*\.hub-card:hover\s*\{\s*transform:\s*translateY\(-2px\);\s*box-shadow:\s*0\s+6px\s+20px\s+rgba\(15,23,42,0\.08\);?\s*\}'

new_style = '''.hub-card { transition: border-color 200ms ease, box-shadow 200ms ease, background-color 200ms ease; }
        .hub-card:hover { border-color: rgba(30, 58, 95, 0.2); box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05); }'''

old_arrow_style = r'\.dir-row-arrow\s*\{\s*transition:\s*transform\s+150ms\s+ease;?\s*\}\s*\.dir-row:hover\s+\.dir-row-arrow\s*\{\s*transform:\s*translateX\(3px\);?\s*\}'

new_arrow_style = '''.dir-row-arrow { transition: transform 200ms ease-out, color 200ms ease-out; }
        .dir-row:hover .dir-row-arrow { transform: translateX(2px); }'''

for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace hub-card jumping transform with smooth, disciplined border/shadow transition
    html = re.sub(old_style, new_style, html)
    
    # Replace arrow jump with smooth 200ms 2px shift
    html = re.sub(old_arrow_style, new_arrow_style, html)
    
    # Fix any inline hover:scale or harsh jumps
    html = html.replace('group-hover:scale-105', '')
    html = html.replace('hover:scale-105', '')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Disciplined animation audit completed for {fpath}")

print("All pages audited successfully.")
