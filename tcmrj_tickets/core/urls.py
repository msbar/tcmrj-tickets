from tcmrj_tickets.core.views import ger_tickets, home
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', home, name='home'),
    path('gerenciamento', ger_tickets, name='gerenciamento'),
]