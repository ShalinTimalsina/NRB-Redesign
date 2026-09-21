import os
import re

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'
master_file = os.path.join(base_dir, 'pages/about/index.html')

with open(master_file, 'r', encoding='utf-8') as f:
    master_content = f.read()

# Extract master header and footer
header_match = re.search(r'(<header.*?id="Site-Header".*?</header>)', master_content, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(<footer.*?</footer>)', master_content, re.DOTALL | re.IGNORECASE)

if not header_match or not footer_match:
    print("Could not find master header or footer in about/index.html")
    exit(1)

master_header_raw = header_match.group(1)
master_footer_raw = footer_match.group(1)

# Normalize paths. In about/index.html, the depth is 2 ("../../")
# We will replace all href="../../ and src="../../ with href=" and src="
normalized_header = master_header_raw.replace('href="../../', 'href="').replace('src="../../', 'src="')
normalized_footer = master_footer_raw.replace('href="../../', 'href="').replace('src="../../', 'src="')

# Some edge case paths that might be absolute-relative in master like `href="../pages` shouldn't exist, but just in case.
# Everything in master header was built with `../../` base.

updated_count = 0
missing_header_count = 0
missing_footer_count = 0

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and 'components' not in root and 'scratch' not in root:
            filepath = os.path.join(root, file)
            
            rel_path = os.path.relpath(filepath, base_dir)
            depth_count = rel_path.count(os.sep)
            
            # The base_dir is depth 0. 
            # if depth_count == 0 (e.g. nrb.html), prefix = ''
            # if depth_count == 1 (e.g. pages/xyz.html), prefix = '../'
            # if depth_count == 2 (e.g. pages/about/xyz.html), prefix = '../../'
            prefix = '../' * depth_count
            
            file_header = normalized_header.replace('href="', f'href="{prefix}').replace('src="', f'src="{prefix}')
            # Fix absolute links that might have gotten broken (e.g. href="http..." -> href="../http...")
            file_header = re.sub(r'href="(\.\./)+http', 'href="http', file_header)
            # Fix fragments (e.g. href="#id" -> href="../#id")
            file_header = re.sub(r'href="(\.\./)+#', 'href="#', file_header)
            
            file_footer = normalized_footer.replace('href="', f'href="{prefix}').replace('src="', f'src="{prefix}')
            file_footer = re.sub(r'href="(\.\./)+http', 'href="http', file_footer)
            file_footer = re.sub(r'href="(\.\./)+#', 'href="#', file_footer)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            # Replace header
            if re.search(r'<header.*?</header>', content, re.DOTALL | re.IGNORECASE):
                content = re.sub(r'<header.*?</header>', file_header, content, flags=re.DOTALL | re.IGNORECASE)
            else:
                # Inject after <div class="nrb-page-frame mx-auto w-full max-w-[1440px]"> or <body>
                frame_pattern = r'(<div class="nrb-page-frame.*?>)'
                if re.search(frame_pattern, content):
                    content = re.sub(frame_pattern, r'\1\n' + file_header, content, count=1)
                else:
                    content = re.sub(r'(<body.*?>)', r'\1\n' + file_header, content, count=1, flags=re.IGNORECASE)
                missing_header_count += 1
                
            # Replace footer
            if re.search(r'<footer.*?</footer>', content, re.DOTALL | re.IGNORECASE):
                content = re.sub(r'<footer.*?</footer>', file_footer, content, flags=re.DOTALL | re.IGNORECASE)
            else:
                # Inject before </body>
                # Wait, if there are scripts at the end, it's better to put footer right before the script block at the end, or just before </body>
                content = re.sub(r'(</body>)', file_footer + r'\n\1', content, flags=re.IGNORECASE)
                missing_footer_count += 1
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                updated_count += 1

print(f"Successfully synced {updated_count} files.")
print(f"Injected missing header in {missing_header_count} files.")
print(f"Injected missing footer in {missing_footer_count} files.")
