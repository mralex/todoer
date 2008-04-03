from django.db import models
from datetime import datetime

class TodoManager(models.Manager):
	def active(self):
		return self.filter(done=False)
		
	def done(self):
		return self.filter(done=True)

PRIORITIES = (
	(1, "High"),
	(2, "Medium"),
	(3, "Low"),
)

class Todo(models.Model):
	todo = models.CharField(max_length = 200)
	done = models.BooleanField(default=False)
	added = models.DateTimeField('Date Added', default=datetime.now())
	priority = models.IntegerField(choices=PRIORITIES, default=2)
	
	objects = TodoManager()
	
	def __unicode__(self):
		return self.todo
	
	class Admin:
		pass
	
	class Meta:
		ordering = ['done', 'priority']