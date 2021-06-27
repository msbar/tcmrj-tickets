from tcmrj_tickets.tickets.views import get_subcategory, TicketCreateView, TicketUpdateView, \
    TicketListView, TicketDatailView, TicketDeleteView

from django.urls import path

urlpatterns = [
    path('getsubcategory', get_subcategory, name='getsubcategory'),
   
    path('list', TicketListView.as_view(), name='ticket_list'), 
    path('create', TicketCreateView.as_view(), name='ticket_create'),    
    path('<int:pk>/update/', TicketUpdateView.as_view(), name='ticket_update'),
    path('<int:pk>/detail/', TicketDatailView.as_view(), name='ticket_detail'),   
    path('<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),

]
