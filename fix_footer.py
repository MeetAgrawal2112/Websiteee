import re

files_to_fix = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

with open('/home/meetagrawal2112/IIITP/New/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract the footer from index.html
footer_match = re.search(r'(<!-- Footer -->\s*<div class="footer">.*?<!-- Footer Ends here /-->)', index_html, re.DOTALL)
if footer_match:
    footer_content = footer_match.group(1)
else:
    print("Could not find footer in index.html")
    exit(1)

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the footer tag
    content = re.sub(
        r'<footer class="footer">.*?</footer>',
        footer_content,
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed footer.")
