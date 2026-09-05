import os
import glob
from bs4 import BeautifulSoup
import re

html_files = glob.glob(r"c:\Users\LOQ\Desktop\NRB Redesign\pages\**\*.html", recursive=True)
base_dir = r"c:\Users\LOQ\Desktop\NRB Redesign"

for file_path in html_files:
    if "node_modules" in file_path or ".gemini" in file_path or "scratch" in file_path:
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    modified = False

    # 1. Remove "Back to..." Links
    for a_tag in soup.find_all('a'):
        if a_tag.text and "Back to " in a_tag.text:
            parent = a_tag.parent
            if parent and parent.name == 'div' and len(parent.find_all('a')) == 1:
                parent.decompose()
                modified = True
            else:
                a_tag.decompose()
                modified = True

    # 2. Remove Section Badges
    for span in soup.find_all('span', class_=True):
        classes = span.get('class', [])
        if 'uppercase' in classes and 'tracking-[0.2em]' in classes and 'font-semibold' in classes:
            span.decompose()
            modified = True

    # 3. Breadcrumbs Normalization
    navs = soup.find_all('nav', attrs={'aria-label': 'Breadcrumb'})
    h1 = soup.find('h1')
    h1_text = h1.text.strip() if h1 else ""

    for nav in navs:
        # Get all links and texts
        children = [c for c in nav.children if c.name in ['a', 'span']]
        
        # Check if the last item is a span (current page indicator)
        if children and children[-1].name == 'span':
            last_span = children[-1]
            if last_span.text.strip() != h1_text:
                last_span.string = h1_text
                modified = True

        # Check first link is Home
        if children and children[0].name == 'a':
            if children[0].text.strip() != 'Home':
                children[0].string = 'Home'
                modified = True
                
        # (Note: Validating folder hierarchy precisely is complex to automate without knowing the exact intended IA,
        # but fixing the H1 mismatch is the most critical and solves 90% of inconsistencies).

    if modified:
        # Convert back to string. We use prettify/formatter to try and preserve, but beautifulsoup might reformat.
        # To avoid massive diffs, let's just do regex replacements for the specific things instead of BS4 if possible,
        # but BS4 is safer for DOM manipulation. We'll use BS4 but it may change formatting slightly.
        # Wait, if we use BS4, we might lose formatting. Let's write the modified HTML out.
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Updated: {file_path}")
