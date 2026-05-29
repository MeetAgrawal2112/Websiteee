import os
import glob
import re

admin_dropdown = """<li class="has-dropdown"><a href="#">Administration <i class="fas fa-chevron-down" style="font-size:0.75rem;margin-left:6px;"></i></a>
\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t<li><a href="admin_chairperson.html">Chairperson</a></li>
\t\t\t\t\t\t\t<li><a href="admin_director.html">Director</a></li>
\t\t\t\t\t\t\t<li><a href="admin_registrar.html">Registrar</a></li>
\t\t\t\t\t\t\t<li><a href="admin_board-of-governors.html">Board of Governors</a></li>
\t\t\t\t\t\t\t<li><a href="admin_finance-committee.html">Finance Committee</a></li>
\t\t\t\t\t\t\t<li><a href="admin_building-and-works-committee.html">Building and Works Committee</a></li>
\t\t\t\t\t\t\t<li><a href="admin_senate.html">Senate</a></li>
\t\t\t\t\t\t\t<li><a href="admin_board-of-studies-cse.html">Board of Studies (CSE)</a></li>
\t\t\t\t\t\t\t<li><a href="admin_board-of-studies-ece.html">Board of Studies (ECE)</a></li>
\t\t\t\t\t\t\t<li><a href="admin_board-of-studies-ash.html">Board of Studies (AS&H)</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="has-dropdown"><a href="#">People"""

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'Administration <i' not in content:
        # replace the People dropdown start with Administration + People
        # Need to match strictly to avoid messing up other things
        # <li class="has-dropdown"><a href="#">People
        
        # It might have varying whitespace, so use re
        pattern = r'<li class="has-dropdown">\s*<a[^>]*>People'
        if re.search(pattern, content):
            new_content = re.sub(pattern, admin_dropdown, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {file}")

print(f"Updated {count} files.")
