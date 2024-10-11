import os
from celery import Celery
#from celery import schedules

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backends.settings')

app = Celery('backends')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

"""
app.conf.beat_schedule = {
    'channel_task_runner_crontab': {
        'task': 'channel_task_runner',
        'schedule': schedules.crontab(minute=0, hour='*/12') # every 12 hours
    }
}
"""