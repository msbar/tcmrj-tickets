from django.urls import path, include
from rest_framework import routers
from tcmrj_tickets.api.views import CategoryViewSet, SubCategoryViewSet, \
    SolverViewSet, TicketViewSet



router = routers.DefaultRouter()
router.register(r'categoria', CategoryViewSet)
router.register(r'subcategoria', SubCategoryViewSet)
router.register(r'responsavel', SolverViewSet)
router.register(r'chamados', TicketViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    
]