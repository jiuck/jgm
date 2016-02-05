from django.contrib import admin
from .models import Post, Tags

# Register your models here.

class PostAdmin(admin.ModelAdmin): 
    list_display = ('headline', 'mod_date', 'pub_date', 'slug', 'text') 
    list_filter = ('pub_date', 'mod_date') 
    search_fields = ('headline', 'text', 'pub_date')
    fields = ('headline', 'text', 'pub_date', 'slug', 'draft')


admin.site.register(Tags)
admin.site.register(Post, PostAdmin)