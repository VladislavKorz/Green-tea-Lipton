from django.contrib import admin
from .models import *

admin.site.register(Column)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'completed')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    inlines = [CommentInline]
# Register your models here.

