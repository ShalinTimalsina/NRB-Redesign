import requests
from bs4 import BeautifulSoup
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# The NRB site uses WordPress with AJAX listings. The actual content is loaded via
# JavaScript/DataTables. Let's try the WP REST API to get the actual posts.

# Try WP REST API for media-releases category
print("=== Trying WP REST API for Media Releases ===\n")
api_urls = [
    'https://www.nrb.org.np/wp-json/wp/v2/posts?categories=media-releases&per_page=20',
    'https://www.nrb.org.np/wp-json/wp/v2/posts?filter[category_name]=media-releases&per_page=20',
    'https://www.nrb.org.np/wp-json/nrb/v1/media-releases',
]

for api_url in api_urls:
    try:
        r = requests.get(api_url, headers=headers, timeout=15)
        print(f"  {api_url[:80]}...")
        print(f"  Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list) and len(data) > 0:
                print(f"  Found {len(data)} items!")
                for item in data[:5]:
                    title = item.get('title', {})
                    if isinstance(title, dict):
                        title = title.get('rendered', '')
                    print(f"    - {title}")
            elif isinstance(data, dict):
                print(f"  Keys: {list(data.keys())[:10]}")
        print()
    except Exception as e:
        print(f"  Error: {e}\n")

# Also try the OFG page raw HTML to find the AJAX data source
print("\n=== Parsing OFG page for DataTable/AJAX sources ===\n")
url = 'https://www.nrb.org.np/departments/ofg/'
resp = requests.get(url, headers=headers, timeout=30)

# Look for AJAX URLs or data-source attributes
ajax_urls = re.findall(r'(?:ajax_url|ajaxurl|data-src|loadUrl|sourceUrl|api_url)\s*[=:]\s*["\']([^"\']+)', resp.text)
print(f"Found {len(ajax_urls)} AJAX URLs:")
for u in ajax_urls:
    print(f"  {u}")

# Look for the nrb_ajax_object or similar
nrb_ajax = re.findall(r'nrb_ajax\w*\s*=\s*(\{[^}]+\})', resp.text)
print(f"\nFound {len(nrb_ajax)} NRB AJAX objects:")
for obj in nrb_ajax:
    print(f"  {obj[:200]}")

# Look for WP admin-ajax URLs
admin_ajax = re.findall(r'(https?://[^"\']+admin-ajax[^"\']*)', resp.text)
print(f"\nFound {len(admin_ajax)} admin-ajax URLs:")
for u in admin_ajax:
    print(f"  {u}")

# Look for DataTable configuration
dt_config = re.findall(r'DataTable\s*\(\s*(\{[^}]+)', resp.text)
print(f"\nFound {len(dt_config)} DataTable configs:")
for c in dt_config:
    print(f"  {c[:200]}")

# Look for category IDs
cat_ids = re.findall(r'"category_id"\s*:\s*"?(\d+)"?', resp.text)
print(f"\nCategory IDs found: {cat_ids}")

# Try the /nrb/ custom endpoint
print("\n\n=== Trying NRB custom endpoints ===\n")
custom_urls = [
    'https://www.nrb.org.np/wp-json/nrb/v1/posts?department=ofg&category=media-releases&per_page=20',
    'https://www.nrb.org.np/wp-json/nrb/v1/department/ofg',
    'https://www.nrb.org.np/wp-json/wp/v2/categories?search=media',
    'https://www.nrb.org.np/wp-json/wp/v2/categories?search=speech',
]

for api_url in custom_urls:
    try:
        r = requests.get(api_url, headers=headers, timeout=15)
        print(f"  {api_url}")
        print(f"  Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            if isinstance(data, list):
                print(f"  Found {len(data)} items")
                for item in data[:5]:
                    if isinstance(item, dict):
                        name = item.get('name', item.get('title', ''))
                        if isinstance(name, dict):
                            name = name.get('rendered', '')
                        cat_id = item.get('id', '')
                        print(f"    id={cat_id}, name={name}")
            elif isinstance(data, dict):
                print(f"  Keys: {list(data.keys())[:10]}")
        print()
    except Exception as e:
        print(f"  Error: {e}\n")
