from django.shortcuts import render

# Create your views here.
def home(request):
    """Home principal do sistema"""
    return render(request, 'core/home.html')