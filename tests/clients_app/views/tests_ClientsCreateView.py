from django.urls import reverse

from tests.test_base import TestBase


class ClientsCreateViewTests(TestBase):

    def test_get_create__when_logged_in_user__expect_200(self):

        self._create_superuser()
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse('clients_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clients_app/clients_create.html')
