from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def _send_mail_course_update(recipient_list):
    send_mail(
        subject='Обновление курса',
        message=f'Обновление курса',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_list]
    )
