from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.models import SubCategory


class SubCategoryDeleteTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)
        self.subcategory = SubCategory.objects.get(pk=1)
        
        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('category:sub_delete', self.subcategory.id))


    def test_get_as_gestor(self):
        """GET /categoria/subcategoria/1/delete must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/subcategoria/1/delete must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_delete', self.subcategory.id))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/subcategoria/1/delete must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_delete', self.subcategory.id))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use category_delete.html"""
        self.assertTemplateUsed(self.response, 'subcategory/subcategory_delete.html')


    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
			    ('<input', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_message(self):
        """Html must contain message alert"""
        self.assertContains(self.response, 'Tem Certeza que deseja deletar a Subcategoria')


    def test_post(self):
        """Valid POST should redirect to /categoria/subcategoria/list"""
        self.response = self.client.post(r('category:sub_delete', self.subcategory.id))
        self.assertRedirects(self.response, r('category:sub_list'), status_code=302)