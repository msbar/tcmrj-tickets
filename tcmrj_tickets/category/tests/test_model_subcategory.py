from django.test import TestCase
from django.contrib.auth.models import User
from tcmrj_tickets.category.models import Category, SubCategory
from django.shortcuts import resolve_url as r


class SubCategoryModelTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json']
    
    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.category = Category.objects.get(pk=1)

        self.subcategory = SubCategory.objects.create(
            category = self.category,
            name = 'Split',
            created_by = self.user
        )

    def test_create(self):
        """Must have exist subcategory object"""
        self.assertTrue(SubCategory.objects.exists())

    def test_str(self):
        self.assertEqual('Split', str(self.subcategory))

    def test_get_absolute_url(self):
        url = r('category:sub_detail', self.subcategory.id)
        self.assertEqual(url, self.subcategory.get_absolute_url())
