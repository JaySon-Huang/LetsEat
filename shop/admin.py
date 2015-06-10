from django.contrib import admin
from .models import ShopKeeperModel, ShopModel, CuisineModel


class ShopKeeperInline(admin.StackedInline):
    model = ShopKeeperModel
    extra = 1


class CuisineInline(admin.StackedInline):
    model = CuisineModel
    extra = 1


@admin.register(ShopKeeperModel)
class ShopKeeperModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'shop')
    search_fields = ('name', 'phone')


@admin.register(ShopModel)
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'shoptype', 'miniprice', 'status', 'announcement')
    search_fields = ('name', 'shoptype', 'miniprice', 'status')
    list_filter = ('address', )

    inlines = [ShopKeeperInline, CuisineInline]


@admin.register(CuisineModel)
class CuisineModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'grade', 'salesvolume', 'shop')
    search_fields = ('name',)
    list_filter = ('shop',)
