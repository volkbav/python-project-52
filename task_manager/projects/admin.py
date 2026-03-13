from django.contrib import admin

# Register your models here.
from .models import Project


@admin.register(Project)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name', 'created_at']