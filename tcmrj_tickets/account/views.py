from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout

# Create your views here.
def user_login(request):
    pass

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

