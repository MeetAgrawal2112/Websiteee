#!/usr/bin/env python3
"""
HTML File Updater - Automatically adds optimization files to all HTML pages
This script adds the optimization CSS and JS files to all HTML files in the project.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import shutil

# Configuration
CSS_LINK = '    <!-- Website Optimizations -->\n    <link rel="stylesheet" href="css/optimizations.css" media="all" />\n'
JS_SCRIPT = '    <!-- Website Optimizations Script -->\n    <script src="js/optimizations.js"></script>\n'

class HTMLUpdater:
    def __init__(self, root_dir='.'):
        self.root_dir = root_dir
        self.updated_files = []
        self.skipped_files = []
        self.backup_dir = os.path.join(root_dir, 'backups', datetime.now().strftime('%Y%m%d_%H%M%S'))

    def create_backup(self, file_path):
        """Create backup of original file"""
        try:
            backup_path = os.path.join(self.backup_dir, os.path.relpath(file_path, self.root_dir))
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            shutil.copy2(file_path, backup_path)
            return backup_path
        except Exception as e:
            print(f"❌ Failed to backup {file_path}: {e}")
            return None

    def add_css_to_head(self, content):
        """Add CSS optimization link to head"""
        # Check if already present
        if 'optimizations.css' in content:
            return content, False

        # Find head closing tag
        head_pattern = r'(</head>)'
        if re.search(head_pattern, content, re.IGNORECASE):
            content = re.sub(
                head_pattern,
                CSS_LINK + r'\1',
                content,
                count=1,
                flags=re.IGNORECASE
            )
            return content, True
        return content, False

    def add_js_to_body(self, content):
        """Add JS optimization script before body closing tag"""
        # Check if already present
        if 'optimizations.js' in content:
            return content, False

        # Find body closing tag
        body_pattern = r'(</body>)'
        if re.search(body_pattern, content, re.IGNORECASE):
            content = re.sub(
                body_pattern,
                JS_SCRIPT + r'\1',
                content,
                count=1,
                flags=re.IGNORECASE
            )
            return content, True
        return content, False

    def update_html_file(self, file_path):
        """Update a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            css_added = False
            js_added = False

            # Add CSS
            content, css_added = self.add_css_to_head(content)

            # Add JS
            content, js_added = self.add_js_to_body(content)

            # If nothing was added, skip
            if not css_added and not js_added:
                self.skipped_files.append(file_path)
                return False

            # Create backup
            backup_path = self.create_backup(file_path)

            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.updated_files.append({
                'file': file_path,
                'css_added': css_added,
                'js_added': js_added,
                'backup': backup_path
            })

            return True

        except Exception as e:
            print(f"❌ Error updating {file_path}: {e}")
            return False

    def find_html_files(self):
        """Find all HTML files in the directory"""
        html_files = []
        excluded_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'backups', 'IIITPWebsite'}
        
        for root, dirs, files in os.walk(self.root_dir):
            # Remove excluded directories from dirs in-place
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))

        return sorted(html_files)

    def run(self):
        """Run the updater"""
        print("🚀 Starting HTML File Updater...")
        print(f"📁 Root directory: {self.root_dir}\n")

        html_files = self.find_html_files()
        print(f"📄 Found {len(html_files)} HTML files\n")

        if not html_files:
            print("⚠️  No HTML files found!")
            return

        # Update each file
        for i, file_path in enumerate(html_files, 1):
            rel_path = os.path.relpath(file_path, self.root_dir)
            print(f"[{i}/{len(html_files)}] Updating: {rel_path}...", end=' ')
            
            if self.update_html_file(file_path):
                print("✅ Updated")
            else:
                print("⏭️  Skipped")

        # Print summary
        print("\n" + "="*60)
        print("📊 SUMMARY")
        print("="*60)
        print(f"✅ Files updated: {len(self.updated_files)}")
        print(f"⏭️  Files skipped: {len(self.skipped_files)}")
        print(f"📦 Backups location: {self.backup_dir}")

        if self.updated_files:
            print("\n📝 Updated files:")
            for item in self.updated_files:
                print(f"  - {os.path.relpath(item['file'], self.root_dir)}")
                if item['css_added']:
                    print(f"    ✅ CSS added")
                if item['js_added']:
                    print(f"    ✅ JS added")

        print("\n✨ Update complete!")

def main():
    """Main entry point"""
    import sys

    # Get root directory from command line or use current directory
    root_dir = sys.argv[1] if len(sys.argv) > 1 else '.'

    if not os.path.isdir(root_dir):
        print(f"❌ Error: Directory '{root_dir}' not found")
        return 1

    # Run updater
    updater = HTMLUpdater(root_dir)
    updater.run()

    return 0

if __name__ == '__main__':
    exit(main())
