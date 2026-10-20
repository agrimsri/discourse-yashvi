import json

def build_html():
    with open('/home/agrim/CODES/Discourse-yashvi/mad_dashboard_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    json_str = json.dumps(data)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Yashvi's MAD 1 & 2 Teaching & Q&A Studio</title>
  
  <!-- Clean, Modern, Elegant Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    :root {{
      --font-sans: 'Poppins', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-display: 'Outfit', 'Poppins', sans-serif;
      --font-mono: 'Fira Code', monospace;
      
      --bg-main: #fcf8fa;
      --card-bg: #ffffff;
      --card-border: rgba(244, 114, 182, 0.14);
      --card-border-hover: rgba(244, 114, 182, 0.35);
      --text-heading: #19121b;
      --text-body: #49414d;
      --text-muted: #827787;
      
      --primary-rose: #f43f5e;
      --primary-pink: #ec4899;
      --badge-mad1: #e11d48;
      --badge-mad1-bg: #fff1f2;
      --badge-mad2: #0284c7;
      --badge-mad2-bg: #f0f9ff;
      
      --shadow-subtle: 0 4px 20px -2px rgba(0, 0, 0, 0.025), 0 2px 6px -1px rgba(244, 114, 182, 0.035);
      --shadow-hover: 0 12px 28px -4px rgba(244, 114, 182, 0.09), 0 4px 10px -2px rgba(0, 0, 0, 0.025);
    }}

    .dark {{
      --bg-main: #0f172a;
      --card-bg: #1e293b;
      --card-border: rgba(244, 114, 182, 0.2);
      --card-border-hover: rgba(244, 114, 182, 0.4);
      --text-heading: #f8fafc;
      --text-body: #cbd5e1;
      --text-muted: #94a3b8;
      --badge-mad1-bg: rgba(225, 29, 72, 0.15);
      --badge-mad2-bg: rgba(2, 132, 199, 0.15);
      --shadow-subtle: 0 4px 20px -2px rgba(0, 0, 0, 0.25);
      --shadow-hover: 0 12px 28px -4px rgba(0, 0, 0, 0.35);
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-main);
      color: var(--text-body);
      background-image: 
        radial-gradient(at 0% 0%, rgba(254, 226, 226, 0.4) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(252, 231, 243, 0.4) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(240, 249, 255, 0.4) 0px, transparent 60%);
      background-attachment: fixed;
    }}

    .font-display {{
      font-family: var(--font-display);
    }}
    .font-mono-code {{
      font-family: var(--font-mono);
    }}

    .clean-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      box-shadow: var(--shadow-subtle);
      border-radius: 1.25rem;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .clean-card:hover {{
      border-color: var(--card-border-hover);
      box-shadow: var(--shadow-hover);
      transform: translateY(-2px);
    }}

    .clean-card-static {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      box-shadow: var(--shadow-subtle);
      border-radius: 1.25rem;
    }}

    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #fbcfe8;
      border-radius: 10px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #f472b6;
    }}
  </style>
</head>
<body class="antialiased min-h-screen selection:bg-pink-100 selection:text-pink-900">

  <!-- MAIN WRAPPER -->
  <div class="max-w-6xl mx-auto px-6 py-12 md:py-16 space-y-12">

    <!-- HERO HEADER -->
    <header class="clean-card-static p-8 md:p-9 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
      <div class="flex items-center gap-5">
        <div class="w-16 h-16 md:w-18 md:h-18 rounded-2xl bg-gradient-to-tr from-rose-400 via-pink-400 to-sky-300 text-white flex items-center justify-center font-bold text-2xl shadow-sm flex-shrink-0">
          🌸
        </div>

        <div class="space-y-1.5">
          <div class="flex flex-wrap items-center gap-2.5">
            <h1 class="text-2xl md:text-3xl font-bold tracking-tight text-[var(--text-heading)] font-display">
              Yashvi's MAD 1 & 2 Teaching Hub
            </h1>
            <span class="px-3 py-0.5 text-xs font-semibold rounded-full bg-rose-50 text-rose-600 border border-rose-100">
              Modern App Dev Specialization
            </span>
          </div>
          <p class="text-xs md:text-sm text-[var(--text-muted)] font-normal">
            Author: <span class="font-mono bg-pink-50/70 text-gray-800 px-2 py-0.5 rounded text-xs border border-pink-100">24f2007780 / Yashvi</span> • Dedicated Archive & Future TA Workstation
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex flex-wrap items-center gap-2.5 w-full md:w-auto">
        <button onclick="toggleTheme()" id="theme-toggle-btn" class="px-3 py-2 rounded-xl text-xs font-medium text-[var(--text-muted)] hover:text-[var(--text-heading)] hover:bg-pink-50/50 border border-transparent hover:border-pink-100 transition flex items-center gap-1.5" title="Toggle theme">
          <span id="theme-icon">🌙</span>
        </button>

        <a href="https://discourse.onlinedegree.iitm.ac.in/u/Yashvi" target="_blank" class="px-4 py-2 rounded-xl text-xs font-medium text-[var(--text-body)] hover:text-rose-600 bg-white border border-gray-200/70 hover:border-pink-200 transition shadow-sm flex items-center gap-1.5">
          <span>🌐 Discourse Profile</span>
        </a>

        <button onclick="exportDataJson()" class="px-4 py-2 rounded-xl text-xs font-semibold bg-rose-500 hover:bg-rose-600 text-white transition shadow-sm flex items-center gap-1.5">
          <span>📥 Export MAD Dataset</span>
        </button>
      </div>
    </header>

    <!-- KEY STATS FOR MAD 1 & MAD 2 -->
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-5">
      <!-- Total MAD Answers -->
      <div class="clean-card p-5 md:p-6 space-y-1.5">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Total MAD Answers</span>
        <div class="text-3xl font-extrabold text-[var(--text-heading)] font-display" id="total-mad-count">1,197</div>
        <div class="text-xs font-medium text-rose-500 flex items-center gap-1">
          <span>🔥 78.6% of all forum posts</span>
        </div>
      </div>

      <!-- MAD 1 Posts -->
      <div class="clean-card p-5 md:p-6 space-y-1.5">
        <div class="flex justify-between items-center">
          <span class="text-xs font-semibold uppercase tracking-wider text-rose-600">MAD 1 Posts</span>
          <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-50 text-rose-600 border border-rose-100">Python + Flask</span>
        </div>
        <div class="text-3xl font-extrabold text-[var(--text-heading)] font-display" id="mad1-count">890</div>
        <div class="text-xs text-[var(--text-muted)]">Projects, Lab Assgns, Viva</div>
      </div>

      <!-- MAD 2 Posts -->
      <div class="clean-card p-5 md:p-6 space-y-1.5">
        <div class="flex justify-between items-center">
          <span class="text-xs font-semibold uppercase tracking-wider text-sky-600">MAD 2 Posts</span>
          <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-50 text-sky-600 border border-sky-100">Vue + Celery + Redis</span>
        </div>
        <div class="text-3xl font-extrabold text-[var(--text-heading)] font-display" id="mad2-count">307</div>
        <div class="text-xs text-[var(--text-muted)]">SPAs, APIs, Async Tasks</div>
      </div>

      <!-- Distinct Discussion Threads -->
      <div class="clean-card p-5 md:p-6 space-y-1.5">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Distinct Doubts Solved</span>
        <div class="text-3xl font-extrabold text-[var(--text-heading)] font-display" id="mad-threads-count">669</div>
        <div class="text-xs text-emerald-600 font-medium">Across all term milestones</div>
      </div>
    </section>

    <!-- ARCHITECTURE & TECH STACK COMPARISON (MAD 1 vs MAD 2) -->
    <section class="clean-card-static p-7 md:p-8 space-y-6">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 border-b border-gray-100 pb-4">
        <div>
          <h2 class="text-lg font-bold text-[var(--text-heading)] font-display">
            Course Tech Stack & Evaluation Paradigm
          </h2>
          <p class="text-xs text-[var(--text-muted)] mt-0.5">
            Key architectural differences between MAD 1 and MAD 2 that dictate student queries.
          </p>
        </div>
        <div class="flex items-center gap-2">
          <span class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-rose-50 text-rose-700 border border-rose-100">Server-Side (MAD 1)</span>
          <span class="text-gray-300">vs</span>
          <span class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-sky-50 text-sky-700 border border-sky-100">Client-Side SPA (MAD 2)</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- MAD 1 Card -->
        <div class="p-5 rounded-2xl bg-rose-50/30 border border-rose-100/70 space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-sm font-bold text-rose-700 font-display">Modern Application Development I (MAD 1)</span>
            <span class="text-[11px] font-semibold text-rose-600 bg-white px-2 py-0.5 rounded border border-rose-100">890 Replies</span>
          </div>
          <p class="text-xs text-[var(--text-body)] leading-relaxed">
            Focuses on classical server-side rendered monolithic web apps with Python Flask, Jinja2 templates, and SQLite/SQLAlchemy.
          </p>
          <div class="space-y-1.5 pt-2 border-t border-rose-100 text-xs">
            <div class="flex items-center gap-2"><span class="text-rose-500 font-bold">• Backend:</span> <span>Python, Flask, Jinja2 template inheritance</span></div>
            <div class="flex items-center gap-2"><span class="text-rose-500 font-bold">• Database:</span> <span>SQLite3 file with SQLAlchemy ORM models</span></div>
            <div class="flex items-center gap-2"><span class="text-rose-500 font-bold">• Auth:</span> <span>Flask-Login or Session cookies with role flags</span></div>
            <div class="flex items-center gap-2"><span class="text-rose-500 font-bold">• Top Inquiries:</span> <span>Milestone 0 git commits, SQLite vs SQLAlchemy, Viva slots</span></div>
          </div>
        </div>

        <!-- MAD 2 Card -->
        <div class="p-5 rounded-2xl bg-sky-50/30 border border-sky-100/70 space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-sm font-bold text-sky-700 font-display">Modern Application Development II (MAD 2)</span>
            <span class="text-[11px] font-semibold text-sky-600 bg-white px-2 py-0.5 rounded border border-sky-100">307 Replies</span>
          </div>
          <p class="text-xs text-[var(--text-body)] leading-relaxed">
            Modern Single Page Application (SPA) architecture with decoupled Vue.js frontend, REST APIs, asynchronous Celery workers, and Redis caching.
          </p>
          <div class="space-y-1.5 pt-2 border-t border-sky-100 text-xs">
            <div class="flex items-center gap-2"><span class="text-sky-600 font-bold">• Frontend:</span> <span>Vue 3 / Vue CLI, Vue Router, Fetch/Axios</span></div>
            <div class="flex items-center gap-2"><span class="text-sky-600 font-bold">• API & Auth:</span> <span>Flask-RESTful endpoints + JWT Bearer token authentication</span></div>
            <div class="flex items-center gap-2"><span class="text-sky-600 font-bold">• Async & Cache:</span> <span>Celery Worker & Celery Beat + Redis server on port 6379</span></div>
            <div class="flex items-center gap-2"><span class="text-sky-600 font-bold">• Top Inquiries:</span> <span>CORS errors, Redis connection refused, Level 2 viva results</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- NAVIGATION TABS -->
    <nav class="flex flex-wrap gap-2 p-1.5 bg-pink-100/30 rounded-2xl border border-pink-100/60 text-xs md:text-sm font-medium">
      <button onclick="switchTab('canned')" id="tab-btn-canned" class="px-4 py-2 rounded-xl bg-white text-rose-600 shadow-sm transition flex items-center gap-2 font-semibold">
        <span>⚡ TA Quick-Reply Bank</span>
        <span class="px-1.5 py-0.2 rounded-full text-[10px] bg-rose-50 text-rose-600 font-bold">10 Ready</span>
      </button>
      <button onclick="switchTab('roadmap')" id="tab-btn-roadmap" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>🗺️ Term Milestone Playbook</span>
      </button>
      <button onclick="switchTab('errors')" id="tab-btn-errors" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>🛠️ Debugging & Error Matrix</span>
      </button>
      <button onclick="switchTab('explorer')" id="tab-btn-explorer" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>🔍 Search All 1,197 Answers</span>
      </button>
      <button onclick="switchTab('scratchpad')" id="tab-btn-scratchpad" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>📝 TA Scratchpad & Notes</span>
      </button>
    </nav>

    <!-- TAB 1: TA FAST-REPLY BANK (1-Click Verified Canned Answers) -->
    <main id="tab-canned" class="space-y-6">
      <div class="clean-card-static p-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h2 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display flex items-center gap-2">
            <span>⚡</span> Canned Response Bank for Future TA Work
          </h2>
          <p class="text-xs md:text-sm text-[var(--text-muted)] mt-1 max-w-2xl leading-relaxed">
            Yashvi can use these verified response templates during active term cycles to answer repeating student queries with a single click.
          </p>
        </div>
        <!-- Filter pills for Canned Responses -->
        <div class="flex items-center gap-1.5 text-xs">
          <button onclick="filterCanned('ALL')" class="canned-filter-btn px-3 py-1 rounded-lg bg-rose-50 text-rose-600 font-semibold border border-rose-200">All</button>
          <button onclick="filterCanned('MAD 1')" class="canned-filter-btn px-3 py-1 rounded-lg bg-white text-gray-600 hover:bg-gray-50 border border-gray-200">MAD 1</button>
          <button onclick="filterCanned('MAD 2')" class="canned-filter-btn px-3 py-1 rounded-lg bg-white text-gray-600 hover:bg-gray-50 border border-gray-200">MAD 2</button>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-5" id="canned-container">
        <!-- Rendered via JS -->
      </div>
    </main>

    <!-- TAB 2: TERM MILESTONE PLAYBOOK (Roadmap of Doubts) -->
    <section id="tab-roadmap" class="hidden space-y-6">
      <div class="clean-card-static p-7 space-y-6">
        <div>
          <h2 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display">
            Term-Cycle Milestone Roadmap (MAD 1 & MAD 2)
          </h2>
          <p class="text-xs md:text-sm text-[var(--text-muted)] mt-1">
            Student questions follow a predictable 12-week lifecycle each term. Here is what students ask at each milestone and how to handle them.
          </p>
        </div>

        <div class="space-y-6">
          <!-- Phase 1 -->
          <div class="p-5 rounded-2xl bg-white border border-gray-100 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-rose-600 uppercase tracking-wider font-mono">Weeks 1 – 3 • Phase 1</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-pink-50 text-rose-700">Milestone 0: Project Statement & DB Schema</span>
            </div>
            <h3 class="text-sm font-bold text-[var(--text-heading)]">Common Doubts: Checksum.py, DB Setup & Milestone 0 Deadlines</h3>
            <p class="text-xs text-[var(--text-body)] leading-relaxed">
              Students ask if SQLite3 is mandatory vs SQLAlchemy, where to place checksum.py, and what to do if they miss Milestone 0.
            </p>
            <div class="bg-gray-50 p-3 rounded-xl text-xs text-[var(--text-muted)] space-y-1">
              <div><b>TA Tip:</b> Advise them to commit Milestone 0 schema changes with a clear git commit message. Revert can be proven via commit timestamp.</div>
            </div>
          </div>

          <!-- Phase 2 -->
          <div class="p-5 rounded-2xl bg-white border border-gray-100 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-amber-600 uppercase tracking-wider font-mono">Weeks 4 – 7 • Phase 2</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-amber-50 text-amber-700">Milestone 1: Core CRUD & Authentication</span>
            </div>
            <h3 class="text-sm font-bold text-[var(--text-heading)]">Common Doubts: RBAC, Session Cookies (MAD 1), JWT & CORS (MAD 2)</h3>
            <p class="text-xs text-[var(--text-body)] leading-relaxed">
              In MAD 1: Jinja template inheritance and Flask session handling. In MAD 2: CORS issues connecting Vue on port 8080 to Flask on 5000, storing JWT tokens in localStorage.
            </p>
            <div class="bg-gray-50 p-3 rounded-xl text-xs text-[var(--text-muted)] space-y-1">
              <div><b>TA Tip:</b> Provide the standard `flask_cors` setup snippet and ensure students check that user roles are enforced in backend decorators.</div>
            </div>
          </div>

          <!-- Phase 3 -->
          <div class="p-5 rounded-2xl bg-white border border-gray-100 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-sky-600 uppercase tracking-wider font-mono">Weeks 8 – 9 • Phase 3</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-sky-50 text-sky-700">Milestone 2: Async Workers & Caching (MAD 2)</span>
            </div>
            <h3 class="text-sm font-bold text-[var(--text-heading)]">Common Doubts: Celery Beat not firing, Redis refused, PDF generation</h3>
            <p class="text-xs text-[var(--text-body)] leading-relaxed">
              Students struggle with Redis installation on Windows/WSL, running separate worker and beat terminals, and setting up MailHog for daily reminder email alerts.
            </p>
            <div class="bg-gray-50 p-3 rounded-xl text-xs text-[var(--text-muted)] space-y-1">
              <div><b>TA Tip:</b> Remind them that Redis must run on port 6379, and worker must be launched before beat scheduler.</div>
            </div>
          </div>

          <!-- Phase 4 -->
          <div class="p-5 rounded-2xl bg-white border border-gray-100 shadow-sm space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider font-mono">Weeks 10 – 12 • Phase 4</span>
              <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-emerald-50 text-emerald-700">Final Submissions & Level 1 / Level 2 Vivas</span>
            </div>
            <h3 class="text-sm font-bold text-[var(--text-heading)]">Common Doubts: Batch 1 vs Batch 2 forms, Viva slot booking, Drive links</h3>
            <p class="text-xs text-[var(--text-body)] leading-relaxed">
              High volume period! Over 50% of questions are "slots are full", "can I submit in Batch 2", and "what does proctor check in Level 2 viva".
            </p>
            <div class="bg-gray-50 p-3 rounded-xl text-xs text-[var(--text-muted)] space-y-1">
              <div><b>TA Tip:</b> Use the pre-composed Viva Deliverable and Batch 2 response templates to answer quickly.</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TAB 3: DEBUGGING & ERROR MATRIX -->
    <section id="tab-errors" class="hidden space-y-6">
      <div class="clean-card-static p-7 space-y-5">
        <div>
          <h2 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display">
            Common MAD Bugs & Troubleshooting Matrix
          </h2>
          <p class="text-xs md:text-sm text-[var(--text-muted)] mt-1">
            Direct diagnosis and recommended solutions for the top technical errors students report on Discourse.
          </p>
        </div>

        <div class="space-y-4" id="error-matrix-container">
          <!-- Rendered via JS -->
        </div>
      </div>
    </section>

    <!-- TAB 4: COMPLETE SEARCHABLE ARCHIVE OF 1,197 ANSWERS -->
    <section id="tab-explorer" class="hidden space-y-6">
      <div class="clean-card-static p-5 space-y-4">
        <div class="flex flex-col md:flex-row gap-3 justify-between items-center">
          <div class="relative w-full md:w-96">
            <span class="absolute left-3.5 top-2.5 text-gray-400 text-xs">🔍</span>
            <input type="text" id="mad-search" oninput="filterMadReplies()" placeholder="Search answers (viva, batch, sqlite, celery)..." class="w-full bg-[var(--card-bg)] border border-gray-200/80 rounded-xl pl-9 pr-4 py-2 text-xs md:text-sm text-[var(--text-heading)] placeholder-gray-400 focus:outline-none focus:border-rose-400 focus:ring-1 focus:ring-rose-400 transition" />
          </div>

          <div class="flex flex-wrap items-center gap-2 w-full md:w-auto text-xs">
            <!-- Course Filter -->
            <select id="mad-course-filter" onchange="filterMadReplies()" class="bg-[var(--card-bg)] border border-gray-200/80 rounded-xl px-3 py-2 font-medium text-[var(--text-body)] focus:outline-none focus:border-rose-400 cursor-pointer shadow-sm">
              <option value="ALL">All Courses (MAD 1 & 2)</option>
              <option value="MAD 1">MAD 1 (890)</option>
              <option value="MAD 2">MAD 2 (307)</option>
            </select>

            <!-- Theme Filter -->
            <select id="mad-theme-filter" onchange="filterMadReplies()" class="bg-[var(--card-bg)] border border-gray-200/80 rounded-xl px-3 py-2 font-medium text-[var(--text-body)] focus:outline-none focus:border-rose-400 cursor-pointer shadow-sm">
              <option value="ALL">All Themes</option>
              <option value="Milestones & Submissions">Milestones & Submissions (380)</option>
              <option value="Viva, Rubrics & Evaluation">Viva, Rubrics & Evaluation (366)</option>
              <option value="General Project Guidance">General Project Guidance (268)</option>
              <option value="Authentication & Security">Authentication & Security (66)</option>
              <option value="Database & SQLAlchemy">Database & SQLAlchemy (49)</option>
              <option value="Exams, Quizzes & Grades">Exams, Quizzes & Grades (45)</option>
              <option value="Celery, Redis & Async Jobs">Celery & Redis (16)</option>
              <option value="Vue.js, Frontend & APIs">Vue.js & Frontend (7)</option>
            </select>
          </div>
        </div>

        <div class="text-xs text-[var(--text-muted)] flex justify-between items-center px-1">
          <span id="results-count">Showing 1,197 answers</span>
          <span>Click any title to view thread on Discourse</span>
        </div>
      </div>

      <div class="space-y-3" id="mad-replies-list">
        <!-- Rendered via JS -->
      </div>

      <div id="pagination-controls" class="flex justify-center items-center gap-3 pt-4">
        <button onclick="changePage(-1)" id="prev-page-btn" class="px-4 py-1.5 rounded-xl border border-gray-200 bg-white text-xs font-semibold hover:bg-gray-50 transition disabled:opacity-40">Previous</button>
        <span class="text-xs font-medium text-[var(--text-muted)]" id="page-indicator">Page 1 of 24</span>
        <button onclick="changePage(1)" id="next-page-btn" class="px-4 py-1.5 rounded-xl border border-gray-200 bg-white text-xs font-semibold hover:bg-gray-50 transition disabled:opacity-40">Next</button>
      </div>
    </section>

    <!-- TAB 5: TA SCRATCHPAD & PERSONAL NOTES (Saved in LocalStorage) -->
    <section id="tab-scratchpad" class="hidden space-y-6">
      <div class="clean-card-static p-7 space-y-5">
        <div class="flex justify-between items-center">
          <div>
            <h2 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display">
              TA Live Scratchpad & Personal Quick-Notes
            </h2>
            <p class="text-xs md:text-sm text-[var(--text-muted)] mt-1">
              Draft answers for new student doubts, customize response templates, or keep term notes. Automatically saved in your browser.
            </p>
          </div>
          <button onclick="clearScratchpad()" class="text-xs text-gray-400 hover:text-rose-500 font-medium">Clear</button>
        </div>

        <div class="space-y-3">
          <textarea id="ta-scratchpad" oninput="saveScratchpad()" placeholder="Type or paste student replies here... Auto-saved locally!" rows="10" class="w-full bg-[var(--card-bg)] border border-gray-200/80 rounded-2xl p-4 text-xs md:text-sm text-[var(--text-heading)] placeholder-gray-400 focus:outline-none focus:border-rose-400 focus:ring-1 focus:ring-rose-400 transition leading-relaxed font-sans"></textarea>

          <div class="flex justify-between items-center text-xs">
            <span class="text-[var(--text-muted)]" id="scratchpad-status">Saved locally in browser</span>
            <div class="flex items-center gap-2">
              <button onclick="copyScratchpad()" class="px-4 py-2 bg-rose-500 hover:bg-rose-600 text-white rounded-xl text-xs font-semibold flex items-center gap-1.5 transition shadow-sm">
                <span>📋 Copy Draft</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="text-center pt-8 pb-4 text-xs text-[var(--text-muted)] font-normal">
      Designed with 🌸 for Yashvi • Modern Application Development 1 & 2 Intelligence Studio
    </footer>

  </div>

  <!-- FLOATING TOAST -->
  <div id="toast" class="fixed bottom-6 right-6 bg-gray-900 text-white px-4 py-2.5 rounded-xl text-xs font-medium shadow-lg opacity-0 transition-opacity duration-200 pointer-events-none flex items-center gap-2 z-50">
    <span class="text-rose-400">✨</span>
    <span id="toast-msg">Copied to clipboard!</span>
  </div>

  <script>
    const DATA = {json_str};

    let currentPage = 1;
    const pageSize = 50;
    let filteredReplies = DATA.all_replies;

    function init() {{
      renderCannedResponses();
      renderErrorMatrix();
      renderMadReplies();
      loadScratchpad();
    }}

    function toggleTheme() {{
      document.documentElement.classList.toggle('dark');
      const isDark = document.documentElement.classList.contains('dark');
      document.getElementById('theme-icon').textContent = isDark ? '☀️' : '🌙';
    }}

    function switchTab(tabId) {{
      const tabs = ['canned', 'roadmap', 'errors', 'explorer', 'scratchpad'];
      tabs.forEach(t => {{
        const el = document.getElementById('tab-' + t);
        const btn = document.getElementById('tab-btn-' + t);
        if (t === tabId) {{
          el.classList.remove('hidden');
          btn.className = "px-4 py-2 rounded-xl bg-white text-rose-600 shadow-sm transition flex items-center gap-2 font-semibold";
        }} else {{
          el.classList.add('hidden');
          btn.className = "px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2 font-medium";
        }}
      }});
    }}

    function renderCannedResponses(filter = 'ALL') {{
      const container = document.getElementById('canned-container');
      container.innerHTML = '';

      const list = DATA.canned_responses.filter(c => filter === 'ALL' || c.course.includes(filter));

      list.forEach(c => {{
        const card = document.createElement('div');
        card.className = "clean-card-static p-6 space-y-4 flex flex-col justify-between";

        const tipsHtml = c.tips.map(t => 
          `<li class="text-xs text-[var(--text-body)] flex items-start gap-1.5">
            <span class="text-rose-400 font-bold leading-none mt-0.5">•</span>
            <span>${{t}}</span>
          </li>`
        ).join('');

        const isMad1 = c.course.includes('MAD 1');
        const badgeColor = isMad1 ? 'bg-rose-50 text-rose-700 border-rose-100' : 'bg-sky-50 text-sky-700 border-sky-100';

        card.innerHTML = `
          <div class="space-y-3">
            <div class="flex justify-between items-start gap-2">
              <div class="space-y-1">
                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full border ${{badgeColor}}">${{c.course}}</span>
                <h3 class="text-sm font-bold text-[var(--text-heading)] font-display mt-1">${{escapeHtml(c.title)}}</h3>
              </div>
            </div>

            <div class="bg-pink-50/20 p-3 rounded-xl border border-pink-100/40 text-xs text-[var(--text-body)] leading-relaxed font-normal whitespace-pre-line">
${{escapeHtml(c.response)}}
            </div>

            <div class="pt-2 border-t border-gray-100">
              <span class="text-[10px] font-bold text-[var(--text-muted)] uppercase tracking-wider">Key Rules:</span>
              <ul class="space-y-1 mt-1">
                ${{tipsHtml}}
              </ul>
            </div>
          </div>

          <button onclick="copyCannedText('${{c.id}}', this)" class="self-end px-3.5 py-1.5 bg-rose-500 hover:bg-rose-600 text-white rounded-xl text-xs font-medium flex items-center gap-1.5 transition shadow-sm active:scale-95">
            <span>📋 Copy Response</span>
          </button>
        `;
        container.appendChild(card);
      }});
    }}

    function filterCanned(val) {{
      document.querySelectorAll('.canned-filter-btn').forEach(b => {{
        if (b.textContent.includes(val)) {{
          b.className = "canned-filter-btn px-3 py-1 rounded-lg bg-rose-50 text-rose-600 font-semibold border border-rose-200";
        }} else {{
          b.className = "canned-filter-btn px-3 py-1 rounded-lg bg-white text-gray-600 hover:bg-gray-50 border border-gray-200";
        }}
      }});
      renderCannedResponses(val);
    }}

    function renderErrorMatrix() {{
      const container = document.getElementById('error-matrix-container');
      container.innerHTML = '';

      DATA.error_matrix.forEach(e => {{
        const row = document.createElement('div');
        row.className = "p-5 rounded-2xl bg-white border border-gray-100/90 shadow-sm space-y-3";

        const isMad1 = e.course.includes('MAD 1');
        const badgeColor = isMad1 ? 'bg-rose-50 text-rose-700 border-rose-100' : 'bg-sky-50 text-sky-700 border-sky-100';

        row.innerHTML = `
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-2 border-b border-gray-100 pb-3">
            <span class="text-xs font-mono font-bold text-rose-600 bg-pink-50/50 px-2 py-0.5 rounded border border-pink-100/50">${{escapeHtml(e.error)}}</span>
            <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full border ${{badgeColor}}">${{e.course}}</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="space-y-1">
              <span class="font-bold text-[var(--text-muted)] uppercase text-[10px] tracking-wider">Root Cause:</span>
              <p class="text-[var(--text-body)]">${{escapeHtml(e.cause)}}</p>
            </div>
            <div class="space-y-1">
              <span class="font-bold text-emerald-600 uppercase text-[10px] tracking-wider">Yashvi's Fix:</span>
              <p class="text-[var(--text-heading)] font-medium">${{escapeHtml(e.solution)}}</p>
            </div>
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function filterMadReplies() {{
      const query = document.getElementById('mad-search').value.toLowerCase().trim();
      const course = document.getElementById('mad-course-filter').value;
      const theme = document.getElementById('mad-theme-filter').value;

      filteredReplies = DATA.all_replies.filter(r => {{
        const matchCourse = course === 'ALL' || r.course === course;
        const matchTheme = theme === 'ALL' || r.theme === theme;
        const matchQuery = !query || r.title.toLowerCase().includes(query) || r.excerpt.toLowerCase().includes(query);
        return matchCourse && matchTheme && matchQuery;
      }});

      currentPage = 1;
      renderMadReplies();
    }}

    function renderMadReplies() {{
      const container = document.getElementById('mad-replies-list');
      container.innerHTML = '';

      document.getElementById('results-count').textContent = `Showing ${{filteredReplies.length}} answers (Page ${{currentPage}} of ${{Math.max(1, Math.ceil(filteredReplies.length / pageSize))}})`;

      const start = (currentPage - 1) * pageSize;
      const pageItems = filteredReplies.slice(start, start + pageSize);

      if (pageItems.length === 0) {{
        container.innerHTML = `<div class="text-center py-16 text-xs text-[var(--text-muted)]">No MAD answers found matching your filters.</div>`;
        return;
      }}

      pageItems.forEach(item => {{
        const card = document.createElement('div');
        card.className = "clean-card-static p-4 md:p-5 space-y-2.5";

        const isMad1 = item.course === 'MAD 1';
        const badgeColor = isMad1 ? 'bg-rose-50 text-rose-700 border-rose-100' : 'bg-sky-50 text-sky-700 border-sky-100';

        card.innerHTML = `
          <div class="flex justify-between items-start gap-3">
            <div class="space-y-1">
              <a href="${{item.url}}" target="_blank" class="text-xs md:text-sm font-semibold text-[var(--text-heading)] hover:text-rose-600 hover:underline transition">
                ${{escapeHtml(item.title)}}
              </a>
              <div class="flex flex-wrap items-center gap-2 text-[11px] text-[var(--text-muted)]">
                <span class="text-[10px] font-bold px-2 py-0.2 rounded-full border ${{badgeColor}}">${{item.course}}</span>
                <span class="bg-gray-50 text-gray-700 font-medium px-2 py-0.2 rounded border border-gray-100">${{escapeHtml(item.theme)}}</span>
                <span>• Post #${{item.post_number}}</span>
                <span class="font-mono text-[10px]">• ${{item.created_at.split('T')[0]}}</span>
              </div>
            </div>
            <button onclick="copyRawText('${{escapeQuotes(item.excerpt)}}', this)" class="px-2.5 py-1 bg-white hover:bg-pink-50 text-[var(--text-body)] border border-gray-200/80 rounded-lg text-xs font-medium transition flex items-center gap-1 shadow-sm whitespace-nowrap active:scale-95">
              <span>📋 Copy</span>
            </button>
          </div>

          <div class="bg-pink-50/20 p-3 rounded-lg border border-pink-100/40 text-xs text-[var(--text-body)] leading-relaxed font-normal">
            ${{escapeHtml(item.excerpt)}}
          </div>
        `;
        container.appendChild(card);
      }});

      // Update Pagination Controls
      const totalPages = Math.max(1, Math.ceil(filteredReplies.length / pageSize));
      document.getElementById('page-indicator').textContent = `Page ${{currentPage}} of ${{totalPages}}`;
      document.getElementById('prev-page-btn').disabled = currentPage <= 1;
      document.getElementById('next-page-btn').disabled = currentPage >= totalPages;
    }}

    function changePage(delta) {{
      const totalPages = Math.max(1, Math.ceil(filteredReplies.length / pageSize));
      currentPage = Math.min(totalPages, Math.max(1, currentPage + delta));
      renderMadReplies();
      window.scrollTo({{ top: document.getElementById('tab-explorer').offsetTop - 80, behavior: 'smooth' }});
    }}

    function copyCannedText(id, btn) {{
      const item = DATA.canned_responses.find(c => c.id === id);
      if (item) {{
        navigator.clipboard.writeText(item.response).then(() => {{
          showToast('Canned reply copied!');
          if (btn) {{
            const orig = btn.innerHTML;
            btn.innerHTML = '<span>✨ Copied!</span>';
            setTimeout(() => btn.innerHTML = orig, 1800);
          }}
        }});
      }}
    }}

    function copyRawText(text, btn) {{
      navigator.clipboard.writeText(text).then(() => {{
        showToast('Answer copied!');
        if (btn) {{
          const orig = btn.innerHTML;
          btn.innerHTML = '<span>✨ Copied!</span>';
          setTimeout(() => btn.innerHTML = orig, 1800);
        }}
      }});
    }}

    function saveScratchpad() {{
      const val = document.getElementById('ta-scratchpad').value;
      localStorage.setItem('yashvi_mad_scratchpad', val);
      document.getElementById('scratchpad-status').textContent = 'Saved at ' + new Date().toLocaleTimeString();
    }}

    function loadScratchpad() {{
      const val = localStorage.getItem('yashvi_mad_scratchpad');
      if (val) {{
        document.getElementById('ta-scratchpad').value = val;
      }}
    }}

    function clearScratchpad() {{
      if (confirm('Clear scratchpad draft?')) {{
        document.getElementById('ta-scratchpad').value = '';
        localStorage.removeItem('yashvi_mad_scratchpad');
        document.getElementById('scratchpad-status').textContent = 'Scratchpad cleared';
      }}
    }}

    function copyScratchpad() {{
      const val = document.getElementById('ta-scratchpad').value;
      if (!val.trim()) {{
        showToast('Scratchpad is empty!');
        return;
      }}
      navigator.clipboard.writeText(val).then(() => {{
        showToast('Draft copied to clipboard!');
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toast-msg');
      toastMsg.textContent = msg;
      toast.style.opacity = '1';
      setTimeout(() => {{
        toast.style.opacity = '0';
      }}, 2000);
    }}

    function exportDataJson() {{
      const blob = new Blob([JSON.stringify(DATA, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'yashvi_mad_complete_archive.json';
      a.click();
    }}

    function escapeHtml(str) {{
      if (!str) return '';
      const div = document.createElement('div');
      div.textContent = str;
      return div.innerHTML;
    }}

    function escapeQuotes(str) {{
      if (!str) return '';
      return str.replace(/'/g, "\\\\'").replace(/"/g, '&quot;');
    }}

    window.onload = init;
  </script>
</body>
</html>
"""

    # Save to workspace files: yashvi_qa_dashboard.html and index.html
    with open('/home/agrim/CODES/Discourse-yashvi/yashvi_qa_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Saved to yashvi_qa_dashboard.html")

    with open('/home/agrim/CODES/Discourse-yashvi/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Saved to index.html")

    # Save to artifact directory
    artifact_path = '/home/agrim/.gemini/antigravity/brain/c6dfafde-7a25-46be-bd11-3fa52a96550b/yashvi_qa_dashboard.html'
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Saved to artifact: {artifact_path}")

if __name__ == '__main__':
    build_html()
