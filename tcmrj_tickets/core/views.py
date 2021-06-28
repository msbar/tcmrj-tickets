from django.shortcuts import render

# Create your views here.
def home(request):
    """Home principal do sistema"""
    return render(request, 'core/home.html')


def ger_tickets(request):
    """Home do Gerenciamento de chamados"""
    return render(request, 'core/gerenciamento_chamados.html')