import re

with open('/home/meetagrawal2112/IIITP/New/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('/home/meetagrawal2112/IIITP/New/faculty.html', 'r', encoding='utf-8') as f:
    faculty_html = f.read()

# Extract header and nav from index.html
# It starts at <header class="custom-iiitp-header"> and ends at <!-- Custom IIITP Header Ends -->
header_match = re.search(r'(<header class="custom-iiitp-header">.*?)<!-- Custom IIITP Header Ends -->', index_html, re.DOTALL)
if header_match:
    header_nav_content = header_match.group(1).strip()
else:
    # Fallback: extract <header class="custom-iiitp-header"> to the end of <div class="nav-section">
    match1 = re.search(r'(<header class="custom-iiitp-header">.*?</header>)', index_html, re.DOTALL)
    match2 = re.search(r'(<div class="nav-section".*?</ul>\s*</div>\s*</div>)', index_html, re.DOTALL)
    header_nav_content = match1.group(1) + '\n' + match2.group(1)

# Find the header and nav in faculty.html
# Starts with <header class="custom-iiitp-header"> and ends with </div> of nav-section
faculty_html = re.sub(
    r'<header class="custom-iiitp-header">.*?</header>\s*<div class="nav-section">.*?</ul>\s*</div>\s*</div>',
    header_nav_content,
    faculty_html,
    flags=re.DOTALL
)

# Update CSS in faculty.html
css_updates = """
        .filter-section a:hover, .filter-section a.active {
            text-decoration: underline;
            cursor: pointer;
            color: #e85d04;
        }
        select {
            margin: 0 10px;
            padding: 10px;
            font-size: 15px;
            border: 1px solid #174873;
            border-radius: 4px;
        }
        .card-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
            padding: 40px 20px;
        }
        .card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            overflow: hidden;
            text-align: center;
            width: 280px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(232, 93, 4, 0.15);
            border-color: #e85d04;
        }
        .card img {
            width: 100%;
            height: 320px;
            object-fit: cover;
            object-position: top;
            transition: transform 0.5s ease;
            border-bottom: 3px solid #174873;
        }
        .card:hover img {
            transform: scale(1.03);
            border-bottom: 3px solid #e85d04;
        }
        .card h3 {
            margin: 15px 15px 5px;
            font-size: 1.15rem;
            color: #174873;
        }
        .card h3 a {
            color: #174873;
            text-decoration: none;
        }
        .card h3 a:hover {
            color: #e85d04;
        }
        .card p {
            margin: 0 15px 15px;
            font-size: 0.9rem;
            color: #555;
            line-height: 1.5;
        }
        .card p strong {
            color: #333;
        }
"""

# Replace the specific CSS block in faculty.html
faculty_html = re.sub(
    r'\.filter-section a:hover.*?\.card p \{.*?\}',
    css_updates.strip(),
    faculty_html,
    flags=re.DOTALL
)

with open('/home/meetagrawal2112/IIITP/New/faculty.html', 'w', encoding='utf-8') as f:
    f.write(faculty_html)

