# 🚀 Yashvi's Discourse Smart Reply Assistant — Installation Guide

This tool runs **100% inside Google Chrome** with **zero servers, zero terminals, and zero setup for Yashvi**.

---

## ✨ What It Does

When Yashvi opens any question on [Discourse](https://discourse.onlinedegree.iitm.ac.in/):
1. **Auto-Detects the Question:** It reads the title and student's doubt.
2. **Finds Similar Past Answers:** Searches through all of her past answers (`Yashvi` / `24f2007780`) and ranks them by similarity.
3. **Floating Assistant Badge:** A blue button appears in the bottom-right corner: **`💡 Past Answers (3)`**.
4. **1-Click Actions:**
   - **`✍️ Insert in Reply`**: Automatically opens Discourse's reply box, pastes her past answer, and lets her make any small edits before posting.
   - **`📋 Copy`**: Copies the answer directly to her clipboard.
   - **`🔍 Search`**: Includes an instant search bar in the drawer to test any keywords.
   - **`🔄 Sync`**: Fetches newly posted answers into her local library with 1 click.

---

## 🛠️ Installation Options (Pick Either A or B)

### Option A: Install via Tampermonkey (Recommended — 30 Seconds)

If Yashvi uses or installs the free **Tampermonkey** extension:

1. Install [Tampermonkey for Chrome](https://chromewebstore.google.com/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo).
2. Click the Tampermonkey icon in Chrome → **"Create a new script"**.
3. Delete any default template text and paste the complete content of:
   👉 **[`discourse_smart_replies.user.js`](file:///home/agrim/CODES/Discourse-yashvi/discourse_smart_replies.user.js)**
4. Press **Ctrl + S** (or File → Save).
5. Open [Discourse](https://discourse.onlinedegree.iitm.ac.in/). Done!

---

### Option B: Load as a Chrome Extension (30 Seconds)

If she doesn't want Tampermonkey and prefers a dedicated Chrome extension:

1. Open Google Chrome and go to `chrome://extensions` in the address bar.
2. In the top-right corner, toggle **Developer mode** to **ON**.
3. In the top-left, click **"Load unpacked"**.
4. Select the folder:
   👉 **`/home/agrim/CODES/Discourse-yashvi/chrome-extension`** (or copy this folder to her computer).
5. The extension **"Discourse Smart Reply Assistant (for Yashvi)"** is now active!

---

## 💡 How Yashvi Uses It

1. Open any topic on IITM Discourse (e.g. `https://discourse.onlinedegree.iitm.ac.in/t/some-question/12345`).
2. On first run, it automatically caches her past answers (shows a brief toast notification: *"Library: 80+ answers cached"*).
3. Whenever she opens a doubt:
   - The badge **`💡 Past Answers`** shows the number of matches.
   - Click it to view the drawer on the right side.
   - Click **`✍️ Insert in Reply`** to immediately drop her previous response into the reply box.
   - Edit any specific details and hit post!

