import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_training.settings")

app = Celery("student_manager")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.test',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

app.conf.timezone = 'UTC'
