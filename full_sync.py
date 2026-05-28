import re

files_to_sync = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

with open('/home/meetagrawal2112/IIITP/New/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Customizer CSS
customizer_match = re.search(r'(<!--Customizer CSS-->.*?<!--/Customizer CSS-->)', index_html, re.DOTALL)
if customizer_match:
    customizer_css = customizer_match.group(1)
else:
    print("Could not find Customizer CSS in index.html")
    exit(1)

for file_path in files_to_sync:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the partial typography CSS block I added earlier
    content = re.sub(
        r'<style type="text/css">\s*h1, h2, h3, h4, h5, h6.*?font-family: \'Montserrat\', sans-serif;\s*}\s*</style>',
        '',
        content,
        flags=re.DOTALL
    )

    # Insert the full customizer CSS before the existing <style> tag
    content = content.replace('<style>', customizer_css + '\n    <style>', 1)
    
    # Let's ensure background color is consistent. In index.html, is there any global background color?
    # theme-styles.css sets body background to default (white).
    # But faculty.html inline style has: `body { background-color: #ffffff; }` which is identical.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Synchronized full Customizer CSS.")
