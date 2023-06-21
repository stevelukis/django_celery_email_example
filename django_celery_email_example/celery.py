import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "django_celery_email_example.settings")

app = Celery('django_celery_email_example')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
