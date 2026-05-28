import re

with open('/home/meetagrawal2112/IIITP/New/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('/home/meetagrawal2112/IIITP/New/non-teaching-staff.html', 'r', encoding='utf-8') as f:
    staff_html = f.read()

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

# Find the header and nav in non-teaching-staff.html
staff_html = re.sub(
    r'<header class="custom-iiitp-header">.*?</header>\s*<div class="nav-section">.*?</ul>\s*</div>\s*</div>',
    header_nav_content,
    staff_html,
    flags=re.DOTALL
)

# Update CSS in non-teaching-staff.html
css_updates = """
        nav ul li a {
            text-decoration: none;
            font-weight: bold;
            color: #174873;
            cursor: pointer;
            transition: color 0.3s ease;
        }
        nav ul li a:hover, nav ul li a.active {
            color: #e85d04;
        }
        .filters {
            text-align: center;
            margin-bottom: 20px;
        }
        .filters select {
            padding: 10px;
            margin: 0 10px;
            border: 1px solid #174873;
            border-radius: 4px;
            background-color: #ffffff;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }
        .filters select:hover {
            border-color: #e85d04;
        }
        .staff-list {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            padding: 20px;
            justify-content: center;
        }
        .staff {
            background-color: white;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            text-align: center;
            width: 250px;
            padding: 15px;
            overflow: hidden;
            position: relative;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        }
        .staff:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(232, 93, 4, 0.15);
            border-color: #e85d04;
        }
        .staff img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            object-position: top;
            transition: transform 0.5s ease;
            border-bottom: 3px solid #174873;
        }
        .staff:hover img {
            transform: scale(1.03);
            border-bottom: 3px solid #e85d04;
        }
        .staff h2 {
            font-size: 1.15rem;
            margin: 15px 0 5px 0;
            cursor: pointer;
            color: #174873;
        }
        .staff h2:hover {
            color: #e85d04;
        }
        .staff p {
            color: #555;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        .staff p strong {
            color: #333;
        }
        .staff-details {
            display: none;
            padding-top: 10px;
            font-size: 0.85rem;
            color: #444;
            text-align: justify;
        }
        .staff.active .staff-details {
            display: block;
        }
        .staff.active {
            transform: scale(1.05);
            z-index: 2;
            border: 2px solid #e85d04;
            box-shadow: 0 10px 25px rgba(232, 93, 4, 0.2);
        }
        .staff.dimmed {
            opacity: 0.5;
        }
        .contact-container a {
            color: #174873;
            text-decoration: none;
            margin: 0 5px;
        }
        .contact-container a:hover {
            color: #e85d04;
        }
"""

staff_html = re.sub(
    r'nav ul li a \{.*?\.contact-container a:hover \{.*?\}',
    css_updates.strip(),
    staff_html,
    flags=re.DOTALL
)

with open('/home/meetagrawal2112/IIITP/New/non-teaching-staff.html', 'w', encoding='utf-8') as f:
    f.write(staff_html)

