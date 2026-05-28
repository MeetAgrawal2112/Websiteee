import re

files_to_sync = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

typography_css = """
    <style type="text/css">
        h1, h2, h3, h4, h5, h6,
        h2 a, h3 a, h4 a, h5 a, h6 a,
        h1 span, h2 span, h3 span, h4 span, h5 span {
            font-family: 'Montserrat', sans-serif;
        }
    </style>
"""

for file_path in files_to_sync:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove inline body stylings
    content = re.sub(
        r'body\s*\{[^}]*font-family:[^}]*\}',
        '',
        content,
        flags=re.IGNORECASE | re.MULTILINE
    )

    # Insert the typography CSS before the existing <style> tag
    if 'font-family: \'Montserrat\'' not in content:
        content = content.replace('<style>', typography_css + '\n    <style>', 1)
    
    # Also adjust card h3 to inherit the correct font family (it currently doesn't specify, so it inherits, which is good)
    # But let's check if card h3 has a specific font? It only has font-size and color.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Synchronized fonts.")
