from django import forms

from .models import Solver, Ticket


class SolverForm(forms.ModelForm):
    class Meta:
        model = Solver
        fields = ['name']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'subcategory', 'solver', 'description']


class TicketManagerForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', 'category', 'subcategory', 'solver', 'description']
    

class TicketBasicForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['solver']