#!/usr/bin/env python3
"""
ZEITGEIST '26 — Official Backend Server & Database Engine | IIT Ropar
- Zero-dependency: Uses Python 3 built-in modules (http.server, sqlite3, json).
- Built-in SQLite database (tasks, users, submissions).
- Serves static website files & API endpoints.
- Supports root path '/' or subpath '/bost/zeitgeist/'.
"""

import http.server
import socketserver
import sqlite3
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PORT = int(os.environ.get("PORT", 8000))
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeitgeist.db")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# DATABASE INITIALIZATION
# ==============================================================================
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Users Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        college TEXT,
        phone TEXT,
        role TEXT DEFAULT 'ca',
        status TEXT DEFAULT 'approved',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Tasks Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        points INTEGER NOT NULL DEFAULT 10,
        status TEXT DEFAULT 'open',
        desc TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Task Submissions Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        user_email TEXT,
        user_name TEXT,
        proof_url TEXT,
        notes TEXT,
        status TEXT DEFAULT 'pending',
        points INTEGER DEFAULT 0,
        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Leaderboard Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        college TEXT,
        score INTEGER DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Pre-seed Admin Users if not exist
    admins = [
        ("Organizing Council Admin", "zeitgeist.ca@iitrpr.ac.in", "snWin%738", "IIT Ropar", "admin"),
        ("Parag Gupta (Admin)", "guptaparag101@gmail.com", "12345678", "IIT Ropar", "admin")
    ]
    for name, email, pwd, college, role in admins:
        cur.execute("SELECT id FROM users WHERE email = ?", (email.lower(),))
        if not cur.fetchone():
            cur.execute("""
            INSERT INTO users (name, email, password, college, role, status)
            VALUES (?, ?, ?, ?, ?, 'approved')
            """, (name, email.lower(), pwd, college, role))

    # Pre-seed Default Tasks if empty
    cur.execute("SELECT COUNT(*) FROM tasks")
    if cur.fetchone()[0] == 0:
        default_tasks = [
            ("Task 1 : Social Media Official Banner Story Blitz", 10, "open", "Post the official Zeitgeist '26 poster on your Instagram / WhatsApp stories and tag @zeitgeist.iitrpr."),
            ("Task 2 : Campus WhatsApp Group Dissemination", 15, "open", "Share the festival dates and event link in 3+ active college WhatsApp / Telegram groups."),
            ("Task 3 : Cultural Society Outreach Broadcast", 20, "open", "Share the competition docket with your college's Music, Dance, and Dramatics societies."),
            ("Task 4 : Flash Pre-Registration Drive", 25, "open", "Get 5+ campus peers registered on the Unstop portal for competitive arenas.")
        ]
        for title, points, status, desc in default_tasks:
            cur.execute("INSERT INTO tasks (title, points, status, desc) VALUES (?, ?, ?, ?)", (title, points, status, desc))

    # Pre-seed Leaderboard from ca_extracted.json if empty
    cur.execute("SELECT COUNT(*) FROM leaderboard")
    if cur.fetchone()[0] == 0:
        json_path = os.path.join(BASE_DIR, "ca_extracted.json")
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    cas = json.load(f)
                    for ca in cas:
                        c_name = ca.get("name", "").strip()
                        c_college = ca.get("college", "Campus Ambassador").strip()
                        c_score = int(ca.get("score", 0))
                        if c_name:
                            cur.execute("INSERT OR IGNORE INTO leaderboard (name, college, score) VALUES (?, ?, ?)", (c_name, c_college, c_score))
                print(f"[OK] Pre-seeded {len(cas)} Ambassadors into SQLite leaderboard.")
            except Exception as e:
                print(f"[WARN] Could not seed leaderboard: {e}")

    conn.commit()
    conn.close()
    print(f"[OK] SQLite Database initialized: {DB_FILE}")

init_db()

# ==============================================================================
# HTTP REQUEST HANDLER
# ==============================================================================
class ZeitgeistHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def normalize_path(self):
        p = urllib.parse.urlparse(self.path).path
        # Strip subpath if hosted under /bost/zeitgeist/ or /zeitgeist/
        for prefix in ["/bost/zeitgeist/", "/bost/zeitgeist", "/zeitgeist/", "/zeitgeist", "/zeitgeist-26/", "/zeitgeist-26"]:
            if p.startswith(prefix):
                p = p[len(prefix):]
                if not p.startswith("/"):
                    p = "/" + p
                break
        return p

    def read_json_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 0:
            raw = self.rfile.read(content_length).decode("utf-8")
            try:
                return json.loads(raw)
            except Exception:
                return {}
        return {}

    # ========================== GET REQUESTS ==========================
    def do_GET(self):
        path = self.normalize_path()

        # API: Health Check
        if path == "/api/health":
            return self.send_json({"status": "healthy", "service": "zeitgeist-26-backend", "time": datetime.utcnow().isoformat()})

        # API: Get All Tasks
        if path == "/api/tasks":
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT id, title, points, status, desc FROM tasks ORDER BY id DESC")
            rows = cur.fetchall()
            conn.close()
            tasks = [{"id": r[0], "title": r[1], "points": r[2], "status": r[3], "desc": r[4]} for r in rows]
            return self.send_json({"success": True, "tasks": tasks})

        # API: Get All Submissions (Admin)
        if path == "/api/submissions":
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("""
            SELECT s.id, s.task_id, s.user_email, s.user_name, s.proof_url, s.notes, s.status, s.points, s.submitted_at, t.title
            FROM submissions s
            LEFT JOIN tasks t ON s.task_id = t.id
            ORDER BY s.id DESC
            """)
            rows = cur.fetchall()
            conn.close()
            subs = [{
                "id": r[0], "task_id": r[1], "user_email": r[2], "user_name": r[3],
                "proof_url": r[4], "notes": r[5], "status": r[6], "points": r[7],
                "submitted_at": r[8], "task_title": r[9] or f"Task #{r[1]}"
            } for r in rows]
            return self.send_json({"success": True, "submissions": subs})

        # API: Get Users / Ambassadors List
        if path == "/api/users":
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT id, name, email, college, role, status FROM users WHERE role != 'admin' ORDER BY id DESC")
            rows = cur.fetchall()
            conn.close()
            users = [{"id": r[0], "name": r[1], "email": r[2], "college": r[3], "role": r[4], "status": r[5]} for r in rows]
            return self.send_json({"success": True, "users": users})

        # API: Get Live Leaderboard
        if path == "/api/leaderboard":
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT id, name, college, score FROM leaderboard ORDER BY score DESC, name ASC")
            rows = cur.fetchall()
            conn.close()
            leaderboard = [{
                "rank": idx + 1,
                "id": r[0],
                "name": r[1],
                "college": r[2],
                "score": r[3]
            } for idx, r in enumerate(rows)]
            return self.send_json({"success": True, "leaderboard": leaderboard})

        # Static file fallback
        self.path = path
        return super().do_GET()

    # ========================== POST REQUESTS ==========================
    def do_POST(self):
        path = self.normalize_path()
        body = self.read_json_body()

        # API: User Login
        if path == "/api/auth/login":
            email = body.get("email", "").strip().lower()
            password = body.get("password", "").strip()

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT id, name, email, college, role, status FROM users WHERE email = ? AND password = ?", (email, password))
            row = cur.fetchone()
            conn.close()

            if row:
                return self.send_json({
                    "success": True,
                    "user": {
                        "id": row[0],
                        "name": row[1],
                        "email": row[2],
                        "college": row[3],
                        "role": row[4],
                        "status": row[5]
                    }
                })
            else:
                return self.send_json({"success": False, "message": "Invalid email or password credentials."}, status=401)

        # API: User Signup
        if path == "/api/auth/signup":
            name = body.get("name", "").strip()
            email = body.get("email", "").strip().lower()
            password = body.get("password", "").strip()
            college = body.get("college", "").strip()
            phone = body.get("phone", "").strip()

            if not email or not password or not name:
                return self.send_json({"success": False, "message": "Missing required fields."}, status=400)

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            try:
                cur.execute("""
                INSERT INTO users (name, email, password, college, phone, role, status)
                VALUES (?, ?, ?, ?, ?, 'ca', 'approved')
                """, (name, email, password, college, phone))
                conn.commit()
                uid = cur.lastrowid
                conn.close()
                return self.send_json({
                    "success": True,
                    "user": {
                        "id": uid,
                        "name": name,
                        "email": email,
                        "college": college,
                        "role": "ca",
                        "status": "approved"
                    }
                })
            except sqlite3.IntegrityError:
                conn.close()
                return self.send_json({"success": False, "message": "This email is already registered."}, status=409)

        # API: Admin Create Task
        if path == "/api/tasks":
            title = body.get("title", "").strip()
            desc = body.get("desc", "").strip()
            points = int(body.get("points", 10))
            status = body.get("status", "open")

            if not title:
                return self.send_json({"success": False, "message": "Title is required."}, status=400)

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("INSERT INTO tasks (title, points, status, desc) VALUES (?, ?, ?, ?)", (title, points, status, desc))
            conn.commit()
            tid = cur.lastrowid
            conn.close()

            return self.send_json({
                "success": True,
                "task": {"id": tid, "title": title, "points": points, "status": status, "desc": desc}
            })

        # API: Toggle Task Status
        if path == "/api/tasks/toggle":
            tid = body.get("id")
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT status FROM tasks WHERE id = ?", (tid,))
            row = cur.fetchone()
            if row:
                new_status = "closed" if row[0] == "open" else "open"
                cur.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, tid))
                conn.commit()
                conn.close()
                return self.send_json({"success": True, "new_status": new_status})
            conn.close()
            return self.send_json({"success": False, "message": "Task not found."}, status=404)

        # API: Delete Task
        if path == "/api/tasks/delete":
            tid = body.get("id")
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("DELETE FROM tasks WHERE id = ?", (tid,))
            conn.commit()
            conn.close()
            return self.send_json({"success": True, "deleted_id": tid})

        # API: Submit Task Proof
        if path == "/api/submissions":
            task_id = body.get("task_id")
            user_email = body.get("user_email", "").strip().lower()
            user_name = body.get("user_name", "").strip()
            proof_url = body.get("proof_url", "").strip()
            notes = body.get("notes", "").strip()

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("""
            INSERT INTO submissions (task_id, user_email, user_name, proof_url, notes, status)
            VALUES (?, ?, ?, ?, ?, 'pending')
            """, (task_id, user_email, user_name, proof_url, notes))
            conn.commit()
            sid = cur.lastrowid
            conn.close()

            return self.send_json({"success": True, "submission_id": sid})

        # API: Approve / Reject Submission
        if path == "/api/submissions/review":
            sub_id = body.get("submission_id")
            status = body.get("status", "approved") # approved / rejected
            points = int(body.get("points", 0))

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            cur.execute("SELECT user_name FROM submissions WHERE id = ?", (sub_id,))
            s_row = cur.fetchone()
            cur.execute("UPDATE submissions SET status = ?, points = ? WHERE id = ?", (status, points, sub_id))

            # If approved with points, auto-credit to leaderboard
            if status == "approved" and points > 0 and s_row and s_row[0]:
                u_name = s_row[0].strip()
                cur.execute("SELECT id, score FROM leaderboard WHERE LOWER(name) = LOWER(?)", (u_name,))
                l_row = cur.fetchone()
                if l_row:
                    cur.execute("UPDATE leaderboard SET score = score + ? WHERE id = ?", (points, l_row[0]))
                else:
                    cur.execute("INSERT INTO leaderboard (name, college, score) VALUES (?, 'Campus Ambassador', ?)", (u_name, points))

            conn.commit()
            conn.close()
            return self.send_json({"success": True, "submission_id": sub_id, "status": status})

        # API: Save Leaderboard / Update Points (Admin)
        if path == "/api/leaderboard":
            items = body.get("items", [])
            if not items and "name" in body:
                items = [body]

            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            for it in items:
                name = it.get("name", "").strip()
                score = int(it.get("score", 0))
                college = it.get("college", "").strip()
                if name:
                    cur.execute("SELECT id FROM leaderboard WHERE LOWER(name) = LOWER(?)", (name,))
                    row = cur.fetchone()
                    if row:
                        if college:
                            cur.execute("UPDATE leaderboard SET score = ?, college = ? WHERE id = ?", (score, college, row[0]))
                        else:
                            cur.execute("UPDATE leaderboard SET score = ? WHERE id = ?", (score, row[0]))
                    else:
                        cur.execute("INSERT INTO leaderboard (name, college, score) VALUES (?, ?, ?)", (name, college or 'Campus Ambassador', score))

            conn.commit()
            conn.close()
            return self.send_json({"success": True, "message": "Leaderboard points updated successfully."})

        return self.send_json({"error": "Endpoint not found"}, status=404)

# ==============================================================================
# MAIN RUNNER
# ==============================================================================
if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), ZeitgeistHandler) as httpd:
        print(f"\n==================================================")
        print(f"🩸 ZEITGEIST'26 OFFICIAL SERVER RUNNING ON PORT {PORT}")
        print(f"• Local access: http://localhost:{PORT}")
        print(f"• Reverse Proxy root: /bost/zeitgeist/")
        print(f"• SQLite Database: {DB_FILE}")
        print(f"==================================================\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            httpd.server_close()
