from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        date TEXT,
        topic TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                        (name, email, password))
            conn.commit()
            conn.close()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("login"))
        except:
            conn.close()
            flash("An account with this email already exists. Please log in or use a different email.", "danger")
            return redirect(url_for("register"))

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()

        conn.close()

        if user:
            session["user"] = user[1]
            flash(f"Welcome back, {user[1]}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

# ---------------- PROJECT PAGES ----------------
@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/satellites")
def satellites():
    return render_template("satellites.html")

@app.route("/members")
def members():
    return render_template("members.html")

# ---------------- BOOK ----------------
@app.route("/book", methods=["GET", "POST"])
def book():
    if "user" not in session:
        flash("You must be logged in to book a session. Please log in or register first.", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        name = session["user"]
        date = request.form["date"]
        topic = request.form["topic"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute("INSERT INTO bookings (user, date, topic) VALUES (?, ?, ?)",
                    (name, date, topic))
        conn.commit()
        conn.close()

        return redirect(url_for("success"))

    return render_template("book.html")

# ---------------- SUCCESS ----------------
@app.route("/success")
def success():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)