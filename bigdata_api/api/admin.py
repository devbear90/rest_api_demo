from django.contrib import admin
from .models import APIKey, SecureData

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'is_active')
    search_fields = ('name', 'key')
    list_filter = ('is_active',)

@admin.register(SecureData)
class SecureDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'value')
