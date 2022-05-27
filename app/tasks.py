from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task
def mail_for_me():
    time.sleep(5)
    send_mail(
        'Mail from celery',
        'bla bla bla',
        '9pedobear@gmail.com',
        ['kayratsagynbekov@gmail.com'],
        fail_silently=True,
    )
    return 'Ready'