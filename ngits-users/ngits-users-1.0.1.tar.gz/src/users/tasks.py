from celery import shared_task
from django.contrib.auth import get_user_model

from users.utils import RemindPassword, StandardRegistration

User = get_user_model()


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 5, "countdown": 5},
)
def delete_account(user_id):
    User.objects.get(pk=user_id).delete()


@shared_task()
def send_auth_email(user_id, protocol, host):
    StandardRegistration.send_auth_email(user_id, protocol, host)


@shared_task()
def send_change_password_email(user_email, protocol, host):
    RemindPassword.send_email(user_email, protocol, host)
