from django.contrib import admin

# Register your models here.
from core.models import Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass