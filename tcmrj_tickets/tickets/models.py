from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Nome da Categoria', max_length=100)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('category_detail', slug=self.slug)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Nome da Sub Categoria', max_length=100)
    slug = models.SlugField('slug')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subcategory_detail', slug=self.slug)


class Solver(models.Model):
    name = models.CharField('Responsável', max_length=255)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('solver_detail', slug=self.slug)


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Aberto', 'Aberto'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluído', 'Concluído'),
    ]

    status = models.CharField('Status', max_length=12, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    solver = models.ForeignKey(Solver, on_delete=models.DO_NOTHING)
    description = models.TextField('Descrição')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
