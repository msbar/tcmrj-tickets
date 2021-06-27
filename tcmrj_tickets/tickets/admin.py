from django.contrib import admin
from .models import Ticket, Category, SubCategory, Solver

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id', 'name')
    search_fields = ('id', 'name')

@admin.register(Solver)
class SolverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'subcategory', 'solver', 'description')
    search_fields = ('id', 'solver')