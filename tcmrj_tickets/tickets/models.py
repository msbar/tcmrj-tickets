from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User
from tcmrj_tickets.core.models import OwnerMixin
from tcmrj_tickets.category.models import Category, SubCategory

class Solver(OwnerMixin):
    name = models.CharField('Responsável', max_length=255)

    class Meta:
        verbose_name_plural = 'Responsáveis'
        verbose_name = 'Responsável'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('tickets:list')


class Ticket(OwnerMixin):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
    ]

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Aberto', verbose_name='Status')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='tickets_category', verbose_name='Categoria')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, related_name='tickets_subcategory', verbose_name='Sub Categoria', blank=True, null=True)
    solver = models.ForeignKey(Solver, on_delete=models.DO_NOTHING, verbose_name='Responsável')
    description = models.TextField(verbose_name='Descrição')
    

    class Meta:
        verbose_name_plural = 'Chamados'
        verbose_name = 'chamado'
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return r('tickets:list')