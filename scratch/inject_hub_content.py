import os
import re

# We will read the exact original regulation-and-supervision/index.html
source_file = 'pages/regulation-and-supervision/index.html'
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split around the <main id="Main-Content"> block
# We want everything before the opening <main> tag and everything after the closing </main> tag.
# Since we are not touching the header, we keep it pristine!
parts = re.split(r'<main[^>]*>', content)
if len(parts) > 1:
    header_part = parts[0] + '<main id="Main-Content">\n'
    footer_part = '\n</main>\n' + re.split(r'</main>', parts[1])[-1]
else:
    print("Could not find <main> tag!")
    exit(1)

# HUB PAGE CONTENT
hub_content = """
<!-- HERO & SNAPSHOT -->
<section class="border-b border-slate-200 bg-white" id="Hero-Banner">
    <div class="nrb-section-shell py-10 lg:py-14">
        <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500" id="Breadcrumb">
            <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
            <span class="text-slate-300">/</span>
            <span class="text-slate-700">Regulation & Supervision</span>
        </nav>
        <div class="grid grid-cols-[1.2fr_1fr] gap-12 items-start">
            <div class="flex flex-col gap-8">
                <div>
                    <span class="inline-flex items-center gap-1.5 rounded-full bg-[#25295B]/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-[#25295B] mb-4">Regulatory Framework</span>
                    <h1 class="text-2xl font-bold text-slate-900 mb-4">Regulation & Supervision</h1>
                    <p class="text-base text-slate-600 leading-relaxed max-w-xl">Nepal Rastra Bank ensures a stable, secure, and transparent financial system by providing robust regulatory frameworks and continuous supervision of all licensed banks, financial institutions, and payment service providers.</p>
                </div>
            </div>
            <div class="flex flex-col gap-5">
                <aside class="overflow-hidden rounded-[20px] bg-[#25295B] text-white">
                    <div class="px-6 py-4 border-b border-white/10">
                        <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-300">Supervision Snapshot</p>
                    </div>
                    <div class="grid grid-cols-2 gap-px bg-white/10">
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Commercial Banks</p>
                            <p class="text-xl font-bold text-white">20</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Development Banks</p>
                            <p class="text-xl font-bold text-white">17</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Finance Companies</p>
                            <p class="text-xl font-bold text-white">17</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Microfinance</p>
                            <p class="text-xl font-bold text-white">55</p>
                        </div>
                    </div>
                    <div class="bg-[#138496] px-6 py-3 text-xs text-white/90 flex justify-between items-center">
                        <span>Data as of Mid-July 2026</span>
                    </div>
                </aside>
            </div>
        </div>
    </div>
</section>

<!-- LOCAL NAVIGATION -->
<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
    <div class="nrb-section-shell">
        <nav aria-label="Local sections" class="nrb-page-nav flex items-center gap-8 py-4">
            <a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
            <a href="#regulations" id="LocalNav-Regulations">Regulations</a>
            <a href="#supervisions" id="LocalNav-Supervisions">Supervisions</a>
        </nav>
    </div>
</div>

<!-- REGULATIONS HUB GRID -->
<section class="bg-slate-50 py-16 border-b border-slate-200" id="regulations">
    <div class="nrb-section-shell">
        <header class="mb-10">
            <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">Departments</p>
            <h2 class="text-2xl font-bold mt-1 text-slate-900">Regulations</h2>
            <p class="mt-2 text-sm text-slate-500">Regulatory departments governing various sectors of the financial system.</p>
        </header>
        <div class="grid grid-cols-2 gap-6">
            <!-- BFR -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="bfr/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Banks & Financial Institutions (BFR)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Directives, Circulars, and Notices for commercial banks, development banks, and finance companies.</p>
                </div>
            </a>
            <!-- FXM -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="fxm/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Foreign Exchange Management (FXM)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Regulations and guidelines pertaining to foreign exchange rates, reserves, and operations.</p>
                </div>
            </a>
            <!-- PSD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="psd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 4H3a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zM1 10h22" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Payment Systems (PSD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Regulations for payment service providers, operators, and digital financial frameworks.</p>
                </div>
            </a>
            <!-- BKD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="bkd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11m16-11v11M8 14v3m4-3v3m4-3v3" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Banking Department (BKD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Notices and ECC notices concerning banking operations and compliance.</p>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- SUPERVISIONS HUB GRID -->
<section class="py-16 bg-white" id="supervisions">
    <div class="nrb-section-shell">
        <header class="mb-10">
            <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">Departments</p>
            <h2 class="text-2xl font-bold mt-1 text-slate-900">Supervisions</h2>
            <p class="mt-2 text-sm text-slate-500">Supervisory bodies monitoring the health and compliance of financial institutions.</p>
        </header>
        <div class="grid grid-cols-2 gap-6">
            <!-- BSD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="bsd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">Bank Supervision (BSD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Enforcement actions, key financial indicators, and annual reports for Class 'A' banks.</p>
                </div>
            </a>
            <!-- FISD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="fisd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z M14 2v6h6" stroke-linecap="round" stroke-linejoin="round"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">Financial Institutions Supervision (FISD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Supervision of development banks and finance companies.</p>
                </div>
            </a>
            <!-- MFD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="mfd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M9 7a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M23 21v-2a4 4 0 0 0-3-3.87 M16 3.13a4 4 0 0 1 0 7.75" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">Microfinance Institutions Supervision (MFD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Monitoring of microfinance activities and progress reports.</p>
                </div>
            </a>
            <!-- NBFISD -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="nbfisd/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">Non-Bank Financial Institutions (NBFISD)</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Oversight of non-bank financial entities, including specific notices and bylaws.</p>
                </div>
            </a>
        </div>
    </div>
</section>

<script>
    (function () {
        const sections = ['overview', 'regulations', 'supervisions'];
        const navLinks = {};
        const keyMap = {
            'overview': 'LocalNav-Overview',
            'regulations': 'LocalNav-Regulations',
            'supervisions': 'LocalNav-Supervisions'
        };
        sections.forEach(id => {
            const el = document.getElementById(keyMap[id]);
            if (el) navLinks[id] = el;
        });
        function setActive(id) {
            sections.forEach(s => {
                const link = navLinks[s];
                if (!link) return;
                s === id
                    ? link.setAttribute('aria-current', 'page')
                    : link.removeAttribute('aria-current');
            });
        }
        function scrollToSection(id) {
            const target = document.getElementById(id);
            if (!target) return;
            const localNav = document.getElementById('Local-Navigation');
            const offset = localNav ? localNav.getBoundingClientRect().height : 56;
            window.scrollTo({
                top: target.offsetTop - offset - 12,
                behavior: 'smooth'
            });
        }
        Object.keys(navLinks).forEach(id => {
            navLinks[id].addEventListener('click', function(e) {
                if (id === 'overview') {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                    setActive('overview');
                    history.replaceState(null, '', '#');
                    e.preventDefault();
                    return;
                }
                e.preventDefault();
                setActive(id);
                scrollToSection(id);
                history.replaceState(null, '', '#' + id);
            });
        });
    })();
</script>
"""

with open(source_file, 'w', encoding='utf-8') as f:
    f.write(header_part + hub_content + footer_part)

print("Hub page rebuilt successfully, leaving the original header untouched.")
