import os
from bs4 import BeautifulSoup

def fix_breadcrumbs():
    target_files = [
        r'pages\notices\index.html',
        r'pages\media-releases\index.html',
        r'pages\contact\index.html',
        r'pages\consumer-services\index.html',
        r'pages\bank-supervision\index.html'
    ]

    for rel_path in target_files:
        if not os.path.exists(rel_path):
            print(f"File not found: {rel_path}")
            continue
            
        with open(rel_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        nav = soup.find('nav', class_='nrb-breadcrumb')
        if not nav:
            print(f"Breadcrumb not found in {rel_path}")
            continue

        # Get the page title
        h1 = soup.find('h1')
        title = h1.get_text(strip=True) if h1 else 'Page'

        # Create new standard breadcrumb
        new_nav = soup.new_tag('nav', attrs={
            'aria-label': 'Breadcrumb',
            'class': 'mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500'
        })
        
        # Link to home
        a_home = soup.new_tag('a', href='../../nrb.html', attrs={'class': 'transition hover:text-[#25295B]'})
        a_home.string = "Home"
        new_nav.append(a_home)

        # Separator
        span_sep = soup.new_tag('span', attrs={'class': 'text-slate-300'})
        span_sep.string = "/"
        new_nav.append(span_sep)

        # Current page
        span_current = soup.new_tag('span', attrs={'class': 'text-slate-700'})
        span_current.string = title
        new_nav.append(span_current)

        # Replace the old nav with the new one
        nav.replace_with(new_nav)

        with open(rel_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Fixed breadcrumb in {rel_path} -> Home / {title}")

if __name__ == '__main__':
    fix_breadcrumbs()
