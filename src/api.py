import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Safe encoding for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from src.job_searcher import JobSearchEngine, FORTUNE_500_COMPANIES, INDIAN_PRODUCT_COMPANIES
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Initialize job search engine
engine = JobSearchEngine()

@app.route('/')
@app.route('/dashboard')
def dashboard():
    """Serves the interactive web dashboard"""
    dashboard_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dashboard', 'index.html'))
    if os.path.exists(dashboard_file):
        return send_file(dashboard_file)
    return "Dashboard file not found", 404

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "companies_available": len(FORTUNE_500_COMPANIES) + len(INDIAN_PRODUCT_COMPANIES)
    })

@app.route('/api/refresh', methods=['GET', 'POST'])
def refresh_jobs():
    """Forces real-time re-scraping of live jobs from portals"""
    try:
        jobs = engine.search_all_companies(force_refresh=True)
        return jsonify({
            "success": True,
            "message": f"Successfully scraped {len(jobs)} live jobs across {len(set(j.company for j in jobs))} companies.",
            "total": len(jobs)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/search', methods=['POST'])
def search_jobs():
    """Search for jobs with filters"""
    try:
        data = request.get_json() or {}
        
        roles = data.get('roles')
        cities = data.get('cities')
        work_types = data.get('work_types')
        min_salary = data.get('min_salary')
        source = data.get('source')
        
        # Perform search
        jobs = engine.search_all_companies()
        filtered_jobs = engine.search_jobs(
            roles=roles,
            cities=cities,
            work_types=work_types,
            min_salary=min_salary
        )

        if source:
            filtered_jobs = [j for j in filtered_jobs if source.lower() in getattr(j, 'source', '').lower()]
        
        # Format response
        jobs_data = [
            {
                "id": job.job_id,
                "title": job.title,
                "company": job.company,
                "company_type": job.company_type,
                "location": job.location,
                "city": job.city,
                "work_type": job.work_type,
                "salary": job.salary_range,
                "description": job.description,
                "requirements": job.requirements,
                "benefits": job.benefits,
                "experience_level": job.experience_level,
                "application_url": job.application_url,
                "source": getattr(job, "source", "Live Portal"),
                "match_score": round(job.match_score * 100),
                "posted_date": job.posted_date
            }
            for job in filtered_jobs
        ]
        
        return jsonify({
            "success": True,
            "total": len(jobs_data),
            "jobs": jobs_data,
            "summary": engine.get_summary()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """Get all jobs (with optional filters)"""
    try:
        # Get query parameters
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        city = request.args.get('city')
        role = request.args.get('role')
        work_type = request.args.get('work_type')
        
        # Filter jobs
        jobs = engine.jobs
        
        if city:
            jobs = [j for j in jobs if j.city.lower() == city.lower()]
        
        if role:
            jobs = [j for j in jobs if role.lower() in j.title.lower()]
        
        if work_type:
            jobs = [j for j in jobs if j.work_type.lower() == work_type.lower()]
        
        # Paginate
        start = (page - 1) * per_page
        end = start + per_page
        paginated_jobs = jobs[start:end]
        
        return jsonify({
            "success": True,
            "page": page,
            "per_page": per_page,
            "total": len(jobs),
            "jobs": [
                {
                    "id": job.job_id,
                    "title": job.title,
                    "company": job.company,
                    "city": job.city,
                    "work_type": job.work_type,
                    "match_score": round(job.match_score * 100)
                }
                for job in paginated_jobs
            ]
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/api/jobs/<job_id>', methods=['GET'])
def get_job_detail(job_id):
    """Get detailed job information"""
    try:
        job = next((j for j in engine.jobs if j.job_id == job_id), None)
        
        if not job:
            return jsonify({"success": False, "error": "Job not found"}), 404
        
        return jsonify({
            "success": True,
            "job": {
                "id": job.job_id,
                "title": job.title,
                "company": job.company,
                "company_type": job.company_type,
                "location": job.location,
                "city": job.city,
                "state": job.state,
                "work_type": job.work_type,
                "salary": job.salary_range,
                "description": job.description,
                "requirements": job.requirements,
                "benefits": job.benefits,
                "experience_level": job.experience_level,
                "application_url": job.application_url,
                "match_score": round(job.match_score * 100),
                "posted_date": job.posted_date,
                "posted_at": job.scraped_at
            }
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get search statistics"""
    try:
        summary = engine.get_summary()
        
        return jsonify({
            "success": True,
            "stats": summary
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/api/cities', methods=['GET'])
def get_cities():
    """Get list of cities with job counts"""
    try:
        cities = {}
        for job in engine.jobs:
            cities[job.city] = cities.get(job.city, 0) + 1
        
        sorted_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
        
        return jsonify({
            "success": True,
            "cities": [{"city": city, "count": count} for city, count in sorted_cities]
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/api/companies', methods=['GET'])
def get_companies():
    """Get list of companies with job counts"""
    try:
        companies = {}
        for job in engine.jobs:
            companies[job.company] = companies.get(job.company, 0) + 1
        
        sorted_companies = sorted(companies.items(), key=lambda x: x[1], reverse=True)
        
        return jsonify({
            "success": True,
            "companies": [{"company": company, "count": count} for company, count in sorted_companies]
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

if __name__ == '__main__':
    # Pre-load jobs
    print("🔄 Loading jobs from all companies...")
    engine.search_all_companies()
    print(f"✅ Loaded {len(engine.jobs)} jobs")
    
    # Start Flask server
    app.run(debug=True, port=5000)
