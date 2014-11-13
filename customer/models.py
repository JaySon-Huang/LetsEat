#encoding:utf-8
from django.db import models

from shop.models import ShopKeeperModel, ShopModel, CuisineModel

class CustomerModel(models.Model):
	'''顾客'''
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	account = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
    

class OrderModel(models.Model):
	'''订单'''
	time = models.DateTimeField()
	status = models.CharField(max_length=5)
	shop = models.ForeignKey(ShopKeeperModel,related_name = "order_shop")
	cusine = models.ManyToManyField(CuisineModel,related_name = "order_cuisine")
	customer = models.ForeignKey(CustomerModel,related_name = "order_customer")
	

class CommentModel(models.Model):
	'''评论'''
	grade = models.FloatField()
	message = models.CharField(max_length=200)
	cuisine = models.ForeignKey(CuisineModel,related_name = "comment_cuisine")
	customer = models.OneToOneField(CustomerModel,related_name = "comment_customer")
