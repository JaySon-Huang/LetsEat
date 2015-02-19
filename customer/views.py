#encoding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from customer.models import CustomerModel, OrderModel

from forms import SignupForm, LoginForm

def signup(request):
	'''注册动作'''
	errors = []
	signupform = SignupForm(auto_id=True)

	if request.method == 'POST':
		signupform = SignupForm(request.POST)
		if signupform.is_valid():
			# 获取form信息
			account = signupform.cleaned_data['account']
			password = signupform.cleaned_data['password']
			nickname = signupform.cleaned_data['nickname']
			address = signupform.cleaned_data['address']
			phone = signupform.cleaned_data['phone']
			ex_phone = signupform.cleaned_data['ex_phone']

			# 创建数据库对象,写入数据库
			newuser = CustomerModel(
				account=account,
				password=password,
				name=nickname,
				address=address,
				phone=phone,
				alternatephone=ex_phone
			)
			newuser.save()
			#仅作debug用
			# user = {
			# 'account':account,
			# 'nickname':nickname,
			# 'password':password,
			# }
			# print user
			return HttpResponseRedirect('/')

	return render_to_response(
		'customer/signup.html',
		{
		 'session' : request.session,
		 'form' : signupform,
		},
		context_instance=RequestContext(request)
	)

def login(request):
	'''登录动作'''
	# 已经是登录状态的用户
	if request.session.get('isLogin',False) == True:
		return HttpResponseRedirect('/')

	# 非登录状态的用户
	loginform = LoginForm(auto_id=True)
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			account = loginform.cleaned_data['account']
			password = loginform.cleaned_data['password']

			# 查询数据库内信息,是否登录成功
			customer = CustomerModel.objects.filter(account=account, password=password)
			if customer :
				request.session['isLogin'] = True
				request.session['uid'] = customer[0].id
				request.session['nickname'] = customer[0].name
				return HttpResponseRedirect('/')
			#仅debug用
			# if account == 'aaaaaa' and password == 'aaaaaa':
			# 	request.session['isLogin'] = True
			# 	return HttpResponseRedirect('/')
	# 表格字段格式错误,或者登录失败
	return render_to_response(
		'customer/login.html',
		{
		 'form' : loginform,
		 'session' : request.session,
		},
		context_instance=RequestContext(request)
	)

def logout(request):
	try :
		del request.session['isLogin']
		del request.session['cart']
		# TODO: 告知用户已成功退出
		print('用户正常退出')
	except KeyError:
		# TODO: 告知用户本来就处于非登录状态
		print('非登录用户点击退出')
	return HttpResponseRedirect('/')

def profile(request):
	if request.session.get('isLogin',False) == False:
		# TODO: 未登录状态，告知用户先登录
		return HttpResponseRedirect('/')

	# 对于已经是登录状态的用户，从数据库获取用户信息并显示出来
	user = CustomerModel.objects.get(id=request.session['uid'])
	userinfo = {
		'account':user.account,
		'nickname':user.name,
		'address':user.address,
		'phone':user.phone,
		'ex_phone':user.alternatephone,
		'orders':[]
	}
	order2str = {
		'status':{},
	}
	for code, s in OrderModel.STATUS_OF_ORDER_CHOICES:
		order2str['status'][code] = s

	for order in user.order_customer.all():
		orderinfo = {
			'status':order2str['status'][order.status],
			'time':order.time,
			'shop':order.shop,
			'cuisines':[],
		}
		for cuisine in order.cuisine.all():
			cuisineinfo = {
				'name':cuisine.name,
				'price':cuisine.price,
			}
			orderinfo['cuisines'].append(cuisineinfo)
		userinfo['orders'].append(orderinfo)
	#仅debug
	# user = {
	# 	'account':'aaaaaa',
	# 	'nickname':'测试用',
	# 	'address':'华南理工大学C12',
	# 	'phone':'135xxxxxxxx',
	# 	'ex_phone':'',
	# }
	return render_to_response(
		'customer/profile.html',
		{
		'session' : request.session,
		'userinfo':userinfo,
		},
		context_instance=RequestContext(request)
	)

class Cart(object):
	def __init__(self):
		self.items = {}
		self.size = 0

	def add(self,cuisineID):
		if cuisineID in self.items:
			self.items[cuisineID] += 1
		else:
			self.items[cuisineID] = 1
		self.size += 1
		return self.size

	def clear():
		self.items = {}
		self.size = 0

import json
import datetime

from shop.models import CuisineModel
from customer.models import OrderModel
from django.http import HttpResponse

def add2Cart(request, cuisineID):
	cart = request.session.get('cart', None)
	if cart is None:
		cart = Cart()
	res = {'size':cart.add(int(cuisineID))}
	request.session['cart'] = cart
	return HttpResponse(json.dumps(res))

def getCart(request):
	totalCost = 0.0
	cuisines = []
	for cuisineID, num in request.session['cart'].items.items():
		cuisine = CuisineModel.objects.get(id=cuisineID)
		totalCost += cuisine.price*num
		cuisines.append((cuisine, num))
	return render_to_response(
		'cart.html',
		{
		'session':request.session,
		'totalCost':totalCost,
		'cuisines':cuisines,
		},
		context_instance=RequestContext(request)
	)

def clearCart(request):
	request.session['cart'] = Cart()
	return HttpResponse(json.dumps({'size':0}))

def confirmCart(request):
	user = CustomerModel.objects.get(id=request.session['uid'])
	cuisines = []
	order = OrderModel(
		status=1
	)
	is_valid_order = True
	shop = None
	for cuisineID, num in request.session['cart'].items.items():
		cuisine = CuisineModel.objects.get(id=cuisineID)
		if not shop:
			shop = cuisine.shop
		else:
			if not shop == cuisine.id:
				is_valid_order = False
				break
		# 把点餐的信息先存储到cuisines中
		cuisines.append( (cuisine,num) )
	if not is_valid_order:
		return HttpResponse(json.dumps({'size':length,'error':'所点的餐来自不同餐厅!'}))
	order.shop = shop
	order.customer = user
	# 进行save之后才有order的id进行多对多的存储
	order.save()
	
	# 进行order与cuisine多对多的绑定
	for i in xrange(num):
		order.cusine.add(cuisine)
	order.save()

	# 把购物车清空
	request.session['cart'] = Cart()
	length = request.session['cart'].size
	return HttpResponse(json.dumps({'size':length}))

# TODO:javascript进行排序
