from django import forms
from django.forms import fields
from .models import Category, SubCategory, Solver, Ticket


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name']


class SolverForm(forms.ModelForm):
    class Meta:
        model = Solver
        fields = ['name']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('category', 'subcategory', 'solver', 'description')