from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestBase(TestCase):
    USER_DATA = {
        'email': 'test_user@opmarch.com',
        'password': 'test',
        'is_superuser': True,
    }

    def _create_superuser(self):
        return UserModel.objects.create_user(**self.USER_DATA)
