import os
import re

hub_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/publications/index.html'

with open(hub_path, 'r', encoding='utf-8') as f:
    content = f.read()

header_match = re.search(r'(.*?<header[^>]*>.*?</header>)', content, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(<footer[^>]*>.*?</footer>.*)', content, re.DOTALL | re.IGNORECASE)

header_html = header_match.group(1).replace('../../', '../../../')
footer_html = footer_match.group(1).replace('../../', '../../../')

# We need to adjust the depth of the Mega Menu links in the header for subpages (depth=3)
# Currently in hub it's depth=2 (../../)
header_html = header_html.replace('href="../../pages/publications/index.html"', 'href="../../../pages/publications/index.html"')
header_html = header_html.replace('href="../../pages/publications/', 'href="../../../pages/publications/')
# Adjust nrb.html link
header_html = header_html.replace('href="../../nrb.html"', 'href="../../../nrb.html"')
header_html = header_html.replace('src="../../assets/', 'src="../../../assets/')
header_html = header_html.replace('href="../../assets/', 'href="../../../assets/')
header_html = header_html.replace('href="../../pages/', 'href="../../../pages/')

pages = {
    'research': {
        'name': 'Research & Analysis',
        'subpages': [
            {'folder': 'economic-review', 'title': 'Economic Review', 'desc': 'Periodic reviews of economic trends.'},
            {'folder': 'macroeconomic-reports', 'title': 'Macroeconomic Reports', 'desc': 'Monthly and annual economic data.'},
            {'folder': 'working-papers', 'title': 'NRB Working Papers', 'desc': 'Research papers from NRB economists.'},
            {'folder': 'study-reports', 'title': 'Study Reports', 'desc': 'In-depth research and study findings.'},
        ]
    },
    'institutional': {
        'name': 'Institutional Reports',
        'subpages': [
            {'folder': 'annual-reports', 'title': 'Annual Reports', 'desc': 'Comprehensive yearly performance reports.'},
            {'folder': 'financial-stability', 'title': 'Financial Stability Reports', 'desc': 'Assessments of financial system health.'},
            {'folder': 'economic-activities', 'title': 'Economic Activities Reports', 'desc': 'Regional and national economic activity.'},
        ]
    },
    'special': {
        'name': 'Special Publications',
        'subpages': [
            {'folder': 'special-publications', 'title': 'Special Publications', 'desc': 'Ad-hoc reports and special releases.'},
            {'folder': 'golden-jubilee', 'title': 'Golden Jubilee Publications', 'desc': '50th anniversary commemorative releases.'},
            {'folder': 'arthabodh', 'title': 'Arthabodh', 'desc': 'Financial literacy and awareness.'},
            {'folder': 'know-your-bank-notes', 'title': 'Know Your Bank Notes', 'desc': 'Security features and banknote guides.'},
        ]
    }
}

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/publications'

# Dummy document grid HTML
document_grid = """
<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">
    <div class="nrb-section-shell">
        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 mb-5">Latest Documents</h3>
        <div class="flex flex-col gap-3">
            <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#" target="_blank">
                <div class="flex items-start gap-4">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                    </div>
                    <div class="flex flex-col gap-1.5">
                        <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Sample Document 1</p>
                        <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">PDF</span><span class="text-slate-300 px-1.5">•</span><span>1.5 MB</span><span class="text-slate-300 px-1.5">•</span><span>15 Aug 2026</span></div>
                    </div>
                </div>
                <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
            </a>
            <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#" target="_blank">
                <div class="flex items-start gap-4">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                    </div>
                    <div class="flex flex-col gap-1.5">
                        <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Sample Document 2</p>
                        <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">PDF</span><span class="text-slate-300 px-1.5">•</span><span>2.1 MB</span><span class="text-slate-300 px-1.5">•</span><span>10 Aug 2026</span></div>
                    </div>
                </div>
                <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
            </a>
            <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#" target="_blank">
                <div class="flex items-start gap-4">
                    <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                    </div>
                    <div class="flex flex-col gap-1.5">
                        <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Sample Document 3</p>
                        <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">PDF</span><span class="text-slate-300 px-1.5">•</span><span>800 KB</span><span class="text-slate-300 px-1.5">•</span><span>01 Aug 2026</span></div>
                    </div>
                </div>
                <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
            </a>
        </div>
    </div>
</section>
"""

for cat_key, category in pages.items():
    cat_name = category['name']
    subpages = category['subpages']
    
    # Generate the local nav for this category
    local_nav_links = '<a href="../index.html" id="LocalNav-Overview">Overview</a>\n'
    for page in subpages:
        local_nav_links += f'                <a href="../{page["folder"]}/index.html" id="LocalNav-{page["folder"]}">{page["title"]}</a>\n'

    for page in subpages:
        folder_path = os.path.join(base_dir, page['folder'])
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, 'index.html')
        
        # Mark current page as active in local nav
        active_nav = local_nav_links.replace(
            f'<a href="../{page["folder"]}/index.html"', 
            f'<a aria-current="page" href="../{page["folder"]}/index.html"'
        )
        
        main_content = f"""
<main>
    <!-- HERO -->
    <section class="border-b border-slate-200 bg-white">
        <div class="nrb-section-shell py-10 lg:py-14">
            <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
                <a class="transition hover:text-[#25295B]" href="../../../nrb.html">Home</a>
                <span class="text-slate-300">/</span>
                <a class="transition hover:text-[#25295B]" href="../index.html">Publications</a>
                <span class="text-slate-300">/</span>
                <span class="text-slate-500">{cat_name}</span>
                <span class="text-slate-300">/</span>
                <span class="text-slate-700">{page['title']}</span>
            </nav>
            <h1 class="text-2xl font-bold text-slate-900 mb-3">{page['title']}</h1>
            <p class="text-base text-slate-600 leading-relaxed max-w-2xl">{page['desc']}</p>
        </div>
    </section>

    <!-- LOCAL NAVIGATION -->
    <div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
        <div class="nrb-section-shell">
            <nav aria-label="{cat_name} sections" class="nrb-page-nav flex items-center gap-8 py-4 overflow-x-auto">
                {active_nav.strip()}
            </nav>
        </div>
    </div>
    
    <!-- DOCUMENT GRID -->
    {document_grid}
</main>
"""
        full_html = header_html + '\n' + main_content + '\n' + footer_html
        
        # Fix title tag
        full_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]} | Publications | NRB</title>', full_html)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
print("Generated 11 subpages for Publications.")
