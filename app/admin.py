from django.contrib import admin

from app.models import Car

# Register your models here.

class CarFilter(admin.ModelAdmin):
    list_display = ("id", "user", "model","brand", "year")
    list_display_links = ("id", "model", "brand", "year")
    list_filter = ("brand","year")
    search_fields = ("model","brand")

admin.site.register(Car, CarFilter)