import os
import urllib.request
from bs4 import BeautifulSoup

# Create the folder
output_dir = "NRB Page md files/Regulations and Supervisions"
os.makedirs(output_dir, exist_ok=True)

url = "https://www.nrb.org.np/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the Regulation dropdown menu
    reg_menu = None
    for a in soup.find_all('a', class_='dropdown-toggle'):
        if 'Regulation' in a.get_text() or 'Supervision' in a.get_text():
            reg_menu = a.find_next_sibling('div', class_='dropdown-menu')
            break
            
    if not reg_menu:
        print("Could not find the dropdown menu.")
        exit(1)

    # Find all department links. In the megamenu, departments are level-2 items.
    # Level-1 is 'Regulations' and 'Supervisions'.
    # Under Level-1, we have UL > LI > A for the departments.
    departments = []
    
    for lvl1_li in reg_menu.find('ul').find_all('li', recursive=False):
        lvl1_title = lvl1_li.find('span').get_text(strip=True) if lvl1_li.find('span') else "Unknown"
        lvl2_ul = lvl1_li.find('ul')
        if lvl2_ul:
            for lvl2_li in lvl2_ul.find_all('li', recursive=False):
                a_tag = lvl2_li.find('a', recursive=False)
                if a_tag and a_tag.has_attr('href'):
                    dep_name = a_tag.get_text(strip=True)
                    dep_url = a_tag['href']
                    # Some URLs might be relative, but WP usually uses absolute
                    departments.append({
                        'category': lvl1_title,
                        'name': dep_name,
                        'url': dep_url
                    })

    # Scrape each department page
    for dep in departments:
        print(f"Scraping: {dep['name']} -> {dep['url']}")
        try:
            dep_req = urllib.request.Request(dep['url'], headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(dep_req) as dep_res:
                dep_html = dep_res.read().decode('utf-8')
                
            dep_soup = BeautifulSoup(dep_html, 'html.parser')
            main_content = dep_soup.find('main')
            if not main_content:
                main_content = dep_soup.find(id='primary') or dep_soup.find(class_='site-main') or dep_soup.find('body')
                
            # Clean up
            for script in main_content(["script", "style", "nav", "header", "footer", "aside"]):
                script.extract()
                
            text = main_content.get_text(separator='\n\n', strip=True)
            
            # Format markdown
            safe_name = dep['name'].replace('&', 'and').replace('/', '-').replace(' ', '_')
            filename = os.path.join(output_dir, f"{safe_name}.md")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# {dep['name']}\n\n")
                f.write(f"**Category:** {dep['category']}\n")
                f.write(f"**Verified Source:** {dep['url']}\n\n")
                f.write("---\n\n")
                f.write(text)
                
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Failed to scrape {dep['url']}: {e}")

except Exception as e:
    print(f"Error: {e}")
