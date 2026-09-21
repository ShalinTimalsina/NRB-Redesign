import os
import re

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

count = 0
for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Change grid classes
            content = content.replace('w-[1080px] grid grid-cols-4 gap-x-6', 'w-[850px] grid grid-cols-3 gap-x-6')
            
            # Remove Column 4 (Featured Publications)
            # Find the start of Column 4 comment, and remove everything up to the end of its div
            # The structure is:
            # <!-- Column 4: Featured Publications -->
            # <div class="flex flex-col">
            #   ...
            # </div>
            # </div> (end of grid)
            # </div> (end of absolute)
            
            featured_pattern = r'<!-- Column 4: Featured Publications -->\s*<div class="flex flex-col">.*?</div>\s*</div>\s*</div>\s*</div>'
            
            # We need to be careful with the regex to not eat too many </div>s.
            # It's better to just match exactly the contents of Column 4
            col_4_pattern = r'<!-- Column 4: Featured Publications -->\s*<div class="flex flex-col">.*?<span class="block font-bold">Digital Currency Impact Study</span>\s*</a>\s*</div>'
            
            content = re.sub(col_4_pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Removed Featured Publications from {count} files.")
