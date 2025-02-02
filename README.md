# Blog Website with Django

This is a simple blog website built using Django, a high-level Python web framework. The website allows users to create, read, update, and delete blog posts. It also supports image uploads for blog posts.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Create Blog Posts**: Authenticated users can create new blog posts with a title, content, and an optional image.
- **View Blog Posts**: All users can view blog posts on the homepage.
- **Edit and Delete Posts**: Authors can edit or delete their own blog posts.
- **Image Uploads**: Blog posts can include images, which are stored in the `media` directory.
- **Responsive Design**: The website is designed to be responsive and works on both desktop and mobile devices.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default for development)
- **Image Handling**: Pillow library

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation and Setup

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   python -m venv venv
   pip install django
   pip install pillow
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Access the website:
Open your browser and go to http://127.0.0.1:8000/.

Access the admin panel:
Go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.
