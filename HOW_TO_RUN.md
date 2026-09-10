# 🚀 WHERE & HOW TO RUN ON YOUR LAPTOP

## **Step-by-Step Guide to Run Locally**

---

## **Prerequisites (Install First)**

### **1. Install Python**
- **Download:** https://www.python.org/downloads/
- **Choose:** Python 3.8 or newer
- **During installation:** ✅ Check "Add Python to PATH"

**Verify installation:**
```bash
python --version
# or
python3 --version
```

### **2. Install Git (Optional but Recommended)**
- **Download:** https://git-scm.com/download
- **This helps you clone the repository**

---

## **SETUP: 5 Minutes**

### **Option A: Clone from GitHub (Easiest)**

#### On Windows:
```bash
# Open Command Prompt or PowerShell
git clone https://github.com/raghug141/job-search-agent.git
cd job-search-agent
```

#### On Mac/Linux:
```bash
# Open Terminal
git clone https://github.com/raghug141/job-search-agent.git
cd job-search-agent
```

---

### **Option B: Download as ZIP**

1. Go to: https://github.com/raghug141/job-search-agent
2. Click **"Code"** → **"Download ZIP"**
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

---

## **INSTALL DEPENDENCIES: 2 Minutes**

### **Windows (Command Prompt or PowerShell):**
```bash
pip install -r requirements.txt
```

### **Mac/Linux (Terminal):**
```bash
pip3 install -r requirements.txt
```

**This installs:**
- ✅ requests (for web requests)
- ✅ beautifulsoup4 (for web scraping)
- ✅ selenium (for advanced scraping)
- ✅ Flask (for dashboard API)
- ✅ Flask-CORS (for API)

---

## **TEST: 2 Minutes**

### **Windows:**
```bash
# Option 1: Use batch script (easiest)
setup_and_test.bat

# Option 2: Manual
python test_agent.py
```

### **Mac/Linux:**
```bash
# Option 1: Use shell script (easiest)
bash setup_and_test.sh

# Option 2: Manual
python3 test_agent.py
```

**Expected Output:**
```
═══════════════════════════════════════════════════════════════════
🔍 JOB SEARCH AGENT - COMPREHENSIVE TEST SUITE
═══════════════════════════════════════════════════════════════════

[1/5] Testing Web Scraper...
✓ Initialized Job Search Engine
  - Fortune 500 Companies: 16
  - Indian Product Companies: 20
  - Total Companies to Scrape: 36

[2/5] Testing Data Structure...
✓ Created sample JobPosting object

[3/5] Testing Filtering & Search...
✓ Filter by Role, City, Work Type

[4/5] Testing Export...
✓ Testing JSON Export

[5/5] Testing Statistics...
✓ Generated Summary Statistics

═══════════════════════════════════════════════════════════════════
TEST SUMMARY
═══════════════════════════════════════════════════════════════════
✓ Passed: 5/5
🎉 All tests passed! Agent is ready to use.
```

---

## **RUN: CHOOSE YOUR METHOD**

---

### **METHOD 1: Run Web Scraper (Simplest)**

**Windows:**
```bash
python src/job_searcher.py
```

**Mac/Linux:**
```bash
python3 src/job_searcher.py
```

**What happens:**
- ✅ Scrapes 45+ company career portals
- ✅ Finds matching jobs
- ✅ Shows statistics in terminal
- ✅ Exports results to JSON file

**Time:** 5-10 minutes
**Output:** Results printed to console + JSON file

---

### **METHOD 2: Start Dashboard (Interactive UI)**

#### **Step 1: Open Terminal/Command Prompt**

#### **Step 2: Start API Server**
**Windows:**
```bash
python src/api.py
```

**Mac/Linux:**
```bash
python3 src/api.py
```

**You'll see:**
```
🔄 Loading jobs from all companies...
✅ Loaded XXX jobs

 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

#### **Step 3: Open Dashboard in Browser**

**Option A: Click this link**
```
http://localhost:5000/dashboard
```

**Option B: Copy-paste into browser address bar**
```
http://127.0.0.1:5000/dashboard
```

**Or directly open:**
```
dashboard/index.html
```

**You'll see:**
- 🎨 Beautiful purple dashboard
- 🔍 Search filters (Role, City, Work Type)
- 📊 Charts (Jobs by city, role, work type)
- 📋 Job listings with details
- ⭐ Match scores
- 🔗 Apply buttons

#### **Step 4: Interact with Dashboard**
1. Click **"Search Jobs"** button
2. Select filters:
   - Job Role (Cloud Engineer, DevOps, etc.)
   - City (Bangalore, Mumbai, Hyderabad, etc.)
   - Work Type (Remote, Hybrid, On-site)
3. View charts and job cards
4. Click job card to expand details
5. Click "Apply Now" to visit company page

---

### **METHOD 3: Use API from Code**

**Windows/Mac/Linux:**
```bash
python3 -c "
from src.job_searcher import JobSearchEngine

engine = JobSearchEngine()
jobs = engine.search_all_companies()

# Print first 5 jobs
for job in jobs[:5]:
    print(f'{job.title} at {job.company} - {job.city}')
"
```

---

### **METHOD 4: Test Individual APIs**

**Start API first (in Terminal 1):**
```bash
python3 src/api.py
```

**Test in Terminal 2:**

#### Get all cities:
```bash
curl http://localhost:5000/api/cities
```

#### Get all companies:
```bash
curl http://localhost:5000/api/companies
```

#### Health check:
```bash
curl http://localhost:5000/api/health
```

#### Search jobs:
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{"roles": ["Cloud Engineer"], "cities": ["Bangalore"]}'
```

---

## **FOLDER STRUCTURE (What Each File Does)**

```
job-search-agent/
│
├── 📄 README.md                    ← Main documentation
├── 📄 TESTING_GUIDE.md             ← Testing instructions
├── 📄 HOW_TO_RUN.md                ← This file!
│
├── 📦 requirements.txt             ← Dependencies (pip install)
├── 🧪 test_agent.py               ← Test suite (python test_agent.py)
│
├── 🪟 setup_and_test.bat           ← Windows setup script
├── 🐧 setup_and_test.sh            ← Mac/Linux setup script
│
├── src/
│   ├── job_searcher.py             ← Main scraper (python src/job_searcher.py)
│   ├── api.py                      ← Dashboard API (python src/api.py)
│   └── __init__.py
│
├── dashboard/
│   └── index.html                  ← Dashboard UI (open in browser)
│
├── agent-config.yaml               ← Agent configuration
├── data/                           ← Stores exported jobs
└── .gitignore
```

---

## **QUICK REFERENCE COMMANDS**

### **Windows PowerShell or Command Prompt:**
```bash
# Setup
pip install -r requirements.txt

# Test
python test_agent.py

# Run scraper
python src/job_searcher.py

# Start dashboard
python src/api.py

# Then open browser:
start http://localhost:5000/dashboard
```

### **Mac Terminal:**
```bash
# Setup
pip3 install -r requirements.txt

# Test
python3 test_agent.py

# Run scraper
python3 src/job_searcher.py

# Start dashboard
python3 src/api.py

# Then open browser:
open http://localhost:5000/dashboard
```

### **Linux Terminal:**
```bash
# Setup
pip3 install -r requirements.txt

# Test
python3 test_agent.py

# Run scraper
python3 src/job_searcher.py

# Start dashboard
python3 src/api.py

# Then open browser:
xdg-open http://localhost:5000/dashboard
```

---

## **COMPLETE WORKFLOW (First Time: 15 Minutes)**

```
1. Clone/Download repo (2 min)
   ↓
2. Open terminal in folder (1 min)
   ↓
3. pip install -r requirements.txt (2 min - downloading)
   ↓
4. python test_agent.py (2 min - testing)
   ↓
5. python src/api.py (1 min - starting server)
   ↓
6. Open http://localhost:5000/dashboard (5 min - using dashboard)
```

---

## **TROUBLESHOOTING**

### **"python: command not found"**
**Solution:**
- Use `python3` instead of `python`
- Or add Python to PATH

### **"ModuleNotFoundError: No module named 'flask'"**
**Solution:**
```bash
pip install -r requirements.txt
```

### **"Port 5000 already in use"**
**Solution:**
```bash
# Kill the process using port 5000
# Windows: taskkill /PID <PID> /F
# Mac/Linux: lsof -ti:5000 | xargs kill -9
```

### **"Dashboard not loading"**
**Solution:**
1. Make sure API is running
2. Clear browser cache (Ctrl+Shift+Delete)
3. Refresh page (Ctrl+F5)
4. Try http://127.0.0.1:5000/dashboard instead

### **"No jobs found"**
**Solution:**
- Wait 5-10 minutes (first scrape takes time)
- Check internet connection
- Try running test first: `python test_agent.py`

---

## **WHAT YOU CAN DO AFTER SETUP**

✅ Search for jobs across 45+ companies
✅ Filter by role, city, work type
✅ See match scores for relevance
✅ View beautiful charts & statistics
✅ Export results to JSON/CSV
✅ Apply directly to company portals
✅ Get daily job alerts (future feature)

---

## **NEXT STEPS**

1. **✅ Setup complete?** → Run `python test_agent.py`
2. **✅ Tests passed?** → Run `python src/api.py`
3. **✅ API started?** → Open `http://localhost:5000/dashboard`
4. **✅ Dashboard works?** → Start job hunting! 🎉

---

## **SUPPORT**

- 📖 **Read:** README.md (full documentation)
- 🧪 **Test:** TESTING_GUIDE.md (testing options)
- 💬 **Ask:** Open GitHub issue if stuck
- ⭐ **Star:** If it helps you!

---

**Happy Job Hunting! 🚀**
