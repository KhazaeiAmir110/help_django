from django.test import TestCase, Client
from django.urls import reverse
from apps.home.views import UserRegisterView


class TestUserRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GTE(self):
        response = self.client.get(reverse('home:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home:register.html')
        self.failUnless(response.context['form'], UserRegisterView)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('home:user_register'), data={})
