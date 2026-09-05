import os
import re
from datetime import datetime

mapping = {
    "acts.html": ("acts-archives-the-official-site-of-the-central-bank-of-nepal-20260906002751.md", "Acts", "Laws and Legislation", "Official repository of acts and legislative documents governing the central bank operations."),
    "rules-and-bylaws.html": ("rules-&-by-laws-archives-the-official-site-of-the-central-bank-of-nepal-20260906002803.md", "Rules and Bylaws", "Laws and Legislation", "Official rules, bylaws, and regulatory frameworks established by Nepal Rastra Bank."),
    "notices.html": ("notices-archives-the-official-site-of-the-central-bank-of-nepal-20260906003107.md", "Notices", "Policies and Guidelines", "Public notices and regulatory announcements issued by Nepal Rastra Bank."),
    "guidelines-and-manuals.html": ("manual-guidelines-archives-the-official-site-of-the-central-bank-of-nepal-20260906003119.md", "Guidelines and Manuals", "Policies and Guidelines", "Comprehensive operational manuals and procedural guidelines for financial institutions."),
    "other-policies.html": ("other-policies-archives-the-official-site-of-the-central-bank-of-nepal-20260906003129.md", "Other Policies", "Policies and Guidelines", "Additional policy documents and regulatory directives."),
    "monetary-policy.html": ("monetary-policy-archives-the-official-site-of-the-central-bank-of-nepal-20260906003136.md", "Monetary Policy", "Policies and Guidelines", "Official monetary policy formulations, reviews, and related archives.")
}

md_dir = r"c:\Users\LOQ\Desktop\NRB Redesign\NRB Page md files\laws-policies"
out_dir = r"c:\Users\LOQ\Desktop\NRB Redesign\pages\regulations"
base_template_path = r"c:\Users\LOQ\Desktop\NRB Redesign\pages\about\annual-financial-statements.html"

os.makedirs(out_dir, exist_ok=True)

with open(base_template_path, "r", encoding="utf-8") as f:
    base_html = f.read()

# Splitted Nav Strips
laws_nav_strip = """<!-- LAWS NAVIGATION STRIP -->
<div class="border-b border-slate-200 bg-white sticky top-0 z-20 shadow-sm">
    <div class="nrb-section-shell">
        <nav aria-label="Laws navigation" class="about-local-nav flex items-center gap-8 py-4 overflow-x-auto">
            <a href="acts.html"{act_active}>Acts</a>
            <a href="rules-and-bylaws.html"{rule_active}>Rules and Bylaws</a>
        </nav>
    </div>
</div>"""

policies_nav_strip = """<!-- POLICIES NAVIGATION STRIP -->
<div class="border-b border-slate-200 bg-white sticky top-0 z-20 shadow-sm">
    <div class="nrb-section-shell">
        <nav aria-label="Policies navigation" class="about-local-nav flex items-center gap-8 py-4 overflow-x-auto">
            <a href="notices.html"{not_active}>Notices</a>
            <a href="guidelines-and-manuals.html"{gui_active}>Guidelines and Manuals</a>
            <a href="other-policies.html"{oth_active}>Other Policies</a>
            <a href="monetary-policy.html"{mon_active}>Monetary Policy</a>
        </nav>
    </div>
</div>"""

def format_size(size_str):
    if not size_str:
        return ""
    try:
        match = re.match(r'([\d.]+)\s*([a-zA-Z]+)', size_str.strip())
        if match:
            val = float(match.group(1))
            unit = match.group(2).upper()
            
            # Convert everything to bytes roughly for calculation
            bytes_val = val
            if unit == "KB": bytes_val *= 1024
            elif unit == "MB": bytes_val *= 1024*1024
            elif unit == "GB": bytes_val *= 1024*1024*1024
            
            mb = bytes_val / (1024 * 1024)
            if mb >= 1.0:
                # Format to max 1 decimal place, but drop .0
                formatted = f"{mb:.1f}".rstrip('0').rstrip('.')
                return f"{formatted} MB"
            else:
                kb = bytes_val / 1024
                formatted = str(int(round(kb)))
                return f"{formatted} KB"
    except Exception:
        pass
    return size_str

def format_date(date_str):
    if not date_str:
        return ""
    try:
        # Expected format: "February 28, 2025" or similar
        d = datetime.strptime(date_str.strip(), "%B %d, %Y")
        return d.strftime("%d %b %Y").lstrip("0")
    except Exception:
        return date_str.strip()

def generate_card(title, url, date_size):
    date = ""
    size = ""
    ds_match = re.search(r'([A-Za-z]+\s+\d{1,2},\s+\d{4})\s*(.*)', date_size)
    if ds_match:
        date = ds_match.group(1).strip()
        size = ds_match.group(2).strip()
    else:
        date = date_size.strip()
    
    is_pdf = url.lower().endswith('.pdf') or 'pdf' in url.lower()
    file_type = "PDF" if is_pdf else "DOC"
    
    date_f = format_date(date)
    size_f = format_size(size)
    
    meta_parts = []
    meta_parts.append(f'<span class="font-medium text-slate-700">{file_type}</span>')
    if size_f:
        meta_parts.append(f'<span class="text-slate-300 px-1.5">•</span><span>{size_f}</span>')
    if date_f:
        meta_parts.append(f'<span class="text-slate-300 px-1.5">•</span><span>{date_f}</span>')
        
    meta_html = "".join(meta_parts)
        
    card = f"""<a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="{url}" target="_blank">
<div class="flex items-start gap-4">
<div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
<svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
</div>
<div class="flex flex-col gap-1.5">
<p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">{title}</p>
<div class="flex items-center text-[13px] text-slate-500">{meta_html}</div>
</div>
</div>
<div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
</a>"""
    return card

for out_name, (md_file, title, parent, desc) in mapping.items():
    md_path = os.path.join(md_dir, md_file)
    if not os.path.exists(md_path):
        continue
        
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.readlines()
        
    cards_html = []
    for line in md_content:
        match = re.search(r'-\s+\[(.*?)\]\((.*?)\)\s*(.*)', line)
        if match:
            doc_title = match.group(1)
            url = match.group(2)
            date_size = match.group(3)
            cards_html.append(generate_card(doc_title, url, date_size))
            
    page_html = base_html
    page_html = page_html.replace('href="financial-statements.html"', 'href="index.html"')
    page_html = re.sub(r'<title>.*?</title>', f'<title>{title} | Regulations | NRB</title>', page_html)
    
    breadcrumb = f"""<nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
<a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
<span class="text-slate-300">/</span>
<a class="transition hover:text-[#25295B]" href="index.html">Regulations</a>
<span class="text-slate-300">/</span>
<span class="text-slate-500">{parent}</span>
<span class="text-slate-300">/</span>
<span class="text-slate-700">{title}</span>
</nav>"""
    page_html = re.sub(r'<nav aria-label="Breadcrumb".*?</nav>', breadcrumb, page_html, flags=re.DOTALL)
    page_html = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 class="text-2xl font-bold text-slate-900 mb-4">{title}</h1>', page_html, count=1)
    page_html = re.sub(r'<p class="text-base text-slate-600 leading-relaxed max-w-2xl">.*?</p>', f'<p class="text-base text-slate-600 leading-relaxed max-w-2xl">{desc}</p>', page_html, count=1)
    
    # Choose and format correct nav
    if out_name in ["acts.html", "rules-and-bylaws.html"]:
        nav = laws_nav_strip
        nav = nav.replace("{act_active}", ' aria-current="page"' if out_name == "acts.html" else "")
        nav = nav.replace("{rule_active}", ' aria-current="page"' if out_name == "rules-and-bylaws.html" else "")
    else:
        nav = policies_nav_strip
        nav = nav.replace("{not_active}", ' aria-current="page"' if out_name == "notices.html" else "")
        nav = nav.replace("{gui_active}", ' aria-current="page"' if out_name == "guidelines-and-manuals.html" else "")
        nav = nav.replace("{oth_active}", ' aria-current="page"' if out_name == "other-policies.html" else "")
        nav = nav.replace("{mon_active}", ' aria-current="page"' if out_name == "monetary-policy.html" else "")
    
    page_html = re.sub(r'<!-- FINANCIAL STATEMENTS NAVIGATION STRIP -->.*?</div>\s*</div>', nav, page_html, flags=re.DOTALL)
    
    docs_joined = "\n".join(cards_html)
    page_html = re.sub(r'<div class="flex flex-col gap-3">.*?</div>\s*</div>\s*</section>', f'<div class="flex flex-col gap-3">\n{docs_joined}\n</div>\n</div>\n</section>', page_html, flags=re.DOTALL)
    page_html = page_html.replace('All Statements', f'All {title}')
    
    with open(os.path.join(out_dir, out_name), "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated {out_name} with {len(cards_html)} documents using new standard size formatting.")
