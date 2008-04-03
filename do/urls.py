from django.conf.urls.defaults import *
from do.models import Todo
from do.forms import TodoForm

todo_dict = {
	'extra_context': {'form': TodoForm()},
	'queryset': Todo.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', todo_dict),
	(r'^create/$', 'do.views.create'),
	(r'^update/$', 'do.views.update'),
)
