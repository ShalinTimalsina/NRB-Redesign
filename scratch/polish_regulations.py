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
                        <span class="inline-flex items-center gap-1.5 rounded-full bg-[#25295B]/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-[#25295B] mb-4">Statutory & Regulatory Framework</span>
                        <h1 class="text-2xl font-bold text-slate-900 mb-4">Regulations</h1>
                        <p class="text-base text-slate-600 leading-relaxed max-w-xl">Central repository for all legislative acts, rules, bylaws, and regulatory guidelines governing Nepal's financial and monetary systems.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 1. LAWS AND LEGISLATION -->
    <section class="bg-slate-50 py-14 border-b border-slate-200">
        <div class="nrb-section-shell">
            <div class="grid grid-cols-[1.6fr_1fr] gap-10 items-start">
                <div>
                    <header class="mb-8">
                        <p class="nrb-display-note">Statutory Framework</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Laws and Legislation</h2>
                        <p class="mt-2 text-sm text-slate-500">Official acts and bylaws establishing the regulatory authority and legal framework.</p>
                    </header>
                    <div class="flex flex-col gap-4">
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="acts.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2z"></path><path d="M12 15v7"></path><path d="M9 22h6"></path><path d="M12 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path></svg>
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
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="rules-and-bylaws.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect><path d="M9 14h6"></path><path d="M9 18h6"></path><path d="M9 10h6"></path></svg>
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
    <section class="bg-white py-14 border-b border-slate-200">
        <div class="nrb-section-shell">
            <div class="grid grid-cols-[1.6fr_1fr] gap-10 items-start">
                <div>
                    <header class="mb-8">
                        <p class="nrb-display-note">Directives & Guidelines</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Policies and Guidelines</h2>
                        <p class="mt-2 text-sm text-slate-500">Comprehensive notices, manuals, and policy documentation to guide financial institutions.</p>
                    </header>
                    <div class="flex flex-col gap-4">
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="notices.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Notices</p>
                                    <p class="text-sm text-slate-600 mt-1">Public regulatory announcements and immediate compliance notifications.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-slate-50 group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="guidelines-and-manuals.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Guidelines and Manuals</p>
                                    <p class="text-sm text-slate-600 mt-1">Comprehensive operational manuals and procedural guidelines.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-slate-50 group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="other-policies.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Other Policies</p>
                                    <p class="text-sm text-slate-600 mt-1">Supplementary frameworks and targeted directives.</p>
                                </div>
                            </div>
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-slate-50 group-hover:bg-[#138496]/10 transition-colors ml-4">
                                <svg class="dir-row-arrow h-5 w-5 text-[#138496]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
                            </div>
                        </a>
                        <a class="dir-row hub-card nrb-elevated-card flex items-center justify-between p-8 bg-white border border-slate-200 rounded-[20px] group hover:border-[#25295B]/20" href="monetary-policy.html">
                            <div class="flex items-center gap-6">
                                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-[16px] bg-slate-50 text-[#25295B] border border-slate-100 group-hover:bg-[#25295B] group-hover:text-white group-hover:border-[#25295B] transition-all duration-300">
                                    <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline></svg>
                                </div>
                                <div>
                                    <p class="text-lg font-semibold text-[#25295B] group-hover:text-[#138496] transition-colors">Monetary Policy</p>
                                    <p class="text-sm text-slate-600 mt-1">Official monetary policy formulations, reviews, and related archives.</p>
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
</main>
    """
    
    new_main_soup = BeautifulSoup(new_main_html, 'html.parser')
    main_tag.replace_with(new_main_soup.main)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Strict landing page with meaningful icons generated at {file_path}")
