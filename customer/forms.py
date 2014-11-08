#encoding=utf-8
from django import forms

class SignupForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=20)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())

