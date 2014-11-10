#encoding:utf-8
from django.db import models

from shop.models import ShopKeeperModel, ShopModel, CuisineModel

class CustomerModel(models.Model):
	'''顾客'''
	pass

class OrderModel(models.Model):
	'''订单'''
	pass

class CommentModel(models.Model):
	'''评论'''
	pass
