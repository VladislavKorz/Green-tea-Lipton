from django.contrib import admin
from users.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'rols', 'phone', 'telegram_id','city','post')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]
 