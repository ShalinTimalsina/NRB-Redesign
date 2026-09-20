import os
import re

# 1. Read the correct footer from monetary-policy/index.html
source_file = 'pages/monetary-policy/index.html'
with open(source_file, 'r', encoding='utf-8') as f:
    source_content = f.read()

# Extract the footer
footer_match = re.search(r'(<footer class="nrb-footer bg-\[#25295B\] text-white" id="Footer">.*?</footer>)', source_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in source file")
    exit(1)

correct_footer = footer_match.group(1)
# Adjust relative paths from depth 2 (../../) to depth 3 (../../../)
# Also handle any src="../../"
correct_footer_depth3 = correct_footer.replace('="../../', '="../../../')

# 2. Inject into the 5 subpages
subpages = [
    'pages/monetary-policy/circulars/index.html',
    'pages/monetary-policy/data-reports/index.html',
    'pages/monetary-policy/monetary-operations/index.html',
    'pages/monetary-policy/notices/index.html',
    'pages/monetary-policy/policies-procedures/index.html'
]

for page in subpages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing footer
    new_content = re.sub(r'<footer class="nrb-footer bg-\[#25295B\] text-white" id="Footer">.*?</footer>', correct_footer_depth3, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed footer in {page}")
    else:
        print(f"No changes needed for {page} or footer not found")

