from django.test import TestCase
from django.shortcuts import resolve_url as r


class TicketsCreateGet(TestCase):

    def setUp(self):
        self.response = self.client.get(r('ticket_create'))

    def test_get(self):
        """GET /tickets/create/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use ticket_create.html"""
        self.assertTemplateUsed(self.response, 'tickets/tickets_create.html')