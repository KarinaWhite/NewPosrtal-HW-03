import os
from celery import Celery
from celery.schedules import crontab  # <--- Проверь 'from' здесь!

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_signup.settings')

app = Celery('simple_signup')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'simpleapp.tasks.weekly_newsletter',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}