import os
import re

files_to_update = [
    (r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\financial-statements.html", 1),
    (r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\annual-financial-statements.html", 2),
    (r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\investment-related-notices.html", 3)
]

nav_template = """
<!-- FINANCIAL STATEMENTS NAVIGATION STRIP -->
<div class="border-b border-slate-200 bg-white sticky top-0 z-20 shadow-sm">
    <div class="nrb-section-shell">
        <nav aria-label="Financial Statements navigation" class="about-local-nav flex items-center gap-8 py-4">
            <a href="financial-statements.html"{active_1}>Overview</a>
            <a href="annual-financial-statements.html"{active_2}>Annual Financial Statements (Audited)</a>
            <a href="investment-related-notices.html"{active_3}>Investment Related Notices</a>
        </nav>
    </div>
</div>
<section class="bg-slate-50"""

for file_path, active_index in files_to_update:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Create the nav block with the correct active state
    nav_html = nav_template.replace("{active_1}", ' aria-current="page"' if active_index == 1 else "")
    nav_html = nav_html.replace("{active_2}", ' aria-current="page"' if active_index == 2 else "")
    nav_html = nav_html.replace("{active_3}", ' aria-current="page"' if active_index == 3 else "")

    # Insert before the content section
    # Avoid double inserting
    if "FINANCIAL STATEMENTS NAVIGATION STRIP" not in content:
        content = content.replace('<section class="bg-slate-50', nav_html, 1)

    # Remove the Publications & Notices header from financial-statements.html
    if active_index == 1:
        # We can use regex to remove the specific header block
        pattern = r'<header class="mb-8">\s*<p class="nrb-display-note">Categories</p>\s*<h2 class="nrb-section-title mt-1 text-slate-900">Publications &amp; Notices</h2>\s*</header>'
        content = re.sub(pattern, '', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated: {file_path}")
