from tcmrj_tickets.category.views import *

from django.urls import path

app_name = 'category'
urlpatterns = [
    path('getsubcategory', get_subcategory, name='getsubcategory'),

    path('list', CategoryListView.as_view(), name='list'), 
    path('create', CategoryCreateView.as_view(), name='create'),    
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', CategoryDatailView.as_view(), name='detail'),   
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),

    path('subcategoria/list', SubCategoryListView.as_view(), name='sub_list'), 
    path('subcategoria/create', SubCategoryCreateView.as_view(), name='sub_create'),    
    path('<int:pk>/subcategoria/update/', SubCategoryUpdateView.as_view(), name='sub_update'),
    path('<int:pk>/subcategoria/detail/', SubCategoryDatailView.as_view(), name='sub_detail'),   
    path('<int:pk>/subcategoria/delete/', SubCategoryDeleteView.as_view(), name='sub_delete'),

]
