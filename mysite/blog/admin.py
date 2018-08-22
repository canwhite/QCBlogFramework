from django.contrib import admin
from blog.models import CommonData

# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'time']




admin.site.register(CommonData, BlogsPostAdmin)
