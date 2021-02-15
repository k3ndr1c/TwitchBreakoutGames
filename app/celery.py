from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from twitch import tasks

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', include=['twitch.tasks'])

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(3000.0, create_new_timebucket)
    
app.conf.beat_schedule = {
 "run-me-every-300-seconds": {
 "task": "twitch.tasks.create_new_timebucket",
 "schedule": 300.0
 }
}

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

'''
Results can also be disabled for individual tasks by
setting the @task(ignore_result=True) option.
'''
