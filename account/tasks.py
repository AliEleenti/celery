from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Acrivate account, asdasd'
    send_mail('Activate account', message, 'iceime302@gmaail.com', [email])
    return 'Sended'