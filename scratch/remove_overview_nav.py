import os
import re

# Regex pattern to match the Overview link block in the dropdown
# We use re.DOTALL to match across newlines
pattern = r'<a class="px-4 py-2\.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-\[#138496\] font-medium transition-colors rounded-lg" href="[^"]*pages/monetary-policy/index\.html#overview">\s*<span class="block">Overview</span>\s*<span class="block text-xs text-slate-400 font-normal mt-0\.5">Policy stance, objectives, and current rates\.</span>\s*</a>\s*'

count = 0

# Walk through all directories and process HTML files
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Sub the pattern
            new_content = re.sub(pattern, '', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Updated {filepath}")

print(f"Total files updated: {count}")
