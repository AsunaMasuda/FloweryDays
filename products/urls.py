from django.urls import path
from. import views

urlpatterns = [
    path('', views.onlineshop, name='onlineshop'),
    path('search_result/', views.all_products, name='products'),
]