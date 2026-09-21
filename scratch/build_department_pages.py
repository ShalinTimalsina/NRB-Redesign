import os
import re
import json

# Read depth 3 template
def get_header_and_footer(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = re.split(r'<main[^>]*>', content)
    header_part = parts[0] + '<main id="Main-Content">\n'
    footer_part = '\n</main>\n' + re.split(r'</main>', parts[1])[-1]
    return header_part, footer_part

header, footer = get_header_and_footer('pages/monetary-policy/circulars/index.html')

# Update title in header
header = re.sub(r'<title>.*?</title>', '<title>{dep_name} | Regulation & Supervision</title>', header)
# Fix breadcrumb nav states
# (We don't need to do complex regex if we just inject the hero banner manually)

tree = [
  {
    "Regulations": [
      {
        "Banks & Financial Institutions": [
          "Notices",
          "Financial Stability Report",
          "Circulars",
          "Financial Consumer Protection"
        ]
      },
      {
        "Foreign Exchange Management": [
          "Notices",
          "Circulars"
        ]
      },
      {
        "Payment Systems": [
          "Notices",
          "Circulars",
          "Policies, Guidelines"
        ]
      },
      {
        "Banking Department": [
          "Notices",
          "ECC Notices"
        ]
      }
    ]
  },
  {
    "Supervisions": [
      {
        "Bank Supervision": [
          "Enforcement Action",
          "Key Financial Indicators",
          "Annual Reports"
        ]
      },
      {
        "Financial Institutions Supervision Department": [
          "Enforcement Action",
          "Key Financial Highlights",
          "Annual Reports"
        ]
      },
      {
        "Microfinance Institutions Supervision Department": [
          "Current Microfinance Activities",
          "Sources/Uses and Progress Report"
        ]
      },
      {
        "Non-Bank Financial Institutions Supervision Department": [
          "Notices",
          "Bylaws"
        ]
      }
    ]
  }
]

# Flatten the tree into a list of departments
departments = []
for category_dict in tree:
    for cat_name, cat_deps in category_dict.items():
        for dep_dict in cat_deps:
            for dep_name, dep_docs in dep_dict.items():
                departments.append({
                    'category': cat_name,
                    'name': dep_name,
                    'docs': dep_docs
                })

# Map full names to acronyms (keys for folder names)
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

for dep in departments:
    acronym = acronym_map.get(dep['name'])
    if not acronym:
        continue
        
    dep_header = header.replace('{dep_name}', dep['name'])
    
    # Generate Hero Banner
    hero = f"""
<section class="border-b border-slate-200 bg-white" id="Hero-Banner">
    <div class="nrb-section-shell py-10 lg:py-14">
        <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
            <a class="transition hover:text-[#25295B]" href="../../../nrb.html">Home</a>
            <span class="text-slate-300">/</span>
            <a class="transition hover:text-[#25295B]" href="../../regulation-and-supervision/index.html">Regulation & Supervision</a>
            <span class="text-slate-300">/</span>
            <span class="text-slate-700">{acronym.upper()}</span>
        </nav>
        <h1 class="text-2xl font-bold text-slate-900 mb-3">{dep['name']}</h1>
        <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Official documents, notices, and directives issued by the {dep['name']}.</p>
    </div>
</section>
"""

    # Generate Local Nav
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

    # Generate Sections for Docs
    sections = ""
    for doc in dep['docs']:
        safe_id = doc.replace(' ', '').replace(',', '').replace('/', '')
        sections += f"""
<section class="py-14 border-b border-slate-200 bg-slate-50" id="{safe_id.lower()}">
    <div class="nrb-section-shell">
        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 mb-5">All {doc}</h3>
        <div class="flex flex-col gap-3">
            <!-- Placeholder Document Card -->
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

    # Generate Script for sticky nav
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
        
    print(f"Scaffolded {out_path}")

