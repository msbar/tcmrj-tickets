from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r
from tcmrj_tickets.tickets.models import Ticket


class TicketListTest(TestCase):
    fixtures = ['user.json','group.json', 'ticket.json', 'category.json', 'subcategory.json', 'solver.json']
    def setUp(self):
        self.user_gestor = User.objects.get(pk=1)
        self.user_suporte = User.objects.get(pk=2)
        self.user_padrao = User.objects.get(pk=3)

        self.client.force_login(self.user_gestor)

        self.ticket = Ticket.objects.get(pk=1)
        self.response = self.client.get(r('tickets:list'))

    
    def test_get_as_gestor(self):
        """GET /categoria/list must return status code 200"""
        self.assertEqual(200, self.response.status_code)


    def test_get_as_suporte(self):
        """GET /categoria/list must return status code 200 for group suporte"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:list'))
        self.assertEqual(200, self.response.status_code)


    def test_get_as_padrao(self):
        """GET /categoria/list must return status code 200 for group padrao"""
        self.client.force_login(self.user_suporte)
        self.response = self.client.get(r('tickets:list'))
        self.assertEqual(200, self.response.status_code)


    def test_template(self):
        """Must use solver_list.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_list.html')

    
    def test_html(self):
        """Html must contain display info detail tags"""
        tags = (('<table', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_p_tag_display_ticket_id(self):
        expected = '<th scope="row">{}</th>'.format(self.ticket.id)
        self.assertContains(self.response, expected)

    def test_p_tag_display_ticket_abertura(self):
        expected = '<td>{}</td>'.format(self.ticket.created_at)
        

    def test_p_tag_display_ticket_status(self):
        expected = '<td>{}</td>'.format(self.ticket.status)
        self.assertContains(self.response, expected)
    
    def test_p_tag_display_ticket_categoria(self):
        expected = '<td>{}</td>'.format(self.ticket.category)
        self.assertContains(self.response, expected)

    def test_p_tag_display_ticket_subcategoria(self):
        expected = '<td>{}</td>'.format(self.ticket.subcategory)
        self.assertContains(self.response, expected)

    def test_p_tag_display_ticket_responsave(self):
        expected = '<td>{}</td>'.format(self.ticket.solver)
        self.assertContains(self.response, expected)


    def test_ticket_detail_link(self):
        """Must have tickets:list link"""
        expected = 'href="{}"'.format(r('tickets:detail', self.ticket.id))
        self.assertContains(self.response, expected)

    def test_ticket_update_link(self):
        """Must have solver update link"""
        expected = 'href="{}"'.format(r('tickets:update', self.ticket.id))
        self.assertContains(self.response, expected)

    def test_ticket_delete_link(self):
        """Must have solver delete link"""
        expected = 'href="{}"'.format(r('tickets:delete', self.ticket.id))
        self.assertContains(self.response, expected)

    def test_ticket_create_link(self):
        """Must have tickets:create link"""
        expected = 'href="{}"'.format(r('tickets:create'))
        self.assertContains(self.response, expected)

    def test_voltar_gerenciamento_link(self):
        """Must have core:gerenciamento link"""
        expected = 'href="{}"'.format(r('core:gerenciamento'))
        self.assertContains(self.response, expected)