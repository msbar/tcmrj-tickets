from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.models import Ticket


class TicketDetailTest(TestCase):
    fixtures = ['user.json','group.json', 'ticket.json', 'category.json', 'subcategory.json', 'solver.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.ticket = Ticket.objects.get(pk=1)
        self.client.force_login(self.user_gestor)

        self.response = self.client.get(r('tickets:detail', self.ticket.id))

    
    def test_get_as_gestor(self):
        """GET tickets:detail must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET tickets:detail must return status code 403 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:detail', self.ticket.id))
        self.assertEqual(200, self.response.status_code)


    def test_get_as_padrao(self):
        """GET tickets:detail must return status code 403 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:detail', self.ticket.id))
        self.assertEqual(200, self.response.status_code)


    def test_template(self):
        """Must use ticket_detail.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_detail.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<p', 8),)

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_ticket_abertura(self):
        expected = '<p><b>Abertura: </b>{}</p>'.format(self.ticket.created_at)
        

    def test_p_tag_display_ticket_status(self):
        expected = '<p><b>Status: </b>{}</p>'.format(self.ticket.status)
        self.assertContains(self.response, expected)


    def test_p_tag_display_ticket_categoria(self):
        expected = '<p><b>Categoria: </b>{}</p>'.format(self.ticket.category)
        self.assertContains(self.response, expected)


    def test_p_tag_display_ticket_subcategoria(self):
        expected = '<p><b>Sub-Categoria: </b>{}</p>'.format(self.ticket.subcategory)
        

    def test_p_tag_display_ticket_responsavel(self):
        expected = '<p><b>Responsável: </b>{}</p>'.format(self.ticket.solver)

    def test_p_tag_display_ticket_descricao(self):
        expected = '<p><b>Descrição:</b>{}</p>'.format(self.ticket.description)
        


    def test_voltar_ticket_list_link(self):
        """Must have tickets:list link"""
        expected = 'href="{}"'.format(r('tickets:list'))
        self.assertContains(self.response, expected)

    def test_ticket_update_link(self):
        """Must have tickets:update link"""
        expected = 'href="{}"'.format(r('tickets:update', self.ticket.id))
        self.assertContains(self.response, expected)

    def test_ticket_delete_link(self):
        """Must have tickets:delete"""
        expected = 'href="{}"'.format(r('tickets:delete', self.ticket.id))
        self.assertContains(self.response, expected)

    