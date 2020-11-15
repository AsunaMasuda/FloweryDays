from django.urls import path
from. import views

urlpatterns = [
    path('', views.onlineshop, name='onlineshop'),
    path('<int:product_pk>/', views.single_product, name='single_product'),
    path('search_result/', views.all_products, name='products'),
    path('filter_result/', views.filter_product, name='filter_product'),
    path('add/', views.add_product, name='add_product'),
]