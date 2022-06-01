from commons.middlewares.sms import M360
from django_training import settings
from django.core.mail import send_mail
from rest_framework.response import Response

sms = M360()

def send_mail_service(*, email: str, content: str):
    subject = content
    body = ""
    to = [email]

    send_mail(subject, body, settings.EMAIL_HOST_USER, to)

def send_user_otp(*, mobile_number: str):
    try:
        sms.send(mobile=mobile_number, message="test message")
    except Exception:
        return Response({"fail"})
