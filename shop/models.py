#encoding:utf-8
from django.db import models

class ShopModel(models.Model):
	'''店铺'''

	# 店铺的不同类型 
	TYPE_OF_SHOP_CHOICES = (
		(1,'中式'),
		(2,'西式'),
		(3,'寿司'),
	)

	# 店铺的不同状态
	STATUS_OF_SHOP_CHOICES = (
		(1,'营业中'),
		(2,'已打烊'),
	)

	name = models.CharField(verbose_name='店铺名',max_length=20)
	address = models.CharField(verbose_name='所在地址',max_length=50)
	shoptype = models.IntegerField(verbose_name='店铺类型',choices=TYPE_OF_SHOP_CHOICES)
	miniprice = models.FloatField(verbose_name='起送价')
	announcement = models.CharField(verbose_name='简介',max_length=200)
	status = models.IntegerField(verbose_name='店铺状态',choices=STATUS_OF_SHOP_CHOICES)

	def __unicode__(self):
		return u'店铺:'+self.name

class ShopKeeperModel(models.Model):
	'''店长'''
	name = models.CharField(verbose_name='姓名',max_length=20)
	phone = models.CharField(verbose_name='联系电话',max_length=50)
	account = models.CharField(verbose_name='账号',max_length=15)
	password = models.CharField(verbose_name='密码',max_length=15)
	shop = models.OneToOneField(ShopModel,related_name = "shop_shopkeeper",verbose_name='店铺')

	def __unicode__(self):
		return u'店长:'+self.name

class CuisineModel(models.Model):
	'''菜式'''
	name = models.CharField(verbose_name='菜式名',max_length=20)
	price = models.FloatField(verbose_name='价格',default=1.0)
	grade = models.FloatField(verbose_name='评分',default=3.0)
	salesvolume = models.PositiveSmallIntegerField(verbose_name='销售量',default=0)
	shop = models.ForeignKey(ShopModel,related_name = "cuisine_shop",verbose_name='店铺')

	def __unicode__(self):
		return u'菜式:'+self.name

