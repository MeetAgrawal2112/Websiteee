import re

files_to_fix = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

dropdown_css = """
        .main-nav li { position: relative; }
        .main-nav .dropdown-menu { display: none; position: absolute; top: 100%; left: 0; background: #ffffff; border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 12px 20px rgba(0,0,0,0.08); min-width: 190px; padding: 0.35rem 0; margin: 0; list-style: none; z-index: 1000; }
        .main-nav .dropdown-menu li { list-style: none; margin: 0; padding: 0; }
        .main-nav .has-dropdown:hover .dropdown-menu { display: block; }
        .main-nav .dropdown-menu li a { display: block; padding: 0.75rem 1rem; color: #111111; text-decoration: none; font-size: 0.95rem; border-bottom: none; }
        .main-nav .dropdown-menu li a:hover { background: #f8f9fa; color: #e85d04; }
"""

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert dropdown_css into <style> tag
    content = content.replace('<style>', '<style>\n' + dropdown_css, 1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed dropdown.")
