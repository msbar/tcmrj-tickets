from django.urls import path, include
from tcmrj_tickets.accounts.views import AccountsCreateView

app_name = 'accounts'
urlpatterns = [
    path('create/', AccountsCreateView.as_view(), name='create'),
    path('', include('django.contrib.auth.urls')),
    
]