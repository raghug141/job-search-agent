# 🎯 QUICK START - 5 MINUTE SETUP

## **Your Complete Job Search Agent is Ready!**

---

## **📥 Step 1: Download (1 minute)**

### Option A: Clone with Git
```bash
git clone https://github.com/raghug141/job-search-agent.git
cd job-search-agent
```

### Option B: Download ZIP
1. Go to https://github.com/raghug141/job-search-agent
2. Click **"Code"** → **"Download ZIP"**
3. Extract and open folder

---

## **📦 Step 2: Install (2 minutes)**

Open terminal/command prompt in the folder and run:

**Windows:**
```bash
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

---

## **🧪 Step 3: Test (1 minute)**

**Windows:**
```bash
python test_agent.py
```

**Mac/Linux:**
```bash
python3 test_agent.py
```

Expected: ✅ All 5 tests pass

---

## **🚀 Step 4: Run (1 minute)**

### **Option A: View in Interactive Dashboard (Recommended)**

**Terminal 1 - Start API:**
```bash
python src/api.py    # Windows
python3 src/api.py   # Mac/Linux
```

**Terminal 2 - Open Browser:**
```
http://localhost:5000/dashboard
```

✨ Beautiful purple dashboard with:
- 🔍 Search filters (Role, City, Work Type)
- 📊 Charts (Jobs by city, role, company)
- 📋 Detailed job listings
- ⭐ Match scores
- 🔗 Apply buttons

---

### **Option B: Run in Terminal**

```bash
python src/job_searcher.py    # Windows
python3 src/job_searcher.py   # Mac/Linux
```

Scrapes jobs and shows results in terminal

---

## **📊 What You Get**

✅ **45+ Companies Tracked**
- 16 Fortune 500 Companies (Google, Microsoft, Amazon, etc.)
- 20 Top Indian Product Companies (Flipkart, Swiggy, Razorpay, etc.)

✅ **All of India Coverage**
- Bangalore, Mumbai, Hyderabad, Delhi, Pune, Chennai, and 11+ more cities
- Remote & Hybrid positions included

✅ **Your Target Roles**
- Cloud Engineer
- DevOps Engineer
- Senior/Lead IT Support Specialist
- Senior/Lead Desktop Support Analyst

✅ **Smart Filtering**
- Filter by role, city, work type
- Match score algorithm (0-100%)
- Salary range detection

✅ **Beautiful Dashboard**
- Interactive charts
- Detailed job cards
- Direct apply links

---

## **📁 File Guide**

| File | What to Do |
|------|-----------|
| **README.md** | Full documentation |
| **HOW_TO_RUN.md** | Detailed setup guide |
| **TESTING_GUIDE.md** | All testing options |
| **test_agent.py** | `python test_agent.py` - Run tests |
| **src/job_searcher.py** | `python src/job_searcher.py` - Web scraper |
| **src/api.py** | `python src/api.py` - Dashboard API |
| **dashboard/index.html** | Open in browser for UI |

---

## **🆘 Common Issues**

| Issue | Solution |
|-------|----------|
| `python: command not found` | Use `python3` instead |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Port 5000 already in use` | Use different port: `python src/api.py --port 5001` |
| Dashboard not loading | Refresh: Ctrl+F5, Clear cache: Ctrl+Shift+Delete |

---

## **⚡ Quickest Commands**

```bash
# Setup & test everything
pip install -r requirements.txt && python test_agent.py

# Start dashboard
python src/api.py

# Run scraper
python src/job_searcher.py

# Test API
curl http://localhost:5000/api/health
```

---

## **🎉 You're Done!**

Your Job Search Agent is now:
- ✅ Installed
- ✅ Tested
- ✅ Ready to find jobs!

**Next:** Open dashboard and start searching! 🚀

---

**Questions?**
- 📖 Read: README.md
- 🧪 Test: TESTING_GUIDE.md
- 🏃 Run: HOW_TO_RUN.md
- 💬 Ask: GitHub Issues

**Happy Job Hunting! 🎯**
