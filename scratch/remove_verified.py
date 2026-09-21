import os
import re

count = 0
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig = content
            
            # Remove <span class="text-slate-300 px-1.5">•</span><span>Verified Source</span>
            content = re.sub(r'<span[^>]*>•</span>\s*<span>Verified Source</span>', '', content)
            # Just in case there's any remaining "Verified: ✅..."
            content = re.sub(r'<span[^>]*>•</span>\s*<span>Verified:\s*✅[^<]*</span>', '', content)
            
            if content != orig:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Removed 'Verified' tags from {count} files.")
