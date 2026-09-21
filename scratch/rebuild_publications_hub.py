import os
import re

hub_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/publications/index.html'

# We'll read the existing hub to grab the header and footer, 
# since it was just updated with the mega menu
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
                <span class="text-slate-700">Publications</span>
            </nav>
            <h1 class="text-2xl font-bold text-slate-900 mb-4">Publications</h1>
            <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Research publications, institutional reports, and educational resources published by the Central Bank.</p>
        </div>
    </section>

    <!-- LOCAL NAVIGATION -->
    <div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
        <div class="nrb-section-shell">
            <nav aria-label="Publications sections" class="nrb-page-nav flex items-center gap-8 py-4 overflow-x-auto">
                <a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
                <a href="#research" id="LocalNav-Research">Research & Analysis</a>
                <a href="#institutional" id="LocalNav-Institutional">Institutional Reports</a>
                <a href="#special" id="LocalNav-Special">Special Publications</a>
            </nav>
        </div>
    </div>

    <!-- OVERVIEW / FEATURED -->
    <section class="bg-slate-50 py-14 border-b border-slate-200" id="overview">
        <div class="nrb-section-shell">
            <header class="mb-8 flex items-end justify-between">
                <div>
                    <p class="nrb-display-note">Overview</p>
                    <h2 class="nrb-section-title mt-1 text-slate-900">Featured Publications</h2>
                </div>
            </header>
            <div class="grid grid-cols-3 gap-6">
                <!-- Featured 1 -->
                <div class="nrb-elevated-card rounded-[20px] bg-[#25295B] p-8 text-white relative overflow-hidden flex flex-col justify-between min-h-[300px]">
                    <div class="absolute right-[-20px] top-[-20px] opacity-10 pointer-events-none">
                        <svg fill="currentColor" height="180" viewBox="0 0 24 24" width="180"><path d="M12 2L2 22h20L12 2z"></path></svg>
                    </div>
                    <div class="relative z-10">
                        <span class="text-xs font-semibold uppercase tracking-[0.22em] text-[#138496] mb-3 block">Latest Report</span>
                        <h3 class="text-xl font-bold mb-3 text-white leading-tight">Annual Report 2025/26</h3>
                        <p class="text-sm leading-relaxed text-slate-300">Comprehensive overview of the Bank's financial performance and operations.</p>
                    </div>
                    <a href="#" class="inline-flex items-center gap-2 text-sm font-medium text-[#138496] hover:text-white transition-colors mt-6 w-fit">
                        Read Report
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>
                <!-- Featured 2 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white border border-slate-200 p-8 relative overflow-hidden flex flex-col justify-between min-h-[300px]">
                    <div class="absolute right-[-20px] top-[-20px] opacity-[0.04] text-[#138496] pointer-events-none">
                        <svg fill="currentColor" height="180" viewBox="0 0 24 24" width="180"><circle cx="12" cy="12" r="10"></circle></svg>
                    </div>
                    <div class="relative z-10">
                        <span class="text-xs font-semibold uppercase tracking-[0.22em] text-[#25295B] mb-3 block">Working Paper</span>
                        <h3 class="text-xl font-bold mb-3 text-slate-900 leading-tight">Digital Currency Impact Study</h3>
                        <p class="text-sm leading-relaxed text-slate-600">Research on the potential economic impacts of CBDC implementation in Nepal.</p>
                    </div>
                    <a href="#" class="inline-flex items-center gap-2 text-sm font-medium text-[#138496] hover:text-[#25295B] transition-colors mt-6 w-fit">
                        Download PDF
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                    </a>
                </div>
                <!-- Featured 3 -->
                <div class="nrb-elevated-card rounded-[20px] bg-white border border-slate-200 p-8 relative overflow-hidden flex flex-col justify-between min-h-[300px]">
                    <div class="absolute right-[-20px] top-[-20px] opacity-[0.04] text-[#25295B] pointer-events-none">
                        <svg fill="currentColor" height="180" viewBox="0 0 24 24" width="180"><path d="M12 2L2 22h20L12 2z"></path></svg>
                    </div>
                    <div class="relative z-10">
                        <span class="text-xs font-semibold uppercase tracking-[0.22em] text-[#25295B] mb-3 block">Macroeconomic</span>
                        <h3 class="text-xl font-bold mb-3 text-slate-900 leading-tight">Q1 2026 Macroeconomic Report</h3>
                        <p class="text-sm leading-relaxed text-slate-600">Current status of inflation, trade, and overall economic performance indicators.</p>
                    </div>
                    <a href="#" class="inline-flex items-center gap-2 text-sm font-medium text-[#138496] hover:text-[#25295B] transition-colors mt-6 w-fit">
                        View Data
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- RESEARCH & ANALYSIS -->
    <section class="bg-white py-14 border-b border-slate-200" id="research">
        <div class="nrb-section-shell">
            <header class="mb-8">
                <p class="nrb-display-note">Category</p>
                <h2 class="nrb-section-title mt-1 text-slate-900">Research & Analysis</h2>
                <p class="mt-2 text-sm text-slate-500">Research publications, analytical reports and economic studies.</p>
            </header>
            <div class="grid grid-cols-2 gap-4">
                <!-- Economic Review -->
                <a href="economic-review/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Economic Review</h3>
                            <p class="text-sm text-slate-500">Periodic reviews of economic trends.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Macroeconomic Reports -->
                <a href="macroeconomic-reports/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Macroeconomic Reports</h3>
                            <p class="text-sm text-slate-500">Monthly and annual economic data.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- NRB Working Papers -->
                <a href="working-papers/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">NRB Working Papers</h3>
                            <p class="text-sm text-slate-500">Research papers from NRB economists.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Study Reports -->
                <a href="study-reports/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Study Reports</h3>
                            <p class="text-sm text-slate-500">In-depth research and study findings.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- INSTITUTIONAL REPORTS -->
    <section class="bg-slate-50 py-14 border-b border-slate-200" id="institutional">
        <div class="nrb-section-shell">
            <header class="mb-8">
                <p class="nrb-display-note">Category</p>
                <h2 class="nrb-section-title mt-1 text-slate-900">Institutional Reports</h2>
                <p class="mt-2 text-sm text-slate-500">Official reports and institutional publications.</p>
            </header>
            <div class="grid grid-cols-2 gap-4">
                <!-- Annual Reports -->
                <a href="annual-reports/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Annual Reports</h3>
                            <p class="text-sm text-slate-500">Comprehensive yearly performance reports.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Financial Stability Reports -->
                <a href="financial-stability/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Financial Stability Reports</h3>
                            <p class="text-sm text-slate-500">Assessments of financial system health.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Economic Activities Reports -->
                <a href="economic-activities/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Economic Activities Reports</h3>
                            <p class="text-sm text-slate-500">Regional and national economic activity.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- SPECIAL PUBLICATIONS -->
    <section class="bg-white py-14 border-b border-slate-200" id="special">
        <div class="nrb-section-shell">
            <header class="mb-8">
                <p class="nrb-display-note">Category</p>
                <h2 class="nrb-section-title mt-1 text-slate-900">Special Publications</h2>
                <p class="mt-2 text-sm text-slate-500">Special publications and educational resources.</p>
            </header>
            <div class="grid grid-cols-2 gap-4">
                <!-- Special Publications -->
                <a href="special-publications/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Special Publications</h3>
                            <p class="text-sm text-slate-500">Ad-hoc reports and special releases.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Golden Jubilee Publications -->
                <a href="golden-jubilee/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Golden Jubilee Publications</h3>
                            <p class="text-sm text-slate-500">50th anniversary commemorative releases.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Arthabodh -->
                <a href="arthabodh/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Arthabodh</h3>
                            <p class="text-sm text-slate-500">Financial literacy and awareness.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
                <!-- Know Your Bank Notes -->
                <a href="know-your-bank-notes/index.html" class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-6 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-colors">
                    <div class="flex items-center gap-6">
                        <div class="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-slate-50 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                            <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                        </div>
                        <div class="flex flex-col gap-1">
                            <h3 class="font-bold text-lg text-slate-900 group-hover:text-[#138496] transition-colors">Know Your Bank Notes</h3>
                            <p class="text-sm text-slate-500">Security features and banknote guides.</p>
                        </div>
                    </div>
                    <div class="dir-row-arrow text-slate-300 group-hover:text-[#138496]">
                        <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                    </div>
                </a>
            </div>
        </div>
    </section>

    <!-- Local Navigation Scroll Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const sections = ['overview', 'research', 'institutional', 'special'];
            const navLinks = {
                'overview': document.getElementById('LocalNav-Overview'),
                'research': document.getElementById('LocalNav-Research'),
                'institutional': document.getElementById('LocalNav-Institutional'),
                'special': document.getElementById('LocalNav-Special')
            };
            
            function setActive(id) {
                sections.forEach(s => {
                    const link = navLinks[s];
                    if (!link) return;
                    if (s === id) {
                        link.setAttribute('aria-current', 'page');
                    } else {
                        link.removeAttribute('aria-current');
                    }
                });
            }

            // Smooth scroll handler
            sections.forEach(id => {
                const link = navLinks[id];
                if (!link) return;
                
                link.addEventListener('click', function(e) {
                    const target = document.getElementById(id);
                    if (target) {
                        e.preventDefault();
                        const localNav = document.getElementById('Local-Navigation');
                        const offset = localNav ? localNav.getBoundingClientRect().height : 56;
                        window.scrollTo({
                            top: target.offsetTop - offset - 12,
                            behavior: 'smooth'
                        });
                        setActive(id);
                        history.replaceState(null, '', '#' + id);
                    }
                });
            });
            
            // Intersection Observer for scroll spy
            const observerOptions = {
                root: null,
                rootMargin: '-140px 0px -60% 0px',
                threshold: 0
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setActive(entry.target.id);
                    }
                });
            }, observerOptions);
            
            sections.forEach(id => {
                const el = document.getElementById(id);
                if (el) observer.observe(el);
            });
        });
    </script>
</main>
"""

new_full_html = header_html + '\n' + main_html + '\n' + footer_html

with open(hub_path, 'w', encoding='utf-8') as f:
    f.write(new_full_html)
print("Rebuilt publications hub.")
