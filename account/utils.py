from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    context = {
        'text_detail': 'you\'re registered',
        'email': email,
        'domain': 'http://localhost:8000/',
        'activation_code': activation_code,
    }
    html_message = render_to_string('activation.html', context)
    message = strip_tags(html_message)
    send_mail(
        'Account activation',
        message,
        'edgarpo0401@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=False
    )
