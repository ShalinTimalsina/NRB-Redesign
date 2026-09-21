import os
from bs4 import BeautifulSoup

def rebuild_contact_page():
    contact_path = r'pages\contact\index.html'
    
    with open(contact_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Extract the existing form
    form = soup.find('form')
    form_html = str(form) if form else '<form></form>'
    
    # 2. Build the new <main> structure
    new_main_html = f'''<main id="Main-Content">
    <!-- HERO -->
    <section class="border-b border-slate-200 bg-white">
        <div class="nrb-section-shell py-10 lg:py-14">
            <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
                <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
                <span class="text-slate-300">/</span>
                <span class="text-slate-700">Contact &amp; Locations</span>
            </nav>
            <h1 class="text-2xl font-bold text-slate-900 mb-4">Contact &amp; Locations</h1>
            <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Official contact channels, office routing, and public inquiry paths for Nepal Rastra Bank.</p>
        </div>
    </section>

    <!-- LOCAL NAVIGATION -->
    <div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
        <div class="nrb-section-shell">
            <nav aria-label="Contact sections" class="nrb-page-nav flex items-center gap-8 py-4 overflow-x-auto">
                <a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
                <a href="#offices" id="LocalNav-Offices">Provincial Offices</a>
                <a href="#departments" id="LocalNav-Departments">Department Routing</a>
                <a href="#inquiry" id="LocalNav-Inquiry">Inquiry Form</a>
            </nav>
        </div>
    </div>

    <!-- MAIN CONTENT SECTIONS -->
    <!-- Overview -->
    <section class="bg-slate-50 py-14 border-b border-slate-200 scroll-mt-20" id="overview">
        <div class="nrb-section-shell">
            <header class="mb-10 max-w-3xl">
                <h2 class="text-3xl font-bold text-slate-900">Head Office</h2>
                <p class="mt-3 text-slate-600">The central headquarters of the Nepal Rastra Bank in Baluwatar.</p>
            </header>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Location Card -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col items-center text-center transition-colors hover:border-[#138496]/30">
                    <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] mb-6">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Central Office</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Baluwatar, Kathmandu<br>Bagmati Province, Nepal<br>P.O. Box: 73</p>
                </div>
                
                <!-- Phone Card -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col items-center text-center transition-colors hover:border-[#138496]/30">
                    <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] mb-6">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Phone</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">+977-1-4419804<br>+977-1-4419805<br>Ext: 112 (General)</p>
                </div>
                
                <!-- Email Card -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col items-center text-center transition-colors hover:border-[#138496]/30">
                    <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] mb-6">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Email</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">General: info@nrb.org.np<br>Grievance: gunaso@nrb.org.np<br>Support: it@nrb.org.np</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Provincial Offices -->
    <section class="bg-white py-14 border-b border-slate-200 scroll-mt-20" id="offices">
        <div class="nrb-section-shell">
            <header class="mb-10 flex items-center justify-between">
                <div>
                    <h2 class="text-2xl font-bold text-slate-900">Provincial Offices</h2>
                    <p class="mt-2 text-slate-600">Regional branches serving the 7 provinces of Nepal.</p>
                </div>
            </header>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Koshi Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Biratnagar Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-21-420362</p>
                        <p>Email: nrbbrt@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Madhesh Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Janakpur Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-41-590059</p>
                        <p>Email: nrbjkp@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Madhesh Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Birgunj Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-51-522105</p>
                        <p>Email: nrbbrg@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Gandaki Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Pokhara Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-61-463283</p>
                        <p>Email: nrbpkr@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Lumbini Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Siddharthanagar Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-71-520188</p>
                        <p>Email: nrbbhw@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Lumbini Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Nepalgunj Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-81-520336</p>
                        <p>Email: nrbnpj@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Karnali Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Surkhet Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-83-520038</p>
                        <p>Email: nrbskt@nrb.org.np</p>
                    </div>
                </div>
                <div class="p-6 rounded-xl border border-slate-200 bg-slate-50 hover:bg-white hover:border-[#138496]/30 transition-colors shadow-sm">
                    <div class="text-[11px] font-bold uppercase tracking-[0.16em] text-[#138496] mb-2">Sudurpashchim Province</div>
                    <h3 class="text-base font-bold text-slate-900 mb-3">Dhangadhi Office</h3>
                    <div class="text-sm text-slate-600 space-y-1">
                        <p>Phone: +977-91-521122</p>
                        <p>Email: nrbdhi@nrb.org.np</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Department Routing -->
    <section class="bg-slate-50 py-14 border-b border-slate-200 scroll-mt-20" id="departments">
        <div class="nrb-section-shell">
            <header class="mb-10">
                <h2 class="text-2xl font-bold text-slate-900">Department Routing</h2>
                <p class="mt-2 text-slate-600">Quickly find the appropriate department for your inquiry.</p>
            </header>
            
            <div class="overflow-hidden rounded-[20px] border border-slate-200 bg-white shadow-sm">
                <div class="overflow-x-auto">
                    <table class="w-full border-collapse text-left whitespace-nowrap">
                        <thead class="bg-slate-100">
                            <tr class="border-b border-slate-200 text-xs uppercase tracking-[0.16em] text-slate-500">
                                <th class="px-6 py-4 font-semibold">Subject Matter</th>
                                <th class="px-6 py-4 font-semibold">Responsible Department</th>
                                <th class="px-6 py-4 font-semibold text-right">Direct Contact</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200">
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-medium text-slate-900">Consumer Banking Complaints</td>
                                <td class="px-6 py-4">Financial Consumer Protection Portal</td>
                                <td class="px-6 py-4 text-right"><a href="#" class="text-[#138496] hover:underline font-medium">gunaso@nrb.org.np</a></td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-medium text-slate-900">Commercial Bank Supervision</td>
                                <td class="px-6 py-4">Bank Supervision Department</td>
                                <td class="px-6 py-4 text-right"><a href="#" class="text-[#138496] hover:underline font-medium">bsd@nrb.org.np</a></td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-medium text-slate-900">Foreign Exchange Approvals</td>
                                <td class="px-6 py-4">Foreign Exchange Management Department</td>
                                <td class="px-6 py-4 text-right"><a href="#" class="text-[#138496] hover:underline font-medium">fxm@nrb.org.np</a></td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-medium text-slate-900">Research &amp; Data Publication</td>
                                <td class="px-6 py-4">Economic Research Department</td>
                                <td class="px-6 py-4 text-right"><a href="#" class="text-[#138496] hover:underline font-medium">erd@nrb.org.np</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>

    <!-- Inquiry Form -->
    <section class="bg-white py-14 scroll-mt-20" id="inquiry">
        <div class="nrb-section-shell">
            <div class="max-w-4xl mx-auto rounded-[24px] bg-white border border-slate-200 overflow-hidden shadow-sm flex flex-col md:flex-row">
                <!-- Left side -->
                <div class="bg-[#25295B] text-white p-10 md:w-2/5 flex flex-col justify-between">
                    <div>
                        <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10 text-white mb-6">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                        </div>
                        <h2 class="text-2xl font-bold mb-4">Inquiry &amp; Feedback</h2>
                        <p class="text-slate-300 text-sm leading-6 mb-8">Use this official channel to submit questions, provide feedback, or request assistance. Your inquiry will be automatically routed to the selected department.</p>
                    </div>
                    <div class="text-xs text-slate-400">
                        <p>Typical response time: 2-3 business days.</p>
                    </div>
                </div>
                
                <!-- Right side (Form) -->
                <div class="p-10 md:w-3/5 bg-white">
                    {form_html}
                </div>
            </div>
        </div>
    </section>
</main>'''

    # Parse new main
    new_main_soup = BeautifulSoup(new_main_html, 'html.parser')
    
    # Find original main and replace it
    old_main = soup.find('main')
    old_main.replace_with(new_main_soup)
    
    # Save the file
    with open(contact_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Successfully rebuilt contact page!")

if __name__ == '__main__':
    rebuild_contact_page()
