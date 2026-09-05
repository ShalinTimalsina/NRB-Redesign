import subprocess
import os

files = [
    'pages/about/board-of-directors.html',
    'pages/about/departments.html',
    'pages/about/financial-statements.html',
    'pages/about/governors-history.html',
    'pages/about/index.html',
    'pages/about/information-officers.html',
    'pages/about/organogram.html',
    'pages/about/principal-officers.html',
    'pages/about/provincial-offices.html',
]

for f in files:
    try:
        res = subprocess.run(['git', 'diff', '--stat', f], capture_output=True, text=True)
        print(f"=== {f} ===")
        print(res.stdout.strip())
    except Exception as e:
        print(f"Error checking {f}: {e}")
