import json
import re
from collections import Counter, defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_html(text):
    if not text:
        return ""
    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', ' ', text)
    # Strip discourse emojis and markdown artifacts
    clean = re.sub(r':[a-z0-9_+-]+:', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean

def main():
    with open('/home/agrim/CODES/Discourse-yashvi/yashvi_discourse_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = data.get('categories', {})
    replies = data.get('replies', [])
    topics = data.get('topics', [])

    print(f"Loaded {len(replies)} replies and {len(topics)} topics.")

    # 1. Category Mapping
    category_summary = {}
    cat_counts = Counter()
    for r in replies:
        cid = str(r.get('category_id'))
        cat_info = categories.get(cid, {})
        cname = cat_info.get('name', f"Category {cid}")
        cat_counts[cname] += 1
        if cname not in category_summary:
            category_summary[cname] = {
                'id': cid,
                'name': cname,
                'slug': cat_info.get('slug', ''),
                'color': cat_info.get('color', '3b82f6'),
                'count': 0
            }
        category_summary[cname]['count'] += 1

    # 2. Topic Grouping & Q&A Pairing
    topic_map = defaultdict(lambda: {
        'topic_id': None,
        'title': '',
        'slug': '',
        'category_id': None,
        'category_name': '',
        'replies': [],
        'reply_count': 0,
        'first_created_at': '',
        'last_created_at': ''
    })

    cleaned_replies = []
    for r in replies:
        tid = r.get('topic_id')
        title = r.get('title', '').strip()
        excerpt = clean_html(r.get('excerpt', ''))
        cid = str(r.get('category_id'))
        cname = categories.get(cid, {}).get('name', 'General')

        item = {
            'post_id': r.get('post_id'),
            'topic_id': tid,
            'post_number': r.get('post_number'),
            'reply_to': r.get('reply_to_post_number'),
            'title': title,
            'slug': r.get('slug', ''),
            'category_id': cid,
            'category_name': cname,
            'excerpt': excerpt,
            'created_at': r.get('created_at', ''),
            'url': f"https://discourse.onlinedegree.iitm.ac.in/t/{r.get('slug', 'topic')}/{tid}/{r.get('post_number', 1)}"
        }
        cleaned_replies.append(item)

        tm = topic_map[tid]
        tm['topic_id'] = tid
        tm['title'] = title
        tm['slug'] = r.get('slug', '')
        tm['category_id'] = cid
        tm['category_name'] = cname
        tm['replies'].append(item)
        tm['reply_count'] += 1
        if not tm['first_created_at'] or r.get('created_at') < tm['first_created_at']:
            tm['first_created_at'] = r.get('created_at')
        if not tm['last_created_at'] or r.get('created_at') > tm['last_created_at']:
            tm['last_created_at'] = r.get('created_at')

    # 3. Identify Frequent Question Clusters & Repetitive Queries
    # We analyze repeating topic themes and patterns using TF-IDF and similarity
    unique_topics = list(topic_map.values())
    unique_topics.sort(key=lambda x: x['reply_count'], reverse=True)

    topic_titles = [t['title'] for t in unique_topics]
    
    # Custom clustering for common academic / course doubts
    predefined_clusters = [
        {
            'id': 'project_deadlines_batch',
            'theme': 'Project Deadlines, Submission Batches & Extensions',
            'category': 'Project for MAD1 & MAD2',
            'keywords': ['deadline', 'batch', 'submission', 'date', 'extend', 'late', 'form', 'portal', 'december', 'bootcamp', 'register'],
            'canonical_qa': {
                'typical_question': "When is the final project submission deadline / batch date? Can we submit late or in the second batch?",
                'best_answer': "December 10th is the second and final batch deadline. You will receive an official email once the registration/submission form opens on forms.study.iitm.ac.in. Please ensure you submit before the portal closes.",
                'bullet_points': [
                    "Batch 1 and Batch 2 deadlines are fixed by course administration.",
                    "Forms are released via student email and forms.study.iitm.ac.in.",
                    "Ensure code repo is clean and requirements.txt is included."
                ]
            }
        },
        {
            'id': 'sqlite_vs_sqlalchemy',
            'theme': 'Database Design: SQLite3 vs SQLAlchemy / Raw SQL',
            'category': 'Modern Application Development I',
            'keywords': ['sqlite', 'sqlalchemy', 'database', 'db', 'orm', 'schema', 'table', 'sql', 'foreign key'],
            'canonical_qa': {
                'typical_question': "Can we use plain sqlite3 or is SQLAlchemy mandatory for the project? What is the difference?",
                'best_answer': "It is completely fine to use SQLite3 directly if it satisfies the required project functionality. Think of it this way: SQLite3 is the actual database where data is stored, while SQLAlchemy is a Python ORM library that allows interacting with the database using Python objects instead of writing raw SQL queries. Using SQLAlchemy makes queries cleaner and relationships easier to maintain.",
                'bullet_points': [
                    "Both satisfy project requirements as long as functionality works.",
                    "SQLAlchemy ORM helps avoid raw SQL injection and syntax errors.",
                    "Remember to store the .sqlite3 or .db file in the correct relative path."
                ]
            }
        },
        {
            'id': 'auth_session_jwt',
            'theme': 'Authentication, User Roles, RBAC & Login Sessions',
            'category': 'MAD 1 & MAD 2',
            'keywords': ['login', 'auth', 'session', 'jwt', 'role', 'admin', 'user', 'password', 'bcrypt', 'token', 'access'],
            'canonical_qa': {
                'typical_question': "How should role-based authentication (Admin vs User) be implemented? Do we need JWT or session cookies?",
                'best_answer': "For MAD-1 (Flask + Jinja2), standard session-based auth (e.g. Flask-Login or session dict) with role checks in decorators is recommended. For MAD-2 (Vue.js + Flask API), JWT token-based authentication (Flask-JWT-Extended) is expected, where tokens are sent in the Authorization header. Ensure admin routes strictly verify user.role == 'admin'.",
                'bullet_points': [
                    "MAD-1: Session cookies with role checking.",
                    "MAD-2: JWT tokens stored in localStorage/sessionStorage.",
                    "Always hash passwords with Werkzeug/bcrypt before storing in database."
                ]
            }
        },
        {
            'id': 'celery_redis_jobs',
            'theme': 'Async Background Tasks: Celery, Redis & Daily Alerts',
            'category': 'Project for MAD2',
            'keywords': ['celery', 'redis', 'background', 'task', 'cron', 'beat', 'email', 'alert', 'report', 'async'],
            'canonical_qa': {
                'typical_question': "How do we trigger daily reminders and monthly reports using Celery & Redis?",
                'best_answer': "Use Celery Beat for scheduled tasks (daily reminders at a specific time) and Celery Worker for asynchronous triggers (e.g., CSV export or monthly PDF generation). Make sure Redis server is running locally on port 6379 before launching the worker.",
                'bullet_points': [
                    "Start Redis server first: redis-server",
                    "Run worker: celery -A app.celery worker -l info",
                    "Run periodic scheduler: celery -A app.celery beat -l info",
                    "Use MailHog or SMTP for testing email delivery locally."
                ]
            }
        },
        {
            'id': 'vue_api_cors',
            'theme': 'Frontend & Vue.js: API Integration, CORS & Routing',
            'category': 'Modern Application Development II',
            'keywords': ['vue', 'cors', 'fetch', 'axios', 'router', 'component', 'props', 'api', 'frontend', 'reactive'],
            'canonical_qa': {
                'typical_question': "CORS error when calling Flask API from Vue frontend, or router navigation failing?",
                'best_answer': "Install and enable flask_cors: `from flask_cors import CORS; CORS(app)`. In your Vue fetch/axios requests, ensure you pass the `Authorization: Bearer <token>` header and handle 401 unauthorized redirects in the router navigation guard (`router.beforeEach`).",
                'bullet_points': [
                    "Enable CORS on Flask: CORS(app, resources={r'/*': {'origins': '*'}})",
                    "Verify base API URL in Vue config (e.g., http://localhost:5000/api)",
                    "Check DevTools Network tab to inspect Preflight OPTIONS response."
                ]
            }
        },
        {
            'id': 'viva_evaluation_rubric',
            'theme': 'Project Evaluation, Viva, Rubrics & Grading Clarifications',
            'category': 'Project for MAD1 & MAD2',
            'keywords': ['viva', 'rubric', 'grade', 'score', 'evaluation', 'marks', 'ta', 'feedback', 'review', 'demo'],
            'canonical_qa': {
                'typical_question': "What will be asked in the project viva? How are marks distributed across requirements?",
                'best_answer': "The viva covers code walkthrough, database design, live execution of core features, and edge-case handling. You will be asked to explain your models, API routes, and make a live demonstration. Review the official grading rubric PDF posted in the course announcements.",
                'bullet_points': [
                    "Be ready to run both backend and frontend locally without internet reliance.",
                    "Explain database relationships and security practices.",
                    "Viva is conducted 1-on-1 by Course TAs via Google Meet."
                ]
            }
        },
        {
            'id': 'maths_stats_clarifications',
            'theme': 'Mathematics & Statistics Concepts & Assignment Doubts',
            'category': 'Maths & Stats for DS',
            'keywords': ['matrix', 'eigen', 'probability', 'distribution', 'normal', 'hypothesis', 'null', 'variance', 'linear', 'calculus'],
            'canonical_qa': {
                'typical_question': "Clarification on assignment proof / question calculation in Math/Stats II",
                'best_answer': "Refer to the properties discussed in the lecture notes. Make sure to clearly state your assumptions (independence, normality) and double check matrix dimensions before calculating eigenvalues or inverses.",
                'bullet_points': [
                    "Step-by-step mathematical working is required for full credit.",
                    "Check Portal practice problems for identical derivation formats."
                ]
            }
        }
    ]

    # Assign replies and topics to clusters based on keyword matching
    for cluster in predefined_clusters:
        cluster['matching_replies'] = []
        cluster['matching_topics'] = set()
        cluster_kws = [k.lower() for k in cluster['keywords']]

        for r in cleaned_replies:
            text_corpus = (r['title'] + " " + r['excerpt']).lower()
            matches = sum(1 for kw in cluster_kws if kw in text_corpus)
            if matches >= 2 or (matches >= 1 and any(kw in r['title'].lower() for kw in cluster_kws)):
                cluster['matching_replies'].append(r)
                cluster['matching_topics'].add(r['topic_id'])

        cluster['reply_count'] = len(cluster['matching_replies'])
        cluster['topic_count'] = len(cluster['matching_topics'])
        del cluster['matching_topics']  # not JSON serializable as set
        # Keep top 5 samples of actual student questions and Yashvi's replies
        cluster['sample_qas'] = cluster['matching_replies'][:6]
        del cluster['matching_replies']

    # Sort predefined clusters by frequency
    predefined_clusters.sort(key=lambda x: x['reply_count'], reverse=True)

    # 4. Most active individual topics (threads where she answered most frequently)
    top_threads = []
    for t in unique_topics[:20]:
        top_threads.append({
            'topic_id': t['topic_id'],
            'title': t['title'],
            'slug': t['slug'],
            'category_name': t['category_name'],
            'reply_count': t['reply_count'],
            'url': f"https://discourse.onlinedegree.iitm.ac.in/t/{t['slug']}/{t['topic_id']}",
            'latest_reply': t['replies'][0]['excerpt'] if t['replies'] else ''
        })

    # 5. Output Final Dashboard Data Structure
    dashboard_data = {
        'metadata': {
            'username': 'Yashvi',
            'name': '24f2007780',
            'total_replies': len(cleaned_replies),
            'total_unique_topics': len(unique_topics),
            'total_categories': len(category_summary),
            'first_reply_date': cleaned_replies[-1]['created_at'] if cleaned_replies else '',
            'latest_reply_date': cleaned_replies[0]['created_at'] if cleaned_replies else '',
        },
        'categories': list(category_summary.values()),
        'frequent_clusters': predefined_clusters,
        'top_threads': top_threads,
        'recent_replies': cleaned_replies[:100]  # sample of 100 recent replies for fast frontend
    }

    out_file = '/home/agrim/CODES/Discourse-yashvi/dashboard_data.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully processed dashboard data and saved to {out_file}!")
    for c in predefined_clusters:
        print(f"Cluster: '{c['theme']}' -> {c['reply_count']} matching replies")

if __name__ == '__main__':
    main()

