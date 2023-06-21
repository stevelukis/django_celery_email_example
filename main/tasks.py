from celery import shared_task
from django.core.mail import send_mail

from main import models


@shared_task
def send_newsletter(subject, body):
    recipients = [user.email for user in models.User.objects.all()]

    send_mail(subject=subject,
              message=body,
              from_email="no-reply@store.com",
              recipient_list=recipients)
