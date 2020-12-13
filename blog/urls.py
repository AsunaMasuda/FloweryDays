from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_feed, name='blog'),
    path('category_view/<str:category>/', views.category_view,
         name='category_view'),
    path('blog_detail/<slug:slug>/', views.post_view, name='post_view'),
    path('delete_comment/<int:comment_pk>', views.delete_comment,
         name='delete_comment'),
]
