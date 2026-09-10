#!/usr/bin/env python3
"""
Job Search Agent - Test Suite
Comprehensive testing for scraping, data structure, filtering, export, and stats.
"""

import os
import sys

# Ensure root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from src.job_searcher import (
    JobSearchEngine,
    JobPosting,
    FORTUNE_500_COMPANIES,
    INDIAN_PRODUCT_COMPANIES,
    TARGET_ROLES
)


def test_1_web_scraper():
    """Test 1: Web Scraper / Engine initialization"""
    engine = JobSearchEngine()
    assert len(FORTUNE_500_COMPANIES) == 16, f"Expected 16 F500 companies, got {len(FORTUNE_500_COMPANIES)}"
    assert len(INDIAN_PRODUCT_COMPANIES) == 20, f"Expected 20 Indian companies, got {len(INDIAN_PRODUCT_COMPANIES)}"
    assert len(FORTUNE_500_COMPANIES) + len(INDIAN_PRODUCT_COMPANIES) == 36
    
    print("[1/5] Testing Web Scraper...")
    print("✓ Initialized Job Search Engine")
    print(f"  - Fortune 500 Companies: {len(FORTUNE_500_COMPANIES)}")
    print(f"  - Indian Product Companies: {len(INDIAN_PRODUCT_COMPANIES)}")
    print(f"  - Total Companies to Scrape: {len(FORTUNE_500_COMPANIES) + len(INDIAN_PRODUCT_COMPANIES)}")
    return True


def test_2_data_structure():
    """Test 2: JobPosting Data Structure and Match Score"""
    engine = JobSearchEngine()
    job = JobPosting(
        job_id="test-101",
        title="Cloud Engineer",
        company="Microsoft",
        company_type="Fortune 500",
        location="Bangalore, Karnataka, India",
        city="Bangalore",
        state="Karnataka",
        work_type="Remote",
        salary_range="₹22,00,000 - ₹34,00,000",
        description="Test description",
        requirements=["AWS", "Kubernetes", "Terraform"],
        benefits=["Health Insurance"],
        experience_level="Senior",
        application_url="https://careers.microsoft.com",
        match_score=0.88,
        posted_date="2026-09-10"
    )
    assert job.job_id == "test-101"
    assert job.title == "Cloud Engineer"
    
    # Test match score calculation
    score = engine.calculate_match_score("DevOps Engineer", ["Docker", "Kubernetes", "CI/CD"])
    assert 0.0 <= score <= 1.0

    print("\n[2/5] Testing Data Structure...")
    print("✓ Created sample JobPosting object")
    print("✓ Match Score Calculation")
    return True


def test_3_filtering():
    """Test 3: Filtering & Search"""
    engine = JobSearchEngine()
    engine.search_all_companies()
    
    # Filter by role
    cloud_jobs = engine.search_jobs(roles=["Cloud Engineer"])
    assert all("cloud engineer" in j.title.lower() for j in cloud_jobs)
    
    # Filter by city
    blr_jobs = engine.search_jobs(cities=["Bangalore"])
    assert all("bangalore" in j.city.lower() for j in blr_jobs)
    
    # Filter by work type
    remote_jobs = engine.search_jobs(work_types=["Remote"])
    assert all("remote" in j.work_type.lower() for j in remote_jobs)

    print("\n[3/5] Testing Filtering & Search...")
    print("✓ Filter by Role, City, Work Type")
    return True


def test_4_export():
    """Test 4: Export to JSON and CSV"""
    engine = JobSearchEngine()
    engine.search_all_companies()
    
    json_path = "test_jobs.json"
    csv_path = "test_jobs.csv"
    
    try:
        engine.export_to_json(json_path)
        assert os.path.exists(json_path)
        assert os.path.getsize(json_path) > 100
        
        engine.export_to_csv(csv_path)
        assert os.path.exists(csv_path)
        assert os.path.getsize(csv_path) > 100
        
        print("\n[4/5] Testing Export...")
        print("✓ Testing JSON Export")
        print("✓ Testing CSV Export")
    finally:
        if os.path.exists(json_path):
            os.remove(json_path)
        if os.path.exists(csv_path):
            os.remove(csv_path)
    return True


def test_5_summary_stats():
    """Test 5: Statistics generation"""
    engine = JobSearchEngine()
    engine.search_all_companies()
    summary = engine.get_summary()
    
    assert summary["total_jobs"] > 0
    assert summary["companies_searched"] >= 36
    assert summary["average_match_score"] > 0
    assert "Bangalore" in summary["by_city"] or len(summary["by_city"]) > 0

    print("\n[5/5] Testing Statistics...")
    print("✓ Generated Summary Statistics")
    return True


def run_all_tests():
    print("═" * 67)
    print("🔍 JOB SEARCH AGENT - COMPREHENSIVE TEST SUITE")
    print("═" * 67 + "\n")

    tests = [
        test_1_web_scraper,
        test_2_data_structure,
        test_3_filtering,
        test_4_export,
        test_5_summary_stats
    ]

    passed = 0
    for test in tests:
        if test():
            passed += 1

    print("\n" + "═" * 67)
    print("TEST SUMMARY")
    print("═" * 67)
    print(f"✓ Passed: {passed}/{len(tests)}")
    if passed == len(tests):
        print("🎉 All tests passed! Agent is ready to use.\n")
    else:
        print("⚠️ Some tests failed.\n")


if __name__ == "__main__":
    run_all_tests()
