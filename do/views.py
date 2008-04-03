from django.http import HttpResponseRedirect, HttpResponse
from do.models import Todo

def create(request):
	return HttpResponse("create()")

def update(request):
	return HttpResponse("update()")