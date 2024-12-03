Saviours 🚨

Saviours is a problem reporting and SOS platform that connects citizens with authorities to address emergencies and incidents in real time. The platform allows users to report problems to concerned authorities, such as the police, while also enabling quick SOS alerts during critical situations. Built using Django, it provides an intuitive interface for both users and responders.
Features 🛠️

    Problem Reporting
        Users can report incidents (e.g., crimes, accidents, hazards) to the relevant authorities.
        Reports include detailed descriptions, categories, and optional media attachments.

    SOS System
        Quick SOS alerts for emergencies, notifying authorities immediately.

    Authority Dashboard
        Allows concerned authorities to view, manage, and respond to reports effectively.

    User-Friendly Interface
        Easy-to-use reporting forms for citizens.
        Notifications for report updates and resolutions.

    Secure Authentication
        Role-based access for users and authorities.
        Secure login, registration, and session management.

    Geolocation Integration (optional)
        Allows users to share their location for faster assistance.

Tech Stack 🖥️

    Backend: Django
    Frontend: Django Templates
    Database: SQLite (default) / PostgreSQL (for production)
    Optional Features: Google Maps API for geolocation

Installation and Setup ⚙️
Prerequisites

Ensure you have the following installed:

    Python 3.8+
    pip
    A virtual environment manager (e.g., venv)

Steps

    Clone the Repository

git clone https://github.com/dashing-dev/Saviours.git
cd Saviours

Create and Activate a Virtual Environment

python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

Install Dependencies

pip install -r requirements.txt

Run Migrations

python manage.py makemigrations
python manage.py migrate

Start the Development Server

    python manage.py runserver

    Access the Application
    Open your browser and navigate to http://127.0.0.1:8000.

Project Structure 📂

Saviours/
├── reporting/           # Django app for problem reporting and SOS
├── templates/           # HTML templates
├── static/              # Static files (CSS, JavaScript, images)
├── saviours/            # Main Django project folder
├── manage.py            # Django CLI utility
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

Usage 🚀
For Users

    Register or log in to the platform.
    Use the reporting form to describe and submit issues.
    Trigger an SOS alert if immediate assistance is required.

For Authorities

    Log in using an authority account.
    View and manage incoming reports and alerts via the dashboard.
    Update report statuses and notify users of actions taken.

Contributions 🤝

Contributions are welcome! Please fork the repository, make changes, and submit a pull request. You can also open issues for suggestions and bug fixes.
License 📜

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments 💡

    Designed to assist authorities in responding to community-reported issues.
    Built with Django for scalability and reliability.

