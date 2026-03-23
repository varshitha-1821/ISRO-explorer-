from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- SATELLITE DATABASE ---------------- #

satellites = [
    {
        "name": "Chandrayaan",
        "year": "2008",
        "description": "India's first lunar exploration mission which confirmed the presence of water molecules on the Moon."
    },
    {
        "name": "Mangalyaan",
        "year": "2014",
        "description": "Mars Orbiter Mission that made India the first country to reach Mars orbit on its first attempt."
    },
    {
        "name": "Gaganyaan",
        "year": "2025",
        "description": "India’s upcoming human spaceflight mission to send astronauts into space."
    },
    {
        "name": "Cartosat",
        "year": "2005",
        "description": "Earth observation satellite used for mapping, urban planning and infrastructure monitoring."
    },
    {
        "name": "RISAT",
        "year": "2009",
        "description": "Radar Imaging Satellite used for surveillance and disaster monitoring."
    }
]

# ---------------- ROUTES ---------------- #

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/satellites', methods=["GET", "POST"])
def satellites_page():

    results = None

    if request.method == "POST":

        query = request.form["search"].lower()

        results = []

        for sat in satellites:
            if query in sat["name"].lower() or query in sat["year"]:
                results.append(sat)

    return render_template("satellites.html", results=results)


@app.route('/members')
def members():
    return render_template("members.html")


@app.route('/book', methods=["GET","POST"])
def book():

    message = None

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        date = request.form["date"]

        message = f"Session booked successfully for {name} on {date}"

    return render_template("book.html", message=message)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)