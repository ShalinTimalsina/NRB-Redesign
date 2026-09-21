import os
from bs4 import BeautifulSoup

def update_homepage():
    with open('nrb.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Ensure it's not already added
    if soup.find('section', id='Quick-Access-Resources'):
        print("Quick Access Resources already added.")
        return
        
    pop_services = soup.find('section', id='Popular-Services')
    if not pop_services:
        print("Popular-Services section not found!")
        return

    new_section_html = """
    <section id="Quick-Access-Resources" class="bg-slate-50 py-20 border-t border-slate-200 mt-16">
        <div class="nrb-section-shell">
            <div class="mb-10 max-w-3xl">
                <h2 class="nrb-section-title mt-2 text-slate-900">Quick Access Resources</h2>
                <p class="mt-3 nrb-body-text max-w-2xl">
                    Frequently used institutional services, external portals, compliance systems, and public resources.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Category 1 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md flex flex-col">
                    <h3 class="text-xl font-bold text-slate-900 mb-2">Financial Services</h3>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Public-facing services, literacy initiatives, and financial inclusion resources.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Financial Inclusion Portal</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Financial Consumer Protection</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Financial Literacy</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Banks &amp; Financial Institutions List</span></a></li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496] hover:text-[#25295B] transition-colors mt-auto">View Resources <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></a>
                </div>

                <!-- Category 2 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md flex flex-col">
                    <h3 class="text-xl font-bold text-slate-900 mb-2">Compliance &amp; Reporting</h3>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Financial intelligence, anti-money laundering registration, and sanction lists.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>FIU Nepal</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>goAML Nepal Registration &amp; Reporting Portal</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Targeted Sanction List and Other</span></a></li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496] hover:text-[#25295B] transition-colors mt-auto">View Resources <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></a>
                </div>

                <!-- Category 3 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md flex flex-col">
                    <h3 class="text-xl font-bold text-slate-900 mb-2">Information &amp; Transparency</h3>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Public right to information, security features of banknotes, and general FAQs.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Right To Information</span></a></li>
                        <li><a href="pages/publications/know-your-bank-notes/index.html" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Bank Notes Security Features</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>FAQs</span></a></li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496] hover:text-[#25295B] transition-colors mt-auto">View Resources <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></a>
                </div>

                <!-- Category 4 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white p-8 transition hover:-translate-y-0.5 hover:shadow-md flex flex-col">
                    <h3 class="text-xl font-bold text-slate-900 mb-2">International &amp; Institutional</h3>
                    <p class="text-sm text-slate-600 mb-6 leading-relaxed">Technical cooperation, multilateral engagements, and government agencies.</p>
                    <ul class="space-y-3 mb-8">
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>International Relation and Technical Cooperation</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>SAARC Finance</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Multinational Institutions</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>Government Agencies</span></a></li>
                        <li><a href="#" class="text-sm font-medium text-slate-700 hover:text-[#138496] flex items-start gap-2.5"><span class="w-1.5 h-1.5 rounded-full bg-[#138496]/50 mt-1.5 shrink-0"></span><span>OBSS</span></a></li>
                    </ul>
                    <a href="#" class="inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496] hover:text-[#25295B] transition-colors mt-auto">View Resources <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg></a>
                </div>
            </div>
        </div>
    </section>
    """
    
    new_section = BeautifulSoup(new_section_html, 'html.parser')
    pop_services.insert_after(new_section)

    with open('nrb.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Quick Access Resources injected into nrb.html")

if __name__ == '__main__':
    update_homepage()
