import re

faculty_file = '/home/meetagrawal2112/IIITP/New/faculty.html'
with open(faculty_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'\.card h3\s*\{\s*margin: 15px 15px 5px;\s*font-size: 1\.15rem;\s*color: #174873;\s*\}',
    '.card h3 {\n            margin: 15px 15px 5px;\n            font-size: 1.05rem;\n            font-weight: 600;\n            color: #174873;\n        }\n        .card h3 a, .card h3 strong {\n            font-weight: 600;\n        }',
    content
)
with open(faculty_file, 'w', encoding='utf-8') as f:
    f.write(content)


staff_file = '/home/meetagrawal2112/IIITP/New/non-teaching-staff.html'
with open(staff_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'\.staff h2\s*\{\s*font-size: 1\.15rem;\s*margin: 15px 0 5px 0;\s*cursor: pointer;\s*color: #174873;\s*\}',
    '.staff h2 {\n            font-size: 1.05rem;\n            font-weight: 600;\n            margin: 15px 0 5px 0;\n            cursor: pointer;\n            color: #174873;\n        }\n        .staff h2 a, .staff h2 strong {\n            font-weight: 600;\n        }',
    content
)
with open(staff_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fonts reduced.")
