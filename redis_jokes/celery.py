import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redis_jokes.settings")

app = Celery("redis_jokes")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery scheduler
app.conf.beat_schedule = {
    "get_joke_5s": {
        "task": "jokes.tasks.get_joke",
        "schedule": 5.0
    }
}

app.autodiscover_tasks()

