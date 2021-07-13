from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r


class AccountsCreateViewTest(TestCase):
    fixtures = ['user.json','group.json']

    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('accounts:create'))

    def test_get_as_gestor(self):
        """GET tickets:create must return status code 200"""
        self.assertEqual(200, self.response.status_code)
