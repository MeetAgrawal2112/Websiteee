import re

files_to_fix = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

foundation_link = '    <link href="css/foundation.min.css" id="foundation-css" media="all" rel="stylesheet" />\n'

for file_path in files_to_fix:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert foundation link just before theme-styles.css link
    content = content.replace('<link href="css/theme-styles.css"', foundation_link + '    <link href="css/theme-styles.css"', 1)

    # Note: adding foundation.min.css might override some body or p margin, 
    # but that's what makes the pages uniform anyway.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added foundation.")
