import json
import re
from collections import Counter, defaultdict

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r':[a-z0-9_+-]+:', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_mad_dataset():
    with open('/home/agrim/CODES/Discourse-yashvi/yashvi_discourse_data.json', 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    replies = raw_data.get('replies', [])
    categories = raw_data.get('categories', {})

    mad_replies = []
    topics_map = defaultdict(lambda: {'count': 0, 'title': '', 'slug': '', 'course': '', 'theme': '', 'category': '', 'sample_replies': []})

    for r in replies:
        cid = str(r.get('category_id'))
        cinfo = categories.get(cid, {})
        cname = cinfo.get('name', '')
        title = r.get('title', '')
        excerpt = clean_html(r.get('excerpt', ''))
        text = (title + " " + excerpt).lower()

        # Check if MAD post
        is_mad = any(k in cname.lower() for k in ['mad', 'modern application']) or 'mad' in title.lower() or 'mad' in r.get('slug', '')
        if not is_mad:
            continue

        # Classify course: MAD 1 vs MAD 2
        if any(k in cname.lower() for k in ['mad2', 'mad-2', 'mad 2']) or any(k in title.lower() for k in ['mad2', 'mad-2', 'mad 2']) or any(k in text for k in ['vue', 'celery', 'redis', 'cors', 'jwt']):
            course = "MAD 2"
        else:
            course = "MAD 1"

        # Classify theme
        if any(k in text for k in ['viva', 'rubric', 'level 1', 'level 2', 'slot', 'booking', 'proctor', 'evaluat', 'marks', 'u grade', 'fail']):
            theme = "Viva, Rubrics & Evaluation"
        elif any(k in text for k in ['deadline', 'batch', 'milestone', 'date', 'late', 'submit', 'submission', 'portal', 'bootcamp', 'extend']):
            theme = "Milestones & Submissions"
        elif any(k in text for k in ['sqlite', 'sqlalchemy', 'database', 'table', 'db', 'model', 'schema', 'foreign key']):
            theme = "Database & SQLAlchemy"
        elif any(k in text for k in ['auth', 'login', 'jwt', 'role', 'admin', 'user', 'session', 'token', 'bcrypt', 'password']):
            theme = "Authentication & Security"
        elif any(k in text for k in ['celery', 'redis', 'background', 'task', 'beat', 'worker', 'cron', 'report', 'alert']):
            theme = "Celery, Redis & Async Jobs"
        elif any(k in text for k in ['vue', 'cors', 'axios', 'frontend', 'fetch', 'api', 'component', 'router', 'props']):
            theme = "Vue.js, Frontend & APIs"
        elif any(k in text for k in ['exam', 'quiz', 'end term', 'pyq', 'bonus', 'theory', 'oppe', 'mock']):
            theme = "Exams, Quizzes & Grades"
        else:
            theme = "General Project Guidance"

        item = {
            'post_id': r.get('post_id'),
            'topic_id': r.get('topic_id'),
            'post_number': r.get('post_number'),
            'title': title,
            'slug': r.get('slug', ''),
            'course': course,
            'category_name': cname,
            'theme': theme,
            'excerpt': excerpt,
            'created_at': r.get('created_at', ''),
            'url': f"https://discourse.onlinedegree.iitm.ac.in/t/{r.get('slug', 'topic')}/{r.get('topic_id')}/{r.get('post_number', 1)}"
        }
        mad_replies.append(item)

        t = topics_map[r.get('topic_id')]
        t['topic_id'] = r.get('topic_id')
        t['title'] = title
        t['slug'] = r.get('slug', '')
        t['course'] = course
        t['theme'] = theme
        t['category'] = cname
        t['count'] += 1
        t['url'] = f"https://discourse.onlinedegree.iitm.ac.in/t/{r.get('slug', 'topic')}/{r.get('topic_id')}"
        if len(t['sample_replies']) < 3 and excerpt:
            t['sample_replies'].append(excerpt)

    # Sort topics by volume
    top_topics = sorted(topics_map.values(), key=lambda x: x['count'], reverse=True)[:30]

    # Predefined curated Canned Responses & TA Playbook for future work
    canned_responses = [
        {
            "id": "viva_slots",
            "course": "MAD 1 & MAD 2",
            "title": "Viva Slot Booking (Slots Full / When do slots open?)",
            "trigger": "Viva slots, unable to book slot, all slots full",
            "response": "Viva booking slots typically open in phases (usually at 10:00 PM or 10:00 AM) and remain open until filled. If all slots are currently showing full, please do not panic — Course Instructors monitor slot capacity and announce additional slot releases on the official Announcement Google Space / Discourse. Keep notifications on and check back as announced.",
            "tips": ["Slots open in batches.", "Watch Announcement Google Space.", "No immediate penalty if waiting for newly released slots."]
        },
        {
            "id": "viva_deliverables",
            "course": "MAD 1 & MAD 2",
            "title": "Viva Deliverables & What to Submit",
            "trigger": "What to submit in viva portal, deliverables, report pdf",
            "response": "For the Viva evaluation, you must upload:\n1. Your complete project zip file (with requirements.txt and database file).\n2. Project Report PDF explaining architecture, models, routes, and screenshots.\n3. Screen-recording video link (Google Drive with 'Anyone with link can view' access) demonstrating all user and admin workflows.\n4. GitHub repository link with commit history demonstrating milestone development.",
            "tips": ["Ensure Drive link permissions are public.", "Verify checksum.py if applicable.", "Have both backend and frontend running locally before entering the Google Meet."]
        },
        {
            "id": "batch_eligibility",
            "course": "MAD 1 & MAD 2",
            "title": "Batch 1 vs Batch 2 Deadlines & Late Submission",
            "trigger": "Can I submit in Batch 2? Missed deadline, extension",
            "response": "Each term cycle has 2 designated project submission batches. If you miss the Batch 1 deadline, you are automatically eligible to submit in Batch 2 (typically scheduled around the final month of the term). You do not need to re-register for the course. Once the Batch 2 submission form opens on forms.study.iitm.ac.in, submit your repository and book your viva in the second slot window.",
            "tips": ["Batch 1 missed -> eligible for Batch 2.", "Check forms.study.iitm.ac.in.", "Maximum 2 batches per term cycle."]
        },
        {
            "id": "milestone_revert",
            "course": "MAD 1",
            "title": "Missed Milestone 0 Deadline / Commits on GitHub",
            "trigger": "Missed milestone 0, git commit revert, milestone marks",
            "response": "If you missed the Milestone 0 submission window, ensure your Milestone 0 changes are committed to your GitHub repository with a clear commit message. During the Level 1 viva, proctors inspect the commit timestamp. If you continued working, you can reference the specific commit_id corresponding to your Milestone 0 state. Note that a minor penalty (4-5 marks) may apply depending on proctor guidelines.",
            "tips": ["Commit timestamps on GitHub serve as proof.", "Do not delete or force-push over milestone commits.", "Explain the milestone commits clearly during Level 1 viva."]
        },
        {
            "id": "sqlite_sqlalchemy",
            "course": "MAD 1",
            "title": "SQLite3 vs SQLAlchemy in Project Requirements",
            "trigger": "Can I use raw sqlite3? Is SQLAlchemy compulsory?",
            "response": "Using SQLite3 directly is acceptable as long as your application satisfies all database and CRUD requirements. However, SQLAlchemy ORM is strongly recommended because it simplifies object-relational mapping, manages sessions cleanly, and prevents raw SQL syntax/injection bugs. SQLite3 is the underlying storage database file, while SQLAlchemy is the Python ORM layer interacting with it.",
            "tips": ["Both satisfy requirements.", "Store the .sqlite3 or .db file in the project root.", "Define clear foreign key relationships."]
        },
        {
            "id": "rbac_auth",
            "course": "MAD 1 & MAD 2",
            "title": "Role-Based Access Control (Admin vs User)",
            "trigger": "How to implement admin role, RBAC, user roles",
            "response": "To implement Role-Based Access Control (RBAC):\n1. In your User model, include a `role` field (e.g. `role = db.Column(db.String(20), default='user')`).\n2. In MAD 1 (Flask): Write a custom decorator (e.g. `@admin_required`) that inspects `session['role'] == 'admin'` and aborts with HTTP 403 Forbidden if not authorized.\n3. In MAD 2 (Vue + JWT): Ensure API endpoints verify user identity and claims from the JWT token, and the Vue router navigation guard (`router.beforeEach`) checks user role before allowing access to `/admin` views.",
            "tips": ["Always check roles on the backend API, not just frontend router.", "Never trust client-side role flags alone.", "Always hash passwords using Werkzeug or bcrypt."]
        },
        {
            "id": "celery_redis_setup",
            "course": "MAD 2",
            "title": "Celery Worker & Redis Setup for Daily Reminders",
            "trigger": "Celery beat not running, Redis connection refused, background tasks",
            "response": "For background tasks and daily scheduled alerts in MAD 2:\n1. Start your local Redis server: `redis-server` (ensure port 6379 is listening).\n2. Launch your Celery worker: `celery -A main.celery worker --loglevel=info`.\n3. Launch Celery Beat for scheduled daily reminders: `celery -A main.celery beat --loglevel=info`.\nEnsure your Celery configuration points to `redis://localhost:6379/0` for both broker and result backend.",
            "tips": ["Always start Redis before Celery.", "Use MailHog or an SMTP test server for local email verification.", "Ensure beat schedule timezone matches your local time."]
        },
        {
            "id": "vue_cors_api",
            "course": "MAD 2",
            "title": "CORS Error & Fetch API Integration in Vue",
            "trigger": "CORS blocked, Access-Control-Allow-Origin, Vue fetch error",
            "response": "If you encounter CORS errors when calling your Flask API from Vue:\n1. In your Flask backend: Install `flask-cors` and enable it: `from flask_cors import CORS; CORS(app, resources={r'/*': {'origins': '*'}})`. \n2. For authenticated requests: Ensure your Vue fetch/axios configuration includes `headers: { 'Authorization': `Bearer ${{token}}` }`.\n3. If handling cookies: Set `supports_credentials=True` in Flask CORS and `credentials: 'include'` in Vue fetch.",
            "tips": ["CORS is a browser security mechanism, test APIs in Postman first.", "Check preflight OPTIONS status code (should be 200).", "Store JWT token in localStorage/sessionStorage."]
        },
        {
            "id": "mock_bonus_criteria",
            "course": "MAD 1 & MAD 2",
            "title": "Bonus Marks & Mock Test Criteria",
            "trigger": "How to get bonus marks? Mock test criteria",
            "response": "For MAD courses, bonus marks (typically 5 marks) are awarded if your average across course mock tests exceeds the benchmark (e.g. average > 40/100 across specified tests). There are no separate course-specific activities beyond the announced mock assessments. Bonus marks are added to your final consolidated course score before grade boundaries are determined.",
            "tips": ["Attempt all scheduled mock tests.", "Check syllabus PDF for exact term benchmark.", "Added to final normalized score."]
        }
    ]

    # Troubleshooting / Common Error Matrix
    error_matrix = [
        {
            "course": "MAD 1",
            "error": "OperationalError: table has no column named ...",
            "cause": "Model was updated in SQLAlchemy, but SQLite schema was not migrated.",
            "solution": "Delete the local .sqlite3 file and re-run `db.create_all()`, or use Flask-Migrate to alter the table schema without data loss."
        },
        {
            "course": "MAD 1",
            "error": "HTTP 403 Forbidden on Admin Routes",
            "cause": "User is authenticated but role check failed in decorator.",
            "solution": "Verify session role payload upon login. Ensure database user record has `role='admin'` and decorator checks `session.get('role') == 'admin'`."
        },
        {
            "course": "MAD 2",
            "error": "CORS policy: No 'Access-Control-Allow-Origin' header is present",
            "cause": "Vue frontend on port 8080 calling Flask backend on port 5000 without CORS headers.",
            "solution": "Initialize `CORS(app)` in Flask application factory, or configure Vue devServer proxy in `vue.config.js`."
        },
        {
            "course": "MAD 2",
            "error": "ConnectionRefusedError: [Errno 111] Connect call failed ('127.0.0.1', 6379)",
            "cause": "Redis server is not running on the system.",
            "solution": "Run `redis-server` in a separate terminal or `sudo service redis-server start` before starting Celery workers."
        },
        {
            "course": "MAD 2",
            "error": "JWT Token Expired / 401 Unauthorized",
            "cause": "Access token lifetime elapsed without refresh token or re-login.",
            "solution": "Implement a router navigation guard in Vue (`router.beforeEach`) to intercept 401 responses and redirect the user to `/login`."
        },
        {
            "course": "MAD 1 & 2",
            "error": "All Viva Slots Full on Portal",
            "cause": "Slot demand exceeded initial release capacity.",
            "solution": "Wait for instructor announcement; additional slots are released in subsequent windows (typically 10 PM or 10 AM)."
        }
    ]

    # Course stats
    mad1_items = [r for r in mad_replies if r['course'] == 'MAD 1']
    mad2_items = [r for r in mad_replies if r['course'] == 'MAD 2']

    stats = {
        'total_mad_replies': len(mad_replies),
        'mad1_count': len(mad1_items),
        'mad2_count': len(mad2_items),
        'unique_topics': len(topics_map),
        'mad1_unique_topics': len(set(r['topic_id'] for r in mad1_items)),
        'mad2_unique_topics': len(set(r['topic_id'] for r in mad2_items)),
        'themes_distribution': dict(Counter(r['theme'] for r in mad_replies)),
        'mad1_themes': dict(Counter(r['theme'] for r in mad1_items)),
        'mad2_themes': dict(Counter(r['theme'] for r in mad2_items))
    }

    final_data = {
        'stats': stats,
        'canned_responses': canned_responses,
        'error_matrix': error_matrix,
        'top_topics': top_topics,
        'all_replies': mad_replies
    }

    with open('/home/agrim/CODES/Discourse-yashvi/mad_dashboard_data.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)

    print(f"MAD dataset processing complete! Total items: {len(mad_replies)} saved to mad_dashboard_data.json")
    return final_data

if __name__ == '__main__':
    process_mad_dataset()
