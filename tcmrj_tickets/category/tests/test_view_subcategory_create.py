from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.forms import SubCategoryForm
from tcmrj_tickets.category.models import Category, SubCategory


class SubCategoryCreateViewTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('category:sub_create'))

    def test_get_as_gestor(self):
        """GET /subcategoria/create must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_get_as_suporte(self):
        """GET /subcategoria/create must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_create'))
        self.assertEqual(403, self.response.status_code)

    def test_get_as_padrao(self):
        """GET /subcategoria/create must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_create'))
        self.assertEqual(403, self.response.status_code)
    
    def test_template(self):
        """Must use subcategory_form.html"""
        self.assertTemplateUsed(self.response, 'subcategory/subcategory_form.html')

    def test_voltar_category_list_link(self):
        """Must have subcategory:list link"""
        expected = 'href="{}"'.format(r('category:sub_list'))
        self.assertContains(self.response, expected)

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
			    ('<input', 2),
                ('<select', 1),
                ('type="text"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have SubCategoryForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubCategoryForm)

    
class SubCategoryCreatePostValid(TestCase):
    fixtures = ['user.json','group.json', 'category.json']
    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.client.force_login(self.user)
            
        self.category = Category.objects.get(pk=1)

        data = dict(category=self.category.id, name='Split')
        self.response = self.client.post(r('category:sub_create'), data)

    def test_post(self):
        """Valid POST should redirect to categoria/subcategoria/list"""
        self.assertRedirects(self.response, r('category:sub_list'))

    def test_save_subcategory(self):
        """check object subcategory exist"""
        self.assertTrue(SubCategory.objects.exists())


class SubCategoryCreatePostInvalid(TestCase):
    fixtures = ['user.json','group.json', 'category.json']
    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.client.force_login(self.user)

        self.response = self.client.post(r('category:sub_create'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use category_form.html"""
        self.assertTemplateUsed(self.response, 'subcategory/subcategory_form.html')

    def test_has_form(self):
        """Context must have SubCategoryForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubCategoryForm)

    def test_dont_save_category(self):
        """check object subcategory exist"""
        self.assertFalse(SubCategory.objects.exists())