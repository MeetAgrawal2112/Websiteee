import os
import glob
import re

html_files = glob.glob('*.html')
count = 0

toggle_html = """<header class="custom-iiitp-header">
			<div class="mobile-menu-toggle" onclick="document.body.classList.toggle('mobile-menu-active')" style="display:none;">
				<i class="fas fa-bars"></i>
			</div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'mobile-menu-toggle' not in content:
        # replace the opening header tag
        new_content = re.sub(r'<header class="custom-iiitp-header">', toggle_html, content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {file}")

print(f"Updated {count} files.")
