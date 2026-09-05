import os
from bs4 import BeautifulSoup

file_path = r"c:\Users\LOQ\Desktop\NRB Redesign\pages\regulations\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, 'html.parser')

main_tag = soup.find('main')
if main_tag:
    new_main_html = """
<main id="Main-Content">
    <!-- HERO SECTION -->
    <section class="border-b border-slate-200 bg-white" id="Hero-Banner">
        <div class="nrb-section-shell py-10 lg:py-14">
            <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500" id="Breadcrumb">
                <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
                <span class="text-slate-300">/</span>
                <span class="text-slate-700">Regulations</span>
            </nav>
            <div class="grid grid-cols-[1.2fr_1fr] gap-12 items-start">
                <div class="flex flex-col gap-8">
                    <div>
                        <span class="inline-flex items-center gap-1.5 rounded-full bg-[#25295B]/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-[#25295B] mb-4">Laws, Policies & Guidelines</span>
                        <h1 class="text-2xl font-bold text-slate-900 mb-4">Regulations</h1>
                        <p class="text-base text-slate-600 leading-relaxed max-w-xl">Central repository for all legislative acts, rules, bylaws, and regulatory guidelines governing Nepal's financial and monetary systems.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- LOCAL NAVIGATION -->
    <div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
        <div class="nrb-section-shell">
            <nav aria-label="Regulations sections" class="about-local-nav flex items-center gap-8 py-4">
                <a aria-current="page" href="#laws" id="LocalNav-Laws">Laws and Legislation</a>
                <a href="#policies" id="LocalNav-Policies">Policies and Guidelines</a>
            </nav>
        </div>
    </div>

    <!-- 1. LAWS AND LEGISLATION -->
    <section class="bg-slate-50 py-14 border-b border-slate-200" id="laws">
        <div class="nrb-section-shell">
            <div class="grid grid-cols-[1.6fr_1fr] gap-10 items-start">
                <div>
                    <header class="mb-8">
                        <p class="nrb-display-note">Statutory Framework</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Laws and Legislation</h2>
                        <p class="mt-2 text-sm text-slate-500">Official acts and bylaws establishing the regulatory authority and legal framework.</p>
                    </header>
                    <div class="flex flex-col gap-4">
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="acts.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Acts</p>
                                    <p class="text-sm text-slate-600 mt-1">Official repository of acts governing central bank operations.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-slate-50 group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="rules-and-bylaws.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Rules and Bylaws</p>
                                    <p class="text-sm text-slate-600 mt-1">Regulatory rules and bylaws established by Nepal Rastra Bank.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-slate-50 group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. POLICIES AND GUIDELINES -->
    <section class="bg-white py-14 border-b border-slate-200" id="policies">
        <div class="nrb-section-shell">
            <div class="grid grid-cols-[1.6fr_1fr] gap-10 items-start">
                <div>
                    <header class="mb-8">
                        <p class="nrb-display-note">Directives & Guidelines</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Policies and Guidelines</h2>
                        <p class="mt-2 text-sm text-slate-500">Comprehensive manuals, notices, and policies directing financial operations.</p>
                    </header>
                    <div class="flex flex-col gap-4">
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-slate-50 border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="notices.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-white text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M22 17H2a3 3 0 0 0 3-3V9a7 7 0 0 1 14 0v5a3 3 0 0 0 3 3zm-8.27 4a2 2 0 0 1-3.46 0"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Notices</p>
                                    <p class="text-sm text-slate-600 mt-1">Public notices and regulatory announcements.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-slate-50 border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="guidelines-and-manuals.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-white text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Guidelines and Manuals</p>
                                    <p class="text-sm text-slate-600 mt-1">Operational manuals and procedural guidelines for institutions.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-slate-50 border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="other-policies.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-white text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Other Policies</p>
                                    <p class="text-sm text-slate-600 mt-1">Additional policy documents and regulatory directives.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-slate-50 border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20 transition-all duration-300" href="monetary-policy.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-white text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Monetary Policy</p>
                                    <p class="text-sm text-slate-600 mt-1">Official monetary policy formulations, reviews, and related archives.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-white group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>
    """
    
    # Parse the new main content and replace the old one
    new_main_soup = BeautifulSoup(new_main_html, 'html.parser')
    main_tag.replace_with(new_main_soup.main)
    
    # Update title
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = "Regulations | NRB"

    # We also need to remove the "Regulations" sticky nav that acts.html had (it might be outside main if we didn't replace it carefully, but looking at my previous script, I put the sticky nav inside <main> or right before it. Wait, the old template had the sticky nav inside the body but maybe before main? No, it's inside <main> right after Hero in annual-financial-statements.html). Let's just write back the string.

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Generated landing page at {file_path}")
