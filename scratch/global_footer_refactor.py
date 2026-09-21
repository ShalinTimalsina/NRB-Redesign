import os
from pathlib import Path
from bs4 import BeautifulSoup

def get_depth_prefix(filepath):
    parts = Path(filepath).parts
    depth = len(parts) - 1
    if depth == 0:
        return ""
    else:
        return "../" * depth

def global_footer_refactor():
    count = 0
    for p in Path('.').rglob('*.html'):
        if 'scratch' in p.parts:
            continue
            
        with open(p, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        footer = soup.find('footer', id='Footer')
        
        if not footer:
            continue
            
        prefix = get_depth_prefix(p)
        
        new_footer_html = f"""
        <footer class="nrb-footer bg-[#25295B] text-white" id="Footer">
            <div class="nrb-section-shell py-14">
                <!-- Top Row: Branding -->
                <div class="flex items-center justify-between pb-8 border-b border-white/10">
                    <div class="flex items-center gap-4">
                        <div class="flex h-11 w-11 items-center justify-center rounded-full bg-white">
                            <img alt="NRB" class="h-10 w-10 object-contain" src="{prefix}assets/images/nrb-logo.png"/>
                        </div>
                        <div>
                            <p class="text-sm font-semibold uppercase tracking-[0.22em] text-white">Nepal Rastra Bank</p>
                            <p class="text-xs text-slate-400 mt-0.5">Central Bank of Nepal &middot; Est. 1956</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-4">
                        <a href="#" class="flex h-9 w-9 items-center justify-center rounded-lg bg-white/5 text-slate-300 hover:bg-white/10 hover:text-white transition" aria-label="Facebook">
                            <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                        </a>
                        <a href="#" class="flex h-9 w-9 items-center justify-center rounded-lg bg-white/5 text-slate-300 hover:bg-white/10 hover:text-white transition" aria-label="Twitter">
                            <svg class="h-4 w-4" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                        </a>
                    </div>
                </div>

                <!-- Middle Row: Navigation Columns -->
                <div class="grid grid-cols-2 md:grid-cols-4 gap-8 pt-8 pb-8">
                    <!-- Column 1: About NRB -->
                    <div class="flex flex-col gap-3">
                        <h3 class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-200 mb-1">About NRB</h3>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/about/index.html">Overview &amp; History</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/about/index.html#leadership">Board of Directors</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/about/index.html#organization">Departments</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/monetary-policy/index.html">Monetary Policy</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/regulation-and-supervision/index.html">Regulation &amp; Supervision</a>
                    </div>

                    <!-- Column 2: Data & Publications -->
                    <div class="flex flex-col gap-3">
                        <h3 class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-200 mb-1">Data &amp; Publications</h3>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/forex-management/index.html">Exchange Rates</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/statistics/index.html">Statistics &amp; Indicators</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/publications/index.html">Publications &amp; Reports</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/media-speeches/index.html">Media &amp; Speeches</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/notices/index.html">Notices &amp; Circulars</a>
                    </div>

                    <!-- Column 3: Public Services -->
                    <div class="flex flex-col gap-3">
                        <h3 class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-200 mb-1">Public Services</h3>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="http://gunaso.nrb.org.np/" target="_blank" rel="noopener">Consumer Protection</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="http://emap.nrb.org.np/" target="_blank" rel="noopener">Financial Inclusion Portal</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="https://goaml.fiu.nrb.org.np/PRD/Home" target="_blank" rel="noopener">goAML Portal</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/procurement/index.html">Procurement</a>
                        <a class="text-sm text-slate-400 transition hover:text-white" href="{prefix}pages/contact/index.html">Contact &amp; Feedback</a>
                    </div>

                    <!-- Column 4: Contact Information -->
                    <div class="flex flex-col gap-3">
                        <h3 class="text-xs font-semibold uppercase tracking-[0.18em] text-slate-200 mb-1">Central Office</h3>
                        <p class="text-sm text-slate-400 leading-relaxed">Baluwatar, Kathmandu<br>Bagmati Province, Nepal</p>
                        <p class="text-sm text-slate-400">Phone: +977-1-4419804</p>
                        <p class="text-sm text-slate-400">Email: info@nrb.org.np</p>
                        <div class="mt-2 pt-3 border-t border-white/5">
                            <p class="text-xs text-slate-500"><span class="text-slate-300">Spokesperson:</span> Dr. Ram Sharan Kharel</p>
                            <p class="text-xs text-slate-500 mt-1"><span class="text-slate-300">Info Officer:</span> Narayan Prasad Pokhrel</p>
                        </div>
                    </div>
                </div>

                <!-- Bottom Row: Legal -->
                <div class="flex flex-wrap items-center justify-between gap-4 border-t border-white/10 pt-6 text-xs text-slate-500">
                    <p>&copy; 2026 Nepal Rastra Bank. All rights reserved.</p>
                    <div class="flex flex-wrap items-center gap-5">
                        <a class="transition hover:text-white" href="#">Privacy Policy</a>
                        <a class="transition hover:text-white" href="#">Accessibility</a>
                        <a class="transition hover:text-white" href="#">Terms of Use</a>
                        <a class="transition hover:text-white" href="#">Sitemap</a>
                    </div>
                </div>
            </div>
        </footer>
        """
        
        new_footer_soup = BeautifulSoup(new_footer_html, 'html.parser')
        footer.replace_with(new_footer_soup)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        count += 1

    print(f"Rebuilt {count} footers across the site.")

if __name__ == '__main__':
    global_footer_refactor()
