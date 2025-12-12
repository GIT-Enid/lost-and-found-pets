
from django.contrib import admin
from .models import CatPost

@admin.register(CatPost)
class CatPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'location', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'location')
