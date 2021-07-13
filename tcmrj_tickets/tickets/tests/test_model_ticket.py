from django.test import TestCase
from django.contrib.auth.models import User
from tcmrj_tickets.category.models import Category, SubCategory
from tcmrj_tickets.tickets.models import Ticket, Solver
from django.shortcuts import resolve_url as r


class TicketModelTest(TestCase):
    fixtures = ['user.json','group.json', 'category.json', 'subcategory.json', 'solver.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.category = Category.objects.get(pk=1)
        self.subcategory = SubCategory.objects.filter(category=self.category)[0]
        self.solver = Solver.objects.get(pk=1)

        self.ticket = Ticket.objects.create(
            status = Ticket.ABERTO,
            category = self.category,
            subcategory = self.subcategory,
            solver = self.solver,
            description = 'Ar-Condicionado com Problemas',
            created_by = self.user
        )

    def test_create(self):
        """Must have exist ticket object"""
        self.assertTrue(Ticket.objects.exists())


    def test_get_absolute_url(self):
        url = r('tickets:detail', self.ticket.id)
        self.assertEqual(url, self.ticket.get_absolute_url())
