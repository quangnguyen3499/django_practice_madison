from celery.utils.log import get_task_logger
from celery.schedules import crontab
from .celery import app

logger = get_task_logger(__name__)

@app.on_after_configure.connect
def invoice_reminder_task(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=7, minute=1, day_of_month=31),
    )

@app.task
def test():
    print("test")
