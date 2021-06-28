from tcmrj_tickets.tickets.views import get_subcategory, TicketCreateView, TicketUpdateView, \
    TicketListView, TicketDatailView, TicketDeleteView

from django.urls import path

app_name = 'tickets'
urlpatterns = [
    path('getsubcategory', get_subcategory, name='getsubcategory'),
    path('list', TicketListView.as_view(), name='list'), 
    path('create', TicketCreateView.as_view(), name='create'),    
    path('<int:pk>/update/', TicketUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', TicketDatailView.as_view(), name='detail'),   
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='delete'),

]
