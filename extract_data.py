import asyncio
import json
import os
import websockets

DEVTOOLS_PORT = 9222

async def get_browser_ws():
    path = os.path.expanduser('~/.config/google-chrome/DevToolsActivePort')
    if os.path.exists(path):
        with open(path) as f:
            lines = [l.strip() for l in f if l.strip()]
            port = lines[0]
            token = lines[1]
            return f'ws://127.0.0.1:{port}{token}'
    raise RuntimeError('Could not find DevToolsActivePort')

async def extract_yashvi_data():
    browser_ws_url = await get_browser_ws()
    print(f'Connecting to {browser_ws_url}...')
    
    async with websockets.connect(browser_ws_url, max_size=100*1024*1024) as ws:
        # 1. Get targets
        await ws.send(json.dumps({'id': 1, 'method': 'Target.getTargets'}))
        targets = []
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 1:
                targets = msg['result']['targetInfos']
                break
        
        target = next((t for t in targets if t.get('type') == 'page' and 'discourse.onlinedegree.iitm.ac.in' in t.get('url', '')), None)
        if not target:
            raise RuntimeError('No Discourse tab found in Chrome!')
        
        print(f'Found Discourse tab: {target["title"]} ({target["targetId"]})')
        
        # 2. Attach to target
        await ws.send(json.dumps({
            'id': 2,
            'method': 'Target.attachToTarget',
            'params': {'targetId': target['targetId'], 'flatten': True}
        }))
        session_id = None
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 2:
                session_id = msg['result']['sessionId']
                break
        print(f'Attached with session {session_id}')
        
        # 3. Execute extraction script
        script = """
        (async () => {
            console.log('[Extractor] Fetching categories...');
            let categories = {};
            try {
                const siteRes = await fetch('/site.json');
                const siteData = await siteRes.json();
                if (siteData.categories) {
                    siteData.categories.forEach(c => {
                        categories[c.id] = { id: c.id, name: c.name, slug: c.slug, color: c.color };
                    });
                }
            } catch(e) { console.error('Categories err', e); }

            const fetchActions = async (filter) => {
                let offset = 0;
                let items = [];
                while (true) {
                    console.log(`[Extractor] Fetching filter=${filter} offset=${offset}...`);
                    const res = await fetch(`/user_actions.json?username=Yashvi&filter=${filter}&offset=${offset}`, {
                        headers: { 'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest' }
                    });
                    if (!res.ok) break;
                    const data = await res.json();
                    const actions = data.user_actions || [];
                    if (actions.length === 0) break;
                    items.push(...actions);
                    offset += 30;
                    if (actions.length < 30) break;
                    await new Promise(r => setTimeout(r, 50));
                }
                return items;
            };

            const replies = await fetchActions(5);
            const topics = await fetchActions(4);

            return {
                extracted_at: new Date().toISOString(),
                username: 'Yashvi',
                categories,
                total_replies: replies.length,
                total_topics: topics.length,
                replies,
                topics
            };
        })()
        """
        
        print('Running in-page extraction script...')
        await ws.send(json.dumps({
            'id': 3,
            'sessionId': session_id,
            'method': 'Runtime.evaluate',
            'params': {
                'expression': script,
                'awaitPromise': True,
                'returnByValue': True
            }
        }))
        
        while True:
            msg = json.loads(await ws.recv())
            if msg.get('id') == 3:
                res = msg.get('result', {})
                if 'exceptionDetails' in res:
                    print('Script exception:', res['exceptionDetails'])
                    return
                data = res['result']['value']
                print(f"Extraction complete! Total replies: {data['total_replies']}, Total topics: {data['total_topics']}")
                
                output_file = '/home/agrim/CODES/Discourse-yashvi/yashvi_discourse_data.json'
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f'Saved all data to {output_file}')
                break

if __name__ == '__main__':
    asyncio.run(extract_yashvi_data())

