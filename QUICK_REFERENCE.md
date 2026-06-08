# Financial Holdings Report Generator - Quick Reference

## ⚡ Quick Start (30 seconds)

```bash
# Install dependencies
pip install -r requirements.txt

# Test setup
python test_environment.py

# Run demo (no PDF needed)
python demo_mode.py

# Run with your PDF (after placing in Downloads)
python financial_report_generator_auto.py
```

---

## 📦 Files Included

| File | Purpose |
|------|---------|
| financial_report_generator_auto.py | Main application |
| test_environment.py | Dependency checker |
| demo_mode.py | Demo without PDF |
| quick_start.py | Interactive guide |
| run_tests.py | Test suite |
| requirements.txt | Dependencies |
| README.md | Full documentation |
| SETUP_GUIDE.md | Setup instructions |
| BUILD_REPORT.md | Build verification |
| QUICK_REFERENCE.md | This file |

---

## 🎯 Main Features

1. **Auto-PDF Detection** - Finds your POW Funds PDF automatically
2. **Holdings Extraction** - Extracts top 10 holdings from PDF
3. **Web Searching** - Searches Google with human-like behavior
4. **Report Generation** - Creates professional Word document

---

## 🚀 Usage Examples

### Generate Report
```bash
python financial_report_generator_auto.py
```

### Test Environment
```bash
python test_environment.py
```

### Demo Mode
```bash
python demo_mode.py
```

### Run Tests
```bash
python run_tests.py
```

---

## ⚙️ Configuration

### More Holdings (default is 10)
```python
generator.extract_top_holdings(num_holdings=15)
```

### Longer Search Delay
```python
delay = random.uniform(3, 7)  # Instead of 2-5
```

### More Search Results Per Company (default is 3)
```python
results = self._search_company(company, num_results=5)
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| ModuleNotFoundError | `pip install -r requirements.txt` |
| PDF not found | Place PDF in Downloads folder |
| No holdings found | Check financial_report.log |
| Google blocked | Wait 10-15 minutes, try again |

---

## 📊 Output Files

- **Financial_Holdings_Report.docx** - Main report
- **financial_report.log** - Execution log
- **Demo_Holdings_Report.docx** - Sample report (demo mode)

---

## ⏱️ Performance

| Task | Time |
|------|------|
| PDF Extraction | 1-2 seconds |
| Per Company Search | 2-5 seconds |
| Total Runtime | 25-60 seconds |

---

## 🔒 Security

✅ HTTPS for searches
✅ No personal data stored
✅ Realistic anti-bot headers
✅ 10-second request timeout

---

## ✅ Pre-Flight Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed
- [ ] PDF in Downloads folder
- [ ] Internet connection ready

---

**Status:** ✅ Production Ready
**Version:** 1.0
**Last Updated:** 2026-06-08
