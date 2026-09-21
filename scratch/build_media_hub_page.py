import os
import re

# 1. Base template structure
def get_header_and_footer(source_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = re.split(r'<main[^>]*>', content)
    header_part = parts[0] + '<main id="Main-Content">\n'
    footer_part = '\n</main>\n' + re.split(r'</main>', parts[1])[-1]
    
    return header_part, footer_part

# Extract header and footer from about/index.html
header, footer = get_header_and_footer('pages/about/index.html')

# Update Title
header = header.replace('<title>About | Nepal Rastra Bank</title>', '<title>Media & Speeches | Nepal Rastra Bank</title>')

# HUB PAGE CONTENT
hub_content = """
<!-- HERO & SNAPSHOT -->
<section class="border-b border-slate-200 bg-white" id="Hero-Banner">
    <div class="nrb-section-shell py-10 lg:py-14">
        <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500" id="Breadcrumb">
            <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
            <span class="text-slate-300">/</span>
            <span class="text-slate-700">Media & Speeches</span>
        </nav>
        <div class="grid grid-cols-[1.2fr_1fr] gap-12 items-start">
            <div class="flex flex-col gap-8">
                <div>
                    <span class="inline-flex items-center gap-1.5 rounded-full bg-[#25295B]/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-[#25295B] mb-4">Office of the Governor</span>
                    <h1 class="text-2xl font-bold text-slate-900 mb-4">Media & Speeches</h1>
                    <p class="text-base text-slate-600 leading-relaxed max-w-xl">Official media releases, press statements, and governor's speeches that communicate the central bank's policy positions, decisions, and responses to national and international audiences.</p>
                </div>
            </div>
            <div class="flex flex-col gap-5">
                <aside class="overflow-hidden rounded-[20px] bg-[#25295B] text-white">
                    <div class="px-6 py-4 border-b border-white/10">
                        <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-300">Communication Snapshot</p>
                    </div>
                    <div class="grid grid-cols-2 gap-px bg-white/10">
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Media Releases</p>
                            <p class="text-xl font-bold text-white">35+</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Speeches</p>
                            <p class="text-xl font-bold text-white">12+</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Notices</p>
                            <p class="text-xl font-bold text-white">28+</p>
                        </div>
                        <div class="bg-[#25295B] px-5 py-4">
                            <p class="text-xs uppercase tracking-widest text-slate-400 mb-1">Study Reports</p>
                            <p class="text-xl font-bold text-white">15+</p>
                        </div>
                    </div>
                    <div class="bg-[#138496] px-6 py-3 text-xs text-white/90 flex justify-between items-center">
                        <span>Data as of Sep 2026</span>
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
            <a href="#communications" id="LocalNav-Communications">Communications</a>
            <a href="#documents" id="LocalNav-Documents">Documents</a>
        </nav>
    </div>
</div>

<!-- COMMUNICATIONS HUB GRID -->
<section class="bg-slate-50 py-16 border-b border-slate-200" id="communications">
    <div class="nrb-section-shell">
        <header class="mb-10">
            <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">Public Relations</p>
            <h2 class="text-2xl font-bold mt-1 text-slate-900">Communications</h2>
            <p class="mt-2 text-sm text-slate-500">Official press statements and speeches from the Governor's office.</p>
        </header>
        <div class="grid grid-cols-2 gap-6">
            <!-- Media Releases -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="media-releases/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 20H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v1m2 13a2 2 0 0 1-2-2V7m2 13a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2m-4-3H9M7 16h6M7 8h4m-4 4h6" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Media Releases</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Official press statements, announcements, and responses to current events.</p>
                </div>
            </a>
            <!-- Speeches -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#138496] group transition-colors" href="speeches/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z M19 10v2a7 7 0 0 1-14 0v-2 M12 19v4 M8 23h8" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#138496] transition-colors leading-tight">Speeches</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Transcripts and PDFs of speeches delivered by the Governor at various forums.</p>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- DOCUMENTS HUB GRID -->
<section class="py-16 bg-white" id="documents">
    <div class="nrb-section-shell">
        <header class="mb-10">
            <p class="text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">Official Publications</p>
            <h2 class="text-2xl font-bold mt-1 text-slate-900">Documents</h2>
            <p class="mt-2 text-sm text-slate-500">Notices, guidelines, and joint study reports issued by the central bank.</p>
        </header>
        <div class="grid grid-cols-2 gap-6">
            <!-- Notices -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="notices/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9 M13.73 21a2 2 0 0 1-3.46 0" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">Notices</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Monetary policy announcements, macroeconomic reports, and regulatory notices.</p>
                </div>
            </a>
            <!-- BOK-KPP Reports -->
            <a class="hub-card nrb-elevated-card flex items-start gap-5 rounded-[20px] bg-white border border-slate-200 p-6 hover:border-[#25295B] group transition-colors" href="bok-kpp/index.html">
                <div class="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                    <svg class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
                <div class="flex flex-col gap-2">
                    <h3 class="font-semibold text-lg text-slate-900 group-hover:text-[#25295B] transition-colors leading-tight">BOK-KPP Study Reports</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">Joint study reports under the Bank of Korea – Knowledge Partnership Program.</p>
                </div>
            </a>
        </div>
    </div>
</section>

<script>
    (function () {
        const sections = ['overview', 'communications', 'documents'];
        const navLinks = {};
        const keyMap = {
            'overview': 'LocalNav-Overview',
            'communications': 'LocalNav-Communications',
            'documents': 'LocalNav-Documents'
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

os.makedirs('pages/media-speeches', exist_ok=True)
with open('pages/media-speeches/index.html', 'w', encoding='utf-8') as f:
    f.write(header + hub_content + footer)

print("Media & Speeches Hub page built successfully.")
