#!/usr/bin/env python3
import datetime
import os

def update_readme():
    # Read current README
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Find or create automation section
    if '## 🤖 Automated Updates' not in content:
        content += '\n\n## 🤖 Automated Updates\n'
    
    # Add timestamp entry
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = f"\n- ✅ Workflow ran successfully at: {timestamp}"
    
    # Append new entry
    updated_content = content + new_entry
    
    # Write back
    with open('README.md', 'w') as f:
        f.write(updated_content)
    
    print(f"README updated at {timestamp}")

if __name__ == "__main__":
    update_readme()
