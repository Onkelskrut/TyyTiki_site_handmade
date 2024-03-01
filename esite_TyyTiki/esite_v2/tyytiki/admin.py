from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'posted')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)


