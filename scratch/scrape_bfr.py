import urllib.request
from bs4 import BeautifulSoup

url = "https://www.nrb.org.np/departments/bfr/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract the main content area (usually <main> or a specific div on WP sites)
    main_content = soup.find('main')
    if not main_content:
        # Fallback to standard WP container
        main_content = soup.find(id='primary') or soup.find(class_='site-main') or soup.find('body')
    
    # Remove script and style elements
    for script in main_content(["script", "style", "nav", "header", "footer"]):
        script.extract()
        
    text = main_content.get_text(separator='\n\n', strip=True)
    
    with open('scratch/bfr_scraped.md', 'w', encoding='utf-8') as f:
        f.write("# Regulation and Supervision (BFR Department)\n\n")
        f.write(text)
        
    print("Scraped successfully to scratch/bfr_scraped.md")
    
except Exception as e:
    print(f"Error: {e}")
