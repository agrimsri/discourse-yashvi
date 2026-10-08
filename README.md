# 🌸 Yashvi's Discourse Q&A Intelligence Studio

An automated Q&A knowledge dashboard and in-browser smart reply assistant for **Yashvi (`24f2007780`)** on the IIT Madras Degree discussion forum.

🌐 **Live Dashboard on GitHub Pages:**  
👉 **[https://agrimsri.github.io/discourse-yashvi/](https://agrimsri.github.io/discourse-yashvi/)**

---

## ✨ Features

- **📊 Comprehensive Q&A Analytics:** 1,517 replies extracted and categorized across 22 subjects (60%+ in MAD 1 & MAD 2 projects).
- **🔥 7 Canonical Doubt Clusters:** Automatically identifies repetitive student questions (viva rubrics, batch deadlines, SQLite vs SQLAlchemy, JWT auth, Celery/Redis) with ready-to-use canonical responses and 1-click clipboard copy.
- **🔍 Searchable Q&A Library:** Instant live search filter across the entire answer database.
- **⚡ Chrome Extension & Tampermonkey Userscript:** Floating assistant on Discourse that detects question topics and offers 1-click **"Insert in Reply"** directly into the composer.

---

## 🛠️ Repository Contents

- `index.html` / `yashvi_qa_dashboard.html`: The minimal, soft, clean modern interactive dashboard deployed to GitHub Pages.
- `dashboard_data.json`: Processed dataset with clusters, top threads, and category breakdowns.
- `yashvi_discourse_data.json`: Full raw dataset of all 1,517 replies and 26 authored topics.
- `discourse_smart_replies.user.js`: Self-contained Tampermonkey userscript.
- `chrome-extension/`: Ready-to-load unpacked Google Chrome Extension.
- `discourse_user_api.md`: Complete reverse-engineered Discourse REST API specification.
- `extract_data.py`: CDP-based data extractor.
- `process_dashboard_data.py`: NLP clustering and analysis script.
- `generate_dashboard_html.py`: Dashboard compilation generator.

---

## 🚀 How to Use the Chrome Extension / Userscript

Refer to [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for 30-second setup instructions for Tampermonkey or unpacked Chrome extension.
