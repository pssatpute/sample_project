from django.core import validators
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core import validators


def validate_first_name(first_name):
    if re.fullmatch('^[A-Z][a-z]+$', first_name) is None:
        raise ValidationError(
            _('First name only allows letters. It should be like Ex. Pradnya, Akshay'),
            code='Invalid'
        )
    return first_name


def validate_last_name(last_name):
    if re.fullmatch('^[A-Z][a-z]+$', last_name) is None:
        raise ValidationError(
            _('Last name only allows letters. Should be like Ex. Satpute, Bamane'),
            code='Invalid'
        )
    return last_name


def validate_city(city):
    city = str(city).lower()
    if re.fullmatch('^[a-z]+$', city) is None:
        raise ValidationError(
            _('City allows only letters'),
            code='Invalid'
        )
    return city


def validate_phone_number(phone_number):
    phone_number = str(phone_number)
    if phone_number.isdigit():
        if re.fullmatch('^([0])?([7-9][0-9]{9})$', phone_number) is None:
            raise ValidationError(
                _('Enter a valid Mobile Number(e.g 08345624986 or 8345624986)'),
                code='Invalid'
            )
    else:
        raise ValidationError(
            _('Phone Number only allows digits.(0-9)'),
        )
    return phone_number


def validate_email(email_id):
    return validators.EmailValidator(message='Enter a valid Email Address',
                                     code='Invalid',
                                     whitelist=['gmail', 'yahoo'])