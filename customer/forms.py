#encoding=utf-8
from django import forms

class SignupForm(forms.Form):
	# 定义必须字段的required类，方便css渲染
	required_css_class = 'required'

	account = forms.CharField(
		label='登录账户名', max_length=20,
		help_text='最长20字符,只能用大小写英文字母或数字')
	nickname = forms.CharField(
		label='昵称', max_length=20, required=False,
		help_text='最长20字符')
	password = forms.CharField(
		label='密码',widget=forms.PasswordInput(),
		min_length=3,
		help_text='至少3位长')
	phone = forms.CharField(label='手机号码')
	ex_phone = forms.CharField(label='备用手机号', required=False, help_text='可选')
	address = forms.CharField(label='送餐地址')

	def clean_account(self):
		account = self.cleaned_data['account']
		if not account[0].isalpha():
			raise forms.ValidationError('首字母必须为英文字母')
		elif not account.isalnum():
			raise forms.ValidationError('账户名只能用大小写英文字母或数字')
		return account

class LoginForm(forms.Form):
	account = forms.CharField(
		label='登录账户名', max_length=20,
		help_text='最长20字符,只能用大小写英文字母或数字')
	password = forms.CharField(
		label='密码',widget=forms.PasswordInput(),
		min_length=3,
		help_text='至少3位长')

	def clean_account(self):
		account = self.cleaned_data['account']
		if not account[0].isalpha():
			raise forms.ValidationError('首字母必须为英文字母')
		elif not account.isalnum():
			raise forms.ValidationError('账户名只能用大小写英文字母或数字')
		return account

class ProfileForm(forms.Form):
	nickname = forms.CharField(
		label='昵称', max_length=20, required=False,
		help_text='最长20字符')
	phone = forms.CharField(label='手机号码')
	ex_phone = forms.CharField(label='备用手机号', required=False, help_text='可选')
	address = forms.CharField(label='送餐地址')

