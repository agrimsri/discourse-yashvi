# Discourse API & Network Calls Reference (IITM Online Degree)

**Target Instance:** [https://discourse.onlinedegree.iitm.ac.in/](https://discourse.onlinedegree.iitm.ac.in/)  
**Platform Version:** `Discourse 2026.10.0-latest`  
**Inspected User Profile:** `Profile 1` (`23f3002782@ds.study.iitm.ac.in`)  
**Identified User:**
- **Username:** `23f3002782`
- **Name:** `Agrim Srivastava`
- **User ID:** `24605`
- **Trust Level:** `1` (Basic)
- **Primary Groups:** `ds-students`, `moderator_CourseTA`, `moderator_TDS`

---

## 1. Authentication & Common Headers

Discourse web app operates via a session cookie combined with CSRF token protection for state-changing requests, and standard JSON headers for API responses.

### 1.1 Web Session Headers (Browser / Cookie Context)
When making calls using an existing browser session (e.g. via Playwright, Puppeteer, Python `requests.Session`, or browser `fetch`):
- **`Cookie`**: Must contain valid session cookies:
  - `_forum_session=<encrypted_session>`
  - `_t=<auth_token>`
- **`X-CSRF-Token`**: Required for all mutation calls (`POST`, `PUT`, `DELETE`). Obtained from:
  - HTML DOM: `<meta name="csrf-token" content="...">`
  - JavaScript context: `Discourse.Session.current().csrfToken`
- **`X-Requested-With`**: `XMLHttpRequest` (crucial to tell Discourse backend to respond with JSON rather than HTML redirects).
- **`Accept`**: `application/json`
- **`Discourse-Logged-In`**: `true`
- **`Discourse-Present`**: `true`

### 1.2 Machine / Service API Key Headers (Server Context)
If an Admin or User API key is configured:
- **`Api-Key`**: `<32_character_hex_key>`
- **`Api-Username`**: `23f3002782`

---

## 2. User Profile, Account & Metadata Endpoints

### 2.1 Current Logged-in Session
Retrieves the logged-in user identity, current permissions, unread notification counts, and site privileges.

- **Method:** `GET`
- **Endpoint:** `/session/current.json`
- **Headers:** `Accept: application/json`, `X-Requested-With: XMLHttpRequest`
- **Sample Response:**
```json
{
  "current_user": {
    "id": 24605,
    "username": "23f3002782",
    "name": "Agrim Srivastava",
    "avatar_template": "/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3002782/{size}/108844_2.png",
    "trust_level": 1,
    "admin": false,
    "moderator": false,
    "title": "Course TA",
    "can_create_topic": true,
    "unread_notifications": 10,
    "all_unread_notifications_count": 10,
    "read_first_notification": true,
    "groups": [
      { "id": 294, "name": "ds-students" },
      { "id": 232, "name": "moderator_CourseTA" },
      { "id": 251, "name": "moderator_TDS" }
    ],
    "muted_category_ids": [],
    "tracked_category_ids": [],
    "watched_category_ids": [7, 9, 61],
    "sidebar_category_ids": [7, 9, 61],
    "can_chat": true,
    "has_chat_enabled": true
  }
}
```

---

### 2.2 Full User Profile & Settings
Returns complete profile details, custom fields (house name, student details), badge list, notification preferences, and account configuration.

- **Method:** `GET`
- **Endpoint:** `/u/{username}.json` (e.g. `/u/23f3002782.json`)
- **Headers:** `Accept: application/json`, `X-Requested-With: XMLHttpRequest`
- **Key Top-level Keys:** `user`, `user_badges`, `badges`, `badge_types`, `users`
- **Sample Response:**
```json
{
  "user": {
    "id": 24605,
    "username": "23f3002782",
    "name": "Agrim Srivastava",
    "email": "23f3002782@ds.study.iitm.ac.in",
    "avatar_template": "/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3002782/{size}/108844_2.png",
    "trust_level": 1,
    "badge_count": 5,
    "created_at": "2023-12-30T06:23:18.827Z",
    "last_posted_at": "2026-10-03T07:14:08.100Z",
    "last_seen_at": "2026-10-07T07:20:29.758Z",
    "primary_group_name": "ds-students",
    "flair_name": "ds-students",
    "user_fields": {
      "1": "Sundarbans"
    },
    "custom_fields": {
      "last_chat_channel_id": 18784
    },
    "user_option": {
      "email_digests": false,
      "email_level": 2,
      "email_messages_level": 2,
      "external_links_in_new_tab": true,
      "auto_track_topics_after_msecs": 300000,
      "notification_level_when_replying": 2,
      "like_notification_frequency": 1,
      "timezone": "Asia/Calcutta",
      "chat_enabled": true
    }
  }
}
```

---

### 2.3 User Summary & Aggregate Statistics
Returns engagement metrics, top replied topics, most liked users, most liked by users, top external links clicked, and solutions count.

- **Method:** `GET`
- **Endpoint:** `/u/{username}/summary.json` (e.g. `/u/23f3002782/summary.json`)
- **Sample Response:**
```json
{
  "user_summary": {
    "likes_given": 12,
    "likes_received": 52,
    "topics_entered": 530,
    "posts_read_count": 2983,
    "days_visited": 302,
    "topic_count": 1,
    "post_count": 83,
    "time_read": 66585,
    "recent_time_read": 4058,
    "bookmark_count": 0,
    "solved_count": 23,
    "replies": [
      {
        "post_number": 7,
        "like_count": 4,
        "created_at": "2026-03-17T07:45:45.548Z",
        "topic_id": 198830
      },
      {
        "post_number": 2,
        "like_count": 2,
        "created_at": "2026-10-03T07:05:56.629Z",
        "topic_id": 216582
      }
    ],
    "most_liked_by_users": [
      {
        "id": 51571,
        "username": "25f3000685",
        "name": "Sayantan Chakraborty",
        "count": 10
      }
    ],
    "most_liked_users": [
      {
        "id": 51571,
        "username": "25f3000685",
        "count": 2
      }
    ]
  },
  "topics": [ /* Topic list */ ],
  "badges": [ /* Badges list */ ]
}
```

---

### 2.4 User Preview Card
Compact profile summary used by Discourse user hover popovers.

- **Method:** `GET`
- **Endpoint:** `/u/{username}/card.json`
- **Sample Response:**
```json
{
  "user": {
    "id": 24605,
    "username": "23f3002782",
    "name": "Agrim Srivastava",
    "bio_excerpt": null,
    "trust_level": 1,
    "badge_count": 5,
    "primary_group_name": "ds-students",
    "featured_user_badge_ids": [55380, 78823, 85474]
  }
}
```

---

### 2.5 User Registered Emails & OAuth Accounts
Retrieves the user's registered emails (primary, secondary, unconfirmed) and connected SSO/OAuth identities.

- **Method:** `GET`
- **Endpoint:** `/u/{username}/emails.json`
- **Sample Response:**
```json
{
  "email": "23f3002782@ds.study.iitm.ac.in",
  "secondary_emails": [],
  "unconfirmed_emails": [],
  "associated_accounts": [
    {
      "name": "google_oauth2",
      "description": "23f3002782@ds.study.iitm.ac.in"
    }
  ]
}
```

---

### 2.6 Update User Profile & Preferences
Updates user profile settings, bio, title, or options.

- **Method:** `PUT`
- **Endpoint:** `/u/{username}.json`
- **Headers:** `X-CSRF-Token`, `Content-Type: application/json`
- **Payload:**
```json
{
  "name": "Agrim Srivastava",
  "title": "Course TA",
  "bio_raw": "Bio text in markdown",
  "timezone": "Asia/Calcutta",
  "user_fields": {
    "1": "Sundarbans"
  },
  "user_option": {
    "external_links_in_new_tab": true,
    "chat_enabled": true
  }
}
```

---

## 3. User Posts, Topics & Activity Stream

### 3.1 User Actions Activity Feed (All Posts, Replies, Likes, Edits)
The unified feed for any activity performed by or directed at a user.

- **Method:** `GET`
- **Endpoint:** `/user_actions.json`
- **Query Parameters:**
  - `username` *(required)*: e.g. `23f3002782`
  - `offset` *(optional, int, default `0`)*: Increments by 30 for pagination
  - `filter` *(optional, int or comma-delimited)*:
    | Filter ID | Action Description |
    |---|---|
    | `1` | Likes Given |
    | `2` | Likes Received |
    | `3` | Bookmarks |
    | `4` | Topics Created |
    | `5` | Replies Created |
    | `6` | Responses (replies directed to user) |
    | `7` | Mentions |
    | `9` | Quotes |
    | `11` | Post Edits |
    | `12` | Messages Sent |
    | `13` | Messages Received |
    | `14` | Solved / Accepted Answer |
    | `15` | Assigned |
- **Example Request:**
  ```http
  GET /user_actions.json?offset=0&username=23f3002782&filter=4,5
  ```
- **Sample Response:**
```json
{
  "user_actions": [
    {
      "action_type": 5,
      "post_id": 841607,
      "post_number": 3,
      "topic_id": 216448,
      "title": "Doubt in TDS link provided on seek",
      "slug": "doubt-in-tds-link-provided-on-seek",
      "category_id": 34,
      "excerpt": "Yes, the content will be updated shortly for the Sept term...",
      "created_at": "2026-10-03T07:14:08.100Z",
      "username": "23f3002782",
      "name": "Agrim Srivastava",
      "user_id": 24605,
      "acting_username": "23f3002782",
      "target_username": "23f3002782",
      "deleted": false,
      "hidden": false
    }
  ]
}
```

---

### 3.2 Topics Created by User
Lists topics authored by the user.

- **Method:** `GET`
- **Endpoint:** `/topics/created-by/{username}.json` (e.g. `/topics/created-by/23f3002782.json`)
- **Query Parameters:** `page` *(optional, int, default `0`)*
- **Sample Response:**
```json
{
  "topic_list": {
    "topics": [
      {
        "id": 191760,
        "title": "Q&A Series",
        "slug": "q-a-series",
        "posts_count": 14,
        "reply_count": 5,
        "highest_post_number": 15,
        "views": 267,
        "like_count": 11,
        "category_id": 19,
        "created_at": "2025-11-19T06:19:40.240Z",
        "last_posted_at": "2025-12-04T10:19:39.126Z",
        "has_accepted_answer": true,
        "tags": [
          { "id": 245, "name": "foundation-level", "slug": "foundation-level" },
          { "id": 364, "name": "term3-2025", "slug": "term3-2025" }
        ]
      }
    ]
  }
}
```

---

### 3.3 Drafts Saved by User
Returns in-progress unposted composer drafts.

- **Method:** `GET`
- **Endpoint:** `/drafts.json`
- **Sample Response:**
```json
{
  "drafts": [
    {
      "draft_key": "topic_206120",
      "sequence": 39,
      "topic_id": 206120,
      "title": "Case: A Tattle Tale? [Week 2 | T2-2026]",
      "created_at": "2026-06-27T13:59:37.745Z",
      "data": "{\"reply\":\"Discussion Report GA-2...\",\"action\":\"reply\",\"categoryId\":57}"
    }
  ]
}
```

---

### 3.4 Detailed Post Content (Raw & Rendered)
Retrieves the full raw Markdown and rendered HTML (`cooked`) for any specific post.

- **Method:** `GET`
- **Endpoint:** `/posts/{post_id}.json` (e.g. `/posts/841607.json`)
- **Sample Response:**
```json
{
  "id": 841607,
  "name": "Agrim Srivastava",
  "username": "23f3002782",
  "post_number": 3,
  "topic_id": 216448,
  "topic_slug": "doubt-in-tds-link-provided-on-seek",
  "topic_title": "Doubt in TDS link provided on seek",
  "cooked": "<p>Yes, the content will be updated shortly for the Sept term...</p>",
  "raw": "Yes, the content will be updated shortly for the Sept term...",
  "like_count": 0,
  "reads": 48,
  "readers_count": 47,
  "score": 8.4,
  "can_edit": true,
  "can_delete": false,
  "actions_summary": [
    { "id": 2, "count": 0, "can_act": true },
    { "id": 3, "can_act": true }
  ]
}
```

---

## 4. Notifications Endpoints

### 4.1 Fetch Notifications
- **Method:** `GET`
- **Endpoint:** `/notifications.json`
- **Query Parameters:**
  - `filter`: `"unread"` or omit for all
  - `limit`: max count (e.g. `30` or `50`)
  - `offset`: pagination offset
  - `silent`: `true` to avoid marking seen indicator
- **Common Notification Type IDs:**
  - `1`: Mention
  - `2`: Replied
  - `3`: Quoted
  - `4`: Post Edited
  - `5`: Liked
  - `6`: Private Message
  - `9`: Watched Topic Post
  - `12`: Badge Awarded
  - `14`: Custom
  - `15`: Group Mention
  - `25`: Reaction / Poll
  - `36`: Course Announcement
- **Sample Response:**
```json
{
  "notifications": [
    {
      "id": 9352741,
      "notification_type": 9,
      "read": true,
      "high_priority": false,
      "created_at": "2026-10-07T05:50:40.271Z",
      "topic_id": 216849,
      "post_number": 5,
      "slug": "stuck-at-question-1-of-ga0-scale-manipulation-repair-in-axis-design",
      "data": {
        "topic_title": "Stuck at question 1 of GA0- Scale Manipulation Repair in Axis Design",
        "original_post_id": 843186,
        "original_username": "23f1000805",
        "display_name": "Gaurav Tomar"
      }
    }
  ],
  "total_rows_notifications": 1483,
  "seen_notification_id": 9320971
}
```

### 4.2 Mark Notifications as Read
- **Method:** `PUT`
- **Endpoint:** `/notifications/mark-read.json`
- **Headers:** `X-CSRF-Token`, `Content-Type: application/json`
- **Payload:**
  - Single: `{"id": 9352716}`
  - All: `{}`

---

## 5. Bookmarks Endpoints

### 5.1 Fetch Bookmarks
- **Bookmark records:** `GET /u/{username}/bookmarks.json`
- **Bookmark topic feed:** `GET /bookmarks.json?page=0&q=query`

### 5.2 Create Bookmark
- **Method:** `POST`
- **Endpoint:** `/bookmarks.json`
- **Headers:** `X-CSRF-Token`, `Content-Type: application/json`
- **Payload:**
```json
{
  "bookmarkable_id": 841607,
  "bookmarkable_type": "Post",
  "name": "Important TDS Doubt",
  "reminder_at": "2026-10-10T09:00:00Z",
  "auto_delete_preference": 0
}
```

### 5.3 Delete Bookmark
- **Method:** `DELETE`
- **Endpoint:** `/bookmarks/{bookmark_id}.json`

---

## 6. Badges & Leaderboard / Directory

### 6.1 User Badges
- **Method:** `GET`
- **Endpoint:** `/user-badges/{username}.json` (e.g. `/user-badges/23f3002782.json`)
- **Sample Response:**
```json
{
  "user_badges": [
    {
      "id": 55380,
      "badge_id": 1,
      "granted_at": "2024-08-15T11:26:33.292Z",
      "user_id": 24605,
      "granted_by_id": -1
    },
    {
      "id": 78823,
      "badge_id": 24,
      "granted_at": "2025-10-17T10:24:10.113Z",
      "user_id": 24605
    }
  ],
  "badges": [
    { "id": 1, "name": "Basic", "description": "Granted all essential community functions", "badge_type_id": 3, "slug": "basic" },
    { "id": 24, "name": "Anniversary", "description": "Active member for a year, posted at least once", "badge_type_id": 2, "slug": "anniversary" }
  ],
  "badge_types": [
    { "id": 3, "name": "Bronze" },
    { "id": 2, "name": "Silver" }
  ]
}
```

### 6.2 Directory Items (Community Leaderboard)
- **Method:** `GET`
- **Endpoint:** `/directory_items.json`
- **Query Parameters:**
  - `period`: `daily` | `weekly` | `monthly` | `quarterly` | `yearly` | `all`
  - `order`: `posts` | `likes_received` | `likes_given` | `topics_entered` | `days_visited` | `solutions`
  - `page`: integer page offset
- **Sample Item:**
```json
{
  "directory_items": [
    {
      "id": 24605,
      "likes_received": 52,
      "likes_given": 12,
      "topic_count": 1,
      "post_count": 83,
      "topics_entered": 525,
      "posts_read": 2887,
      "days_visited": 301,
      "solutions": 23,
      "gamification_score": 698,
      "time_read": 66585,
      "user": {
        "id": 24605,
        "username": "23f3002782",
        "name": "Agrim Srivastava",
        "title": "Course TA",
        "primary_group_name": "ds-students"
      }
    }
  ]
}
```

---

## 7. Private Messages & Chat

### 7.1 Private Messages (PMs)
- **Inbox:** `GET /topics/private-messages/{username}.json?page=0`
- **Sent:** `GET /topics/private-messages-sent/{username}.json?page=0`
- **Archive:** `GET /topics/private-messages-archive/{username}.json?page=0`

### 7.2 Discourse Chat
- **List Channels:** `GET /chat/api/me/channels`
- **Fetch Channel Messages:** `GET /chat/api/channels/{channel_id}/messages?page_size=30`
- **Sample Message Item:**
```json
{
  "messages": [
    {
      "id": 298860,
      "chat_channel_id": 18966,
      "message": "come back soon...",
      "created_at": "2026-06-18T16:42:19Z",
      "user": {
        "id": 36240,
        "username": "Yashvi",
        "name": "24f2007780"
      }
    }
  ]
}
```

---

## 8. Search Endpoint

- **Method:** `GET`
- **Endpoint:** `/search.json`
- **Query Parameter:** `q`
- **Useful Filters:**
  - `user:{username}`: Returns posts authored by user.
  - `@username`: Mentions of user.
  - `in:bookmarks`: Search bookmarks.
  - `in:messages`: Search PMs.
  - `status:solved`: Solved topics.
- **Example Request:**
  ```http
  GET /search.json?q=user:23f3002782
  ```

---

## 9. Write & Mutation Endpoints

### 9.1 Create Post / Reply
- **Method:** `POST`
- **Endpoint:** `/posts.json`
- **Payload (Reply):**
```json
{
  "raw": "This is the reply content.",
  "topic_id": 216448,
  "reply_to_post_number": 3
}
```
- **Payload (New Topic):**
```json
{
  "raw": "Topic introduction and body...",
  "title": "Discussion Topic Title",
  "category": 34,
  "tags": ["clarification", "term1-2026"]
}
```

### 9.2 Edit Post
- **Method:** `PUT`
- **Endpoint:** `/posts/{post_id}.json`
- **Payload:**
```json
{
  "post": {
    "raw": "Updated text...",
    "edit_reason": "Fix typo"
  }
}
```

### 9.3 Like / Unlike Post
- **Like:** `POST /post_actions.json`
  - Payload: `{"id": 841607, "post_action_type_id": 2}`
- **Unlike:** `DELETE /post_actions/{post_id}.json?post_action_type_id=2`

---

## 10. Python Client Example

Below is a complete Python script demonstrating how to interact with these endpoints using session cookies:

```python
import requests

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
USERNAME = "23f3002782"

# Session setup
session = requests.Session()
session.headers.update({
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

# Add cookies from Chrome Profile
session.cookies.set("_t", "<YOUR_AUTH_TOKEN>", domain="discourse.onlinedegree.iitm.ac.in")
session.cookies.set("_forum_session", "<YOUR_FORUM_SESSION>", domain="discourse.onlinedegree.iitm.ac.in")

# 1. Fetch current session
res = session.get(f"{BASE_URL}/session/current.json")
current_user = res.json().get("current_user", {})
print(f"Logged in as: {current_user.get('name')} ({current_user.get('username')})")

# 2. Fetch user profile
res = session.get(f"{BASE_URL}/u/{USERNAME}.json")
user_profile = res.json().get("user", {})
print(f"Trust Level: {user_profile.get('trust_level')}, Badges: {user_profile.get('badge_count')}")

# 3. Fetch user summary
res = session.get(f"{BASE_URL}/u/{USERNAME}/summary.json")
summary = res.json().get("user_summary", {})
print(f"Likes: +{summary.get('likes_received')} / -{summary.get('likes_given')}, Solved: {summary.get('solved_count')}")

# 4. Fetch user posts & replies
res = session.get(f"{BASE_URL}/user_actions.json", params={
    "username": USERNAME,
    "offset": 0,
    "filter": "4,5"  # 4 = topics, 5 = replies
})
actions = res.json().get("user_actions", [])
print(f"Retrieved {len(actions)} recent posts/topics")
for a in actions[:5]:
    print(f"- [{a.get('created_at')}] {a.get('title')} (Topic: {a.get('topic_id')}, Post: #{a.get('post_number')})")
```

---

## 11. Quick Reference Cheat Sheet

| Category | Method | Endpoint | Description |
|---|---|---|---|
| **Session** | `GET` | `/session/current.json` | Logged-in user state & unread counts |
| **Profile** | `GET` | `/u/{username}.json` | Complete profile & preferences |
| **Summary** | `GET` | `/u/{username}/summary.json` | Overall statistics & metrics |
| **Card** | `GET` | `/u/{username}/card.json` | Hovercard user preview |
| **Emails** | `GET` | `/u/{username}/emails.json` | Linked email accounts |
| **Activity** | `GET` | `/user_actions.json?username={u}&filter=4,5` | User's posts & replies |
| **Topics** | `GET` | `/topics/created-by/{username}.json` | Topics created by user |
| **Drafts** | `GET` | `/drafts.json` | In-progress drafts |
| **Single Post** | `GET` | `/posts/{post_id}.json` | Raw & cooked post body |
| **Notifications** | `GET` | `/notifications.json` | Notifications list |
| **Mark Read** | `PUT` | `/notifications/mark-read.json` | Clear unread notifications |
| **Bookmarks** | `GET` | `/u/{username}/bookmarks.json` | Bookmarked posts |
| **Badges** | `GET` | `/user-badges/{username}.json` | Badges awarded to user |
| **Directory** | `GET` | `/directory_items.json` | Leaderboard and rank |
| **PMs** | `GET` | `/topics/private-messages/{username}.json` | Private messages inbox |
| **Chat** | `GET` | `/chat/api/me/channels` | Direct message channels |
| **Search** | `GET` | `/search.json?q=user:{username}` | Search user's contributions |
| **Reply** | `POST` | `/posts.json` | Submit a reply or topic |
| **Like** | `POST` | `/post_actions.json` | Like post (`post_action_type_id=2`) |

