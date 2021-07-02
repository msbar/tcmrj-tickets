from unittest.case import expectedFailure
from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.models import Category


class GetSubcategoryTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

        self.category = Category.objects.get(pk=1)
        self.response = self.client.get(r('category:getsubcategory'), {'pk':self.category.id})

    def test_get(self):
        """GET /categoria/getsubcategory must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    
    def test_json_content(self):
        """ test content json """
        expected = [{"id": 1, "name": "Split"}, {"id": 2, "name": "Janela"}]
        self.assertJSONEqual(self.response.content, expected)
