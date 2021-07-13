from django.db import models
from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User


class ModelCreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Criado por')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True