from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.shortcuts import resolve_url as r
from tcmrj_tickets.category.models import Category, SubCategory


class SubCategoryListTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)
        self.subcategory = SubCategory.objects.get(pk=1)

        self.client.force_login(self.user_gestor)

        self.response = self.client.get(r('category:sub_list'))

    
    def test_get_as_gestor(self):
        """GET /categoria/subcategoria/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/subcategoria/list must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_list'))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/subcategoria/list must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('category:sub_list'))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use category_list.html"""
        self.assertTemplateUsed(self.response, 'subcategory/subcategory_list.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<table', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_subcategory_id(self):
        expected = '<th scope="row">{}</th>'.format(self.subcategory.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_category_name(self):
        expected = '<td>{}</td>'.format(self.subcategory.category)
        self.assertContains(self.response, expected)

    def test_p_tag_display_subcategory_name(self):
        expected = '<td>{}</td>'.format(self.subcategory.name)
        self.assertContains(self.response, expected)

    def test_category_detail_link(self):
        """Must have category:sub_list link"""
        expected = 'href="{}"'.format(r('category:sub_detail', self.subcategory.id))
        self.assertContains(self.response, expected)


    def test_category_update_link(self):
        """Must have category sub_update link"""
        expected = 'href="{}"'.format(r('category:sub_update', self.subcategory.id))
        self.assertContains(self.response, expected)


    def test_category_delete_link(self):
        """Must have category sub_delete link"""
        expected = 'href="{}"'.format(r('category:sub_delete', self.subcategory.id))
        self.assertContains(self.response, expected)

    
    def test_subcategory_create_link(self):
        """Must have category:sub_create link"""
        expected = 'href="{}"'.format(r('category:sub_create'))
        self.assertContains(self.response, expected)

    def test_voltar_gerenciamento_link(self):
        """Must have core:gerenciamento link"""
        expected = 'href="{}"'.format(r('core:gerenciamento'))
        self.assertContains(self.response, expected)