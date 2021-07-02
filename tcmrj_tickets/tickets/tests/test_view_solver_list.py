from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.models import Solver


class SolverListTest(TestCase):
    fixtures = ['user.json','group.json', 'solver.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)

        self.solver = Solver.objects.get(pk=1)
        self.response = self.client.get(r('tickets:solver_list'))

    
    def test_get_as_gestor(self):
        """GET /categoria/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/list must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_list'))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/list must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_list'))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use solver_list.html"""
        self.assertTemplateUsed(self.response, 'solver/solver_list.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<table', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_solver_id(self):
        expected = '<th scope="row">{}</th>'.format(self.solver.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_solver_name(self):
        expected = '<td>{}</td>'.format(self.solver.name)
        self.assertContains(self.response, expected)


    def test_solver_detail_link(self):
        """Must have tickets:solver_list link"""
        expected = 'href="{}"'.format(r('tickets:solver_detail', self.solver.id))
        self.assertContains(self.response, expected)

    def test_solver_update_link(self):
        """Must have solver update link"""
        expected = 'href="{}"'.format(r('tickets:solver_update', self.solver.id))
        self.assertContains(self.response, expected)

    def test_solver_delete_link(self):
        """Must have solver delete link"""
        expected = 'href="{}"'.format(r('tickets:solver_delete', self.solver.id))
        self.assertContains(self.response, expected)

    def test_solver_create_link(self):
        """Must have tickets:solver_create link"""
        expected = 'href="{}"'.format(r('tickets:solver_create'))
        self.assertContains(self.response, expected)

    def test_subsolver_create_link(self):
        """Must have tickets:solver_sub_create link"""
        expected = 'href="{}"'.format(r('tickets:solver_create'))
        self.assertContains(self.response, expected)

    def test_voltar_gerenciamento_link(self):
        """Must have core:gerenciamento link"""
        expected = 'href="{}"'.format(r('core:gerenciamento'))
        self.assertContains(self.response, expected)