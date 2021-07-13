from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['user.json','group.json']

    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.client.force_login(self.user)
        self.response = self.client.get(r('core:home'))
        
    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use home.html"""
        self.assertTemplateUsed(self.response, 'core/home.html')
    
    def test_ticket_home_link(self):
        """Must have tickets create link"""
        expected = 'href="{}"'.format(r('core:home'))
        self.assertContains(self.response, expected)
    
    def test_ticket_create_link(self):
        """Must have tickets create link"""
        expected = 'href="{}"'.format(r('tickets:create'))
        self.assertContains(self.response, expected)
    
    def test_ticket_list_link(self):
        """Must have tickets list link"""
        expected = 'href="{}"'.format(r('tickets:list'))
        self.assertContains(self.response, expected)

    def test_username_data(self):
        """Must have username data in template"""
        expected = '<span>{}</span>'.format(self.user.username)
        self.assertContains(self.response, expected)
    
    def test_group_data(self):
        """Must have group name data in template"""
        expected = '<span>{}</span>'.format(self.user.groups.all()[0])
        self.assertContains(self.response, expected)
    
    def test_logout_link(self):
        """Must have tickets list link"""
        expected = 'href="{}"'.format(r('accounts:logout'))
        self.assertContains(self.response, expected)
