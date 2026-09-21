import os
import re

subpages = {
    'media-releases': 'Media Releases',
    'speeches': 'Speeches',
    'notices': 'Notices',
    'bok-kpp': 'BOK-KPP Study Reports'
}

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches'

for folder, title in subpages.items():
    filepath = os.path.join(base_dir, folder, 'index.html')
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Generate the correct horizontal local navigation
    nav_links = f'<a href="../index.html" id="LocalNav-Overview">Overview</a>\n'
    for k, v in subpages.items():
        if k == folder:
            nav_links += f'<a aria-current="page" href="../{k}/index.html" id="LocalNav-{k}">{v}</a>\n'
        else:
            nav_links += f'<a href="../{k}/index.html" id="LocalNav-{k}">{v}</a>\n'
            
    correct_local_nav = f"""<!-- LOCAL NAVIGATION -->
<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
    <div class="nrb-section-shell">
        <nav aria-label="Media & Speeches sections" class="nrb-page-nav flex items-center gap-8 py-4">
            {nav_links.strip()}
        </nav>
    </div>
</div>"""

    # Replace the existing local navigation block we added earlier
    pattern = r'<!-- LOCAL NAVIGATION -->\s*<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">.*?</div>\s*</div>'
    content = re.sub(pattern, correct_local_nav, content, flags=re.DOTALL)
    
    # Remove the JS we added earlier
    js_pattern = r'<script>\s*\(function \(\) \{\s*const sections = \[\'overview\', \'documents\'\];.*?\)\(\);\s*</script>'
    content = re.sub(js_pattern, '', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated local nav in media-speeches subpages.")
