# SimpleQ

## Introduction
SimpleQ is an application that enables registered users create and manage a private queue specific to their user account.

Suppose you're a business that deals with clients, you currently have your hands full and so can't accept new clients. Rather than simply turning new clients down, you can add them to the queue, and get back to them as soon as you have an open slot.

I would have called this app 'RevolutionaryQ', but that would have been a stretch...

Queue entry fields include: first name, last name, email, phone number and additional notes.<br>
Database fields are encrypted using django-cryptography.<br> User authentication is built on Django's CustomUser model.


## Usage

Application is hosted and free to use at: https://queueme2.herokuapp.com/

Watch a short demo of the application [here](https://youtu.be/LrhMhWaD0KU).

### How to Install and Run the Application

Create and activate a virtual environment in an empty folder.
```
   python -m venv .venv
   .venv/Scripts/Activate.ps1
```
Clone the project.
```
   git clone https://github.com/pe-et/simpleQ
```
cd into the project folder (same folder as requirements.txt) and install dependencies.
```
   pip install -r requirements.txt
```
Rename .env.example to .env, generate a new secret key and copy/paste to env under SECRET_KEY.
```
   python -c "import secrets; print(secrets.token_urlsafe())"
```
In .env: Add sqlite to DATABASE_URL.
```
   DATABASE_URL=sqlite:///db.sqlite3
```
Option 1, using email service provider:<br>
Using a service for transactional emails such as Sendinblue, SendGrid etc. Obtain your email credentials and add them to the remaining fields in .env.
```
   EMAIL_HOST=
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   DEFAULT_FROM_EMAIL=
   EMAIL_PORT=
```
Option 2, output emails to console:<br>
Remove email credential refs in django_project/settings.py line 145-150, and change EMAIL_BACKEND (line 143) to output emails to console like so:
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```
Make migrations
```
   python manage.py migrate
```
Run the application on a local server
```
   python manage.py runserver
```
Visit 127.0.0.1:8000 in your browser to view the application.

### Built with
[Django](https://www.djangoproject.com/) - a high-level Python web framework.<br>
[Bootstrap](https://getbootstrap.com/) - a CSS framework.<br>
[Sendinblue](https://www.sendinblue.com/) - A transactional email service provider.
