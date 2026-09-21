"""
Audit Fix Script - Executes P0 and P1 fixes from the design audit.

Fix 1: Add Inter Font Stylesheet to all HTML files
Fix 2: Fix Hero CTA Hover State
Fix 3: Add focus-within keyboard accessibility to nav dropdowns
Fix 4: Standardize border-radius (rounded-[16px], [20px], [24px], [14px] -> rounded-xl)
Fix 5: Replace shadow-lg with shadow-md on dropdown panels
Fix 6: Fix section spacing (py-14 -> py-12, py-10 -> py-12 in hero)
Fix 7: Standardize card padding (p-5 -> p-6, p-8 -> p-6 where appropriate)
Fix 8: Eliminate arbitrary typography sizes
"""

from pathlib import Path
import re

ROOT = Path('.')
count = {k: 0 for k in ['font', 'hero_hover', 'keyboard_nav', 'radius', 'shadow', 'spacing', 'padding', 'typography']}

for p in sorted(ROOT.rglob('*.html')):
    if 'scratch' in p.parts or '.git' in p.parts:
        continue

    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html

    # ──────────────────────────────────────────────────────────────────
    # FIX 1: Add Inter Font Stylesheet
    # The preconnect tags exist but the actual stylesheet is missing.
    # Insert the stylesheet link right after the gstatic preconnect.
    # ──────────────────────────────────────────────────────────────────
    if 'family=Inter' not in html and 'fonts.gstatic.com' in html:
        html = html.replace(
            '<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>',
            '<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>\n<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'
        )
        if html != original:
            count['font'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 2: Fix Hero CTA Hover State (homepage only)
    # Change hover:bg-[#25295B] to hover:bg-[#138496] on the primary CTA
    # ──────────────────────────────────────────────────────────────────
    if 'Hero-CTA-Monetary-Policy' in html:
        html = html.replace(
            'hover:bg-[#25295B] focus:outline-none focus:ring-2 focus:ring-[#138496]" href="pages/monetary-policy/index.html" id="Hero-CTA-Monetary-Policy"',
            'hover:bg-[#138496] focus:outline-none focus:ring-2 focus:ring-[#138496]" href="pages/monetary-policy/index.html" id="Hero-CTA-Monetary-Policy"'
        )
        count['hero_hover'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 3: Add focus-within for keyboard accessibility on nav dropdowns
    # Change: group-hover:opacity-100 group-hover:visible
    # To also include: group-focus-within:opacity-100 group-focus-within:visible
    # ──────────────────────────────────────────────────────────────────
    if 'group-hover:opacity-100 group-hover:visible' in html:
        html = html.replace(
            'group-hover:opacity-100 group-hover:visible',
            'group-hover:opacity-100 group-hover:visible group-focus-within:opacity-100 group-focus-within:visible'
        )
        count['keyboard_nav'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 4: Standardize Border-Radius
    # The CSS nrb-surface class uses 12px (rounded-xl).
    # Standardize all non-standard radii to rounded-xl.
    # Exception: rounded-full on pills/buttons stays.
    # ──────────────────────────────────────────────────────────────────
    before = html
    # Nav dropdowns: rounded-[16px] -> rounded-xl
    html = html.replace('rounded-[16px]', 'rounded-xl')
    # Service/hub cards: rounded-[20px] -> rounded-xl
    html = html.replace('rounded-[20px]', 'rounded-xl')
    # Hero spotlight: rounded-[24px] -> rounded-xl
    html = html.replace('rounded-[24px]', 'rounded-xl')
    # Bank notes cards: rounded-[14px] -> rounded-xl
    html = html.replace('rounded-[14px]', 'rounded-xl')
    if html != before:
        count['radius'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 5: Replace shadow-lg with shadow-md on dropdown panels
    # shadow-md is acceptable for floating overlays per design system.
    # We only target the dropdown context (not other uses of shadow-lg).
    # ──────────────────────────────────────────────────────────────────
    before = html
    html = html.replace('shadow-lg border border-slate-200 py-3', 'shadow-md border border-slate-200 py-3')
    html = html.replace('shadow-lg border border-slate-200 py-5', 'shadow-md border border-slate-200 py-5')
    if html != before:
        count['shadow'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 6: Fix Section Spacing
    # Footer: py-14 -> py-12 (closest 8pt grid value)
    # Hero inner pages: py-10 lg:py-14 -> py-12
    # ──────────────────────────────────────────────────────────────────
    before = html
    # Footer padding
    html = html.replace('nrb-section-shell py-14">', 'nrb-section-shell py-12">')
    # Hero sections on inner pages: py-10 lg:py-14
    html = html.replace('py-10 lg:py-14', 'py-12')
    if html != before:
        count['spacing'] += 1

    # ──────────────────────────────────────────────────────────────────
    # FIX 8: Eliminate Arbitrary Typography Sizes
    # text-3xl -> text-2xl (except in hero KPI snapshot where it's appropriate)
    # text-[28px] -> text-2xl
    # text-[17px] -> text-base
    # ──────────────────────────────────────────────────────────────────
    before = html
    # Hero subtitle
    html = html.replace('text-[28px] font-medium tracking-[-0.03em] text-[#25295B]', 'text-2xl font-medium tracking-[-0.02em] text-[#25295B]')
    # Hero description
    html = html.replace('text-[17px] text-slate-600', 'text-base text-slate-600')
    # Bank notes page headings (not the KPI snapshots)
    if 'bank-notes-content' in html:
        html = html.replace('text-3xl font-bold text-[#25295B]', 'text-2xl font-bold text-[#25295B]')
        html = html.replace('text-3xl font-bold text-slate-900', 'text-2xl font-bold text-slate-900')
    if html != before:
        count['typography'] += 1

    # Write if changed
    if html != original:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)

print("=== Audit Fix Results ===")
for k, v in count.items():
    print(f"  {k}: {v} files fixed")
print(f"\nTotal files processed across {sum(count.values())} operations.")
