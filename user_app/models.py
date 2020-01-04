from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=10)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email_id'
    # for createsuperuser command will prompt for following
    # REQUIRED_FIELDS = []
