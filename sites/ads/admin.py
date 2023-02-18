from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'importance', 'is_published', 'publication_date', 'send_email_notification', 'send_telegram_notification', 'created_at', 'updated_at')
    list_filter = ('is_published', 'send_email_notification', 'send_telegram_notification')

admin.site.register(Advertisement, AdvertisementAdmin)
