#encoding:utf-8
from django.db import models

from shop.models import ShopKeeperModel, ShopModel, CuisineModel

class CustomerModel(models.Model):
	'''顾客'''
	name = models.CharField(verbose_name='昵称',max_length=20)
	address = models.CharField(verbose_name='地址',max_length=50)
	phone = models.CharField(verbose_name='电话',max_length=50)
	alternatephone = models.CharField(verbose_name='电话2',max_length=50,blank=True)
	account = models.CharField(verbose_name='账号',max_length=15)
	password = models.CharField(verbose_name='密码',max_length=15)

	def __unicode__(self):
		return self.name

class OrderModel(models.Model):
	'''订单'''

	# 订单的不同状态
	STATUS_OF_ORDER_CHOICES = (
		(1,'已下单'),
		(2,'餐厅已确认'),
		(3,'成功交易'),
	)

	time = models.DateTimeField(verbose_name='下单时间',auto_now_add=True)
	status = models.IntegerField(verbose_name='状态',choices=STATUS_OF_ORDER_CHOICES)
	shop = models.ForeignKey(ShopModel,related_name="order_shop",verbose_name='店铺')
	cuisine = models.ManyToManyField(CuisineModel,related_name="order_cuisine",verbose_name='菜式')
	customer = models.ForeignKey(CustomerModel,related_name="order_customer",verbose_name='顾客')
	
	def __unicode__(self):
		return unicode(self.id)

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

	customer = models.OneToOneField(CustomerModel,related_name="comment_customer",verbose_name='顾客')
	cuisine = models.OneToOneField(CuisineModel,related_name="comment_cuisine",verbose_name='菜式')
	grade = models.FloatField(verbose_name='评分',choices=GRADE_OF_CUISINE_CHOICES,default=3.0)
	message = models.CharField(verbose_name='留言',max_length=200,default='我的最爱')

	def __unicode__(self):
		return '%s:%f'%(self.cuisine.__unicode__(),self.grade)
