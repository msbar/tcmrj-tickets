from tcmrj_tickets.tickets.views import *
from django.urls import path

app_name = 'tickets'
urlpatterns = [
    path('list', TicketListView.as_view(), name='list'), 
    path('create', TicketCreateView.as_view(), name='create'),    
    path('<int:pk>/update/', TicketUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', TicketDatailView.as_view(), name='detail'),   
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='delete'),

    path('responsavel/list', SolverListView.as_view(), name='solver_list'), 
    path('responsavel/create', SolverCreateView.as_view(), name='solver_create'),    
    path('<int:pk>/responsavel/update/', SolverUpdateView.as_view(), name='solver_update'),
    path('<int:pk>/responsavel/detail/', SolverDatailView.as_view(), name='solver_detail'),   
    path('<int:pk>/responsavel/delete/', SolverDeleteView.as_view(), name='solver_delete'),

]
