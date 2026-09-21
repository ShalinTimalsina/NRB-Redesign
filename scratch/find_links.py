import urllib.request
import re

url = "https://www.nrb.org.np/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
        links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)
        for link in links:
            if 'regulation' in link[0].lower() or 'supervision' in link[0].lower() or 'regulation' in link[1].lower():
                print(f"Found: {link[1].strip()} -> {link[0]}")
except Exception as e:
    print(f"Error: {e}")
