from tcmrj_tickets.tickets.views import ticket_create
from django.urls import path

urlpatterns = [
    path('create', ticket_create, name='ticket_create'),
]
