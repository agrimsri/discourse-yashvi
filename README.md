# 🌸 Yashvi's Modern Application Development (MAD 1 & MAD 2) Teaching Studio

A specialized intelligence studio, knowledge repository, and active TA workstation engineered exclusively for **Yashvi (`24f2007780`)** covering **Modern Application Development 1 & 2** on the IIT Madras Degree discussion forum.

🌐 **Live Dashboard on GitHub Pages:**  
👉 **[https://agrimsri.github.io/discourse-yashvi/](https://agrimsri.github.io/discourse-yashvi/)**

---

## 🎯 Executive Overview & Analysis

Out of Yashvi's 1,517 total forum interactions, **1,197 posts (78.6%)** are dedicated exclusively to Modern Application Development:
- **MAD 1 (890 Posts):** Python, Flask SSR, Jinja2 templates, SQLite3, SQLAlchemy ORM, Milestone 0-2 deliverables, Level 1 & 2 Vivas.
- **MAD 2 (307 Posts):** Vue 3 SPA, Flask-RESTful APIs, JWT Auth, Celery background workers, Redis caching, MailHog reminders, final project submissions.
- **669 Distinct Threads Resolved:** Spanning all milestone lifecycles across multiple academic terms.

---

## 🛠️ Built-in Productivity Tools for Future TA Work

The studio includes 5 practical tools designed to streamline Yashvi's future TA and mentoring terms:

1. **⚡ TA Quick-Reply Bank (Canned Responses):**
   - 10 verified response templates for the most repetitive questions (Viva slot booking, presentation slide requirements, Batch 2 late policies, Milestone 0 git recovery, SQLite vs SQLAlchemy rules, RBAC implementation, Celery & Redis connection fixes, Vue CORS setup).
   - 1-click clipboard copy with instant visual confirmation.
   - Filterable by `All`, `MAD 1`, and `MAD 2`.

2. **🗺️ Term Milestone Playbook (12-Week Lifecycle):**
   - **Phase 1 (Weeks 1–3):** Milestone 0 DB Schema, checksum.py, Git history verification.
   - **Phase 2 (Weeks 4–7):** Core CRUD, Authentication (Session cookies in MAD 1 vs JWT in MAD 2), RBAC roles.
   - **Phase 3 (Weeks 8–9):** Celery background workers, Redis message brokers, monthly reports & daily alerts.
   - **Phase 4 (Weeks 10–12):** Final project submission forms, Drive upload link permissions, Level 1 & Level 2 viva rubrics.

3. **🛠️ Common MAD Debugging & Error Matrix:**
   - Quick reference matrix mapping common student errors to their root causes and Yashvi's verified fixes:
     - CORS policy preflight blocked (Vue on :8080 to Flask on :5000)
     - `ConnectionRefusedError: [Errno 111]` (Redis port 6379 service down)
     - `OperationalError: no such table` (SQLAlchemy schema drift vs SQLite file)
     - 403 Forbidden / Unauthorized admin routes
     - Celery Beat scheduled tasks not triggering

4. **🔍 Searchable Archive of 1,197 Q&A Interactions:**
   - Real-time search across all 1,197 replies with dual filters (Course: MAD 1 / MAD 2, Theme: 8 categories).
   - Direct clickable links to original Discourse threads.
   - 1-click copy for any previous explanation.
   - Client-side pagination (50 items/page).

5. **📝 TA Live Scratchpad & Notes:**
   - In-browser scratchpad automatically synchronized with `localStorage`.
   - Allows Yashvi to draft, adapt, and refine replies before pasting into Discourse.

---

## 💻 Tech Stack & Design

- **Typography:** Outfit + Plus Jakarta Sans + Poppins + Fira Code.
- **Aesthetic:** Minimal, soft, clean modern pastel design with high contrast, generous whitespace, and responsive mobile/desktop layout.
- **Dark Mode Support:** Smooth 1-click toggle between soft blush pastel light mode and comfortable slate dark mode.
- **Data Export:** 1-click JSON export button for external analysis or script integrations.
