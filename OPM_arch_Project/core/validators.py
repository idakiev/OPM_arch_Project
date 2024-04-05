from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def check_only_digits(value):
    is_valid = all(x.isdigit() for x in value)

    if not is_valid:
        raise ValidationError("Only digits are allowed")


def validate_file_size(file):
    max_file_size_in_mb = 1024 * 1024 * 10

    if file.size > max_file_size_in_mb:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
