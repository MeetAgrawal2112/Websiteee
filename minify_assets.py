#!/usr/bin/env python3
"""
Minify JavaScript files
Run this script to create minified versions of JavaScript files
"""

import os
import re
from pathlib import Path

def minify_js(js_content):
    """Basic JavaScript minification"""
    
    # Remove comments
    js_content = re.sub(r'//.*?$', '', js_content, flags=re.MULTILINE)  # Single line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)   # Multi-line comments
    
    # Remove whitespace
    js_content = re.sub(r'\s+', ' ', js_content)  # Multiple spaces to single
    js_content = re.sub(r'\s*([{};:,])\s*', r'\1', js_content)  # Remove spaces around brackets
    
    # Trim
    js_content = js_content.strip()
    
    return js_content

def minify_css(css_content):
    """Basic CSS minification"""
    
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    
    # Trim
    css_content = css_content.strip()
    
    return css_content

def main():
    """Main entry point"""
    
    js_file = 'js/optimizations.js'
    css_file = 'css/optimizations.css'
    
    # Minify JS
    if os.path.exists(js_file):
        print(f"Minifying {js_file}...", end=' ')
        with open(js_file, 'r') as f:
            js_content = f.read()
        
        minified = minify_js(js_content)
        
        with open('js/optimizations.min.js', 'w') as f:
            f.write(minified)
        
        original_size = len(js_content)
        minified_size = len(minified)
        reduction = round(100 * (1 - minified_size / original_size), 1)
        
        print(f"✅ Done ({original_size} → {minified_size} bytes, {reduction}% reduction)")
    
    # Minify CSS
    if os.path.exists(css_file):
        print(f"Minifying {css_file}...", end=' ')
        with open(css_file, 'r') as f:
            css_content = f.read()
        
        minified = minify_css(css_content)
        
        with open('css/optimizations.min.css', 'w') as f:
            f.write(minified)
        
        original_size = len(css_content)
        minified_size = len(minified)
        reduction = round(100 * (1 - minified_size / original_size), 1)
        
        print(f"✅ Done ({original_size} → {minified_size} bytes, {reduction}% reduction)")

if __name__ == '__main__':
    main()
