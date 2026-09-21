from bs4 import BeautifulSoup
import re

file_path = 'pages/about/principal-officers.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

tbodies = soup.find_all('tbody')

for tbody in tbodies:
    # Find all rows in this tbody
    rows = tbody.find_all('tr', recursive=False)
    
    if len(rows) > 15:
        print(f"Found table body with {len(rows)} rows. Truncating to 12.")
        # Keep the first 12
        for row in rows[12:]:
            row.decompose()
            
# Also update the counts in the headers
counts = soup.find_all('span', text=re.compile(r'\d+\s+Executive Directors|\d+\s+Directors|\d+\s+Acting Directors'))
for count_span in counts:
    text = count_span.string
    if text:
        new_text = re.sub(r'\d+', '12', text)
        count_span.string.replace_with(new_text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Done processing.")
