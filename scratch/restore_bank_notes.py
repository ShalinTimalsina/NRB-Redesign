import markdown
from pathlib import Path
from bs4 import BeautifulSoup

md_path = Path('NRB Page md files/Publications/bank-notes-security-features-the-official-site-of-the-central-bank-of-nepal-20260921142117.md')
html_path = Path('pages/publications/know-your-bank-notes/index.html')

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Clean up the markdown a bit for better HTML rendering
# Replace the raw image links with styled ones
md_content = md_content.replace('![](', '![Banknote](')

# Convert to HTML
html_content = markdown.markdown(md_content)

# Style the HTML output
styled_html = f"""
<div class="nrb-section-shell">
    <div class="prose prose-slate max-w-none prose-headings:text-slate-900 prose-a:text-[#138496] hover:prose-a:text-[#25295B] prose-img:rounded-xl prose-img:shadow-sm">
        {html_content}
    </div>
</div>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find the main section to replace
main_tag = soup.find('main')
if main_tag:
    # We want to keep the HERO and LOCAL NAVIGATION, and only replace the DOCUMENT GRID
    documents_section = main_tag.find('section', id='documents')
    if documents_section:
        new_section = BeautifulSoup(f'<section class="py-14 border-b border-slate-200 bg-white" id="bank-notes-content">{styled_html}</section>', 'html.parser')
        documents_section.replace_with(new_section)
        
        # Clean up any leftover Nepali if any was in the markdown
        final_html = str(soup)
        final_html = final_html.replace('नोटलाई उज्यालो प्रकाश तर्फ राखेर हेर्दा अथवा नोटको पछाडिबाट लाईट(टर्च लाइट/मोबाइलको लाइट) को माध्यमबाट नोटको उक्त स्थानमा प्रकाश प्रसारण हुँदा लालीगुँरासको आकृति स्पष्ट देखिन्छ ।', 'When you hold the banknote against the light, the rhododendron watermark is clearly visible.')
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Restored Know Your Bank Notes content successfully.")
    else:
        print("Could not find the documents section to replace.")
else:
    print("Could not find the main tag.")
