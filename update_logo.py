import glob
import re

html_files = glob.glob('*.html')
count = 0

new_logo_html = """<div class="logo-text-wrapper" style="flex-direction: row; align-items: center; justify-content: flex-start; width: 100%;">
						<div class="logo-container">
							<a href="index.html"><img src="images/header_logo.png" alt="IIIT Pune Logo" class="main-logo" style="max-height: 100px; width: auto; object-fit: contain;" /></a>
						</div>
					</div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block we want to replace
    pattern = r'<div class="logo-text-wrapper">.*?</div>\s*</div>\s*<div class="constitution-logo-container">'
    
    # Actually let's just replace the logo-text-wrapper completely
    pattern = r'<div class="logo-text-wrapper">.*?</div>\s*</div>'
    
    # Wait, the structure is:
    # <div class="logo-text-wrapper">
    #     <div class="logo-container">...</div>
    #     <div class="text-container">...</div>
    # </div>
    
    pattern2 = r'<div class="logo-text-wrapper">.*?<div class="text-container">.*?</div>\s*</div>'
    
    if re.search(pattern2, content, re.DOTALL):
        new_content = re.sub(pattern2, new_logo_html, content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Updated {count} files.")
