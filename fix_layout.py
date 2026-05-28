import re

files = [
    '/home/meetagrawal2112/IIITP/New/faculty.html',
    '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # remove main-container max-width
    content = content.replace('.main-container { max-width:1400px; margin:0 auto; }', '')

    # add it to page-content
    content = content.replace('.page-content { padding:0 22px 34px; }', '.page-content { padding:0 22px 34px; max-width: 1400px; margin: 0 auto; }')

    # Fix the active class in the navbar
    if 'faculty.html' in file:
        content = content.replace('<li><a href="#" class="active">Home</a></li>', '<li><a href="index.html">Home</a></li>')
        content = content.replace('<li><a href="faculty.html">Faculty</a></li>', '<li><a href="faculty.html" class="active">Faculty</a></li>')
        # fix logo link
        content = content.replace('<a href="#"><img src="images/logo%20copy.png"', '<a href="index.html"><img src="images/logo%20copy.png"')
    
    if 'non-teaching-staff.html' in file:
        content = content.replace('<li><a href="#" class="active">Home</a></li>', '<li><a href="index.html">Home</a></li>')
        content = content.replace('<li><a href="non-teaching-staff.html">Non Teaching Staff</a></li>', '<li><a href="non-teaching-staff.html" class="active">Non Teaching Staff</a></li>')
        content = content.replace('<a href="#"><img src="images/logo%20copy.png"', '<a href="index.html"><img src="images/logo%20copy.png"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed layout")
