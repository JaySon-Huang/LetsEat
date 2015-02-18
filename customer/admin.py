from django.contrib import admin
from models import CustomerModel,OrderModel,CommentModel

class CustomerModelAdmin(admin.ModelAdmin):
    list_display=('name','address','phone','alternatephone')
    search_fields =('name','phone')

admin.site.register(CustomerModel,CustomerModelAdmin)

class OrderModelAdmin(admin.ModelAdmin):
    list_display=('id','time','status')
    date_hierarchy ='time'
    
admin.site.register(OrderModel,OrderModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display=('cuisine','grade','message')
    
admin.site.register(CommentModel,CommentModelAdmin)

