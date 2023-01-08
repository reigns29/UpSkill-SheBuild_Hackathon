from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# from django_celery_beat.models import PeriodicTask, PeriodicTasks
# from django_cron import crontab

email_user = ""

# @periodic_task(
# run_every=(crontab(hour=3, minute=34)), #runs exactly at 3:34am every day
# name="Dispatch_scheduled_mail",
# reject_on_worker_lost=True,
# ignore_result=True)
def schedule_mail():
    message = render_to_string('app/schedule_mail.html')
    mail_subject = 'Scheduled Email'
    to_email = email_user
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()