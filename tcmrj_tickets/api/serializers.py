from tcmrj_tickets.category.models import Category
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from tcmrj_tickets.tickets.models import Ticket, Solver
from tcmrj_tickets.category.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category       
        fields = ['name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory       
        fields = ['category', 'name']


class SolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solver       
        fields = ['name']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket       
        fields = ['status', 'category', 'subcategory', 'solver', 'description']
