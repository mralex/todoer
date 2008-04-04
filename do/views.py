from django.http import HttpResponseRedirect, HttpResponse
from do.models import Todo
from do.forms import TodoForm

def create(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			new_todo = Todo(todo=form.cleaned_data['todo'], priority=int(form.cleaned_data['priority']))
			new_todo.save()
	
	return HttpResponseRedirect("/todo/")

def update(request):
	if request.method == 'POST':
		todo = Todo.objects.get(pk=request.POST['id'])
		todo.done = not todo.done
		todo.save()
		
	return HttpResponse('')