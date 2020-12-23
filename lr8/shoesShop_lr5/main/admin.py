from django.contrib import admin
from .models import Shoes, Manufacturer, Color, Category

admin.site.site_header = 'Shoes Shop Admin Panel'


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "manufacturer", "price")
    list_filter = ("category", "manufacturer", "price")
    search_fields = ("name__startswith",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
