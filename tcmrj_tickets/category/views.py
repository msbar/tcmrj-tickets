from django.contrib.auth.decorators import login_required
from tcmrj_tickets.core.decorators import group_required
from django.utils.decorators import method_decorator
from tcmrj_tickets.category.forms import CategoryForm, SubCategoryForm
from tcmrj_tickets.category.models import Category, SubCategory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def get_subcategory(request):
    pk = request.GET.get('pk')
    result = list(SubCategory.objects.filter(
        category_id=int(pk)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryCreateView(CreateView):
    template_name = 'category/category_form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryUpdateView(UpdateView):
    template_name = 'category/category_form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    model = Category
    paginate_by = 10


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryDatailView(DetailView):
    template_name = 'category/category_detail.html'
    model = Category
    

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryDeleteView(DeleteView):
    template_name = 'category/category_delete.html'
    model = Category
    success_url = reverse_lazy('category:list')


"""SUB CATEORIAS"""

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SubCategoryCreateView(CreateView):
    template_name = 'subcategory/subcategory_form.html'
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('category:sub_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SubCategoryUpdateView(UpdateView):
    template_name = 'subcategory/subcategory_form.html'
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('category:sub_list')


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SubCategoryListView(ListView):
    template_name = 'subcategory/subcategory_list.html'
    model = SubCategory
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SubCategoryDatailView(DetailView):
    template_name = 'subcategory/subcategory_detail.html'
    model = SubCategory


@method_decorator(login_required, name='dispatch')
@method_decorator(group_required('gestor'), name='dispatch')
class SubCategoryDeleteView(DeleteView):
    template_name = 'subcategory/subcategory_delete.html'
    model = SubCategory
    success_url = reverse_lazy('category:sub_list')


