#!/usr/bin/env python3
import datetime
import os

print("Starting README update...")

# Read current README
try:
    with open('README.md', 'r') as f:
        content = f.read()
    print("✅ README read successfully")
except Exception as e:
    print(f"❌ Error reading README: {e}")
    exit(1)

# Get current time
now = datetime.datetime.utcnow()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
date_str = now.strftime("%Y-%m-%d")

# Create update section
update_section = f"\n\n---\n\n### 🤖 Automated Update\n*Last run: {timestamp}*  \n"
update_section += f"*This update was generated automatically by GitHub Actions on {date_str}.*"

# Append to README
new_content = content.rstrip() + update_section

# Write back
try:
    with open('README.md', 'w') as f:
        f.write(new_content)
    print(f"✅ README updated successfully at {timestamp}")
except Exception as e:
    print(f"❌ Error writing README: {e}")
    exit(1)
