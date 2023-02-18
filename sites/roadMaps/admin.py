from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *


@admin.register(guideAction)
class guideActionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["order_count", "title", "bigBox", "required"]
    list_display_links = ["order_count", "title"]
    list_filter = ['department__title', ]
    search_fields = ["title", "text"]
    ordering = ['order_count']

