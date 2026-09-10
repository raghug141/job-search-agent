#!/bin/bash

# Job Search Agent - Setup & Testing Script
# This script sets up the environment and runs all tests

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🔍 Job Search Agent - Setup & Testing Script             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "1️⃣  Checking Python version..."
python3 --version

# Create virtual environment (optional but recommended)
echo ""
echo "2️⃣  Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "3️⃣  Activating virtual environment..."
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "4️⃣  Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Run tests
echo ""
echo "5️⃣  Running test suite..."
echo ""
python3 test_agent.py

echo ""
echo "6️⃣  Ready to use!"
echo ""
echo "📌 NEXT STEPS:"
echo "   • Run web scraper: python3 src/job_searcher.py"
echo "   • Start Flask API: python3 src/api.py"
echo "   • Open dashboard: http://localhost:5000/dashboard"
echo ""
