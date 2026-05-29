import os
import glob
import re

NEW_NAV = """<li class="has-dropdown"><a href="#">Academics</a>
\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t<li><a href="page_btech-cse-new.html">B.Tech CSE</a></li>
\t\t\t\t\t\t\t<li><a href="page_electronics-and-communication-engineering.html">B.Tech ECE</a></li>
\t\t\t\t\t\t\t<li><a href="page_btech-honors.html">B.Tech Honors</a></li>
\t\t\t\t\t\t\t<li><a href="page_mtechcse.html">M.Tech CSE</a></li>
\t\t\t\t\t\t\t<li><a href="page_mtech-ece.html">M.Tech ECE</a></li>
\t\t\t\t\t\t\t<li><a href="page_phd.html">Ph.D.</a></li>
\t\t\t\t\t\t\t<li><a href="page_visiting-faculty.html">Visiting Faculty</a></li>
\t\t\t\t\t\t\t<li><a href="page_admissionfee.html">Admission/Fee</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="has-dropdown"><a href="#">Research</a>
\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t<li><a href="page_research-consultancy4.html">Research & Consultancy</a></li>
\t\t\t\t\t\t\t<li><a href="page_horizon.html">Horizon</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>
\t\t\t\t\t<li class="has-dropdown"><a href="#">Student Life</a>
\t\t\t\t\t\t<ul class="dropdown-menu">
\t\t\t\t\t\t\t<li><a href="page_sports.html">Sports</a></li>
\t\t\t\t\t\t\t<li><a href="page_student.html">Student Clubs</a></li>
\t\t\t\t\t\t\t<li><a href="page_rofies.html">Rofies</a></li>
\t\t\t\t\t\t\t<li><a href="page_vanity-crew.html">Vanity Crew</a></li>
\t\t\t\t\t\t\t<li><a href="page_electic.html">Electic</a></li>
\t\t\t\t\t\t\t<li><a href="page_c-cube.html">C-Cube</a></li>
\t\t\t\t\t\t\t<li><a href="page_bit-legion.html">Bit Legion</a></li>
\t\t\t\t\t\t\t<li><a href="page_abhinay.html">Abhinay</a></li>
\t\t\t\t\t\t\t<li><a href="page_q-riocity.html">Q-Riocity</a></li>
\t\t\t\t\t\t</ul>
\t\t\t\t\t</li>"""

def main():
    files = glob.glob('*.html')
    updated = 0
    pattern = re.compile(r'<li>\s*<a href="#">Academics</a>\s*</li>\s*<li>\s*<a href="#">Research</a>\s*</li>\s*<li>\s*<a href="#">Student Life</a>\s*</li>', re.MULTILINE)
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if pattern.search(content):
            content = pattern.sub(NEW_NAV, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
            print(f"Updated {file}")
            
    print(f"Total updated files: {updated}")

if __name__ == '__main__':
    main()
