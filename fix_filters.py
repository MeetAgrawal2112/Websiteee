import re

premium_filter_css = """
        /* Premium Filter Styling */
        .filter-section {
            padding: 30px 20px;
            background-color: #ffffff;
            margin-bottom: 40px;
        }
        .alphabet-filter-container, #alphabet-filter {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin: 0 auto 25px auto;
            padding: 0;
            list-style: none;
            max-width: 1100px;
        }
        #alphabet-filter li {
            margin: 0;
        }
        .alphabet-filter-container a, #alphabet-filter a {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 20px;
            background-color: #f4f6fb;
            border: 1px solid #eaeaea;
            color: #174873;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        .alphabet-filter-container a:hover, .alphabet-filter-container a.active, #alphabet-filter a:hover, #alphabet-filter a.active {
            background-color: #e85d04;
            color: #ffffff;
            border-color: #e85d04;
            box-shadow: 0 4px 10px rgba(232, 93, 4, 0.2);
        }
        .filters {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
        }
        .filters select {
            padding: 10px 15px;
            font-size: 0.95rem;
            color: #333;
            border: 1px solid #d0d0d0;
            border-radius: 6px;
            background-color: #ffffff;
            cursor: pointer;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
            min-width: 180px;
            font-family: inherit;
        }
        .filters select:hover, .filters select:focus {
            border-color: #e85d04;
            outline: none;
            box-shadow: 0 4px 10px rgba(232, 93, 4, 0.1);
        }
"""

def update_faculty():
    with open('/home/meetagrawal2112/IIITP/New/faculty.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace CSS
    css_pattern = r'\.filter-section \{.*?\border-radius: 4px;\s*\}'
    content = re.sub(css_pattern, premium_filter_css, content, flags=re.DOTALL)

    # Replace HTML
    content = content.replace('<div><a class="active"', '<div class="alphabet-filter-container"><a class="active"')
    
    # Just in case `select` inline style still matched another way, let's just make sure.
    
    with open('/home/meetagrawal2112/IIITP/New/faculty.html', 'w', encoding='utf-8') as f:
        f.write(content)

def update_staff():
    with open('/home/meetagrawal2112/IIITP/New/non-teaching-staff.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace CSS
    css_pattern = r'\.filters \{.*?\border-color: #e85d04;\s*\}'
    content = re.sub(css_pattern, premium_filter_css, content, flags=re.DOTALL)

    # Replace HTML: Remove the non-breaking spaces around ALL
    content = content.replace('<a data-letter="ALL">                            ALL</a>', '<a data-letter="ALL" class="active">ALL</a>')
    
    with open('/home/meetagrawal2112/IIITP/New/non-teaching-staff.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_faculty()
update_staff()
print("Updated filters!")
