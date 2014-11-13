from django.contrib import admin
from LetsEat.customer.models import CustomerModel,OrderModel,CommentModel
# Register your models here.

class CustomerModelAdmin(admin.ModelAdmin):
    list_display=('name','address','phone','alternatephone')
    search_fields =('name','phone')

admin.site.register(CustomerModel,CustomerModelAdmin)

class OrderModelAdmin(admin.ModelAdmin):
    list_display=('time','status')
    date_hierarchy ='time'
    
admin.site.register(OrderModel,OrderModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    list_display=('grade','message')
    
admin.site.register(CommentModel,CommentModelAdmin)

