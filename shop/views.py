#encoding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def index(request):
	return render_to_response(
		'index.html',
		{
		},
		context_instance=RequestContext(request)
	)
