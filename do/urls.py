from django.conf.urls.defaults import *
from do.models import Todo

todo_dict = {
	'queryset': Todo.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', todo_dict),
	(r'^create/$', 'do.views.create'),
	(r'^update/$', 'do.views.update'),
)
