#encoding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from forms import SignupForm

def signup(request):
	errors = []
	if request.method == 'POST':
		signupform = SignupForm(request.POST)
		if signupform.is_valid():
			# 获取form信息
			username = signupform.cleaned_data['username']
			password = signupform.cleaned_data['password']

			# TODO:创建数据库对象,写入数据库
			user = {
			'username':username,
			'password':password,
			}
			print user

			return HttpResponseRedirect('/')

	signupform = SignupForm()
	return render_to_response(
		'customer/signup.html',
		{
		 'form' : signupform,
		},
		context_instance=RequestContext(request)
	)
