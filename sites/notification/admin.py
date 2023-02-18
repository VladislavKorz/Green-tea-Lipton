from django.contrib import admin
from notification.models import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'call_day', 'call_time', 'rols')


@admin.register(NotificationUser)
class NotificationUserAdmin(admin.ModelAdmin):
    list_display = ["user", "notification"]
    list_display_links = ["user"]
    search_fields = ["user"]
