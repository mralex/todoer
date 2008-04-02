from django.db import models
import datetime

class Todo(models.Model):
	todo = models.CharField(max_length = 200)
	done = models.BooleanField()
	due = models.DateTimeField('Date Due')
	added = models.DateTimeField('Date Added')
	
	def __unicode__(self):
		return self.todo
	
	class Admin:
		pass