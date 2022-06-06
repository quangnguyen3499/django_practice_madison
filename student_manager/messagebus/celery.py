import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_training.settings")

app = Celery("student_manager")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send_email_invoice': {
#         'task': 'tasks.send_invoice',
#         'schedule': 30.0,
#         'args': (16,16)
#     },
#     'create_monthly_invoice': {
#         'task': 'tasks.create_invoice',
#         'schedule': crontab(0, 0, day_of_month='28'),
#     },
# }

app.conf.timezone = 'UTC'
