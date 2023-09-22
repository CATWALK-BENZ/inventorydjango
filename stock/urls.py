
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>',views.product_detail,name='productdetail'),
    path('create',views.product_create,name='productcreate'),
    path('delete/<int:id>',views.product_delete,name='product_delete'),
]