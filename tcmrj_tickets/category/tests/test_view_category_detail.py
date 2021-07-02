from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.models import Category


class CategoryDetailTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.category = Category.objects.get(pk=1)
        self.client.force_login(self.user_gestor)

        self.response = self.client.get(r('category:detail', self.category.id))

    
    def test_get_as_gestor(self):
        """GET /categoria/1/detail must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/detail must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:detail', self.category.id))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/detail must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:detail', self.category.id))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use category_detail.html"""
        self.assertTemplateUsed(self.response, 'category/category_detail.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<p', 5),)

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_category_id(self):
        expected = '<p><b>id: </b>{}</p>'.format(self.category.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_category_name(self):
        expected = '<p><b>Nome: </b>{}</p>'.format(self.category.name)
        self.assertContains(self.response, expected)


    def test_p_tag_display_category_owner(self):
        expected = '<p><b>Criador: </b>{}</p>'.format(self.category.owner)
        self.assertContains(self.response, expected)


    def test_p_tag_display_category_created_at(self):
        expected = '<p><b>Criado: </b>{}</p>'.format(self.category.created_at)
        


    def test_p_tag_display_category_updated_at(self):
        expected = '<p><b>Modificado: </b>{}</p>'.format(self.category.updated_at)
        


    def test_voltar_category_list_link(self):
        """Must have category:list link"""
        expected = 'href="{}"'.format(r('category:list'))
        self.assertContains(self.response, expected)

    def test_category_update_link(self):
        """Must have category update link"""
        expected = 'href="{}"'.format(r('category:update', self.category.id))
        self.assertContains(self.response, expected)

    def test_category_delete_link(self):
        """Must have category update link"""
        expected = 'href="{}"'.format(r('category:delete', self.category.id))
        self.assertContains(self.response, expected)

    