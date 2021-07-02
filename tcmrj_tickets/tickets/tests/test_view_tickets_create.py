from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.forms import TicketForm
from tcmrj_tickets.category.models import Category, SubCategory
from tcmrj_tickets.tickets.models import Ticket, Solver


class TicketCreateViewTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json', 'solver.json']
    
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)
        self.response = self.client.get(r('tickets:create'))

    def test_get_as_gestor(self):
        """GET tickets:create must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_get_as_suporte(self):
        """GET tickets:create must return status code 200 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:create'))
        self.assertEqual(200, self.response.status_code)

    def test_get_as_padrao(self):
        """GET tickets:create must return status code 200 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:create'))
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use tickets_form.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_form.html')

    def test_voltar_tickets_list_link(self):
        """Must have tickets:list link"""
        expected = 'href="{}"'.format(r('tickets:list'))
        self.assertContains(self.response, expected)

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 1),
			    ('<input', 1),
                ('<select', 3),
                ('<textarea', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have TicketManagerForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, TicketForm)

    
class TicketCreatePostValid(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json', 'solver.json']
    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.category = Category.objects.get(pk=1)
        self.subcategory = SubCategory.objects.filter(category=self.category)[0]
        self.solver = Solver.objects.get(pk=1)

        self.client.force_login(self.user)

        data = dict(
            status = Ticket.ABERTO,
            category = self.category.id,
            subcategory = self.subcategory.id,
            solver = self.solver.id,
            description = 'Ar-Condicionado com Problemas',
            owner = self.user.id
        )
        self.response = self.client.post(r('tickets:create'), data)

    def test_post(self):
        """Valid POST should redirect to tickets:list"""
        self.assertRedirects(self.response, r('tickets:list'))

    def test_save_tickets(self):
        """check object tickets exist"""
        self.assertTrue(Ticket.objects.exists())


class TicketCreatePostInvalid(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json', 'solver.json']
    def setUp(self):
        self.user =User.objects.get(pk=1)
        self.category = Category.objects.get(pk=1)
        self.subcategory = SubCategory.objects.filter(category=self.category)[0]
        self.solver = Solver.objects.get(pk=1)
        self.client.force_login(self.user)

        self.response = self.client.post(r('tickets:create'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use tickets_form.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_form.html')

    def test_has_form(self):
        """Context must have TicketForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, TicketForm)

    def test_dont_save_tickets(self):
        """check object tickets exist"""
        self.assertFalse(Ticket.objects.exists())