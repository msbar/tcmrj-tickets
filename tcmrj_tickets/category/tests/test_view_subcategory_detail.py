from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.models import SubCategory


class SubCategoryDetailTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json']

    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)
        self.subcategory = SubCategory.objects.get(pk=1)

        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('category:sub_detail', self.subcategory.id))

    
    def test_get_as_gestor(self):
        """GET categoria/subcategoria/1/detail must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET categoria/subcategoria/1/detail must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_detail', self.subcategory.id))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET categoria/subcategoria/1/detail must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_detail', self.subcategory.id))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use subcategory_detail.html"""
        self.assertTemplateUsed(self.response, 'subcategory/subcategory_detail.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<p', 6),)

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_subcategory_id(self):
        expected = '<p><b>id: </b>{}</p>'.format(self.subcategory.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_category_name(self):
        expected = '<p><b>Categoria: </b>{}</p>'.format(self.subcategory.category)
        self.assertContains(self.response, expected)

    def test_p_tag_display_subcategory_name(self):
        expected = '<p><b>Sub Categoria: </b>{}</p>'.format(self.subcategory.name)
        self.assertContains(self.response, expected)

    def test_p_tag_display_subsubcategory_owner(self):
        expected = '<p><b>Criador: </b>{}</p>'.format(self.subcategory.owner)
        self.assertContains(self.response, expected)

    def test_p_tag_display_subcategory_created_at(self):
        expected = '<p><b>Criado: </b>{}</p>'.format(self.subcategory.created_at)


    def test_p_tag_display_category_updated_at(self):
        expected = '<p><b>Modificado: </b>{}</p>'.format(self.subcategory.updated_at)


    def test_voltar_subcategory_list_link(self):
        """Must have category:sub_list link"""
        expected = 'href="{}"'.format(r('category:sub_list'))
        self.assertContains(self.response, expected)

    def test_subcategory_update_link(self):
        """Must have subcategory update link"""
        expected = 'href="{}"'.format(r('category:sub_update', self.subcategory.id))
        self.assertContains(self.response, expected)

    def test_subcategory_delete_link(self):
        """Must have subcategory update link"""
        expected = 'href="{}"'.format(r('category:sub_delete', self.subcategory.id))
        self.assertContains(self.response, expected)