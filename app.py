from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("login.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Satellites Page
@app.route("/satellites")
def satellites():
    return render_template("satellites.html")

# Members Page
@app.route("/members")
def members():
    return render_template("members.html")

# Booking Page
@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        return redirect(url_for("success"))
    return render_template("book.html")

# Success Page
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)