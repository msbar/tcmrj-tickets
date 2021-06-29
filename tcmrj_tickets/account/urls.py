from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import user_login, logout_view

app_name = 'account'
urlpatterns = [
    path('logout/', logout_view, name="logout"),
    path('', include('django.contrib.auth.urls')),
    
]