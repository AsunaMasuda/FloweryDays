from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_feed, name='blog'),
    path('category_view/<str:category>/', views.category_view,
         name='category_view'),
    path('blog_detail/<slug:slug>/', views.post_view, name='post_view'),
    path('delete_comment/<int:comment_pk>', views.delete_comment,
         name='delete_comment'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_pk>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_pk>/', views.delete_blog, name='delete_blog'),
]
