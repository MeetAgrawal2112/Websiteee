import os
import glob
import re

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Remove Admissions menu item. We'll find it by looking for "Admissions</a>" and removing the enclosing <li>
    # Since it might be multiline, we'll use a regex that matches <li> to </li> containing "Admissions"
    content = re.sub(r'<li[^>]*>\s*<a[^>]*>(?:\s*<i[^>]*></i>)?\s*Admissions\s*</a>\s*</li>', '', content, flags=re.IGNORECASE)
    
    # Also handle the specific case from index.html where it's split across lines
    content = re.sub(r'<li>\s*<a href="#">\s*<i class="fas fa-certificate"\s*style="color:#d9534f; font-size: 12px; margin-right: 4px;"></i>Admissions</a>\s*</li>', '', content, flags=re.DOTALL)

    # General regex for Admissions li just in case
    content = re.sub(r'<li><a href="#">(?:<i class="fas fa-certificate"[^>]*></i>)?Admissions</a></li>', '', content)

    # Remove down arrows: <i class="fas fa-chevron-down" ...></i>
    content = re.sub(r'<i class="fas fa-chevron-down"[^>]*></i>', '', content)
    
    # Remove red danger marks: <i class="fas fa-certificate" ...></i>
    content = re.sub(r'<i class="fas fa-certificate"[^>]*></i>', '', content)
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {file}")

print(f"Updated {count} files.")
