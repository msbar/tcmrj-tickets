from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.models import Solver


class solverDetailTest(TestCase):
    fixtures = ['user.json','group.json', 'solver.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.solver = Solver.objects.get(pk=1)
        self.client.force_login(self.user_gestor)

        self.response = self.client.get(r('tickets:solver_detail', self.solver.id))

    
    def test_get_as_gestor(self):
        """GET /categoria/1/detail must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/detail must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_detail', self.solver.id))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/detail must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_detail', self.solver.id))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use solver_detail.html"""
        self.assertTemplateUsed(self.response, 'solver/solver_detail.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<p', 5),)

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_solver_id(self):
        expected = '<p><b>id: </b>{}</p>'.format(self.solver.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_solver_name(self):
        expected = '<p><b>Nome: </b>{}</p>'.format(self.solver.name)
        self.assertContains(self.response, expected)


    def test_p_tag_display_solver_created_by(self):
        expected = '<p><b>Criador: </b>{}</p>'.format(self.solver.created_by)
        self.assertContains(self.response, expected)


    def test_p_tag_display_solver_created_at(self):
        expected = '<p><b>Criado: </b>{}</p>'.format(self.solver.created_at)
        


    def test_p_tag_display_solver_updated_at(self):
        expected = '<p><b>Modificado: </b>{}</p>'.format(self.solver.updated_at)
        


    def test_voltar_solver_list_link(self):
        """Must have tickets:solver_list link"""
        expected = 'href="{}"'.format(r('tickets:solver_list'))
        self.assertContains(self.response, expected)

    def test_solver_update_link(self):
        """Must have tickets:solver_update link"""
        expected = 'href="{}"'.format(r('tickets:solver_update', self.solver.id))
        self.assertContains(self.response, expected)

    def test_solver_delete_link(self):
        """Must have tickets:solver_delete"""
        expected = 'href="{}"'.format(r('tickets:solver_delete', self.solver.id))
        self.assertContains(self.response, expected)

    