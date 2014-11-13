from django.contrib import admin
from LetsEat.shop.moedls import ShopKeeperModel,ShopModel,CuisineModel
# Register your models here.

class ShopKeeperModelAdmin(admin.ModelAdmin):
    list_display =('name','phone')
    search_fields =('name','phone')

class ShopModelAdmin(admin.ModelAdmin):
    list_display =('name','shoptype','minprice','status','announcement')
    search_fields =('name','shoptype','minprice','status')
    list_filter=('address',)

class CuisineModelAdmin(admin.ModelAdmin):
    list_display=('name','price','grade','salesvolume')
    search_fields =('name')


admin.site.register(ShopKeeperModel,ShopKeeperModelAdmin)
admin.site.register(ShopModel,ShopModelAdmin)
admin.site.register(CuisineModel,CuisineModelAdmin)
    
