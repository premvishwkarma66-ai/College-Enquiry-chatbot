from flask import Flask, request, jsonify, render_template, session, redirect
from chatbot.faq_cache import load_faq_cache
from chatbot.nlp_engine import process_user_message
from core.db import get_db

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "college_chatbot_secure_key"

#HOME(CHATBOT)
@app.route("/")
def home():
    return render_template("chatbot.html")


#LOGIN(ADMIN + USER)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM users
            WHERE email=? AND password=?
        """, (email, password))

        user = cur.fetchone()
        conn.close()

        if not user:
            return render_template("login.html", error="Invalid credentials")

        session["user_id"] = user["id"]
        session["role"] = user["role"]

        if user["role"] == "admin":
            return redirect("/admin/dashboard")
        else:
            return redirect("/")

    return render_template("login.html")


#ADMIN DASHBOARD
@app.route("/admin/dashboard")
def admin_dashboard():
    if "role" not in session or session["role"] != "admin":
        return redirect("/login")

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT user_query, bot_reply, intent, confidence, created_on
        FROM enquiry_logs
        ORDER BY id DESC
    """)
    logs = cur.fetchall()
    conn.close()

    return render_template("admin/dashboard.html", logs=logs)


#CHATAPI
@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    user_message = data.get("message", "")

    reply, meta = process_user_message(user_message)

    return jsonify({
        "reply": reply,
        "intent": meta.get("intent"),
        "confidence": meta.get("confidence")
    })

#LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    load_faq_cache()
    app.run(debug=True)

