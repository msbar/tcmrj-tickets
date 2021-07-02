from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r


class HomeAsGestorTest(TestCase):
    fixtures = ['user.json','group.json']

    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.client.force_login(self.user)

        self.response = self.client.get(r('core:home'))

    def test_ticket_create_link_as_gestor(self):
        """Must have tickets create link"""
        expected = 'href="{}"'.format(r('tickets:create'))
        self.assertContains(self.response, expected)
    
    def test_ticket_list_link_as_gestor(self):
        """Must have tickets list link"""
        expected = 'href="{}"'.format(r('tickets:list'))
        self.assertContains(self.response, expected)
          
    def test_gerenciamento_link_as_gestor(self):
        """Must have tickets gerenciamento link"""
        expected = 'href="{}"'.format(r('core:gerenciamento'))
        self.assertContains(self.response, expected)
    
    def test_group_data_as_gestor(self):
        """Must have group name gestor data in template"""
        expected = '<span>{}</span>'.format(self.user.groups.all()[0])
        self.assertContains(self.response, expected)
    
