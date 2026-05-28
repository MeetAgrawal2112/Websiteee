import re

files_to_fix = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

css_links = """
    <link href="//fonts.googleapis.com" rel="dns-prefetch">
    <link href="css/css.css" id="google-fonts-css" media="all" rel="stylesheet" />
    <link href="css/theme-styles.css" id="wc-styles-css" media="all" rel="stylesheet" />
"""

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert the CSS links before the <style> tag
    content = re.sub(r'(<style>)', css_links + r'\n    \1', content, count=1)
    
    # Remove the inline styles that conflict with theme-styles.css
    # We will remove everything from .custom-iiitp-header to #top:hover
    content = re.sub(
        r'\.custom-iiitp-header \{.*?#top:hover \{ background:#121f4d; \}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove another inline style block that was accidentally added inside nav-section
    content = re.sub(
        r'<style>\s*\.main-nav li \{ position: relative; \}.*?</style>',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed headers.")
