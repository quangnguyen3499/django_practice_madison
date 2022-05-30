from django_training import settings
from django.core.mail import send_mail

def send_mail_service(*, email: str, content: str):
    subject = content
    body = ""
    to = [email]

    send_mail(subject, body, settings.EMAIL_HOST_USER, to)
