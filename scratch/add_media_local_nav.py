import os

subpages = [
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/media-releases/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/speeches/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/notices/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches/bok-kpp/index.html'
]

local_nav_html = """
<!-- LOCAL NAVIGATION -->
<div class="sticky top-0 z-10 border-b border-slate-200 bg-white shadow-sm" id="Local-Navigation">
    <div class="nrb-section-shell">
        <nav aria-label="Local sections" class="nrb-page-nav flex items-center gap-8 py-4">
            <a href="../../media-speeches/index.html" class="flex items-center gap-2 text-slate-500 hover:text-[#25295B] transition-colors pr-4 border-r border-slate-200">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                Back to Hub
            </a>
            <a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
            <a href="#documents" id="LocalNav-Documents">Documents</a>
        </nav>
    </div>
</div>
"""

local_nav_js = """
<script>
    (function () {
        const sections = ['overview', 'documents'];
        const navLinks = {};
        const keyMap = {
            'overview': 'LocalNav-Overview',
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
            // Fallback for overview to scroll to top if hero banner is considered overview
            if (id === 'overview' && !target) {
                 window.scrollTo({ top: 0, behavior: 'smooth' });
                 return;
            }
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

count = 0
for filepath in subpages:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="Local-Navigation"' not in content:
        # Insert local_nav_html right before <section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">
        target = '<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">'
        if target in content:
            content = content.replace(target, local_nav_html + '\n' + target)
            
            # Insert local_nav_js right before closing </main>
            content = content.replace('</main>', local_nav_js + '\n</main>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

print(f"Added local navigation to {count} files.")
