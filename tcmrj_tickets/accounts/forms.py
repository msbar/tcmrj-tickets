from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class AccountsRegristrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']