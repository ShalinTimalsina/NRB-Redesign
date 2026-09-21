import os

base_dir = 'c:/Users/LOQ/Desktop/NRB Redesign'

for root, _, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html') and 'scratch' not in root and 'components' not in root:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            count = content.count('id="Site-Header"')
            if count > 1:
                print(f"{filepath} has {count} headers")
