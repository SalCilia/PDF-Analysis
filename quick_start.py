#!/usr/bin/env python3
"""
Quick Start Guide for Financial Holdings Report Generator
This script walks you through the entire process step-by-step
"""

import os
import sys

def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")

def main():
    print_header("Financial Holdings Report Generator - Quick Start")
    
    print("Welcome! This guide will help you get started.\n")
    
    # Step 1: Check Python
    print("STEP 1: Verify Your Python Installation")
    print("-" * 80)
    print(f"Python Version: {sys.version}\n")
    print("✓ Python is installed and working!\n")
    
    # Step 2: Check Downloads folder
    print("STEP 2: Check Your Downloads Folder")
    print("-" * 80)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    print(f"Downloads folder: {downloads_path}\n")
    
    if os.path.exists(downloads_path):
        pdf_files = [f for f in os.listdir(downloads_path) if f.endswith('.pdf')]
        print(f"Found {len(pdf_files)} PDF file(s) in Downloads:")
        for pdf in pdf_files:
            print(f"  • {pdf}")
        print()
        
        pow_pdfs = [f for f in pdf_files if 'POW' in f.upper() or 'FUND' in f.upper()]
        if pow_pdfs:
            print(f"✓ Found potential POW Funds file(s):")
            for pdf in pow_pdfs:
                print(f"  • {pdf}")
        else:
            print("⚠ No POW/Funds PDFs found yet. Please download your PDF first.\n")
    else:
        print(f"✗ Downloads folder not found at {downloads_path}\n")
    
    # Step 3: Installation instructions
    print("STEP 3: Install Dependencies")
    print("-" * 80)
    print("Run this command in your terminal:\n")
    print("  pip install -r requirements.txt\n")
    print("This will install:")
    print("  • pdfplumber - PDF text extraction")
    print("  • requests - Web requests")
    print("  • beautifulsoup4 - HTML parsing")
    print("  • python-docx - Word document creation")
    print("  • lxml - Fast HTML parsing\n")
    
    # Step 4: Test environment
    print("STEP 4: Test Your Environment")
    print("-" * 80)
    print("Run this command to verify all dependencies:\n")
    print("  python test_environment.py\n")
    
    # Step 5: Run the main application
    print("STEP 5: Run the Application")
    print("-" * 80)
    print("Once dependencies are installed, run:\n")
    print("  python financial_report_generator_auto.py\n")
    print("The script will:")
    print("  1. Auto-find your POW Funds PDF in Downloads")
    print("  2. Extract the top 10 holdings")
    print("  3. Search Google for each company")
    print("  4. Generate a formatted Word report\n")
    
    # Step 6: Output files
    print("STEP 6: Check Your Results")
    print("-" * 80)
    print("After running, you'll get:")
    print("  • Financial_Holdings_Report.docx - Your formatted report")
    print("  • financial_report.log - Detailed execution log\n")
    
    # Summary
    print_header("Quick Start Summary")
    print("1️⃣  Download your POW Funds Report PDF")
    print("2️⃣  Place it in your Downloads folder")
    print("3️⃣  Run: pip install -r requirements.txt")
    print("4️⃣  Run: python test_environment.py")
    print("5️⃣  Run: python financial_report_generator_auto.py")
    print("6️⃣  Open: Financial_Holdings_Report.docx\n")
    print("=" * 80)
    print("Questions? Check financial_report.log for detailed logs")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()