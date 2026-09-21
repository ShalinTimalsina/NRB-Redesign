import os
import re

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'
master_file = os.path.join(base_dir, 'pages/about/index.html')

with open(master_file, 'r', encoding='utf-8') as f:
    master_content = f.read()

header_match = re.search(r'(<header[^>]*id="Site-Header"[^>]*>.*?</header>)', master_content, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(<footer[^>]*>.*?</footer>)', master_content, re.DOTALL | re.IGNORECASE)

if not header_match or not footer_match:
    print("Could not find master header or footer")
    exit(1)

master_header_raw = header_match.group(1)
master_footer_raw = footer_match.group(1)

normalized_header = master_header_raw.replace('href="../../', 'href="').replace('src="../../', 'src="')
normalized_footer = master_footer_raw.replace('href="../../', 'href="').replace('src="../../', 'src="')

updated_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and 'components' not in root and 'scratch' not in root:
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, base_dir)
            depth_count = rel_path.count(os.sep)
            prefix = '../' * depth_count
            
            file_header = normalized_header.replace('href="', f'href="{prefix}').replace('src="', f'src="{prefix}')
            file_header = re.sub(r'href="(\.\./)+http', 'href="http', file_header)
            file_header = re.sub(r'href="(\.\./)+#', 'href="#', file_header)
            
            file_footer = normalized_footer.replace('href="', f'href="{prefix}').replace('src="', f'src="{prefix}')
            file_footer = re.sub(r'href="(\.\./)+http', 'href="http', file_footer)
            file_footer = re.sub(r'href="(\.\./)+#', 'href="#', file_footer)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # SAFE REPLACE (count=1 so it only replaces the global header if there are multiples, but really it looks for id="Site-Header")
            if re.search(r'<header[^>]*id="Site-Header"[^>]*>.*?</header>', content, re.DOTALL | re.IGNORECASE):
                content = re.sub(r'<header[^>]*id="Site-Header"[^>]*>.*?</header>', file_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)
            else:
                # If it doesn't have Site-Header, it might have an old <header class="bg-[#25295B]...
                # Replace the first <header> that has bg-[#25295B]
                if re.search(r'<header[^>]*bg-\[\#25295B\].*?</header>', content, re.DOTALL | re.IGNORECASE):
                    content = re.sub(r'<header[^>]*bg-\[\#25295B\].*?</header>', file_header, content, count=1, flags=re.DOTALL | re.IGNORECASE)
                else:
                    # Inject it
                    frame_pattern = r'(<div class="nrb-page-frame.*?>)'
                    if re.search(frame_pattern, content):
                        content = re.sub(frame_pattern, r'\1\n' + file_header, content, count=1)
                        
            if re.search(r'<footer.*?</footer>', content, re.DOTALL | re.IGNORECASE):
                content = re.sub(r'<footer.*?</footer>', file_footer, content, count=1, flags=re.DOTALL | re.IGNORECASE)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_count += 1

print(f"Safely synced {updated_count} files.")
