from django.contrib import admin
from .models import FAQ, Category


admin.site.register(Category)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')


