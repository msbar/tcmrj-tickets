from django.db import models
from django.shortcuts import resolve_url as r
from tcmrj_tickets.core.models import ModelCreatedByMixin


# Create your models here.
class Category(ModelCreatedByMixin):
    name = models.CharField('Nome da Categoria', max_length=150)

    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('category:detail', pk=self.id)



class SubCategory(ModelCreatedByMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory_parent')
    name = models.CharField(verbose_name='Nome da Sub Categoria', max_length=150)
    
    class Meta:
        verbose_name_plural = 'Sub Categorias'
        verbose_name = 'Sub Categoria'
        ordering = ['category']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('category:sub_detail', pk=self.id)