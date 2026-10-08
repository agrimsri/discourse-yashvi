document.addEventListener('DOMContentLoaded', () => {
  const usernameInput = document.getElementById('usernameInput');
  const cachedCount = document.getElementById('cachedCount');
  const lastSyncTime = document.getElementById('lastSyncTime');
  const saveSyncBtn = document.getElementById('saveSyncBtn');

  // Load current values from chrome storage or localStorage
  if (chrome?.storage?.local) {
    chrome.storage.local.get(['username', 'count', 'lastSync'], (res) => {
      if (res.username) usernameInput.value = res.username;
      if (res.count !== undefined) cachedCount.textContent = res.count;
      if (res.lastSync) {
        lastSyncTime.textContent = 'Last sync: ' + new Date(res.lastSync).toLocaleString();
      }
    });
  }

  saveSyncBtn.addEventListener('click', () => {
    const username = usernameInput.value.trim() || 'Yashvi';
    if (chrome?.storage?.local) {
      chrome.storage.local.set({ username }, () => {
        saveSyncBtn.textContent = 'Saved! Refresh Discourse page.';
        setTimeout(() => {
          saveSyncBtn.textContent = '🔄 Save & Sync Library';
        }, 2000);
      });
    }
  });
});

