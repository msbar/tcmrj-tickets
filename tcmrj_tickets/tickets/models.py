from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Nome da Categoria', max_length=150)

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('tickets:category-detail', self.pk)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory_parent')
    name = models.CharField('Nome da Sub Categoria', max_length=150)
    
    class Meta:
        verbose_name_plural = 'Sub Categorias'
        verbose_name = 'Sub Categoria'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('tickets:subcategory-detail', self.pk)


class Solver(models.Model):
    name = models.CharField('Responsável', max_length=255)

    class Meta:
        verbose_name_plural = 'Responsáveis'
        verbose_name = 'Responsável'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('tickets:solver-detail', self.pk)

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
    ]

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Aberto', verbose_name='Status')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='tickets_category', verbose_name='Categoria')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, related_name='tickets_subcategory', verbose_name='Sub Categoria')
    solver = models.ForeignKey(Solver, on_delete=models.DO_NOTHING, verbose_name='Responsável')
    description = models.TextField(verbose_name='Descrição')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tickets_owner', verbose_name='Criado por')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Chamados'
        verbose_name = 'chamado'
        ordering = ['-id']

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return r('tickets:list')