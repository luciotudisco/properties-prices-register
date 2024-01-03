import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ppr.settings")

app = Celery("ppr")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Scheduler Name
    "print-time-twenty-seconds": {
        # Task Name (Name Specified in Decorator)
        "task": "load_properties",
        # Schedule
        "schedule": 20.0,
    },
}
