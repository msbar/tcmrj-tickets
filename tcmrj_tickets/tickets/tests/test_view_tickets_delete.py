from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.models import Ticket


class TicketDeleteTest(TestCase):
    fixtures = ['user.json','group.json', 'ticket.json', 'category.json', 'subcategory.json', 'solver.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)

        self.ticket = Ticket.objects.get(pk=1)
        self.response = self.client.get(r('tickets:delete', self.ticket.id))


    def test_get_as_gestor(self):
        """GET tickets:delete must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET tickets:delete must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:delete', self.ticket.id))
        self.assertEqual(403, self.response.status_code)


    def test_get_as_padrao(self):
        """GET tickets:delete must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:delete', self.ticket.id))
        self.assertEqual(403, self.response.status_code)


    def test_template(self):
        """Must use tickets_delete.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_delete.html')


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
        self.assertContains(self.response, 'Tem Certeza que deseja deletar o Chamado')


    def test_post(self):
        """Valid POST should redirect to /ticket/list"""
        self.response = self.client.post(r('tickets:delete', self.ticket.id))
        self.assertRedirects(self.response, r('tickets:list'), status_code=302)