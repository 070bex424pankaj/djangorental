from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'property_type', 'area', 'price')
    list_display_links = ('title',)
    list_filter = ('property_type',)
    search_fields = ('title',)
    # fields = ('title',)

# Register your models here.
admin.site.register(Property, PropertyAdmin)