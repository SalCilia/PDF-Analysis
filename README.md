# Financial Holdings Report Generator

## 📊 Overview

The Financial Holdings Report Generator is an automated Python application that:

1. **Automatically finds** your POW Funds Report PDF in your Downloads folder
2. **Extracts** the top 10 holdings from the PDF
3. **Searches Google** for information about each company (with human-like behavior)
4. **Generates** a professionally formatted Word document (`.docx`) report

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

## ✨ Key Features

| Feature | Benefit |
|---------|----------|
| **Auto-Detection** | Automatically finds PDF in Downloads folder |
| **Realistic Headers** | Uses Chrome user-agent to avoid bot detection |
| **Random Delays** | 2-5 second delays simulate human browsing |
| **Error Handling** | Gracefully handles PDF/network errors |
| **Comprehensive Logging** | Detailed logs to console + file |
| **Professional Output** | Clean, formatted Word document |
| **No Configuration** | Set it and forget it! |

---

## 📋 Prerequisites

- **Python 3.7+** installed on your computer
- **Internet connection** (for Google searches)
- **POW Funds Report PDF** in your Downloads folder
- ~5 minutes to run the application

### Verify Python Installation

```bash
python --version
# or
python3 --version
```

Should show: `Python 3.x.x`

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pdfplumber` - PDF text extraction
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `python-docx` - Word document generation
- `lxml` - Fast HTML parsing

### 2. Test Your Environment

```bash
python test_environment.py
```

**Expected output:**
```
✓ Python Version: 3.10.12

Checking dependencies...

✓ pdfplumber         - PDF extraction
✓ requests           - Web requests
✓ bs4                - HTML parsing
✓ docx               - Word document generation
✓ lxml               - Fast HTML parsing

============================================================
✓ All dependencies installed successfully!
```

### 3. Prepare Your PDF

1. Download your **POW Funds Report PDF**
2. Save it to your **Downloads folder**
3. Filename should contain "POW" or "Funds"

### 4. Run the Application

```bash
python financial_report_generator_auto.py
```

### 5. Check Results

Two files are created:
- **Financial_Holdings_Report.docx** ← Open in Microsoft Word
- **financial_report.log** ← Detailed execution log

---

## 🎮 Demo Mode (No PDF Required)

Want to see how it works without a real PDF?

```bash
python demo_mode.py
```

This generates `Demo_Holdings_Report.docx` with sample data!

---

## 📊 Output Example

Your Word document will contain:

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
    that designs and manufactures electronics...
    
  • Result 2: Apple Official Website
    Discover the latest Apple products and services...
    
  • Result 3: Apple Inc. - Investor Relations
    Apple financial information and investor relations...

Microsoft Corporation
  • Result 1: Microsoft - Official Website
    ...

[Continues for all 10 holdings]
```

---

## 🔧 How It Works in Detail

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
- Formatted company headings (dark blue)
- Bulleted search results
- Bold titles, italic snippets
- Clean spacing and layout

---

## ⚠️ Troubleshooting

### "ModuleNotFoundError: No module named 'pdfplumber'"

**Solution:**
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
- PDF doesn't have "Top Holdings" section
- Section name is different (e.g., "Holdings", "Portfolio")
- PDF is corrupted or encrypted

**Solution:** Check `financial_report.log` for details

### "Network error" or "Google blocked requests"

**Why:** Google detects automated scraping

**Solution:**
- Wait a few minutes and try again
- Script includes anti-detection headers
- Random delays simulate human behavior

### "No search results found"

**Why:** Google page structure changed or internet issue

**Solution:**
- Check internet connection
- Try again later
- Check logs for details

---

## 📁 File Structure

```
pdf-analysis/
├── financial_report_generator_auto.py  # Main application
├── test_environment.py                 # Dependency verification
├── demo_mode.py                        # Demo without PDF
├── quick_start.py                      # Quick start guide
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

---

## 📝 Logging

The application creates a detailed log file: `financial_report.log`

**Log entries include:**
- PDF file location and reading status
- Holdings extraction details
- Web search queries and results
- Document generation status
- Any errors or warnings

---

## 🎓 Learning Resources

- [pdfplumber documentation](https://github.com/jsvine/pdfplumber)
- [requests documentation](https://docs.python-requests.org/)
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [python-docx documentation](https://python-docx.readthedocs.io/)

---

## 💡 Tips & Tricks

1. **First time?** Run `demo_mode.py` to see output format
2. **Troubleshooting?** Check `financial_report.log`
3. **Customize?** Script is well-commented for modifications
4. **Multiple PDFs?** Script uses first one found - rename others
5. **Want fewer/more results?** Edit `num_results` parameter in code

---

## 🐛 Known Issues

- **Google may block requests** if made too frequently. Solution: Wait a few minutes or use proxy.
- **PDF with different section names** won't extract. Solution: Edit section markers in code.
- **Encrypted PDFs** cannot be read. Solution: Unlock PDF first.

---

## 📞 Support

If something doesn't work:

1. Check `financial_report.log` for detailed error messages
2. Verify dependencies: `python test_environment.py`
3. Ensure PDF is in Downloads folder with correct name
4. Check internet connection
5. Try again - sometimes Google blocks temporarily

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 🎉 Ready to Get Started?

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test environment
python test_environment.py

# 3. Place PDF in Downloads folder

# 4. Run the application
python financial_report_generator_auto.py

# 5. Open Financial_Holdings_Report.docx
```

**Questions?** Check the logs or review the inline code comments.

**Happy analyzing!** 📊
