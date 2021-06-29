from django.shortcuts import render
from tcmrj_tickets.core.decorators import group_required
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """Home principal do sistema"""
    return render(request, 'core/home.html')


@login_required
@group_required('gestor')
def ger_tickets(request):
    """Home do Gerenciamento de chamados"""
    return render(request, 'core/gerenciamento_chamados.html')