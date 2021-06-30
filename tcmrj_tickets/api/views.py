from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TicketSerializer, CategorySerializer, SubCategorySerializer, SolverSerializer
from tcmrj_tickets.tickets.models import Category, SubCategory, Solver, Ticket
from tcmrj_tickets.tickets.mixins import TicketListMixin


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer



class SolverViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solver.objects.all()
    serializer_class = SolverSerializer



class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
