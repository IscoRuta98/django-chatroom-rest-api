# Django REST API Project

This repository contains a Django project with a REST API for user accounts and chat messages, along with database integration and Dockerization. Follow the steps below to set up, configure, and run the application.

## Configure the project on your local machine

### Step 1: Project Setup

1. Clone the repository to your local machine.
```
git clone <repository_url>
cd <project_directory>
```

2. Create and activate a virtual environment.
```
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

3. Install project dependencies.
```
pip install -r requirements.txt
```

### Step 2: Django Configuration

1. Set up the Django project.
```
python manage.py migrate
```

2. Create a superuser for administration.
```
python manage.py createsuperuser.
```

3. Run the development server.
```
python manage.py runserver
```

4. Access the Django admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

### Step 3: API Endpoints
Explore the following API endpoints:
- User Registration: POST /register/
- User Login: POST /login/
- User Logout: POST /logout/
- Send Chat Message: POST /send-chat-message/
- Get Chat History: GET /get-chat-history/`<receiver_username>`/

## Running the project on docker.

1. Make sure Docker and Docker Compose on your machine.

2. Once docker is running, access the application at `http://127.0.0.1:8000/`.