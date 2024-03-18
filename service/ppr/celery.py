import os

import celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ppr.settings")

app = celery.Celery("ppr")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "load_properties": {
        "task": "load_properties",
        "schedule": crontab(hour=8),  # Every day at 8am UTC
        "args": [2],  # Load properties sold in the past 3 months
    }
}
