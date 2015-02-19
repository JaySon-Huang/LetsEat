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
	return render_to_response(
		'customer/profile.html',
		{
		'session' : request.session,
		'userinfo':userinfo,
		},
		context_instance=RequestContext(request)
	)





# TODO:javascript进行排序
