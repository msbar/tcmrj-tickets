from django.test import TestCase
from django.contrib.auth.models import User
from tcmrj_tickets.category.models import Category
from django.shortcuts import resolve_url as r


class CategoryModelTest(TestCase):
    fixtures = ['user.json','group.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

        self.category = Category.objects.create(
            name = 'Ar-condicionado',
            created_by = self.user,
        )

    def test_create(self):
        """Must have exist category object"""
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual('Ar-condicionado', str(self.category))

    def test_get_absolute_url(self):
        url = r('category:detail', self.category.id)
        self.assertEqual(url, self.category.get_absolute_url())