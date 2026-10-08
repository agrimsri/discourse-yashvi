import json

def generate_html():
    with open('/home/agrim/CODES/Discourse-yashvi/dashboard_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    json_str = json.dumps(data)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Yashvi's Discourse Q&A Dashboard</title>
  
  <!-- Clean, Modern, Elegant Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <style>
    :root {{
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-display: 'Outfit', sans-serif;
      --font-mono: 'Fira Code', monospace;
      
      /* Minimal Soft Pastel Theme */
      --bg-main: #fcf8fa;
      --card-bg: #ffffff;
      --card-border: rgba(244, 114, 182, 0.15);
      --card-border-hover: rgba(244, 114, 182, 0.35);
      --text-heading: #18121a;
      --text-body: #4a424e;
      --text-muted: #837887;
      
      --accent-rose: #f43f5e;
      --accent-rose-soft: #fff1f4;
      --accent-pink: #ec4899;
      --accent-pink-soft: #fdf2f8;
      --accent-teal: #0d9488;
      --accent-teal-soft: #f0fdfa;
      --accent-amber: #d97706;
      --accent-amber-soft: #fffbeb;
      --accent-purple: #8b5cf6;
      --accent-purple-soft: #f5f3ff;
      
      --shadow-subtle: 0 4px 20px -2px rgba(0, 0, 0, 0.03), 0 2px 6px -1px rgba(244, 114, 182, 0.04);
      --shadow-hover: 0 12px 30px -4px rgba(244, 114, 182, 0.10), 0 4px 12px -2px rgba(0, 0, 0, 0.03);
    }}

    .dark {{
      --bg-main: #0f172a;
      --card-bg: #1e293b;
      --card-border: rgba(244, 114, 182, 0.2);
      --card-border-hover: rgba(244, 114, 182, 0.4);
      --text-heading: #f8fafc;
      --text-body: #cbd5e1;
      --text-muted: #94a3b8;
      
      --accent-rose-soft: rgba(244, 63, 94, 0.15);
      --accent-pink-soft: rgba(236, 72, 153, 0.15);
      --accent-teal-soft: rgba(13, 148, 136, 0.15);
      --accent-amber-soft: rgba(217, 119, 6, 0.15);
      --accent-purple-soft: rgba(139, 92, 246, 0.15);
      
      --shadow-subtle: 0 4px 20px -2px rgba(0, 0, 0, 0.25);
      --shadow-hover: 0 12px 30px -4px rgba(0, 0, 0, 0.35);
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-main);
      color: var(--text-body);
      background-image: 
        radial-gradient(at 0% 0%, rgba(254, 226, 226, 0.35) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(252, 231, 243, 0.4) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(245, 243, 255, 0.35) 0px, transparent 60%);
      background-attachment: fixed;
    }}

    .font-display {{
      font-family: var(--font-display);
    }}

    /* Minimal Soft Card */
    .clean-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      box-shadow: var(--shadow-subtle);
      border-radius: 1.25rem;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
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

    /* Custom subtle scrollbar */
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

  <!-- MAIN WRAPPER (Generous Negative Space) -->
  <div class="max-w-5xl mx-auto px-6 py-12 md:py-16 space-y-10">

    <!-- HERO PROFILE HEADER (Clean, Minimal, Modern) -->
    <header class="clean-card-static p-8 md:p-9 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
      <div class="flex items-center gap-5">
        <div class="w-14 h-14 md:w-16 md:h-16 rounded-2xl bg-gradient-to-tr from-rose-400 via-pink-400 to-rose-300 text-white flex items-center justify-center font-bold text-xl md:text-2xl shadow-sm flex-shrink-0">
          Y
        </div>

        <div class="space-y-1">
          <div class="flex flex-wrap items-center gap-2.5">
            <h1 class="text-xl md:text-2xl font-bold tracking-tight text-[var(--text-heading)] font-display">
              Yashvi's Q&A Studio
            </h1>
            <span class="px-2.5 py-0.5 text-xs font-medium rounded-full bg-pink-50 text-rose-600 border border-pink-100/80">
              Discourse TA & Mentor
            </span>
          </div>
          <p class="text-xs md:text-sm text-[var(--text-muted)] font-normal">
            Roll: <span class="font-mono bg-pink-50/60 text-gray-700 px-1.5 py-0.5 rounded text-xs border border-pink-100/50">24f2007780</span> • IITM Degree Forum
          </p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-2.5 w-full md:w-auto">
        <button onclick="toggleTheme()" id="theme-toggle-btn" class="px-3 py-2 rounded-xl text-xs font-medium text-[var(--text-muted)] hover:text-[var(--text-heading)] hover:bg-pink-50/50 border border-transparent hover:border-pink-100 transition flex items-center gap-1.5" title="Toggle theme">
          <span id="theme-icon">🌙</span>
        </button>

        <a href="https://discourse.onlinedegree.iitm.ac.in/u/Yashvi" target="_blank" class="px-4 py-2 rounded-xl text-xs font-medium text-[var(--text-body)] hover:text-rose-600 bg-white border border-gray-200/70 hover:border-pink-200 transition shadow-sm flex items-center gap-1.5">
          <span>🌐 Profile</span>
        </a>

        <button onclick="exportDataJson()" class="px-4 py-2 rounded-xl text-xs font-semibold bg-rose-500 hover:bg-rose-600 text-white transition shadow-sm flex items-center gap-1.5">
          <span>📥 Export JSON</span>
        </button>
      </div>
    </header>

    <!-- KEY METRICS (Minimal, Clean Soft Pastel Cards) -->
    <section class="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5">
      <!-- Total Answers -->
      <div class="clean-card p-5 md:p-6 space-y-2">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Total Answers</span>
        <div class="text-2xl md:text-3xl font-extrabold text-[var(--text-heading)] font-display">1,517</div>
        <div class="text-[11px] font-medium text-rose-500 flex items-center gap-1">
          <span>🌸 100% Extracted</span>
        </div>
      </div>

      <!-- Solved Questions -->
      <div class="clean-card p-5 md:p-6 space-y-2">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Questions Solved</span>
        <div class="text-2xl md:text-3xl font-extrabold text-[var(--text-heading)] font-display">901</div>
        <div class="text-[11px] font-medium text-[var(--text-muted)]">Across 22 course topics</div>
      </div>

      <!-- Repeating Themes -->
      <div class="clean-card p-5 md:p-6 space-y-2">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Repeating Themes</span>
        <div class="text-2xl md:text-3xl font-extrabold text-[var(--text-heading)] font-display">7</div>
        <div class="text-[11px] font-medium text-amber-600">~80% of student doubts</div>
      </div>

      <!-- Top Subject -->
      <div class="clean-card p-5 md:p-6 space-y-2">
        <span class="text-xs font-semibold uppercase tracking-wider text-[var(--text-muted)]">Top Courses</span>
        <div class="text-xl md:text-2xl font-extrabold text-[var(--text-heading)] font-display truncate" title="Modern Application Development">MAD 1 & 2</div>
        <div class="text-[11px] font-medium text-[var(--text-muted)]">1,192 posts (78.5%)</div>
      </div>
    </section>

    <!-- MINIMAL PILL NAVIGATION TABS -->
    <nav class="flex flex-wrap gap-2 p-1 bg-pink-100/30 rounded-2xl border border-pink-100/60 text-xs md:text-sm font-medium">
      <button onclick="switchTab('frequent')" id="tab-btn-frequent" class="px-4 py-2 rounded-xl bg-white text-rose-600 shadow-sm transition flex items-center gap-2 font-semibold">
        <span>🔥 Frequent Doubts</span>
        <span class="px-1.5 py-0.2 rounded-full text-[10px] bg-pink-50 text-rose-600 font-semibold">7</span>
      </button>
      <button onclick="switchTab('categories')" id="tab-btn-categories" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>📊 Course Breakdown</span>
      </button>
      <button onclick="switchTab('threads')" id="tab-btn-threads" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>💬 Milestone Threads</span>
      </button>
      <button onclick="switchTab('explorer')" id="tab-btn-explorer" class="px-4 py-2 rounded-xl text-[var(--text-muted)] hover:text-rose-600 transition flex items-center gap-2">
        <span>🔍 Search Library</span>
      </button>
    </nav>

    <!-- TAB 1: FREQUENT QUESTION CLUSTERS & CANONICAL ANSWERS -->
    <main id="tab-frequent" class="space-y-6">
      <div class="clean-card-static p-6 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h2 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display flex items-center gap-2">
            <span>🌸</span> Canonical Answers for Repetitive Doubts
          </h2>
          <p class="text-xs md:text-sm text-[var(--text-muted)] mt-1 max-w-2xl leading-relaxed">
            When students ask these common questions, Yashvi can click <b>"Copy Answer"</b> to grab the verified response immediately.
          </p>
        </div>
        <span class="text-xs text-rose-600 font-medium bg-pink-50 px-3 py-1 rounded-full border border-pink-100">
          ✨ 1-Click Clipboard Copy
        </span>
      </div>

      <div class="grid grid-cols-1 gap-6" id="clusters-container">
        <!-- Rendered via JS -->
      </div>
    </main>

    <!-- TAB 2: COURSE & CATEGORY BREAKDOWN -->
    <section id="tab-categories" class="hidden space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <!-- Visual Bar Chart Card -->
        <div class="lg:col-span-2 clean-card-static p-7 space-y-5">
          <div class="flex justify-between items-center border-b border-gray-100 pb-3">
            <h3 class="text-base font-bold text-[var(--text-heading)] font-display">Answers by Course Category</h3>
            <span class="text-xs text-[var(--text-muted)] font-medium">22 Categories</span>
          </div>
          <div class="space-y-3.5" id="categories-chart-container">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Activity Highlights Card -->
        <div class="clean-card p-6 space-y-4 flex flex-col justify-between">
          <div>
            <h3 class="text-base font-bold text-[var(--text-heading)] font-display flex items-center gap-2 border-b border-gray-100 pb-3">
              <span>💡</span> Key Highlights
            </h3>
            <div class="space-y-3 mt-4 text-xs md:text-sm leading-relaxed">
              <div class="p-3.5 rounded-xl bg-pink-50/40 border border-pink-100/60 space-y-1">
                <span class="text-[11px] font-bold text-rose-600 uppercase tracking-wider">Top Concentration</span>
                <p class="font-semibold text-[var(--text-heading)]">Project for MAD1 & MAD2</p>
                <p class="text-xs text-[var(--text-muted)]">Comprises <b>913 replies</b> (60.2% of her overall forum presence).</p>
              </div>

              <div class="p-3.5 rounded-xl bg-purple-50/40 border border-purple-100/60 space-y-1">
                <span class="text-[11px] font-bold text-purple-600 uppercase tracking-wider">Concept Guidance</span>
                <p class="font-semibold text-[var(--text-heading)]">MAD-1 Coursework</p>
                <p class="text-xs text-[var(--text-muted)]"><b>279 replies</b> addressing HTML/CSS/JS, SQLite syntax, and route structuring.</p>
              </div>

              <div class="p-3.5 rounded-xl bg-teal-50/40 border border-teal-100/60 space-y-1">
                <span class="text-[11px] font-bold text-teal-600 uppercase tracking-wider">Foundation & Math</span>
                <p class="font-semibold text-[var(--text-heading)]">Math 2, Stats 2 & Python</p>
                <p class="text-xs text-[var(--text-muted)]"><b>139 replies</b> providing step-by-step mathematical clarifications and code fixes.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TAB 3: MEGA DISCUSSION THREADS -->
    <section id="tab-threads" class="hidden space-y-6">
      <div class="clean-card-static p-7 space-y-5">
        <div>
          <h3 class="text-base font-bold text-[var(--text-heading)] font-display">High Volume Milestone Threads</h3>
          <p class="text-xs text-[var(--text-muted)] mt-1">Discussions where students asked numerous repetitive questions and Yashvi posted multiple clarifications.</p>
        </div>
        <div class="divide-y divide-gray-100" id="threads-container">
          <!-- Rendered via JS -->
        </div>
      </div>
    </section>

    <!-- TAB 4: SEARCHABLE Q&A LIBRARY -->
    <section id="tab-explorer" class="hidden space-y-6">
      <div class="clean-card-static p-5 space-y-4">
        <div class="flex flex-col md:flex-row gap-4 justify-between items-center">
          <div class="relative w-full md:w-80">
            <span class="absolute left-3.5 top-2.5 text-gray-400 text-xs">🔍</span>
            <input type="text" id="explorer-search" oninput="filterExplorer()" placeholder="Search doubts (sqlite, deadline, jwt)..." class="w-full bg-[var(--card-bg)] border border-gray-200/80 rounded-xl pl-9 pr-4 py-2 text-xs md:text-sm text-[var(--text-heading)] placeholder-gray-400 focus:outline-none focus:border-rose-400 focus:ring-1 focus:ring-rose-400 transition" />
          </div>
          <div class="flex items-center gap-2 w-full md:w-auto">
            <select id="explorer-category-filter" onchange="filterExplorer()" class="w-full md:w-auto bg-[var(--card-bg)] border border-gray-200/80 rounded-xl px-3.5 py-2 text-xs font-medium text-[var(--text-body)] focus:outline-none focus:border-rose-400 cursor-pointer shadow-sm">
              <option value="ALL">All Course Subjects</option>
            </select>
          </div>
        </div>
      </div>

      <div class="space-y-3.5" id="explorer-results">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="text-center pt-8 pb-4 text-xs text-[var(--text-muted)] font-normal">
      Designed with 🌸 for Yashvi • IITM Degree Q&A Knowledge Studio
    </footer>

  </div>

  <!-- MINIMAL TOAST -->
  <div id="toast" class="fixed bottom-6 right-6 bg-gray-900 text-white px-4 py-2.5 rounded-xl text-xs font-medium shadow-lg opacity-0 transition-opacity duration-200 pointer-events-none flex items-center gap-2 z-50">
    <span class="text-rose-400">✨</span>
    <span id="toast-msg">Copied to clipboard!</span>
  </div>

  <script>
    const DATA = {json_str};

    function init() {{
      renderClusters();
      renderCategories();
      renderThreads();
      populateExplorerCategories();
      renderExplorer();
    }}

    function toggleTheme() {{
      document.documentElement.classList.toggle('dark');
      const isDark = document.documentElement.classList.contains('dark');
      document.getElementById('theme-icon').textContent = isDark ? '☀️' : '🌙';
    }}

    function switchTab(tabId) {{
      const tabs = ['frequent', 'categories', 'threads', 'explorer'];
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

    function renderClusters() {{
      const container = document.getElementById('clusters-container');
      container.innerHTML = '';

      DATA.frequent_clusters.forEach((c, idx) => {{
        const card = document.createElement('div');
        card.className = "clean-card-static p-6 md:p-7 space-y-5";

        const bulletsHtml = c.canonical_qa.bullet_points.map(b => 
          `<li class="text-xs text-[var(--text-body)] flex items-start gap-2">
            <span class="text-rose-400 font-bold leading-none mt-0.5">•</span>
            <span>${{b}}</span>
          </li>`
        ).join('');

        const samplesHtml = (c.sample_qas || []).map(s => 
          `<div class="bg-[var(--card-bg)] p-3.5 rounded-xl border border-gray-100 text-xs space-y-1">
            <div class="flex justify-between items-start gap-2">
              <a href="${{s.url}}" target="_blank" class="font-semibold text-rose-600 hover:underline truncate">${{escapeHtml(s.title)}}</a>
              <span class="text-[10px] text-[var(--text-muted)] whitespace-nowrap font-mono">${{s.created_at.split('T')[0]}}</span>
            </div>
            <p class="text-[var(--text-muted)] line-clamp-2 italic leading-relaxed">"${{escapeHtml(s.excerpt)}}"</p>
          </div>`
        ).join('');

        card.innerHTML = `
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-3 border-b border-gray-100 pb-4">
            <div class="space-y-1">
              <div class="flex items-center gap-2.5">
                <span class="w-6 h-6 rounded-lg bg-pink-50 text-rose-600 flex items-center justify-center text-xs font-semibold font-mono">0${{idx + 1}}</span>
                <h3 class="text-base md:text-lg font-bold text-[var(--text-heading)] font-display">${{escapeHtml(c.theme)}}</h3>
              </div>
              <div class="text-xs text-[var(--text-muted)] flex items-center gap-2 pl-8">
                <span class="px-2 py-0.5 rounded bg-pink-50/70 text-rose-700 text-[11px] font-medium border border-pink-100/60">${{escapeHtml(c.category)}}</span>
                <span>• Answered in <b class="text-[var(--text-heading)] font-semibold">${{c.reply_count}}</b> discussions</span>
              </div>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-semibold bg-rose-50 text-rose-600 border border-rose-100 whitespace-nowrap">
              🌸 ${{c.reply_count}} Answers Given
            </span>
          </div>

          <!-- Split: Doubt vs Canonical Answer -->
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <!-- Left: Typical Doubt -->
            <div class="p-4 md:p-5 rounded-xl bg-amber-50/30 border border-amber-100/60 space-y-2.5">
              <span class="text-[11px] font-bold text-amber-700 uppercase tracking-wider flex items-center gap-1.5">
                <span>💬</span> Typical Student Question:
              </span>
              <p class="text-xs md:text-sm font-semibold text-[var(--text-heading)] italic leading-relaxed">
                "${{escapeHtml(c.canonical_qa.typical_question)}}"
              </p>
              <div class="pt-2 border-t border-amber-100/60">
                <span class="text-[11px] font-bold text-amber-800 uppercase tracking-wider">Key Takeaways:</span>
                <ul class="space-y-1 mt-1.5">
                  ${{bulletsHtml}}
                </ul>
              </div>
            </div>

            <!-- Right: Canonical Answer -->
            <div class="p-4 md:p-5 rounded-xl bg-rose-50/30 border border-rose-100/60 flex flex-col justify-between space-y-3">
              <div>
                <span class="text-[11px] font-bold text-rose-600 uppercase tracking-wider flex items-center gap-1.5 mb-1.5">
                  <span>✨</span> Canonical Response:
                </span>
                <p class="text-xs md:text-sm text-[var(--text-body)] leading-relaxed font-normal" id="canonical-${{c.id}}">
                  ${{escapeHtml(c.canonical_qa.best_answer)}}
                </p>
              </div>
              <button onclick="copyAnswer('${{c.id}}', this)" class="self-end px-3.5 py-1.5 bg-rose-500 hover:bg-rose-600 text-white rounded-lg text-xs font-medium flex items-center gap-1.5 transition shadow-sm active:scale-95">
                <span>📋 Copy Answer</span>
              </button>
            </div>
          </div>

          <!-- Real Samples Accordion -->
          <details class="pt-1 group">
            <summary class="cursor-pointer text-xs font-medium text-rose-600 hover:text-rose-700 flex items-center gap-1.5 select-none">
              <span>View sample real answers by Yashvi on this theme (${{c.sample_qas ? c.sample_qas.length : 0}})</span>
            </summary>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 mt-2.5">
              ${{samplesHtml}}
            </div>
          </details>
        `;
        container.appendChild(card);
      }});
    }}

    function renderCategories() {{
      const container = document.getElementById('categories-chart-container');
      container.innerHTML = '';
      const total = DATA.metadata.total_replies;

      DATA.categories.sort((a,b) => b.count - a.count).forEach(cat => {{
        const pct = Math.round((cat.count / total) * 100);
        const row = document.createElement('div');
        row.className = "space-y-1";
        row.innerHTML = `
          <div class="flex justify-between text-xs font-medium">
            <span class="text-[var(--text-heading)] font-semibold">${{escapeHtml(cat.name)}}</span>
            <span class="text-[var(--text-muted)] font-mono">${{cat.count}} answers (${{pct}}%)</span>
          </div>
          <div class="w-full h-2 rounded-full bg-pink-100/40 overflow-hidden">
            <div class="h-full rounded-full bg-gradient-to-r from-rose-400 to-pink-500 transition-all duration-500" style="width: ${{Math.max(2, pct)}}%;"></div>
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function renderThreads() {{
      const container = document.getElementById('threads-container');
      container.innerHTML = '';

      DATA.top_threads.forEach(t => {{
        const row = document.createElement('div');
        row.className = "py-3.5 flex flex-col md:flex-row justify-between items-start md:items-center gap-3";
        row.innerHTML = `
          <div class="space-y-1 max-w-2xl">
            <a href="${{t.url}}" target="_blank" class="text-xs md:text-sm font-semibold text-[var(--text-heading)] hover:text-rose-600 hover:underline transition">
              ${{escapeHtml(t.title)}}
            </a>
            <div class="flex items-center gap-2 text-xs text-[var(--text-muted)]">
              <span class="bg-pink-50/70 text-rose-700 px-2 py-0.5 rounded text-[11px] border border-pink-100/50">${{escapeHtml(t.category_name)}}</span>
            </div>
            ${{t.latest_reply ? `<p class="text-xs text-[var(--text-muted)] line-clamp-1 italic mt-0.5">"${{escapeHtml(t.latest_reply)}}"</p>` : ''}}
          </div>
          <div class="flex items-center gap-3 whitespace-nowrap">
            <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-pink-50 text-rose-600 border border-pink-100">
              ${{t.reply_count}} replies by Yashvi
            </span>
            <a href="${{t.url}}" target="_blank" class="px-2.5 py-1 rounded-lg border border-gray-200 text-xs font-medium text-[var(--text-body)] hover:bg-pink-50 transition">
              Open ↗
            </a>
          </div>
        `;
        container.appendChild(row);
      }});
    }}

    function populateExplorerCategories() {{
      const select = document.getElementById('explorer-category-filter');
      DATA.categories.sort((a,b) => b.count - a.count).forEach(c => {{
        const opt = document.createElement('option');
        opt.value = c.name;
        opt.textContent = `${{c.name}} (${{c.count}})`;
        select.appendChild(opt);
      }});
    }}

    function renderExplorer(items = null) {{
      const container = document.getElementById('explorer-results');
      container.innerHTML = '';
      const list = items || DATA.recent_replies;

      if (list.length === 0) {{
        container.innerHTML = `<div class="text-center py-12 text-[var(--text-muted)] text-xs font-medium">No answers match your search keywords.</div>`;
        return;
      }}

      list.forEach(item => {{
        const card = document.createElement('div');
        card.className = "clean-card-static p-4 md:p-5 space-y-2.5";
        card.innerHTML = `
          <div class="flex justify-between items-start gap-4">
            <div class="space-y-0.5">
              <a href="${{item.url}}" target="_blank" class="text-xs md:text-sm font-semibold text-[var(--text-heading)] hover:text-rose-600 hover:underline transition">
                ${{escapeHtml(item.title)}}
              </a>
              <div class="flex flex-wrap items-center gap-2 text-[11px] text-[var(--text-muted)]">
                <span class="bg-pink-50 text-rose-700 font-medium px-2 py-0.2 rounded border border-pink-100">${{escapeHtml(item.category_name)}}</span>
                <span>• Post #${{item.post_number}}</span>
                <span class="font-mono">• ${{item.created_at.split('T')[0]}}</span>
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
    }}

    function filterExplorer() {{
      const query = document.getElementById('explorer-search').value.toLowerCase().trim();
      const cat = document.getElementById('explorer-category-filter').value;

      const filtered = DATA.recent_replies.filter(r => {{
        const matchQuery = !query || r.title.toLowerCase().includes(query) || r.excerpt.toLowerCase().includes(query);
        const matchCat = cat === 'ALL' || r.category_name === cat;
        return matchQuery && matchCat;
      }});

      renderExplorer(filtered);
    }}

    function copyAnswer(clusterId, btn) {{
      const cluster = DATA.frequent_clusters.find(c => c.id === clusterId);
      if (cluster) {{
        navigator.clipboard.writeText(cluster.canonical_qa.best_answer).then(() => {{
          showToast('Canonical answer copied!');
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
        showToast('Answer text copied!');
        if (btn) {{
          const orig = btn.innerHTML;
          btn.innerHTML = '<span>✨ Copied!</span>';
          setTimeout(() => btn.innerHTML = orig, 1800);
        }}
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
      a.download = 'yashvi_discourse_qa_library.json';
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

    ws_path = '/home/agrim/CODES/Discourse-yashvi/yashvi_qa_dashboard.html'
    with open(ws_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Saved minimal clean modern dashboard to workspace: {ws_path}")

    artifact_path = '/home/agrim/.gemini/antigravity/brain/c6dfafde-7a25-46be-bd11-3fa52a96550b/yashvi_qa_dashboard.html'
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Saved minimal clean modern dashboard to artifact: {artifact_path}")

if __name__ == '__main__':
    generate_html()
