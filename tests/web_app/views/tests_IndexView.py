from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.client import Client
from tests.test_base import TestBase

UserModel = get_user_model()


class IndexViewTests(TestBase):
    def setUp(self):
        self.test_client = Client()

    def test_get_index__when_not_logged_in__expect_200(self):

        response = self.test_client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/index.html')

    def test_get_index__when_logged_in__expect_200(self):
        self._create_superuser()
        self.test_client.login(**self.USER_DATA)

        response = self.test_client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web_app/index.html')
