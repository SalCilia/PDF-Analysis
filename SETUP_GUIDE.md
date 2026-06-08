# Financial Holdings Report Generator - Complete Setup Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running)
5. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The Financial Holdings Report Generator is a Python automation tool that:

1. **Finds** your POW Funds Report PDF in your Downloads folder
2. **Extracts** the top 10 holdings from the PDF
3. **Searches** Google for information about each company
4. **Generates** a professionally formatted Word report (`.docx`)

### How It Works

```
PDF File (Downloads)
    ↓
Extract Holdings (pdfplumber)
    ↓
Google Search Each Company (requests + BeautifulSoup)
    ↓
Generate Word Report (python-docx)
    ↓
Financial_Holdings_Report.docx
```

---

## ✅ Prerequisites

- **Python 3.7+** installed on your computer
- **Internet connection** (for Google searches)
- **POW Funds Report PDF** in your Downloads folder
- ~5 minutes to run the script

### Check Your Python Installation

Open your terminal/command prompt and run:

```bash
python --version
```

You should see something like:
```
Python 3.10.12
```

If you get "command not found", [install Python here](https://www.python.org/downloads/).

---

## 🔧 Installation

### 1. Download/Prepare the Files

Make sure you have these files in a folder:
- `financial_report_generator_auto.py` (main script)
- `requirements.txt` (dependencies list)
- `test_environment.py` (verification script)

### 2. Install Dependencies

Open terminal in the folder with the files and run:

```bash
pip install -r requirements.txt
```

**This installs:**
- `pdfplumber` - Extract text from PDFs
- `requests` - Make web requests to Google
- `beautifulsoup4` - Parse HTML search results
- `python-docx` - Create Word documents
- `lxml` - Fast HTML parsing

### 3. Verify Installation

Run the test script:

```bash
python test_environment.py
```

**Expected output:**
```
✓ Python Version: 3.10.12 (main, ...)

Checking dependencies...

✓ pdfplumber         - PDF extraction
✓ requests           - Web requests
✓ bs4                - HTML parsing
✓ docx               - Word document generation
✓ lxml               - Fast HTML parsing

============================================================
✓ All dependencies installed successfully!
Ready to run: python financial_report_generator_auto.py
============================================================
```

---

## 🚀 Running the Application

### Step 1: Prepare Your PDF

1. Download your **POW Funds Report PDF**
2. Save it to your **Downloads folder**
3. Filename should contain "POW" or "Funds" (e.g., `POW Funds Report.pdf`)

The script will auto-detect it!

### Step 2: Run the Script

In terminal, run:

```bash
python financial_report_generator_auto.py
```

### Step 3: Watch It Work

You'll see real-time progress:

```
================================================================================
Financial Holdings Report Generator
================================================================================

[Step 0] Locating POW Funds Report PDF...
✓ Found POW Funds PDF: /Users/YourName/Downloads/POW Funds Report.pdf

[Step 1] Extracting holdings from PDF...
Reading PDF file: /Users/YourName/Downloads/POW Funds Report.pdf
✓ Found holdings section: 'top ten holdings'
Extracted: Apple Inc.
Extracted: Microsoft
Extracted: Tesla
...
✓ Extracted 10 holdings from PDF
Holdings: Apple Inc., Microsoft, Tesla, ...

[Step 2] Performing web searches...
Starting web search for 10 companies
[1/10] Searching: Apple Inc.
  Waiting 3.45s before next search...
[2/10] Searching: Microsoft
...
✓ Web search completed

[Step 3] Generating Word document...
Generating Word document...
✓ Word document saved: Financial_Holdings_Report.docx

✓ SUCCESS!
Report saved as: Financial_Holdings_Report.docx
PDF processed: POW Funds Report.pdf
================================================================================
```

### Step 4: Open Your Report

Two files are created:

1. **Financial_Holdings_Report.docx** ← Open this in Microsoft Word
2. **financial_report.log** ← Detailed execution log

---

## 🎮 Demo Mode (Test Without PDF)

Want to see how it works before running with your PDF?

```bash
python demo_mode.py
```

This generates `Demo_Holdings_Report.docx` with sample data, so you can see the output format!

---

## 📊 Output Format

Your Word document will look like:

```
═══════════════════════════════════════
    Financial Holdings Report
    Top 10 Holdings Analysis
    Generated: 2026-06-08 14:30:45
    Source: POW Funds Report.pdf
═══════════════════════════════════════

Apple Inc.
  • Result 1: Apple - Wikipedia
    Apple Inc. is an American multinational technology company 
    that designs and manufactures electronics and computer software.
    
  • Result 2: Apple Official Website
    Discover the latest Apple products and services. Shop iPhone...
    
  • Result 3: Apple Inc. - Investor Relations
    Apple financial information and investor relations...

Microsoft Corporation
  • Result 1: Microsoft - Official Website
    ...
    
[continues for all 10 holdings]
```

---

## 🔍 How It Works in Detail

### PDF Extraction
- Uses `pdfplumber` to read PDF text
- Searches for "Top Ten Holdings" section
- Cleans company names (removes %, Inc, Ltd, etc.)
- Extracts exactly 10 holdings

### Web Searching
- For each company, constructs Google search URL
- Uses realistic browser headers:
  - User-Agent: Chrome on Windows
  - Accept-Language: en-US
  - DNT (Do Not Track): 1
- Adds random 2-5 second delays (human-like behavior)
- Parses HTML with BeautifulSoup
- Extracts top 3 organic results (title + snippet)

### Word Document Generation
- Creates professional Word document
- Formatted headings (dark blue)
- Bulleted search results
- Bold titles, italic snippets
- Clean spacing and layout

---

## ⚠️ Troubleshooting

### "ModuleNotFoundError: No module named 'pdfplumber'"

**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### "PDF file not found"

**Solution:** 
1. Download your POW Funds PDF
2. Save to Downloads folder
3. Filename must contain "POW" or "Funds"
4. Try again

### "No holdings found in PDF"

**Possible causes:**
- PDF doesn't have a "Top Holdings" section
- Section name is different (e.g., "Holdings", "Portfolio")
- PDF is corrupted or encrypted

**Solution:** Check the `financial_report.log` file for details

### "Network error" / Google blocked requests

**Why:** Google detects automated scraping

**Solution:**
- Wait a few minutes and try again
- Script already includes anti-detection headers
- Random delays between requests simulate human behavior

### "No search results found"

**Why:** Google page structure changed or internet issue

**Solution:**
- Check internet connection
- Try again later
- Check logs for details

---

## 📝 Key Features

| Feature | Benefit |
|---------|----------|
| **Auto-detection** | Finds PDF automatically in Downloads |
| **Error handling** | Gracefully handles PDF/network errors |
| **Realistic headers** | Avoids bot detection on Google |
| **Random delays** | 2-5 second delays simulate human browsing |
| **Detailed logging** | Console + file logs for debugging |
| **Professional output** | Clean, formatted Word document |
| **No manual input** | Set it and forget it! |

---

## 🎓 Learning Resources

- [pdfplumber docs](https://github.com/jsvine/pdfplumber)
- [requests docs](https://docs.python-requests.org/)
- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [python-docx docs](https://python-docx.readthedocs.io/)

---

## 💡 Tips

1. **First time?** Run `demo_mode.py` to see output format
2. **Troubleshooting?** Check `financial_report.log`
3. **Want to modify?** Edit the script - it's well-commented
4. **Multiple PDFs?** Script uses first one found - rename others

---

## 📞 Support

If something doesn't work:

1. Check `financial_report.log` for detailed error messages
2. Verify all dependencies: `python test_environment.py`
3. Ensure PDF is in Downloads folder with correct name
4. Check your internet connection
5. Try running again - sometimes Google blocks temporarily

---

**Ready to generate your report? Let's go! 🚀**
