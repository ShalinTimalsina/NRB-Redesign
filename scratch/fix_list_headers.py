import os
import re

subpages = {
    'pages/monetary-policy/circulars/index.html': 'All Circulars',
    'pages/monetary-policy/data-reports/index.html': 'All Data & Reports',
    'pages/monetary-policy/monetary-operations/index.html': 'All Monetary Operations',
    'pages/monetary-policy/notices/index.html': 'All Notices',
    'pages/monetary-policy/policies-procedures/index.html': 'All Policies & Procedures'
}

# The block to replace:
# <div class="flex items-center justify-between mb-8">\n<p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500">\d+ Documents</p>\n\n</div>
# Note: Notices might have "4 Notices" because it was the template, or "4 Documents". Let's use regex.

pattern = re.compile(r'<div class="flex items-center justify-between mb-8">\s*<p class="text-xs font-semibold uppercase tracking-\[0\.18em\] text-slate-500">\d+ (?:Documents|Notices)</p>\s*</div>')

for filepath, title in subpages.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacement = f'<h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 mb-5">{title}</h3>'
    
    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} to use '{title}'")
    else:
        print(f"Pattern not found in {filepath} (might already be updated)")

