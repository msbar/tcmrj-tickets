from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.forms import SolverForm
from tcmrj_tickets.tickets.models import Solver


class SolverCreateViewTest(TestCase):
    fixtures = ['user.json','group.json', 'solver.json']
    
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('tickets:solver_create'))

    def test_get_as_gestor(self):
        """GET tickets:solver_create must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_get_as_suporte(self):
        """GET tickets:solver_create must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_create'))
        self.assertEqual(403, self.response.status_code)

    def test_get_as_padrao(self):
        """GET tickets:solver_create must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:solver_create'))
        self.assertEqual(403, self.response.status_code)
    
    def test_template(self):
        """Must use solver_form.html"""
        self.assertTemplateUsed(self.response, 'solver/solver_form.html')

    def test_voltar_solver_list_link(self):
        """Must have tickets:solver_list link"""
        expected = 'href="{}"'.format(r('tickets:solver_list'))
        self.assertContains(self.response, expected)

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
			    ('<input', 2),
                ('type="text"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have SolverForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, SolverForm)

    
class SolverCreatePostValid(TestCase):
    fixtures = ['user.json','group.json']
    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.client.force_login(self.user)

        data = dict(name='Ar-Condicionado')
        self.response = self.client.post(r('tickets:solver_create'), data)

    def test_post(self):
        """Valid POST should redirect to tickets:solver_list"""
        self.assertRedirects(self.response, r('tickets:solver_list'))

    def test_save_solver(self):
        """check object solver exist"""
        self.assertTrue(Solver.objects.exists())


class SolverCreatePostInvalid(TestCase):
    fixtures = ['user.json','group.json']
    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

        self.response = self.client.post(r('tickets:solver_create'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use solver_form.html"""
        self.assertTemplateUsed(self.response, 'solver/solver_form.html')

    def test_has_form(self):
        """Context must have SolverForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, SolverForm)

    def test_dont_save_solver(self):
        """check object solver exist"""
        self.assertFalse(Solver.objects.exists())