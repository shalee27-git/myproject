# MyProject

A Django project with REST API endpoints, Telegram bot integration, and user authentication.

## Features
- Public and protected API endpoints
- User registration and login (web and API)
- Telegram bot that stores user Telegram usernames
- Celery integration for background tasks

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/shalee27-git/myproject.git
cd myproject
```

### 2. Create and activate a virtual environment
```
python -m venv myenv
myenv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root with the following variables:
```
DEBUG=False
SECRET_KEY=your-django-secret-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

### 5. Apply migrations
```
python manage.py migrate
```

### 6. Run the development server
```
python manage.py runserver
```

### 7. Start Celery worker (optional, for background tasks)
```
celery -A myproject worker --loglevel=info
```

### 8. Run the Telegram bot
```
python core/bot.py
```

## Environment Variables Used
- `DEBUG`: Django debug mode (True/False)
- `SECRET_KEY`: Django secret key
- `TELEGRAM_BOT_TOKEN`: Telegram bot token

## How to Run Locally
1. Follow the setup instructions above.
2. Access the web app at `http://127.0.0.1:8000/`
3. API endpoints are available under `/api/`
4. Telegram bot runs separately with `python core/bot.py`

## API Documentation

### Public Endpoint
- **URL:** `/api/public/`
- **Method:** GET
- **Auth:** None
- **Response:** `{ "message": "Public Access" }`

### Protected Endpoint
- **URL:** `/api/protected/`
- **Method:** GET
- **Auth:** Token or JWT required
- **Response:** `{ "message": "Protected Access" }`

### Register Endpoint
- **URL:** `/api/register/`
- **Method:** POST
- **Body:** `{ "username": "", "email": "", "password": "" }`
- **Response:** Success or error message

### Login (Web)
- **URL:** `/login/`
- **Method:** GET/POST
- **Description:** Django web login form

## Telegram Bot
- Responds to `/start` command
- Stores Telegram username in the database

---

For more details, see the source code and comments.
