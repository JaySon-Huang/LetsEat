#encoding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from forms import SignupForm,LoginForm

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

			# TODO:创建数据库对象,写入数据库
			user = {
			'account':account,
			'nickname':nickname,
			'password':password,
			}
			print user

			return HttpResponseRedirect('/')

	return render_to_response(
		'customer/signup.html',
		{
		 'form' : signupform,
		},
		context_instance=RequestContext(request)
	)

def login(request):
	'''登录动作'''
	# 已经是登录状态的用户
	if request.session.get('isLogin',False) == True:
		return HttpResponseRedirect('/')
	s = dir(request.session)
	# 非登录状态的用户
	loginform = LoginForm(auto_id=True)
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			account = loginform.cleaned_data['account']
			password = loginform.cleaned_data['password']

			print('account:%s,password:%s'%(account,password))
			# TODO:查询数据库内信息,是否登录成功
			if account == 'aaaaaa' and password == 'aaaaaa':
				request.session['isLogin'] = True
				return HttpResponseRedirect('/')

	# 表格字段格式错误,或者登录失败
	return render_to_response(
		'customer/login.html',
		{
		 'form' : loginform,
		 # TODO: debug用
		 'session' : request.session.items(),
		},
		context_instance=RequestContext(request)
	)

def logout(request):
	try :
		del request.session['isLogin']
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

	# TODO: 对于已经是登录状态的用户，从数据库获取用户信息并显示出来
	user = {
		'account':'aaaaaa',
		'nickname':'测试用',
		'address':'华南理工大学C12',
		'phone':'135xxxxxxxx',
		'ex_phone':'',
	}
	return render_to_response(
		'customer/profile.html',
		{
			'userinfo':user,
		},
		context_instance=RequestContext(request)
	)


