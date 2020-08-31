from django.urls import path
from. import views

urlpatterns = [
    path('', views.onlineshop, name='onlineshop'),
    path('<int:product_pk>/', views.single_product, name='single_product'),
    path('search_result/', views.all_products, name='products'),
]