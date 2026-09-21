from pathlib import Path
import re

count = 0
for p in sorted(Path('.').rglob('*.html')):
    if 'scratch' in p.parts or '.git' in p.parts:
        continue
    
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # We want to add 'focus:outline-none focus:ring-2 focus:ring-[#138496]' 
    # to class attributes of <a> and <button> if they don't have 'focus:' already.
    # We can do this with regex:
    # Find all class="..." strings inside <a or <button tags. (Simplistic approach: just find class="... hover:..." and add it if no focus).
    
    # To be safe, let's just target our main button types and card types.
    
    # 1. Action buttons
    # px-5 py-3 text-sm font-semibold
    html = re.sub(
        r'(class="[^"]*?(hover:bg-[#138496]|bg-[#25295B]|bg-[#138496])[^"]*?)"',
        lambda m: m.group(1) + ' focus:outline-none focus:ring-2 focus:ring-[#138496] focus:ring-offset-2"' if 'focus:' not in m.group(1) else m.group(0),
        html
    )
    
    # 2. Elevated cards (a tags)
    html = re.sub(
        r'(class="[^"]*?nrb-elevated-card[^"]*?)"',
        lambda m: m.group(1) + ' focus:outline-none focus:ring-2 focus:ring-[#138496] rounded-xl"' if 'focus:' not in m.group(1) else m.group(0),
        html
    )

    # 3. Footer links (hover:text-white)
    html = re.sub(
        r'(class="[^"]*?hover:text-white[^"]*?)"',
        lambda m: m.group(1) + ' focus:outline-none focus:text-white focus:underline"' if 'focus:' not in m.group(1) else m.group(0),
        html
    )
    
    if html != original:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1

print(f'Added focus styles to {count} files.')
