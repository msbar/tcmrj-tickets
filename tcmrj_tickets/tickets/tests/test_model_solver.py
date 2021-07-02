from django.test import TestCase
from django.contrib.auth.models import User
from tcmrj_tickets.tickets.models import Solver
from django.shortcuts import resolve_url as r


class SolverModelTest(TestCase):
    fixtures = ['user.json','group.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)

        self.solver = Solver.objects.create(
            name = 'José',
            owner = self.user
        )

    def test_create(self):
        """Must have exist solver object"""
        self.assertTrue(Solver.objects.exists())

    def test_str(self):
        self.assertEqual('José', str(self.solver))

    def test_get_absolute_url(self):
        url = r('tickets:solver_detail', self.solver.id)
        self.assertEqual(url, self.solver.get_absolute_url())