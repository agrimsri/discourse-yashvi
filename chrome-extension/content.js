// Content Script for Discourse Smart Reply Assistant (for Yashvi)

(function () {
  'use strict';

  console.log('%c[Discourse Q&A Helper Extension] Initializing...', 'background: #2563eb; color: #fff; font-size: 13px; font-weight: bold; padding: 4px 8px; border-radius: 4px;');

  const CONFIG = {
    defaultUsernames: ['Yashvi', '24f2007780'],
    storageKey: 'discourse_yashvi_qa_cache_v1',
    syncTimestampKey: 'discourse_yashvi_last_sync_v1',
    userPrefKey: 'discourse_yashvi_user_prefs',
    autoSyncIntervalHours: 24,
    maxResults: 6,
    minSimilarityScore: 0.10
  };

  const STOPWORDS = new Set([
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren',
    'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
    'can', 'could', 'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
    'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself',
    'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its', 'itself', 'just', 'me', 'more',
    'most', 'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
    'our', 'ours', 'ourselves', 'out', 'over', 'own', 's', 'same', 'she', 'should', 'so', 'some', 'such',
    'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'we', 'were',
    'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', 'would',
    'you', 'your', 'yours', 'yourself', 'yourselves', 'sir', 'maam', 'hello', 'hi', 'please', 'help', 'doubt'
  ]);

  let cachedAnswers = [];
  let isSyncing = false;
  let currentTopicId = null;
  let isDrawerOpen = false;

  function getActiveUsername() {
    const saved = localStorage.getItem(CONFIG.userPrefKey);
    if (saved) return saved;

    try {
      const emberUser = window.Discourse?.User?.current()?.username;
      if (emberUser) return emberUser;
    } catch (e) {}

    return CONFIG.defaultUsernames[0];
  }

  function loadLocalAnswers() {
    try {
      const data = localStorage.getItem(CONFIG.storageKey);
      if (data) {
        cachedAnswers = JSON.parse(data);
      }
    } catch (e) {
      console.warn('[Discourse Assistant] Failed to read cached answers:', e);
      cachedAnswers = [];
    }
    return cachedAnswers;
  }

  function saveLocalAnswers(items) {
    try {
      localStorage.setItem(CONFIG.storageKey, JSON.stringify(items));
      localStorage.setItem(CONFIG.syncTimestampKey, Date.now().toString());
      cachedAnswers = items;
      if (chrome?.storage?.local) {
        chrome.storage.local.set({ count: items.length, lastSync: Date.now() });
      }
    } catch (e) {
      console.error('[Discourse Assistant] Error saving to storage:', e);
    }
  }

  async function fetchUserReplies(username, maxPages = 10) {
    const replies = [];
    const headers = {
      'Accept': 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    };

    let offset = 0;
    for (let page = 0; page < maxPages; page++) {
      try {
        const url = `/user_actions.json?username=${encodeURIComponent(username)}&filter=5&offset=${offset}`;
        const res = await fetch(url, { headers });
        if (!res.ok) break;

        const data = await res.json();
        const actions = data.user_actions || [];
        if (actions.length === 0) break;

        for (const action of actions) {
          replies.push({
            id: action.post_id,
            topicId: action.topic_id,
            postNumber: action.post_number,
            title: action.title || '',
            slug: action.slug || '',
            excerpt: cleanHtml(action.excerpt || ''),
            createdAt: action.created_at,
            category: action.category_id
          });
        }

        offset += 30;
        if (actions.length < 30) break;
      } catch (err) {
        console.error('[Discourse Assistant] Error fetching actions page ' + page, err);
        break;
      }
    }

    const uniqueMap = new Map();
    for (const r of replies) {
      uniqueMap.set(r.id, r);
    }
    return Array.from(uniqueMap.values());
  }

  async function fetchPostDetails(postId) {
    try {
      const res = await fetch(`/posts/${postId}.json`, {
        headers: { 'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest' }
      });
      if (res.ok) {
        const data = await res.json();
        return data.raw || cleanHtml(data.cooked || '');
      }
    } catch (e) {}
    return null;
  }

  async function searchDiscourseUserPosts(username, query) {
    if (!query || query.trim().length < 3) return [];
    try {
      const q = `user:${username} ${query}`;
      const url = `/search.json?q=${encodeURIComponent(q)}`;
      const res = await fetch(url, {
        headers: { 'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest' }
      });
      if (res.ok) {
        const data = await res.json();
        return (data.posts || []).map(p => ({
          id: p.id,
          topicId: p.topic_id,
          postNumber: p.post_number,
          title: (data.topics || []).find(t => t.id === p.topic_id)?.title || '',
          excerpt: cleanHtml(p.blurb || ''),
          raw: null
        }));
      }
    } catch (e) {}
    return [];
  }

  function cleanHtml(html) {
    if (!html) return '';
    const tmp = document.createElement('div');
    tmp.innerHTML = html;
    return tmp.textContent || tmp.innerText || '';
  }

  function tokenize(text) {
    if (!text) return [];
    return text
      .toLowerCase()
      .replace(/[^a-z0-9_\s-]/g, ' ')
      .split(/\s+/)
      .filter(w => w.length > 2 && !STOPWORDS.has(w));
  }

  function computeSimilarity(queryTokens, docTokens, docTitleTokens) {
    if (queryTokens.length === 0 || (docTokens.length === 0 && docTitleTokens.length === 0)) {
      return 0;
    }

    const querySet = new Set(queryTokens);
    let titleMatches = 0;
    let bodyMatches = 0;

    for (const t of docTitleTokens) {
      if (querySet.has(t)) titleMatches++;
    }

    for (const b of docTokens) {
      if (querySet.has(b)) bodyMatches++;
    }

    const titleScore = docTitleTokens.length > 0 ? (titleMatches / Math.sqrt(docTitleTokens.length * queryTokens.length)) : 0;
    const bodyScore = docTokens.length > 0 ? (bodyMatches / Math.sqrt(docTokens.length * queryTokens.length)) : 0;

    return (titleScore * 0.75) + (bodyScore * 0.25);
  }

  function rankAnswers(queryTitle, queryBody, library) {
    const queryTokens = [...tokenize(queryTitle), ...tokenize(queryBody)];
    if (queryTokens.length === 0) return [];

    const scored = library.map(item => {
      const docTitleTokens = tokenize(item.title);
      const docBodyTokens = tokenize(item.excerpt);
      const score = computeSimilarity(queryTokens, docBodyTokens, docTitleTokens);
      return {
        ...item,
        score: Math.min(1.0, score * 1.5)
      };
    });

    return scored
      .filter(item => item.score >= CONFIG.minSimilarityScore)
      .sort((a, b) => b.score - a.score)
      .slice(0, CONFIG.maxResults);
  }

  async function insertIntoComposer(text) {
    let editor = document.querySelector('.d-editor-input');

    if (!editor) {
      const replyBtn = document.querySelector('button.create.reply') ||
                       document.querySelector('.timeline-controls button.reply-to-post') ||
                       document.querySelector('.post-controls button.reply');
      if (replyBtn) {
        replyBtn.click();
      } else {
        const toggle = document.querySelector('#topic-footer-buttons .btn-primary');
        if (toggle) toggle.click();
      }

      for (let i = 0; i < 20; i++) {
        await new Promise(r => setTimeout(r, 100));
        editor = document.querySelector('.d-editor-input');
        if (editor) break;
      }
    }

    if (editor) {
      const existing = editor.value || '';
      const separator = existing.trim().length > 0 ? '\n\n' : '';
      editor.value = existing + separator + text;

      editor.dispatchEvent(new Event('input', { bubbles: true }));
      editor.dispatchEvent(new Event('change', { bubbles: true }));
      editor.focus();

      editor.scrollIntoView({ behavior: 'smooth', block: 'center' });
      showToast('✅ Answer inserted into reply composer!');
    } else {
      await copyToClipboard(text);
      showToast('📋 Copied to clipboard! (Click Reply to paste)');
    }
  }

  async function copyToClipboard(text) {
    try {
      await navigator.clipboard.writeText(text);
      showToast('📋 Answer copied to clipboard!');
    } catch (e) {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      showToast('📋 Answer copied to clipboard!');
    }
  }

  function showToast(message) {
    const existing = document.getElementById('yashvi-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'yashvi-toast';
    toast.textContent = message;
    toast.style.cssText = `
      position: fixed !important;
      bottom: 24px !important;
      left: 24px !important;
      background: #1e293b !important;
      color: #f8fafc !important;
      padding: 12px 20px !important;
      border-radius: 8px !important;
      font-size: 14px !important;
      font-weight: 500 !important;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
      z-index: 2147483647 !important;
      transition: all 0.3s ease !important;
      border-left: 4px solid #3b82f6 !important;
      font-family: system-ui, -apple-system, sans-serif !important;
    `;
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  function createUI() {
    let btn = document.getElementById('yashvi-trigger-btn');
    if (!btn) {
      btn = document.createElement('button');
      btn.id = 'yashvi-trigger-btn';
      btn.innerHTML = `<span>💡 Past Answers</span><span id="yashvi-badge-count" style="display:none">0</span>`;
      btn.onclick = toggleDrawer;
      document.body.appendChild(btn);
    }
    btn.style.display = 'flex';

    let drawer = document.getElementById('yashvi-drawer');
    if (!drawer) {
      drawer = document.createElement('div');
      drawer.id = 'yashvi-drawer';
      drawer.innerHTML = `
        <div class="yashvi-drawer-header">
          <div class="yashvi-title">
            <span>✨ Yashvi's Q&A Helper</span>
          </div>
          <div class="yashvi-header-actions">
            <button class="yashvi-icon-btn" id="yashvi-sync-btn" title="Refresh/Sync Answers">🔄 Sync</button>
            <button class="yashvi-icon-btn" id="yashvi-close-btn" title="Close">✕</button>
          </div>
        </div>
        <div class="yashvi-sync-banner" id="yashvi-sync-banner" style="display:none;">
          <span id="yashvi-sync-status">Library: 0 answers cached</span>
        </div>
        <div class="yashvi-search-box">
          <input type="text" class="yashvi-search-input" id="yashvi-search-input" placeholder="Search keywords..." />
        </div>
        <div class="yashvi-cards-container" id="yashvi-cards-container">
          <div class="yashvi-empty-state">
            <p>💡 <b>Answer Library</b></p>
            <p style="font-size:13px; color:#64748b;">Open any question on Discourse to automatically see matching answers you wrote in the past.</p>
            <p style="font-size:12px; color:#94a3b8; margin-top:10px;">Or type keywords in the search bar above to look up past solutions.</p>
          </div>
        </div>
      `;
      document.body.appendChild(drawer);

      document.getElementById('yashvi-close-btn').onclick = closeDrawer;
      document.getElementById('yashvi-sync-btn').onclick = syncAnswersNow;

      const searchInput = document.getElementById('yashvi-search-input');
      searchInput.oninput = (e) => {
        performManualSearch(e.target.value.trim());
      };
    }

    updateSyncBanner();
  }

  function updateSyncBanner() {
    const banner = document.getElementById('yashvi-sync-banner');
    const statusText = document.getElementById('yashvi-sync-status');
    if (banner && statusText) {
      const count = cachedAnswers.length;
      statusText.textContent = `Library: ${count} past answers cached.`;
      banner.style.display = 'flex';
    }
  }

  function toggleDrawer() {
    isDrawerOpen = !isDrawerOpen;
    const drawer = document.getElementById('yashvi-drawer');
    if (drawer) {
      drawer.classList.toggle('open', isDrawerOpen);
    }
  }

  function closeDrawer() {
    isDrawerOpen = false;
    const drawer = document.getElementById('yashvi-drawer');
    if (drawer) {
      drawer.classList.remove('open');
    }
  }

  function renderMatches(matches, currentQuery = '') {
    const container = document.getElementById('yashvi-cards-container');
    const badge = document.getElementById('yashvi-badge-count');
    const searchInput = document.getElementById('yashvi-search-input');

    if (searchInput && currentQuery && !searchInput.matches(':focus')) {
      searchInput.value = currentQuery;
    }

    if (!container) return;

    if (badge) {
      if (matches.length > 0) {
        badge.textContent = matches.length.toString();
        badge.style.display = 'inline-block';
      } else {
        badge.style.display = 'none';
      }
    }

    if (matches.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; color: #64748b; padding: 40px 20px;">
          <p>🔍 No closely matching past answers found.</p>
          <p style="font-size:12px; margin-top:8px;">Try modifying the keywords above or click <b>🔄 Sync</b> to pull your newest replies.</p>
        </div>
      `;
      return;
    }

    container.innerHTML = '';
    matches.forEach(item => {
      const card = document.createElement('div');
      card.className = 'yashvi-match-card';

      const pct = Math.round(item.score * 100);
      const scoreColor = pct >= 60 ? '#16a34a' : (pct >= 35 ? '#2563eb' : '#64748b');

      card.innerHTML = `
        <div class="yashvi-card-top">
          <a href="/t/${item.slug || 'topic'}/${item.topicId}/${item.postNumber || 1}" target="_blank" class="yashvi-card-title">
            ${escapeHtml(item.title || 'Topic #' + item.topicId)}
          </a>
          <span class="yashvi-score-badge" style="background:${scoreColor}15; color:${scoreColor};">
            ${pct}% Match
          </span>
        </div>
        <div class="yashvi-card-body">
          ${escapeHtml(item.excerpt || 'No preview available')}
        </div>
        <div class="yashvi-card-actions">
          <button class="yashvi-btn-primary" data-action="insert">
            ✍️ Insert in Reply
          </button>
          <button class="yashvi-btn-secondary" data-action="copy">
            📋 Copy
          </button>
        </div>
      `;

      const insertBtn = card.querySelector('[data-action="insert"]');
      insertBtn.onclick = async () => {
        let textToInsert = item.raw || item.excerpt;
        if (!item.raw && item.id) {
          insertBtn.textContent = '⏳ Loading...';
          const full = await fetchPostDetails(item.id);
          if (full) {
            item.raw = full;
            textToInsert = full;
          }
          insertBtn.innerHTML = '✍️ Insert in Reply';
        }
        await insertIntoComposer(textToInsert);
      };

      const copyBtn = card.querySelector('[data-action="copy"]');
      copyBtn.onclick = async () => {
        let textToCopy = item.raw || item.excerpt;
        if (!item.raw && item.id) {
          copyBtn.textContent = '⏳ Loading...';
          const full = await fetchPostDetails(item.id);
          if (full) {
            item.raw = full;
            textToCopy = full;
          }
          copyBtn.innerHTML = '📋 Copy';
        }
        await copyToClipboard(textToCopy);
      };

      container.appendChild(card);
    });
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  async function syncAnswersNow() {
    if (isSyncing) return;
    isSyncing = true;
    const syncBtn = document.getElementById('yashvi-sync-btn');
    if (syncBtn) syncBtn.textContent = '⏳ Syncing...';

    const username = getActiveUsername();
    showToast(`🔄 Syncing past answers for ${username}...`);

    try {
      const replies = await fetchUserReplies(username);
      saveLocalAnswers(replies);
      showToast(`✅ Synced! ${replies.length} past answers stored in your library.`);
      updateSyncBanner();
      detectTopicAndSearch();
    } catch (e) {
      console.error(e);
      showToast('❌ Failed to sync answers. Please check network connection.');
    } finally {
      isSyncing = false;
      if (syncBtn) syncBtn.textContent = '🔄 Sync';
    }
  }

  function performManualSearch(query) {
    if (!query) {
      renderMatches([]);
      return;
    }
    const matches = rankAnswers(query, '', cachedAnswers);
    renderMatches(matches, query);
  }

  async function detectTopicAndSearch() {
    createUI();

    const match = window.location.pathname.match(/\/t\/(?:[^/]+\/)?(\d+)/);
    const badge = document.getElementById('yashvi-badge-count');

    if (!match) {
      if (badge) badge.style.display = 'none';
      return;
    }

    const topicId = match[1];
    if (topicId === currentTopicId) return;
    currentTopicId = topicId;

    await new Promise(r => setTimeout(r, 400));

    const titleEl = document.querySelector('.fancy-title') ||
                    document.querySelector('#topic-title h1 a') ||
                    document.querySelector('h1.fancy-title');
    const topicTitle = titleEl ? titleEl.innerText.trim() : '';

    const firstPostEl = document.querySelector('.topic-post:first-child .cooked') ||
                        document.querySelector('#post_1 .cooked');
    const firstPostBody = firstPostEl ? firstPostEl.innerText.trim() : '';

    if (!topicTitle && !firstPostBody) return;

    let localMatches = rankAnswers(topicTitle, firstPostBody, cachedAnswers);

    const username = getActiveUsername();
    const searchTerms = tokenize(topicTitle).slice(0, 4).join(' ');
    if (searchTerms) {
      searchDiscourseUserPosts(username, searchTerms).then(remotePosts => {
        if (remotePosts.length > 0) {
          const existingIds = new Set(localMatches.map(m => m.id));
          for (const rp of remotePosts) {
            if (!existingIds.has(rp.id)) {
              localMatches.push({ ...rp, score: 0.5 });
            }
          }
          localMatches.sort((a, b) => b.score - a.score);
          renderMatches(localMatches.slice(0, CONFIG.maxResults), topicTitle);
        }
      });
    }

    renderMatches(localMatches, topicTitle);
  }

  function init() {
    createUI();
    loadLocalAnswers();

    const lastSync = parseInt(localStorage.getItem(CONFIG.syncTimestampKey) || '0', 10);
    const hoursElapsed = (Date.now() - lastSync) / (1000 * 60 * 60);

    if (cachedAnswers.length === 0 || hoursElapsed > CONFIG.autoSyncIntervalHours) {
      setTimeout(syncAnswersNow, 1200);
    } else {
      detectTopicAndSearch();
    }

    let lastUrl = location.href;
    const observer = new MutationObserver(() => {
      const url = location.href;
      if (url !== lastUrl) {
        lastUrl = url;
        currentTopicId = null;
        detectTopicAndSearch();
      }
    });
    observer.observe(document.body || document.documentElement, { subtree: true, childList: true });

    window.addEventListener('popstate', () => {
      currentTopicId = null;
      detectTopicAndSearch();
    });

    console.log('%c[Discourse Q&A Helper Extension] Loaded successfully!', 'color: #16a34a; font-weight: bold;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
