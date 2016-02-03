from django.contrib import admin
from .models import Post, Tags

# Register your models here.

admin.site.register(Tags)
admin.site.register(Post)