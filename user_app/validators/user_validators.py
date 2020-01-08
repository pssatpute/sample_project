from django.core import validators
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


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
    if re.fullmatch('^[a-z][A-Z]+$', city) is None:
        raise ValidationError(
            _('City allows only characters'),
            code='Invalid'
        )
    return city