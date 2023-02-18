from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import *



@admin.register(guideAction)
class guideActionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["order_count", "title", "bigBox", "required"]
    list_display_links = ["order_count", "title"]
    list_filter = ['category__title', ]
    search_fields = ["title", "text"]


@admin.register(guideActionCategoria)
class guideActionCategoriaAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]
