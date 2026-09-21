import os

count = 0
for root, dirs, files in os.walk('c:/Users/LOQ/Desktop/NRB Redesign/pages/media-speeches'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig = content
            # Replace the generic OFG page link with the real PDF link of the Governor's speech to simulate a real document opening
            content = content.replace(
                'href="https://www.nrb.org.np/ofg/"',
                'href="https://www.nrb.org.np/contents/uploads/2026/04/71th-Anniversary-Govorners-Speech-1.pdf"'
            )
            
            if content != orig:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Updated links to actual PDF documents in {count} files.")
