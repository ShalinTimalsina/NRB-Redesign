import os
import re

pattern = re.compile(
    r'<a class="px-4 py-2\.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-\[#138496\] font-medium transition-colors rounded-lg" href="([^"]*)pages/monetary-policy/index\.html#(monetary-operations|data-reports|circulars|notices|policies-procedures)">'
)

count = 0

for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Sub the pattern by moving the anchor tag word into the path
            def replace_href(match):
                prefix = match.group(1)
                folder = match.group(2)
                return f'<a class="px-4 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors rounded-lg" href="{prefix}pages/monetary-policy/{folder}/index.html">'
            
            new_content = pattern.sub(replace_href, content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed headers in {filepath}")

print(f"Total files fixed: {count}")
