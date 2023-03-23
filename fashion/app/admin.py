from django.contrib import admin
from app.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Product._meta.fields]
    raw_id_fields = ['brand']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Size._meta.fields]
    raw_id_fields = ['product']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Brand._meta.fields]

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Price._meta.fields]
    raw_id_fields = ['size']

