from django.test import TestCase
from apps.home.forms import UserRegistrationForm
from apps.users.models import User


class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('amin', 'amin@gmail.com', 'aminpass')

    def test_valid_data(self):
        form = UserRegistrationForm(
            data={'username': 'amir', 'email': 'amir@gmail.com', 'password1': 'amirpass',
                  'password2': 'amirpass'})
        self.assertTrue(form.is_valid(), "register success")

    def test_empty_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid(), 'error in register')
        self.assertEqual(len(form.errors), 4)
