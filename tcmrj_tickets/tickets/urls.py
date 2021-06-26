from tcmrj_tickets.tickets.views import list
from django.urls import path

urlpatterns = [
    path('', list, name='ticket_list'),
]
