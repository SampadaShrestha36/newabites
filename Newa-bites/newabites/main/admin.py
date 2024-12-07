
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'maps_link', 'contact')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'maps_link', 'contact')

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'tutorial_video_url')
    filter_horizontal = ('ingredient_list',)

@admin.register(OnlineShop)
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient', 'product_url')
    search_fields = ('name', 'ingredient__name')