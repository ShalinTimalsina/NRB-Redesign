import re

cur = "http://localhost:3000/pages/media-speeches/index.html"

hrefs = [
    "../../pages/about/index.html",
    "../../pages/regulations/index.html",
    "../../pages/regulation-and-supervision/index.html",
    "../../pages/publications/index.html",
    "../../pages/statistics/index.html",
    "../../pages/procurement/index.html",
    "../../pages/careers/index.html",
    "../../pages/monetary-policy/index.html",
    "../../pages/media-speeches/index.html"
]

for href in hrefs:
    m = re.search(r'/pages/([^/]+)/', href)
    if m:
        folder = m.group(1)
        check = f"/pages/{folder}/"
        if check in cur:
            print(f"Matched: {href} (folder: {folder})")
