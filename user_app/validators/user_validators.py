from django.core import validators

def validate_first_name(first_name):
    return validators.RegexValidator(
        regex='^[A-Z][a-z]+$',
        message='First name is invalid',
        code='Invalid',
        inverse_match=False,
        flags=0
    )