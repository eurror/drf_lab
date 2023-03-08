from .utils import send_activation_code, send_recovery_code
from drf.celery import app


@app.task
def send_activation_code_celery(email, activation_code):
    send_activation_code(email, activation_code)

@app.task
def send_recovery_code_celery(email, activation_code):
    send_recovery_code(email, activation_code)
