from django import newforms as forms
from do.models import Todo

class TodoForm(forms.Form):
	todo = forms.CharField(max_length=200)
	priority = forms.ChoiceField(choices=Todo.PRIORITIES)