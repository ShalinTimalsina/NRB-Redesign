import os
import re

hub_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/index.html'

with open(hub_path, 'r', encoding='utf-8') as f:
    content = f.read()

header_match = re.search(r'(.*?<header[^>]*>.*?</header>)', content, re.DOTALL | re.IGNORECASE)
footer_match = re.search(r'(<footer[^>]*>.*?</footer>.*)', content, re.DOTALL | re.IGNORECASE)

if not header_match or not footer_match:
    print("Could not find header or footer.")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

main_html = """
<main>
    <!-- HERO -->
    <section class="border-b border-slate-200 bg-white">
        <div class="nrb-section-shell py-10 lg:py-14">
            <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
                <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
                <span class="text-slate-300">/</span>
                <span class="text-slate-700">Statistics</span>
            </nav>
            <h1 class="text-2xl font-bold text-slate-900 mb-4">Statistics</h1>
            <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Official economic, monetary, financial and institutional statistics published by Nepal Rastra Bank.</p>
        </div>
    </section>

    <!-- LOCAL NAVIGATION -->
    <div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
        <div class="nrb-section-shell">
            <nav aria-label="Statistics sections" class="nrb-page-nav flex items-center gap-8 py-4 overflow-x-auto">
                <a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
                <a href="#macroeconomic" id="LocalNav-Macroeconomic">Macroeconomic Statistics</a>
                <a href="#financial-sector" id="LocalNav-FinancialSector">Financial Sector Statistics</a>
                <a href="#monetary-forex" id="LocalNav-MonetaryForex">Monetary & Forex Statistics</a>
                <a href="#financial-inclusion" id="LocalNav-FinancialInclusion">Financial Inclusion & Payments</a>
            </nav>
        </div>
    </div>

    <!-- STATISTICS CATEGORIES -->
    <section class="bg-slate-50 py-14 border-b border-slate-200" id="overview">
        <div class="nrb-section-shell">
            <header class="mb-10 text-center max-w-3xl mx-auto">
                <h2 class="text-3xl font-bold text-slate-900">Data & Statistics Categories</h2>
                <p class="mt-3 text-slate-600">Access comprehensive datasets and reports categorized by economic sector.</p>
            </header>
            
            <div class="grid lg:grid-cols-2 gap-6">
                <!-- Macroeconomic -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col justify-between h-full group hover:border-[#138496]/30 transition-colors">
                    <div>
                        <div class="flex items-center gap-4 mb-5">
                            <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>
                            </div>
                            <h3 class="text-xl font-bold text-slate-900">Macroeconomic Statistics</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-6 leading-relaxed">Economic indicators, surveys, economic bulletins and macroeconomic data.</p>
                        
                        <div class="mb-8">
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3">Resources Available</p>
                            <ul class="space-y-2 text-sm text-slate-700">
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Current Macro-Economic Situation</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Economic Bulletin</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Database on Nepalese Economy</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> National Summary Data Page</li>
                            </ul>
                        </div>
                    </div>
                    <a href="macroeconomic/index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#25295B] hover:text-[#138496] transition-colors w-fit">
                        View Statistics
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>

                <!-- Financial Sector -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col justify-between h-full group hover:border-[#138496]/30 transition-colors">
                    <div>
                        <div class="flex items-center gap-4 mb-5">
                            <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg>
                            </div>
                            <h3 class="text-xl font-bold text-slate-900">Financial Sector Statistics</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-6 leading-relaxed">Banking and financial sector performance indicators and reports.</p>
                        
                        <div class="mb-8">
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3">Resources Available</p>
                            <ul class="space-y-2 text-sm text-slate-700">
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Monthly Statistics of BFIs</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Key Financial Indicators</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Financial Highlights</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Microfinance Statistics</li>
                            </ul>
                        </div>
                    </div>
                    <a href="financial-sector/index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#25295B] hover:text-[#138496] transition-colors w-fit">
                        View Statistics
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>

                <!-- Monetary & Forex -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col justify-between h-full group hover:border-[#138496]/30 transition-colors" id="monetary-forex">
                    <div>
                        <div class="flex items-center gap-4 mb-5">
                            <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            </div>
                            <h3 class="text-xl font-bold text-slate-900">Monetary & Forex Statistics</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-6 leading-relaxed">Interest rates, monetary operations, policy rates and exchange rates.</p>
                        
                        <div class="mb-8">
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3">Resources Available</p>
                            <ul class="space-y-2 text-sm text-slate-700">
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Policy Rates</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Interest Rates</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Monetary Operations</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Daily Exchange Rate</li>
                            </ul>
                        </div>
                    </div>
                    <a href="monetary-forex/index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#25295B] hover:text-[#138496] transition-colors w-fit">
                        View Statistics
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>

                <!-- Financial Inclusion -->
                <div class="nrb-elevated-card bg-white border border-slate-200 rounded-[20px] p-8 flex flex-col justify-between h-full group hover:border-[#138496]/30 transition-colors" id="financial-inclusion">
                    <div>
                        <div class="flex items-center gap-4 mb-5">
                            <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-slate-50 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors">
                                <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            </div>
                            <h3 class="text-xl font-bold text-slate-900">Financial Inclusion & Payments</h3>
                        </div>
                        <p class="text-sm text-slate-600 mb-6 leading-relaxed">Financial inclusion and payment-system performance indicators.</p>
                        
                        <div class="mb-8">
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-3">Resources Available</p>
                            <ul class="space-y-2 text-sm text-slate-700">
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Financial Inclusion Index</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Financial Inclusion Portal</li>
                                <li class="flex items-center gap-2"><svg class="w-4 h-4 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg> Payment System Indicators</li>
                            </ul>
                        </div>
                    </div>
                    <a href="financial-inclusion/index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#25295B] hover:text-[#138496] transition-colors w-fit">
                        View Statistics
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- FEATURED DATASETS -->
    <section class="bg-white py-14 border-b border-slate-200">
        <div class="nrb-section-shell">
            <header class="mb-10 flex items-end justify-between">
                <div>
                    <h2 class="text-2xl font-bold text-slate-900">Featured Datasets</h2>
                    <p class="mt-2 text-sm text-slate-600">Quick access to key economic indicators.</p>
                </div>
                <a href="macroeconomic/index.html" class="text-sm font-medium text-[#138496] hover:text-[#25295B] transition-colors">View all indicators &rarr;</a>
            </header>
            
            <div class="grid grid-cols-4 gap-4">
                <div class="nrb-elevated-card rounded-[16px] bg-slate-50 border border-slate-200 p-6 flex flex-col h-full hover:border-[#138496]/30 transition-colors">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500 mb-1">Current Policy Rate</p>
                    <p class="text-3xl font-bold text-[#25295B] mb-2">5.5<span class="text-lg text-slate-500">%</span></p>
                    <p class="text-xs text-slate-400 mt-auto">As of latest monetary policy</p>
                </div>
                <div class="nrb-elevated-card rounded-[16px] bg-slate-50 border border-slate-200 p-6 flex flex-col h-full hover:border-[#138496]/30 transition-colors">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500 mb-1">Daily Exchange Rate</p>
                    <p class="text-3xl font-bold text-[#25295B] mb-2">133.<span class="text-lg text-slate-500">45</span></p>
                    <p class="text-xs text-slate-400 mt-auto">NPR per 1 USD</p>
                </div>
                <div class="nrb-elevated-card rounded-[16px] bg-slate-50 border border-slate-200 p-6 flex flex-col h-full hover:border-[#138496]/30 transition-colors">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500 mb-1">Inflation Indicator</p>
                    <p class="text-3xl font-bold text-[#25295B] mb-2">4.8<span class="text-lg text-slate-500">%</span></p>
                    <p class="text-xs text-slate-400 mt-auto">Year-on-year average</p>
                </div>
                <div class="nrb-elevated-card rounded-[16px] bg-slate-50 border border-slate-200 p-6 flex flex-col h-full hover:border-[#138496]/30 transition-colors">
                    <p class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-500 mb-1">Financial Inclusion</p>
                    <p class="text-3xl font-bold text-[#25295B] mb-2">67<span class="text-lg text-slate-500">%</span></p>
                    <p class="text-xs text-slate-400 mt-auto">Adult population access</p>
                </div>
            </div>
        </div>
    </section>

    <!-- LATEST STATISTICAL RELEASES -->
    <section class="bg-slate-50 py-14 border-b border-slate-200">
        <div class="nrb-section-shell">
            <header class="mb-8">
                <h2 class="text-2xl font-bold text-slate-900">Latest Statistical Releases</h2>
                <p class="mt-2 text-sm text-slate-600">Recently published data and reports across all categories.</p>
            </header>
            
            <div class="flex flex-col gap-3">
                <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="#" target="_blank">
                    <div class="flex items-start gap-4">
                        <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                            <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                        </div>
                        <div class="flex flex-col gap-1.5">
                            <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Current Macro-Economic Situation (First Month 2026/27)</p>
                            <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">PDF</span><span class="text-slate-300 px-1.5">•</span><span>2.4 MB</span><span class="text-slate-300 px-1.5">•</span><span>Macroeconomic</span></div>
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
                            <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Monthly Statistics of BFIs (Shrawan 2083)</p>
                            <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">EXCEL</span><span class="text-slate-300 px-1.5">•</span><span>5.1 MB</span><span class="text-slate-300 px-1.5">•</span><span>Financial Sector</span></div>
                        </div>
                    </div>
                    <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                </a>
            </div>
            
            <div class="mt-8 text-center">
                 <a href="macroeconomic/index.html" class="inline-flex items-center gap-2 px-6 py-3 bg-white border border-slate-200 rounded-xl text-sm font-semibold text-slate-700 hover:border-[#25295B] hover:text-[#25295B] transition-colors shadow-sm">
                    Browse All Documents
                 </a>
            </div>
        </div>
    </section>

    <!-- Local Navigation Scroll Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sections = ['overview', 'financial-sector', 'monetary-forex', 'financial-inclusion'];
            // Just basic link handler for smooth scroll
            const navLinks = document.querySelectorAll('.nrb-page-nav a');
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    const id = this.getAttribute('href').substring(1);
                    const target = document.getElementById(id);
                    if (target) {
                        e.preventDefault();
                        const localNav = document.getElementById('Local-Navigation');
                        const offset = localNav ? localNav.getBoundingClientRect().height : 56;
                        window.scrollTo({
                            top: target.offsetTop - offset - 12,
                            behavior: 'smooth'
                        });
                        navLinks.forEach(l => l.removeAttribute('aria-current'));
                        this.setAttribute('aria-current', 'page');
                    }
                });
            });
        });
    </script>
</main>
"""

new_full_html = header_html + '\n' + main_html + '\n' + footer_html

with open(hub_path, 'w', encoding='utf-8') as f:
    f.write(new_full_html)
print("Rebuilt statistics hub.")
