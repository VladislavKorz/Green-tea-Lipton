from django.contrib import admin
from .models import *



@admin.register(guideAction)
class guideActionAdmin(admin.ModelAdmin):
    list_display = ["order_count", "title", "bigBox", "required"]
    list_display_links = ["order_count", "title"]
    search_fields = ["title", "text"]
