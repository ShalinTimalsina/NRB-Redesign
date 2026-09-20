import re

filepath = 'pages/monetary-policy/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Local Navigation
local_nav_old = '''<nav aria-label="Monetary Policy sections" class="nrb-page-nav flex items-center gap-8 py-4">
<a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
<a href="#monetary-operations" id="LocalNav-MonetaryOperations">Monetary Operations</a>
<a href="#data-reports" id="LocalNav-DataReports">Data &amp; Reports</a>
<a href="#circulars" id="LocalNav-Circulars">Circulars</a>
<a href="#notices" id="LocalNav-Notices">Notices</a>
<a href="#policies-procedures" id="LocalNav-PoliciesProcedures">Policies &amp; Procedures</a>
</nav>'''

local_nav_new = '''<nav aria-label="Monetary Policy sections" class="nrb-page-nav flex items-center gap-8 py-4">
<a aria-current="page" href="#overview" id="LocalNav-Overview">Overview</a>
<a href="#quick-access" id="LocalNav-QuickAccess">Quick Access</a>
</nav>'''

content = content.replace(local_nav_old, local_nav_new)

# 2. Change section ID for Quick Access from "monetary-operations" to "quick-access"
content = content.replace('<section class="bg-white py-14 border-b border-slate-200" id="monetary-operations">', '<section class="bg-white py-14 border-b border-slate-200" id="quick-access">')

# 3. Remove target="_blank" from Quick Access links and update hrefs
content = content.replace('href="monetary-operations/index.html" target="_blank"', 'href="monetary-operations/index.html"')
content = content.replace('href="notices/index.html" target="_blank"', 'href="notices/index.html"')
content = content.replace('href="#data-reports" target="_blank"', 'href="data-reports/index.html"')
content = content.replace('href="#circulars" target="_blank"', 'href="circulars/index.html"')

# 4. Strip sections 3 to 6
# From <!-- 3. DATA & REPORTS (Featured Resources) --> up to but not including </main></div>

pattern = r'<!-- 3\. DATA & REPORTS.*?<!-- GLOBAL FOOTER -->'
replacement = '<!-- GLOBAL FOOTER -->'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Landing page simplified.")
