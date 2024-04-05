import string
import random

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def generate_verification_code(length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    verification_code = ''
    for _ in range(length):
        verification_code += random.choice(characters)
    return verification_code


def send_verification_email(email, verification_code):
    context = {
        'user_email': email,
        'verification_code': verification_code
    }

    subject = 'Verification Code'
    html_message = render_to_string('core/email_with_verification.html', context=context)
    message = strip_tags(html_message)
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(
        subject=subject,
        message=message,
        from_email=sender_email,
        recipient_list=recipient_list,
        html_message=html_message,
    )
