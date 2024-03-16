from django.core.exceptions import ValidationError


def check_only_digits(value):
    is_valid = all(x.isdigit() for x in value)

    if not is_valid:
        raise ValidationError("Only digits are allowed")
