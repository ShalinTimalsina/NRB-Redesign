import re

fpath = 'pages/about/index.html'

with open(fpath, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for section #organization
old_org_section = r'<!-- 3\. ORGANIZATIONAL STRUCTURE -->.*?</section>'

new_org_section = '''<!-- 3. ORGANIZATIONAL STRUCTURE -->
            <section id="organization" class="bg-slate-50 py-14 border-b border-slate-200">
                <div class="nrb-section-shell">
                    <header class="mb-10">
                        <p class="nrb-display-note">Structure</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Organizational Structure</h2>
                        <p class="mt-2 text-sm text-slate-500">The functional hierarchy and operational divisions of the central bank.</p>
                    </header>
                    <div class="grid grid-cols-3 gap-6">
                        <!-- Card 1: Organogram -->
                        <a href="organogram.html" class="hub-card nrb-elevated-card group flex flex-col rounded-[20px] bg-white border border-slate-200 p-8 hover:border-[#1E3A5F]/20 transition-all">
                            <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] mb-5 group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                                <svg viewBox="0 0 24 24" class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="4" rx="1"/><rect x="1" y="16" width="6" height="4" rx="1"/><rect x="9" y="16" width="6" height="4" rx="1"/><rect x="17" y="16" width="6" height="4" rx="1"/><path d="M4 16V9h16v7"/><path d="M12 6v3"/></svg>
                            </div>
                            <h3 class="font-semibold text-lg text-slate-900 mb-2 group-hover:text-[#138496] transition-colors">Organogram</h3>
                            <p class="text-sm text-slate-600 leading-6 flex-grow">Explore the institutional hierarchy, executive decision-making bodies, and reporting structure of Nepal Rastra Bank.</p>
                            <span class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496]">View Organogram <svg class="dir-row-arrow h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
                        </a>

                        <!-- Card 2: Departments -->
                        <a href="departments.html" class="hub-card nrb-elevated-card group flex flex-col rounded-[20px] bg-white border border-slate-200 p-8 hover:border-[#1E3A5F]/20 transition-all">
                            <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] mb-5 group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                                <svg viewBox="0 0 24 24" class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16"/><path d="M4 20V8l8-6 8 6v12"/><path d="M10 20v-6h4v6"/></svg>
                            </div>
                            <h3 class="font-semibold text-lg text-slate-900 mb-2 group-hover:text-[#138496] transition-colors">Departments, Divisions &amp; Units</h3>
                            <p class="text-sm text-slate-600 leading-6 flex-grow">Directory of 17 specialized departments, 1 executive office, 6 division offices, and 1 unit supporting monetary policy, supervision, and payment systems.</p>
                            <span class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496]">View Departments <svg class="dir-row-arrow h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
                        </a>

                        <!-- Card 3: Provincial Offices -->
                        <a href="provincial-offices.html" class="hub-card nrb-elevated-card group flex flex-col rounded-[20px] bg-white border border-slate-200 p-8 hover:border-[#1E3A5F]/20 transition-all">
                            <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-100 text-[#25295B] mb-5 group-hover:bg-[#25295B] group-hover:text-white transition-colors">
                                <svg viewBox="0 0 24 24" class="h-6 w-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                            </div>
                            <h3 class="font-semibold text-lg text-slate-900 mb-2 group-hover:text-[#138496] transition-colors">Provincial Offices</h3>
                            <p class="text-sm text-slate-600 leading-6 flex-grow">7 regional offices situated across Nepal's provinces extending regulatory, supervisory, currency management, and public treasury services nationwide.</p>
                            <span class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-[#138496]">View Provincial Offices <svg class="dir-row-arrow h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
                        </a>
                    </div>
                </div>
            </section>'''

html = re.sub(old_org_section, new_org_section, html, flags=re.DOTALL)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed placeholder and top images from organizational structure cards in index.html!")
