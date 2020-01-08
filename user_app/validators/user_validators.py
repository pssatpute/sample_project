from django.core import validators
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_first_name(first_name):
    if re.fullmatch('^[A-Z][a-z]+$', first_name) is None:
        raise ValidationError(
            _('First name is invalid. Should be like Ex. Pradnya, Akshay'),
            code='Invalid'
        )
    return first_name
