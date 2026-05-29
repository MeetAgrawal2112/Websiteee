import os
import json
import re

def build_index():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    index = []
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).split('|')[0].strip() if title_match else file
        
        # remove scripts and styles
        content = re.sub(r'<script.*?>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<style.*?>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
        
        # remove nav, header, footer to avoid common terms matching every page
        content = re.sub(r'<div class="nav-section".*?</div>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<header.*?>.*?</header>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<div class="footer".*?</div>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
        
        # extract text
        text = re.sub(r'<[^>]+>', ' ', content)
        # clean up whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        index.append({
            'url': file,
            'title': title,
            'content': text
        })
        
    js_content = "window.siteSearchIndex = " + json.dumps(index) + ";"
    with open('js/search_index_data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

if __name__ == '__main__':
    build_index()
