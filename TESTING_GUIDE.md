# Job Search Agent - Quick Start Testing Guide

## 🚀 How to Test This Now?

There are **5 easy ways** to test the Job Search Agent:

---

## **Option 1: Run Complete Test Suite (⭐ RECOMMENDED)**

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Test Script
```bash
# Linux/Mac
bash setup_and_test.sh

# Windows
setup_and_test.bat

# Or manually
python3 test_agent.py
```

**What it tests:**
✓ Web scraper functionality
✓ Job data structure
✓ Filtering & search
✓ Export functionality
✓ Summary statistics

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
✓ Match Score Calculation

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

## **Option 2: Run Individual Tests**

### Test 1: Web Scraper Only
```bash
python3 -c "
from test_agent import test_1_web_scraper
test_1_web_scraper()
"
```

### Test 2: Data Structure
```bash
python3 -c "
from test_agent import test_2_data_structure
test_2_data_structure()
"
```

### Test 3: Filtering
```bash
python3 -c "
from test_agent import test_3_filtering
test_3_filtering()
"
```

### Test 4: Export
```bash
python3 -c "
from test_agent import test_4_export
test_4_export()
"
```

### Test 5: Statistics
```bash
python3 -c "
from test_agent import test_5_summary_stats
test_5_summary_stats()
"
```

---

## **Option 3: Run Web Scraper**

### Quick Start
```bash
python3 src/job_searcher.py
```

### What it does:
- Scrapes 45+ Fortune 500 and Indian product company career portals
- Finds jobs matching target roles
- Generates summary statistics
- Exports results to JSON

### Expected Output:
```
══════════════════════════════════════════════════════════════════
🚀 STARTING COMPREHENSIVE JOB SEARCH ACROSS INDIA
══════════════════════════════════════════════════════════════════

📍 Scraping Fortune 500 Companies...
──────────────────────────────────────────────────────────────────
🔍 Scraping Microsoft (Fortune 500)...
✅ Found 12 jobs from Microsoft

🔍 Scraping Google (Fortune 500)...
✅ Found 18 jobs from Google

📍 Scraping Top Indian Product-Based Companies...
──────────────────────────────────────────────────────────────────
🔍 Scraping Flipkart (Product-based)...
✅ Found 8 jobs from Flipkart

═══════════════════════════════════════════════════════════════════
✅ SEARCH COMPLETED!
═══════════════════════════════════════════════════════════════════

📊 Summary:
   Total Jobs Found: XXX
   Companies Searched: 36
   Average Match Score: XX.X%
```

---

## **Option 4: Start Flask Dashboard API**

### Start the Server
```bash
python3 src/api.py
```

### Expected Output:
```
🔄 Loading jobs from all companies...
✅ Loaded XXX jobs

 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
 * Debugger is active!
```

### Test the API Endpoints
Open a new terminal and try:

#### Test 1: Health Check
```bash
curl http://localhost:5000/api/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-09-10T19:06:00.123456",
  "companies_available": 36
}
```

#### Test 2: Get All Cities
```bash
curl http://localhost:5000/api/cities
```

**Expected Response:**
```json
{
  "success": true,
  "cities": [
    {"city": "Bangalore", "count": 45},
    {"city": "Mumbai", "count": 32},
    {"city": "Hyderabad", "count": 28}
  ]
}
```

#### Test 3: Get All Companies
```bash
curl http://localhost:5000/api/companies
```

#### Test 4: Search Jobs
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "roles": ["Cloud Engineer"],
    "cities": ["Bangalore"],
    "work_types": ["Remote", "Hybrid"]
  }'
```

#### Test 5: Get Statistics
```bash
curl http://localhost:5000/api/stats
```

---

## **Option 5: Open Interactive Dashboard**

### Method A: Via Flask (Recommended)
```bash
# Terminal 1: Start API server
python3 src/api.py

# Terminal 2: Open browser
# Visit: http://localhost:5000/dashboard
```

### Method B: Direct HTML File
```bash
# Open dashboard/index.html directly in your browser
# Just double-click the file or:
open dashboard/index.html  # Mac
xdg-open dashboard/index.html  # Linux
start dashboard/index.html  # Windows
```

### Dashboard Features to Test:
1. **Search Button** - Click to load jobs
2. **Filter Options** - Select roles, cities, work types
3. **View Statistics** - See total jobs, average match score
4. **Charts** - View job distribution by city and role
5. **Job Cards** - Click to expand and see details
6. **Apply Button** - Links to company career pages

---

## **Complete Test Workflow**

### Step 1: Install & Setup (2 minutes)
```bash
git clone https://github.com/raghug141/job-search-agent.git
cd job-search-agent
pip install -r requirements.txt
```

### Step 2: Run Test Suite (1 minute)
```bash
python3 test_agent.py
```

### Step 3: Run Web Scraper (5-10 minutes)
```bash
python3 src/job_searcher.py
```

### Step 4: Start API (Terminal 1)
```bash
python3 src/api.py
```

### Step 5: Open Dashboard (Terminal 2)
```bash
# Option A: Web browser at http://localhost:5000/dashboard
# Option B: Or open dashboard/index.html directly
```

### Step 6: Test Dashboard
- Click "Search Jobs" button
- Filter by role, city, work type
- View statistics and charts
- Click on job cards to expand details
- Click "Apply Now" to visit company career pages

---

## **Troubleshooting**

### Issue: "Module not found" Error
**Solution:**
```bash
pip install -r requirements.txt
python3 -m pip install --upgrade pip
```

### Issue: Port 5000 Already in Use
**Solution:**
```bash
# Use different port
python3 src/api.py --port 5001
# Visit: http://localhost:5001/dashboard
```

### Issue: Dashboard Not Loading
**Solution:**
```bash
# Check if API is running
curl http://localhost:5000/api/health

# If not, start API:
python3 src/api.py

# Clear browser cache (Ctrl+Shift+Delete)
# Refresh page (Ctrl+F5)
```

### Issue: No Jobs Found
**Solution:**
```bash
# Check if scraping is working
python3 src/job_searcher.py

# Verify internet connection
# Some sites may block automated requests
# Wait a moment before retrying
```

---

## **Expected Test Results Summary**

```
✅ Test 1: Web Scraper
   - Loads 36 company portals
   - Extracts job listings
   - Normalizes data

✅ Test 2: Data Structure
   - Creates JobPosting objects
   - Stores all required fields
   - Calculates match scores

✅ Test 3: Filtering
   - Filters by role ✓
   - Filters by city ✓
   - Filters by work type ✓
   - Sorts by match score ✓

✅ Test 4: Export
   - Exports to JSON ✓
   - Exports to CSV ✓
   - File created successfully ✓

✅ Test 5: Statistics
   - Calculates total jobs ✓
   - Counts by city ✓
   - Counts by company ✓
   - Counts by work type ✓
   - Averages match scores ✓
```

---

## **Next Steps After Testing**

Once all tests pass:

1. **Customize the agent** - Edit `agent-config.yaml`
2. **Add more companies** - Extend `FORTUNE_500_COMPANIES` dict
3. **Adjust filters** - Modify `TARGET_ROLES`, `INDIAN_CITIES`
4. **Set up notifications** - Configure email alerts
5. **Schedule searches** - Run daily via cron/Task Scheduler
6. **Deploy dashboard** - Host on cloud platform

---

## **Quick Reference Commands**

```bash
# Setup
pip install -r requirements.txt

# Test
python3 test_agent.py

# Run scraper
python3 src/job_searcher.py

# Start API
python3 src/api.py

# Open dashboard
open http://localhost:5000/dashboard

# Test API
curl http://localhost:5000/api/health
curl http://localhost:5000/api/stats
curl http://localhost:5000/api/cities
```

---

**🎉 You're all set! Start testing now!**
