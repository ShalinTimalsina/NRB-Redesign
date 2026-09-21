import os
import hashlib

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

header_hashes = {}
footer_hashes = {}

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and not file.startswith('components'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract header (strip out the relative path differences to compare structure)
            import re
            header_match = re.search(r'<header.*?</header>', content, re.DOTALL | re.IGNORECASE)
            footer_match = re.search(r'<footer.*?</footer>', content, re.DOTALL | re.IGNORECASE)
            
            if header_match:
                header = header_match.group(0)
                # Normalize relative paths (e.g. href="../../pages" -> href="pages")
                header = re.sub(r'href="\.\./\.\./\.\./', 'href="', header)
                header = re.sub(r'href="\.\./\.\./', 'href="', header)
                header = re.sub(r'href="\.\./', 'href="', header)
                header = re.sub(r'src="\.\./\.\./\.\./', 'src="', header)
                header = re.sub(r'src="\.\./\.\./', 'src="', header)
                header = re.sub(r'src="\.\./', 'src="', header)
                # Remove active state classes since they differ per page
                header = re.sub(r'nrb-nav-active', '', header)
                
                h_hash = hashlib.md5(header.encode()).hexdigest()
                header_hashes.setdefault(h_hash, []).append(filepath)
            else:
                print(f"No header in {filepath}")
                
            if footer_match:
                footer = footer_match.group(0)
                # Normalize relative paths
                footer = re.sub(r'href="\.\./\.\./\.\./', 'href="', footer)
                footer = re.sub(r'href="\.\./\.\./', 'href="', footer)
                footer = re.sub(r'href="\.\./', 'href="', footer)
                footer = re.sub(r'src="\.\./\.\./\.\./', 'src="', footer)
                footer = re.sub(r'src="\.\./\.\./', 'src="', footer)
                footer = re.sub(r'src="\.\./', 'src="', footer)
                
                f_hash = hashlib.md5(footer.encode()).hexdigest()
                footer_hashes.setdefault(f_hash, []).append(filepath)
            else:
                print(f"No footer in {filepath}")

print(f"Total unique headers found: {len(header_hashes)}")
for h, files in header_hashes.items():
    print(f"Header Hash {h[:6]}: {len(files)} files (e.g. {files[0]})")

print(f"\nTotal unique footers found: {len(footer_hashes)}")
for f, files in footer_hashes.items():
    print(f"Footer Hash {f[:6]}: {len(files)} files (e.g. {files[0]})")
