#encoding:utf-8
from django.db import models

from shop.models import ShopKeeperModel, ShopModel, CuisineModel

class CustomerModel(models.Model):
        id=models.IntegerField()
	name = models.CharField(max_length=20)
        address = models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        account = models.CharField(max_length=15)
        password = models.CharField(max_length=15)
        
	pass

class OrderModel(models.Model):
        id=models.IntegerField()
	time = models.DateTimeField()
        status = models.CharField(max_length=5)
	
	pass

class CommentModel(models.Model):
	id=models.IntegerField()
	grade = models.FloatField()
        message = models.CharField(max_length=200)
	pass
