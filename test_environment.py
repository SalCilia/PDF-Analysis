#!/usr/bin/env python3
"""Test script to verify all dependencies are installed."""

import sys
print(f"✓ Python Version: {sys.version}\n")

dependencies = {
    'pdfplumber': 'PDF extraction',
    'requests': 'Web requests',
    'bs4': 'HTML parsing',
    'docx': 'Word document generation',
    'lxml': 'Fast HTML parsing'
}

print("Checking dependencies...\n")
all_good = True

for package, purpose in dependencies.items():
    try:
        __import__(package)
        print(f"✓ {package:20s} - {purpose}")
    except ImportError:
        print(f"✗ {package:20s} - MISSING!")
        all_good = False

print("\n" + "=" * 60)
if all_good:
    print("✓ All dependencies installed successfully!")
    print("Ready to run: python financial_report_generator_auto.py")
else:
    print("✗ Some dependencies are missing.")
    print("Run: pip install -r requirements.txt")
print("=" * 60)