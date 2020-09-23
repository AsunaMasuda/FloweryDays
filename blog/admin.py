from django.contrib import admin
from .models import BlogPost, BlogImage, BlogComments
 
 
class BlogAdmin(admin.ModelAdmin):
   list_display = ('title', 'slug', 'status','post_created_date')
   list_filter = ("status",)
   search_fields = ['title', 'content']
   prepopulated_fields = {'slug': ('title',)}
 
class PostImageAdmin(admin.ModelAdmin):
   list_display = ('image', 'image_article_id')
 
class BlogCommentsAdmin(admin.ModelAdmin):
   list_display = ('comment_article_id', 'user_name', 'blog_comment', 'created_on')
   search_fields = ['blog_comment']
 
 
admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(BlogComments)
