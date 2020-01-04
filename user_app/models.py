from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

GENDER_OPTIONS = [
    ('female', 'Female'),
    ('male', 'Male')
]


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS, default=GENDER_OPTIONS[0][0])
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email_id'
    # for createsuperuser command will prompt for following
    # REQUIRED_FIELDS = []

    is_active = models.BooleanField(
        _('is_active'),
        default=True,
        help_text=_(
            "Desinates whether this user should be considered active or not."
        ),
    )

    # permissions for accessing admin page
    is_staff = models.BooleanField(
        _('is_staff'),
        default=False,
        help_text=_(
            'Designates whether this user is a member of staff to access the admin page or not'
        )
    )
    is_superuser = models.BooleanField(
        _('is_superuser'),
        default=False,
        help_text=_(
            'Designates whether this user has all permissions in the admin page or not'
        )
    )
