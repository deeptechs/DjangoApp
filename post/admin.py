from django.contrib import admin

# My models imports
from .models import Post


# Register your models here.


# Models' admin panel classes
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date']
    list_filter = ['title', 'publish_date']
    search_fields = ['title']


# My models' admin panel's registers
admin.site.register(Post, PostAdmin)
