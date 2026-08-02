from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'مدیر ارشد'
        MANAGER = 'manager', 'مدیر'
        M88_OFFICER = 'm88_officer', 'کارشاس ماده 88'
        M5_OFFICER = 'm5_officer', 'کارشناس امور باشگاه ها'
        INSURANCE_OFFICER = 'insurance_officer', 'کارشناس بیمه'
        SPORT_OFFICER = 'sport_officer', 'کارشناس ورزش'
        FEDERATION_REP = 'federation_rep', 'هیات ورزشی'

    role = models.CharField(max_length=30, choices=Role.choices, default=Role.SPORT_OFFICER)
