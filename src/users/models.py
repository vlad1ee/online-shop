import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.db.models.signals import post_save


class User(AbstractUser):
    objects = UserManager()
    verification_uuid = models.UUIDField(default=uuid.uuid4)
    verified = models.BooleanField(default=False)
    created_by_template = models.BooleanField(default=False)
    email = models.EmailField(blank=False, null=False)


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.verified and instance.created_by_template:
        print('РАЗ')
        send_mail('Подтвердите свой аккаунт',
        'Перейдите по ссылке ниже:\n'
        'http://localhost:8000'+ str(reverse('verify',
        kwargs={'uuid': str(instance.verification_uuid)})),
        settings.EMAIL_HOST_USER, [instance.email]
        )

post_save.connect(user_post_save, sender=get_user_model())