from OPM_arch_Project.clients_app.forms import ClientsCreateForm
from tests.test_base import TestBase


class ClientsCreateFormTestCase(TestBase):

    def test_clients_create_form_when_no_website__returns_false(self):
        valid_telephone_number = '05090550909'
        valid_client_data = {
            'name': 'TestClient',
            'country': 'TestCountry',
            'city': 'TestCity',
            'street_name': 'TestStreet',
            'street_number': '55',
            'website': '',
            'telephone_number': valid_telephone_number,
        }

        form = ClientsCreateForm(data=valid_client_data)

        self.assertFalse(form.is_valid())

    def test_clients_create_form_when_valid_telephone_number__returns_true(self):
        valid_telephone_number = '05090550909'
        valid_client_data = {
            'name': 'TestClient',
            'country': 'TestCountry',
            'city': 'TestCity',
            'street_name': 'TestStreet',
            'street_number': '55',
            'website': 'test.web',
            'telephone_number': valid_telephone_number,
        }

        form = ClientsCreateForm(data=valid_client_data)

        self.assertTrue(form.is_valid())

    def test_clients_create_form_when_invalid_telephone_number__returns_false(self):
        invalid_telephone_number = 'a05090550909'
        invalid_client_data = {
            'name': 'TestClient',
            'country': 'TestCountry',
            'city': 'TestCity',
            'street_name': 'TestStreet',
            'street_number': '55',
            'website': 'test.web',
            'telephone_number': invalid_telephone_number,
        }

        form = ClientsCreateForm(data=invalid_client_data)

        self.assertFalse(form.is_valid())