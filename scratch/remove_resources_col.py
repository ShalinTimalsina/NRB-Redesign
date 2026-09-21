from pathlib import Path
import re

count = 0
for p in Path('.').rglob('*.html'):
    if 'scratch' in p.parts:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # The resources column in Regulation & Supervision looks like this:
    # <!-- Column 3: Resources -->
    # <div class="flex flex-col">
    # <div class="px-2 py-2 text-xs font-semibold uppercase tracking-wider text-slate-400 border-b border-slate-100 mb-1">Resources</div>
    # ...
    # </div>
    # </div>
    # </div>
    # </div>
    # <div class="relative group">
    # <a class="flex items-center gap-1.5 text-slate-100 transition hover:text-[#138496]" href="../../../pages/publications/index.html" id="Nav-Publications">
    
    # We need to remove Column 3 and change the grid from grid-cols-3 to grid-cols-2 and w-[720px] to w-[480px]
    
    pattern = re.compile(
        r'(<!-- Column 3: Resources -->.*?</div>\s*</div>\s*</div>\s*</div>\s*<div class="relative group">\s*<a class="flex items-center gap-1\.5 text-slate-100 transition hover:text-\[#138496\]" href=".*?pages/publications/index\.html")',
        re.DOTALL
    )
    
    if '<!-- Column 3: Resources -->' in html:
        # We know it's there. Let's just do string replacement
        # First, fix the grid
        html = html.replace('w-[720px] grid grid-cols-3', 'w-[480px] grid grid-cols-2')
        
        # Now remove Column 3
        # I'll use regex to remove from <!-- Column 3: Resources --> up to the closing div of the dropdown.
        # The dropdown closes with three </div>.
        
        col3_pattern = re.compile(r'<!-- Column 3: Resources -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
        
        # Replace it with just </div>\s*</div>
        def replace_func(match):
            return '</div>\n</div>'
            
        html = col3_pattern.sub(replace_func, html)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Removed Resources column in {count} files.')
