import re
import os

# 1. Update the landing page
landing_path = 'pages/monetary-policy/index.html'
with open(landing_path, 'r', encoding='utf-8') as f:
    landing = f.read()

# Remove the Overview card from Quick Access
# The Overview card is the first card in the grid
card_pattern = r'<a class="hub-card nrb-elevated-card group flex flex-col rounded-\[20px\] bg-white border border-slate-200 p-8 hover:border-\[#25295B\]/20 transition-all" href="#overview">.*?</a>\n'
landing = re.sub(card_pattern, '', landing, flags=re.DOTALL)

with open(landing_path, 'w', encoding='utf-8') as f:
    f.write(landing)
print("Updated landing page Quick Access grid.")

# 2. Add Sticky Local Nav to all subpages
subpages = [
    ('monetary-operations', 'Monetary Operations'),
    ('data-reports', 'Data & Reports'),
    ('circulars', 'Circulars'),
    ('notices', 'Notices'),
    ('policies-procedures', 'Policies & Procedures')
]

for folder, name in subpages:
    page_path = f'pages/monetary-policy/{folder}/index.html'
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Build the local nav HTML
    nav_links = f'''<a href="../index.html" id="LocalNav-Overview">Overview</a>
<a {"aria-current='page'" if folder == 'monetary-operations' else ""} href="../monetary-operations/index.html" id="LocalNav-MonetaryOperations">Monetary Operations</a>
<a {"aria-current='page'" if folder == 'data-reports' else ""} href="../data-reports/index.html" id="LocalNav-DataReports">Data &amp; Reports</a>
<a {"aria-current='page'" if folder == 'circulars' else ""} href="../circulars/index.html" id="LocalNav-Circulars">Circulars</a>
<a {"aria-current='page'" if folder == 'notices' else ""} href="../notices/index.html" id="LocalNav-Notices">Notices</a>
<a {"aria-current='page'" if folder == 'policies-procedures' else ""} href="../policies-procedures/index.html" id="LocalNav-PoliciesProcedures">Policies &amp; Procedures</a>'''
    
    local_nav_html = f'''<!-- LOCAL NAVIGATION -->
<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
<div class="nrb-section-shell">
<nav aria-label="Monetary Policy sections" class="nrb-page-nav flex items-center gap-8 py-4">
{nav_links}
</nav>
</div>
</div>'''
    
    # Insert it directly after the Hero Banner
    # We find </section> that corresponds to Hero-Banner
    # Wait, the hero banner ends with </section>. The next tag is usually <section class="py-14"...
    # Let's use regex to insert after the first </section> inside <main>
    
    # Check if Local-Navigation already exists
    if 'id="Local-Navigation"' not in content:
        pattern = r'(<section class="border-b border-slate-200 bg-white" id="Hero-Banner">.*?</section>)'
        replacement = r'\1\n' + local_nav_html
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added sticky local nav to {folder}")
    else:
        print(f"Sticky nav already in {folder}")

