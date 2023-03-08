# Udemy clone
This app is Udemy clone. In this app you can buy courses and enroll them. Also if you're a mentor you can add, edit and remove your courses.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Udemy clone, but first, create a virtual environment for a project

```bash
# Also you can create virtual environment using conda, virtualenv, poetry etc.
# 1. Install virtual environment
python3 -m venv <name of virtual environment>
# 2. Activate virtual environment
. venv/bin/activate

```
```bash
# Clone this repository to your local machine
git clone git@github.com:eurror/drf_lab.git
```
```bash
# Install dependencies
pip install -r requirements.txt
```

## .env file
Fields to be filled in:
```bash
SECRET_KEY= # django project secret key
DB_NAME= # your database name
DB_USER= # your user of database
DB_PASSWORD= # your user's password
HOST= #localhost or your host otherwise
PORT= #port for postgreSQL, default is 5432
EMAIL_BACKEND= django.core.mail.backends.smtp.EmailBackend # you can leave this settings or edit if you need custom settings
EMAIL_HOST= smtp.gmail.com # you can leave this settings or edit if you need custom settings
EMAIL_PORT= #port
EMAIL_USE_TLS= # True or False
EMAIL_HOST_USER= # your email
EMAIL_HOST_PASSWORD= # password

```

## Usage
After you're done setting up steps above, run celery, redis and django server. You may need only run django server but this way features like sending activation code or recovering password to email won't be available

```bash
# run redis
redis-server
# run celery
celery -A drf worker -l info
# run django server
./manage.py runserver
```
