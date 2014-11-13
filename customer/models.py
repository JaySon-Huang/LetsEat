#encoding:utf-8
from django.db import models

from shop.models import ShopKeeperModel, ShopModel, CuisineModel

class CustomerModel(models.Model):
	'''顾客'''
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	alternatephone = models.CharField(max_length=50,blank=True)
	account = models.CharField(max_length=15)
	password = models.CharField(max_length=15)
    

class OrderModel(models.Model):
	'''订单'''

	# 订单的不同状态
	STATUS_OF_ORDER_CHOICES = (
		(1,'已下单'),
		(2,'餐厅已确认'),
		(3,'成功交易'),
	)

	time = models.DateTimeField()
	status = models.IntegerField(choices=STATUS_OF_ORDER_CHOICES)
	shop = models.ForeignKey(ShopKeeperModel,related_name = "order_shop")
	cusine = models.ManyToManyField(CuisineModel,related_name = "order_cuisine")
	customer = models.ForeignKey(CustomerModel,related_name = "order_customer")
	

class CommentModel(models.Model):
	'''评论'''

	# 评分的等级
	GRADE_OF_CUISINE_CHOICES = (
		(0.0,'0.0'),(0.5,'0.5'),
		(1.0,'1.0'),(1.5,'1.5'),
		(2.0,'2.0'),(2.5,'2.5'),
		(3.0,'3.0'),(3.5,'3.5'),
		(4.0,'4.0'),(4.5,'4.5'),
		(5.0,'5.0'),
	)

	grade = models.FloatField(choices=GRADE_OF_CUISINE_CHOICES)
	message = models.CharField(max_length=200)
	cuisine = models.OneToOneField(CuisineModel,related_name = "comment_cuisine")
	customer = models.OneToOneField(CustomerModel,related_name = "comment_customer")
