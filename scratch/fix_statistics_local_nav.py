import os

files_to_update = [
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/macroeconomic/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/financial-sector/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/monetary-forex/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/statistics/financial-inclusion/index.html',
    'c:/Users/LOQ/Desktop/NRB Redesign/pages/forex-management/index.html'
]

replacements = {
    '>Financial Sector Statistics<': '>Bank and Financial Sector Statistics<',
    '>Monetary & Forex Statistics<': '>Interest Rates and Monetary Operations<',
    '>Monetary &amp; Forex Statistics<': '>Interest Rates and Monetary Operations<',
    '>Financial Inclusion & Payments<': '>Financial Inclusion<',
    '>Financial Inclusion &amp; Payments<': '>Financial Inclusion<',
    # Handle titles
    '<title>Financial Sector Statistics': '<title>Bank and Financial Sector Statistics',
    '<title>Monetary & Forex Statistics': '<title>Interest Rates and Monetary Operations',
    '<title>Monetary &amp; Forex Statistics': '<title>Interest Rates and Monetary Operations',
    '<title>Financial Inclusion & Payments': '<title>Financial Inclusion',
    '<title>Financial Inclusion &amp; Payments': '<title>Financial Inclusion'
}

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply replacements but only AFTER the header to avoid touching the global nav which is already correct.
        # But wait, we DO want to change the local nav and main content.
        # Let's split by </header>
        if '</header>' in content:
            header, body = content.split('</header>', 1)
            for old_text, new_text in replacements.items():
                body = body.replace(old_text, new_text)
            
            # Also apply title replacements to header
            for old_text, new_text in replacements.items():
                if '<title>' in old_text:
                    header = header.replace(old_text, new_text)
                    
            content = header + '</header>' + body
        else:
            for old_text, new_text in replacements.items():
                content = content.replace(old_text, new_text)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"File not found: {filepath}")
