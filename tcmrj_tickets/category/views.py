from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from tcmrj_tickets.core.decorators import group_required
from django.utils.decorators import method_decorator
from tcmrj_tickets.category.forms import CategoryForm, SubCategoryForm
from tcmrj_tickets.category.models import Category, SubCategory
from django.urls import reverse_lazy
from django.http import HttpResponse
import json
from tcmrj_tickets.core.mixins import ViewCreatedByMixin, MessageSuccessDeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


@login_required
def get_subcategory(request):
    pk = request.GET.get('pk')
    result = list(SubCategory.objects.filter(category_id=pk).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryCreateView(ViewCreatedByMixin, SuccessMessageMixin, CreateView):
    template_name = 'category/category_form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    success_message = "Categoria criada com sucesso!"


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'category/category_form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')
    success_message = "Categoria atualizada com sucesso!"
    

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
class CategoryDeleteView(MessageSuccessDeleteView):
    template_name = 'category/category_delete.html'
    model = Category
    success_url = reverse_lazy('category:list')
    success_message = "Categoria deletada com sucesso!"


"""SUB CATEORIAS"""

decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SubCategoryCreateView(ViewCreatedByMixin, SuccessMessageMixin, CreateView):
    template_name = 'subcategory/subcategory_form.html'
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('category:sub_list')
    success_message = "Subcategoria criada com sucesso!"


decorators = [login_required, group_required('gestor')]
@method_decorator(decorators, name='dispatch')
class SubCategoryUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'subcategory/subcategory_form.html'
    model = SubCategory
    form_class = SubCategoryForm
    success_url = reverse_lazy('category:sub_list')
    success_message = "Subcategoria atualizada com sucesso!"


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
class SubCategoryDeleteView(MessageSuccessDeleteView):
    template_name = 'subcategory/subcategory_delete.html'
    model = SubCategory
    success_url = reverse_lazy('category:sub_list')
    success_message = "Subcategoria excluída com sucesso!"


