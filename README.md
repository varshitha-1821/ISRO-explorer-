ISRO Explorer

Project Description:
    ISRO Explorer is a full‑stack web application developed to present information about major missions conducted by the Indian Space Research Organisation (ISRO). The platform allows users to explore well‑known satellite missions, search for satellites using their name or launch year, and learn about important scientists who contributed to India's space program.

    The website is designed with a space‑themed interface and structured navigation so that users can easily move between different sections such as missions, satellites, and scientists. The application also includes a simple booking feature that allows users to schedule a learning session related to ISRO missions.

    From a technical perspective, the project demonstrates the integration of a Flask backend with HTML/CSS frontend templates, along with dynamic data rendering using the Jinja templating engine. The application follows a modular project structure where routes, templates, and static assets are organized separately.

    This project was created as part of a Full Stack Development coursework project, with the objective of implementing both backend functionality and frontend design in a single web application.

Technologies Used:
    Backend
        Python 3
        Flask Framework – used to handle routing, server logic, and page rendering
        Jinja2 Template Engine – used for dynamic HTML rendering

    Frontend
        HTML5 – page structure
        CSS3 – styling and layout
        Bootstrap – responsive layout and UI components

    Custom Fonts – used for headings and navigation styling

    Tools & Development Environment
        Visual Studio Code – development environment
        Git – version control
        GitHub – remote repository hosting
        Python Virtual Environment (venv) – dependency isolation

Key Features:
    The application includes several functional modules:
    1. Mission Exploration
        Displays major ISRO missions such as Chandrayaan and Mangalyaan
        Organized project cards with mission details and images

    2.Satellite Search
        Users can search satellites by name or launch year
        Backend processes the query using Flask routes
        Results are dynamically rendered using Jinja templates
        Displays a "No results found" message for invalid searches

    3.Scientists / Members Page
        Highlights important figures in India’s space program
        Displays brief descriptions of key ISRO scientists
        Authentication Interface
        Includes login and registration pages
        Demonstrates typical authentication UI structure (for full‑stack architecture)

    4.Session Booking Page
        Allows users to book a learning session
        Form submission handled through Flask POST request
        Displays a confirmation message after successful submission

    5.Consistent UI Design
        Dark space‑themed layout
        Yellow and white accent colors for readability
        Hover effects and UI transitions

Project Structure:
    The project follows the standard Flask directory structure:

        ISRO-explorer
        │
        ├── app.py
        │
        ├── templates
        │   ├── base.html
        │   ├── index.html
        │   ├── projects.html
        │   ├── satellites.html
        │   ├── members.html
        │   ├── book.html
        │   ├── login.html
        │   └── register.html
        │
        ├── static
        │   ├── css
        │   │   └── style.css
        │   ├── images
        │   └── fonts
        │
        ├── venv
        └── README.md


Explanation:
    app.py – main Flask application file containing routes and backend logic
    templates/ – HTML pages rendered using the Jinja template engine
    static/ – stores CSS files, fonts, and images used in the UI
    venv/ – Python virtual environment for managing dependencies

Setup Instructions:
Follow these steps to run the project locally.
    1. Clone the repository  --> git clone https://github.com/varshitha-1821/ISRO-explorer.git
    2. Navigate to the project directory  --> cd ISRO-explorer
    3. Create a Python virtual environment  --> python -m venv venv
    4. Activate the virtual environment  --> Windows:venv\Scripts\activate
    5. Install required dependencies --> pip install flask
    6. Run the application --> python app.py
    7. Open the application in your browser --> http://127.0.0.1:5000


Demo Steps:
    Open the Home Page to view the introduction to the ISRO Explorer platform.
    Navigate to the Projects Page to explore important ISRO missions.
    Visit the Satellites Page and search for missions such as Chandrayaan or Mangalyaan.
    Go to the Members Page to learn about scientists involved in India's space program.
    Use the Register and Login pages to access user features.
    Open the Book Session page and submit the form to schedule a learning session.

Future Improvements:
Some features that can be added in future versions include:
    Real user authentication with Flask‑Login
    Mission detail pages for each satellite
    Interactive satellite timeline
    Image gallery for ISRO missions
    Admin dashboard to manage mission data


This project demonstrates how a Flask‑based web application can integrate backend routing, frontend templates, and dynamic search functionality while maintaining a structured project architecture.
