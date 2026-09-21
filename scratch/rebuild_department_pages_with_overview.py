import os
import re

def get_header_and_footer(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = re.split(r'<main[^>]*>', content)
    header_part = parts[0] + '<main id="Main-Content">\n'
    footer_part = '\n</main>\n' + re.split(r'</main>', parts[1])[-1]
    return header_part, footer_part

# Use pristine restored header from monetary-policy/circulars/index.html (depth 3)
header, footer = get_header_and_footer('pages/monetary-policy/circulars/index.html')
header = re.sub(r'<title>.*?</title>', '<title>{dep_name} | Regulation & Supervision</title>', header)

tree = [
  {
    "Regulations": [
      {"Banks & Financial Institutions": ["Notices", "Financial Stability Report", "Circulars", "Financial Consumer Protection"]},
      {"Foreign Exchange Management": ["Notices", "Circulars"]},
      {"Payment Systems": ["Notices", "Circulars", "Policies, Guidelines"]},
      {"Banking Department": ["Notices", "ECC Notices"]}
    ]
  },
  {
    "Supervisions": [
      {"Bank Supervision": ["Enforcement Action", "Key Financial Indicators", "Annual Reports"]},
      {"Financial Institutions Supervision Department": ["Enforcement Action", "Key Financial Highlights", "Annual Reports"]},
      {"Microfinance Institutions Supervision Department": ["Current Microfinance Activities", "Sources/Uses and Progress Report"]},
      {"Non-Bank Financial Institutions Supervision Department": ["Notices", "Bylaws"]}
    ]
  }
]

departments = []
for category_dict in tree:
    for cat_name, cat_deps in category_dict.items():
        for dep_dict in cat_deps:
            for dep_name, dep_docs in dep_dict.items():
                departments.append({'category': cat_name, 'name': dep_name, 'docs': dep_docs})

acronym_map = {
    'Banks & Financial Institutions': 'bfr',
    'Foreign Exchange Management': 'fxm',
    'Payment Systems': 'psd',
    'Banking Department': 'bkd',
    'Bank Supervision': 'bsd',
    'Financial Institutions Supervision Department': 'fisd',
    'Microfinance Institutions Supervision Department': 'mfd',
    'Non-Bank Financial Institutions Supervision Department': 'nbfisd'
}

def extract_overview(dep_name):
    # Determine the markdown filename
    safe_name = dep_name.replace('&', 'and').replace('/', '-').replace(' ', '_')
    md_path = os.path.join('NRB Page md files/Regulations and Supervisions', f'{safe_name}.md')
    if not os.path.exists(md_path):
        return "<p class='text-slate-600 leading-relaxed'>Information and notices for this department.</p>"
        
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    overview_items = []
    capture = False
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # If we see Key Functions or something similar, start capturing
        if "Key Functions" in line or "Functions" in line or "Objective" in line:
            capture = True
            continue
            
        # Stop capturing if we hit another main section
        if capture and line in ["Principal Officers", "Notices", "Directives", "Circulars", "Guidelines"]:
            break
            
        if capture:
            # Clean up the line
            line = line.lstrip('-').lstrip('1234567890.').strip()
            if line:
                overview_items.append(line)
                
    if not overview_items:
        # Fallback to the first few lines of actual text if no Key Functions section found
        for line in lines:
            if line.startswith('#') or line.startswith('*') or "Skip to content" in line or "Home" in line or "»" in line or "Central Office" in line or "Telephone:" in line or "Fax:" in line or "Email:" in line or "nrb.org.np" in line:
                continue
            if len(line) > 30:
                overview_items.append(line)
                break
                
    if overview_items:
        html = '<ul class="list-disc list-outside ml-5 space-y-2 text-slate-600 leading-relaxed">'
        for item in overview_items:
            html += f'<li>{item}</li>'
        html += '</ul>'
        return html
        
    return "<p class='text-slate-600 leading-relaxed'>Information and notices for this department.</p>"

for dep in departments:
    acronym = acronym_map.get(dep['name'])
    if not acronym: continue
        
    dep_header = header.replace('{dep_name}', dep['name'])
    
    # 1. FIXED BREADCRUMBS: Use dep['name'] instead of acronym!
    hero = f"""
<section class="border-b border-slate-200 bg-white" id="Hero-Banner">
    <div class="nrb-section-shell py-10 lg:py-14">
        <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
            <a class="transition hover:text-[#25295B]" href="../../../nrb.html">Home</a>
            <span class="text-slate-300">/</span>
            <a class="transition hover:text-[#25295B]" href="../../regulation-and-supervision/index.html">Regulation & Supervision</a>
            <span class="text-slate-300">/</span>
            <span class="text-slate-700">{dep['name']}</span>
        </nav>
        <h1 class="text-2xl font-bold text-slate-900 mb-3">{dep['name']}</h1>
        <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Official documents, notices, and directives issued by the {dep['name']}.</p>
    </div>
</section>
"""

    nav_links = f'<a aria-current="page" href="#overview" id="LocalNav-overview">Overview</a>\n'
    for doc in dep['docs']:
        safe_id = doc.replace(' ', '').replace(',', '').replace('/', '')
        nav_links += f'            <a href="#{safe_id.lower()}" id="LocalNav-{safe_id}">{doc}</a>\n'

    local_nav = f"""
<!-- LOCAL NAVIGATION -->
<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
    <div class="nrb-section-shell">
        <nav aria-label="Department sections" class="nrb-page-nav flex items-center gap-8 py-4 overflow-x-auto">
            {nav_links.strip()}
        </nav>
    </div>
</div>
"""

    # 2. OVERVIEW CONTENT: Extracted from actual website
    overview_html = extract_overview(dep['name'])
    
    sections = f"""
<section class="py-14 border-b border-slate-200 bg-white" id="overview">
    <div class="nrb-section-shell">
        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 mb-5">Department Overview</h3>
        <div class="bg-slate-50 p-8 rounded-[20px] border border-slate-200">
            <h4 class="text-lg font-bold text-slate-900 mb-4">Key Functions</h4>
            {overview_html}
        </div>
    </div>
</section>
"""

    for doc in dep['docs']:
        safe_id = doc.replace(' ', '').replace(',', '').replace('/', '')
        sections += f"""
<section class="py-14 border-b border-slate-200 bg-slate-50" id="{safe_id.lower()}">
    <div class="nrb-section-shell">
        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 mb-5">All {doc}</h3>
        <div class="flex flex-col gap-3">
            <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#">
                <div class="flex items-start gap-4">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                    </div>
                    <div class="flex flex-col gap-1.5">
                        <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Sample {doc} Document</p>
                        <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">PDF</span><span class="text-slate-300 px-1.5">•</span><span>Verified Source</span></div>
                    </div>
                </div>
                <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
            </a>
        </div>
    </div>
</section>
"""

    nav_keys = ["'overview'"] + [f"'{d.replace(' ', '').replace(',', '').replace('/', '').lower()}'" for d in dep['docs']]
    nav_map = ["'overview': 'LocalNav-overview'"] + [f"'{d.replace(' ', '').replace(',', '').replace('/', '').lower()}': 'LocalNav-{d.replace(' ', '').replace(',', '').replace('/', '')}'" for d in dep['docs']]
    
    script = f"""
<script>
    (function () {{
        const sections = [{', '.join(nav_keys)}];
        const navLinks = {{}};
        const keyMap = {{
            {', '.join(nav_map)}
        }};
        sections.forEach(id => {{
            const el = document.getElementById(keyMap[id]);
            if (el) navLinks[id] = el;
        }});
        function setActive(id) {{
            sections.forEach(s => {{
                const link = navLinks[s];
                if (!link) return;
                s === id
                    ? link.setAttribute('aria-current', 'page')
                    : link.removeAttribute('aria-current');
            }});
        }}
        function scrollToSection(id) {{
            const target = document.getElementById(id);
            if (!target) return;
            const localNav = document.getElementById('Local-Navigation');
            const offset = localNav ? localNav.getBoundingClientRect().height : 56;
            window.scrollTo({{
                top: target.offsetTop - offset - 12,
                behavior: 'smooth'
            }});
        }}
        Object.keys(navLinks).forEach(id => {{
            navLinks[id].addEventListener('click', function(e) {{
                if (id === 'overview') {{
                    window.scrollTo({{ top: 0, behavior: 'smooth' }});
                    setActive('overview');
                    history.replaceState(null, '', '#');
                    e.preventDefault();
                    return;
                }}
                e.preventDefault();
                setActive(id);
                scrollToSection(id);
                history.replaceState(null, '', '#' + id);
            }});
        }});
    }})();
</script>
"""

    full_html = dep_header + hero + local_nav + sections + script + footer
    
    out_dir = f'pages/regulation-and-supervision/{acronym}'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print(f"Scaffolded {out_path} with injected overview content.")
