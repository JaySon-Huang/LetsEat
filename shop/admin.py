from django.contrib import admin
from models import ShopKeeperModel, ShopModel, CuisineModel

class ShopKeeperModelAdmin(admin.ModelAdmin):
    list_display = ('name','phone')
    search_fields = ('name','phone')

class ShopModelAdmin(admin.ModelAdmin):
    list_display = ('name','shoptype','miniprice','status','announcement')
    search_fields = ('name','shoptype','miniprice','status')
    list_filter = ('address',)

class CuisineModelAdmin(admin.ModelAdmin):
    list_display = ('name','price','grade','salesvolume')
    search_fields = ('name',)


admin.site.register(ShopKeeperModel,ShopKeeperModelAdmin)
admin.site.register(ShopModel,ShopModelAdmin)
admin.site.register(CuisineModel,CuisineModelAdmin)
    
