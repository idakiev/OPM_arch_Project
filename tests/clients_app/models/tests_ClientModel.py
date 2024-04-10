from django.core.exceptions import ValidationError

from OPM_arch_Project.clients_app.models import Client
from tests.test_base import TestBase


class ClientModelTestCase(TestBase):
    def test_create_client_when_valid_telephone_number__should_create(self):
        valid_telephone_number = '05090550909'
        client = Client(
            name='TestClient',
            country='TestCountry',
            city='TestCity',
            street_name='TestStreet',
            street_number='55',
            telephone_number=valid_telephone_number,
        )

        client.full_clean()
        client.save()

        self.assertIsNotNone(client)

    def test_create_client_when_invalid_telephone_number__should_raise(self):
        invalid_telephone_number = 'a05090550909'
        client = Client(
            name='TestClient',
            country='TestCountry',
            city='TestCity',
            street_name='TestStreet',
            street_number='55',
            telephone_number=invalid_telephone_number,
        )

        with self.assertRaises(ValidationError):
            client.full_clean()
