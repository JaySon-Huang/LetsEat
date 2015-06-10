from django.contrib import admin
from .models import CustomerModel, OrderModel, CommentModel


@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'alternatephone')
    search_fields = ('name', 'phone')


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'status')
    date_hierarchy = 'time'


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('cuisine', 'grade', 'message')
