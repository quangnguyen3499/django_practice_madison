from celery.utils.log import get_task_logger
from .celery import app
from student_manager.users.services import send_mail_service

logger = get_task_logger(__name__)

@app.task(name="send_invoice", bind=True, default_retry_delay=300, max_retries=5)
def send_invoice(message, email):
    email = "hicole1609@oceore.com"
    print("sent")
    send_mail_service(email=email, subject="Monthly Invoice", message=message)

# @app.task(name="create monthly invoice")
# def create_monthly_invoice():
    