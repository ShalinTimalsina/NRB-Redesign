from bs4 import BeautifulSoup

def rebuild_quick_access():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    old_section = soup.find('section', id='Quick-Access-Resources')
    if not old_section:
        print("Section not found!")
        return

    ext_icon = '<svg class="w-3.5 h-3.5 ml-1 shrink-0 opacity-50 group-hover:opacity-100 transition-opacity" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>'

    def make_link(url, label):
        return f'''<li><a href="{url}" target="_blank" rel="noopener noreferrer" class="group flex items-start gap-2.5 text-sm font-medium text-slate-700 hover:text-[#138496]"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span class="flex items-center">{label} {ext_icon}</span></a></li>'''

    new_section_html = f"""
    <section id="Quick-Access-Resources" class="bg-slate-50 py-20 border-t border-slate-200 mt-16">
        <div class="nrb-section-shell">
            <div class="mb-10 max-w-3xl">
                <h2 class="nrb-section-title mt-2 text-slate-900">Quick Access Resources</h2>
                <p class="mt-3 nrb-body-text max-w-2xl">
                    External portals, compliance systems, and institutional resources maintained outside this website.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Category 1: Financial Portals -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md hover:border-[#138496]/50 flex flex-col group border border-transparent">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#138496] group-hover:bg-[#138496]/10 transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900">Financial Portals</h3>
                    </div>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Public-facing financial inclusion and consumer protection portals.</p>
                    <ul class="space-y-3">
                        {make_link('http://emap.nrb.org.np/', 'Financial Inclusion Portal')}
                        {make_link('http://gunaso.nrb.org.np/', 'Financial Consumer Protection')}
                    </ul>
                </div>

                <!-- Category 2: Compliance & Reporting -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md hover:border-[#138496]/50 flex flex-col group border border-transparent">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#138496] group-hover:bg-[#138496]/10 transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900">Compliance &amp; Reporting</h3>
                    </div>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Anti-money laundering registration and reporting systems.</p>
                    <ul class="space-y-3">
                        {make_link('https://goaml.fiu.nrb.org.np/PRD/Home', 'goAML Nepal Registration &amp; Reporting Portal')}
                        {make_link('https://obss.nrb.org.np/', 'OBSS')}
                    </ul>
                </div>

                <!-- Category 3: International & Institutional -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md hover:border-[#138496]/50 flex flex-col group border border-transparent">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#138496] group-hover:bg-[#138496]/10 transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900">International &amp; Institutional</h3>
                    </div>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Technical cooperation and multilateral engagement portals.</p>
                    <ul class="space-y-3">
                        {make_link('https://archive.nrb.org.np/irtc/irtcindex.php', 'International Relation and Technical Cooperation')}
                        {make_link('https://www.saarcfinance.org/', 'SAARC Finance')}
                    </ul>
                </div>
            </div>
        </div>
    </section>
    """
    
    new_section = BeautifulSoup(new_section_html, 'html.parser')
    old_section.replace_with(new_section)

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Quick Access Resources rebuilt with only external portal links!")

if __name__ == '__main__':
    rebuild_quick_access()
