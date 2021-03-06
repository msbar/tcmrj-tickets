"""tcmrj_tickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('tcmrj_tickets.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('tcmrj_tickets.core.urls', namespace='core')),   
    path('api/', include('tcmrj_tickets.api.urls', namespace='rest_framework')),
    path('chamados/', include('tcmrj_tickets.tickets.urls', namespace='tickets')),
    path('categoria/', include('tcmrj_tickets.category.urls', namespace='category')),
]
