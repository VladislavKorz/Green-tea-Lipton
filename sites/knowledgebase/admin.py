from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(KnowledgeBase)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'file','photo','category')