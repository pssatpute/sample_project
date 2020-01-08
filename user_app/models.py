from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers.user_managers import UserManager
from sample_project import settings
from .validators import user_validators
from django.core import validators

GENDER_OPTIONS = [
    ('female', 'Female'),
    ('male', 'Male')
]


class User(PermissionsMixin, AbstractBaseUser):
    "Django's permission framework gives you all the methods and db fields to support permission model"

    phone_number = models.CharField(db_column="Phone Number", max_length=10, unique=True, primary_key=True)
    email_id = models.EmailField(db_column="Email ID", max_length=40, unique=True)
    first_name = models.CharField(db_column="First Name", max_length=15,
                                  validators=[validators.MaxLengthValidator(limit_value=15),
                                              user_validators.validate_first_name])
    last_name = models.CharField(db_column="Last Name", max_length=30,
                                 validators=[validators.MaxLengthValidator(limit_value=20),
                                             user_validators.validate_last_name])
    password = models.CharField(db_column="Password", max_length=200)
    date_of_birth = models.DateField(db_column="Date of Birth", help_text="date format should be YYYY-MM-DD")
    city = models.CharField(db_column="City", max_length=10, validators=[user_validators.validate_city])
    gender = models.CharField(db_column="Gender", max_length=10, choices=GENDER_OPTIONS, default=GENDER_OPTIONS[0][0],
                              help_text="Choose either Female or Male")
    date_joined = models.DateTimeField(db_column="Date Joined", auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email_id'
    # for createsuperuser command will prompt for following
    REQUIRED_FIELDS = ['email_id', 'first_name', 'last_name', 'date_of_birth', 'city', 'gender']

    is_active = models.BooleanField(
        db_column="Is Active",
        default=True,
        help_text=_(
            "Desinates whether this user should be considered active or not."
        ),
    )

    # permissions for accessing admin page
    is_staff = models.BooleanField(
        _('is_staff'),
        db_column='Is Staff',
        default=False,
        help_text=_(
            'Designates whether this user is a member of staff to access the admin page or not'
        )
    )
    is_superuser = models.BooleanField(
        _('is_superuser'),
        db_column='Is Superuser',
        default=False,
        help_text=_(
            'Designates whether this user has all permissions in the admin page or not'
        )
    )

    # custom user model defining username field other than username should define Custom Model Manager
    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    # access of the user to admin content: permissions
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        if self.is_staff or self.is_superuser:
            return True
        else:
            return False

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
