import re

# Read the full approved header from about index
with open('pages/about/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header
header_match = re.search(r'(<header class="bg-\[#25295B\].*?id="Site-Header">.*?</header>)', content, re.DOTALL)
header_html = header_match.group(1)

# Replace relative paths for 3-level depth
header_html = header_html.replace('href="../../', 'href="../../../')
header_html = header_html.replace('src="../../', 'src="../../../')
header_html = header_html.replace('href="index.html"', 'href="../../../pages/about/index.html"')

# Function to replace header in a target file
def replace_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        target_content = f.read()
    
    # Replace existing header
    new_content = re.sub(r'<header class="bg-\[#25295B\].*?id="Site-Header">.*?</header>', header_html, target_content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Updated header in {filepath}')

replace_header('pages/monetary-policy/monetary-operations/index.html')
replace_header('pages/monetary-policy/notices/index.html')
