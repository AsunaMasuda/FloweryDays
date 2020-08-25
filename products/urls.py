from django.urls import path
from. import views

urlpatterns = [
    path('', views.initial_products, name='products'),
    path('search_result/', views.all_products, name='products'),
]