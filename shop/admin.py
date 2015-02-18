from django.contrib import admin
from models import ShopKeeperModel, ShopModel, CuisineModel

class ShopKeeperModelAdmin(admin.ModelAdmin):
    list_display = ('name','phone','shop')
    search_fields = ('name','phone')

admin.site.register(ShopKeeperModel,ShopKeeperModelAdmin)

class ShopModelAdmin(admin.ModelAdmin):
    list_display = ('name','shoptype','miniprice','status','announcement')
    search_fields = ('name','shoptype','miniprice','status')
    list_filter = ('address',)

admin.site.register(ShopModel,ShopModelAdmin)

class CuisineModelAdmin(admin.ModelAdmin):
    list_display = ('name','price','grade','salesvolume','shop')
    search_fields = ('name',)
    list_filter = ('shop',)

admin.site.register(CuisineModel,CuisineModelAdmin)
