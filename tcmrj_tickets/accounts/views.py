from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import AccountsRegristrationForm

class AccountsCreateView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/accounts_form.html'
    model = User
    form_class = AccountsRegristrationForm
    #success_url = reverse_lazy('accounts:datail')
    success_message = "Chamado criado com sucesso!"