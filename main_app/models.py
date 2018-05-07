from django.db import models

# Create your models here.

# https://stackoverflow.com/questions/17166895/save-date-in-one-format-in-database-django

# How to import classes from models.py to the shell
# from main_app.models import Lesson, Assignment

# How to insert an assignment related to a lesson on the shell.
#a = Assignment(lesson_due=Lesson.objects.get(number=1), title="First Assignment", points=50)

# Potentially make obj's their own model? Like assignments.

class Lesson(models.Model):
    
	number = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=100,default='-')
	reading = models.CharField(max_length=100,default='-')
	notes = models.CharField(max_length=300,default='-')

	# I might change this assigns due thing to being another class in this file.
	assigns_due = models.CharField(max_length=100,default='-')

	# This is going to be an ordered list, is that a diff field type?
	objs = models.CharField(max_length=100,default='-')

	# Does this method need additional arguments?
	# No, it works like this, have to give the data as "YYYY-MM-DD" when creating.
	date = models.DateField()

	# This is going to be an unordered list, is that a diff field type?
	help_resources = models.CharField(max_length=100,default='-')
    
	def __str__(self):
		return self.title

class Assignment(models.Model): # this table will be related to lesson.
	lesson_due = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	title = models.CharField(max_length=100,default='')
	points = models.IntegerField()
	assignment_link = models.CharField(max_length=300,default='-')
    
	def __str__(self):
		return self.title


class ClassFile(models.Model): # this table will have a many to many relationship to Assignment
	id = models.AutoField(primary_key=True) # I thought this was supposed to be here automatically... it ended up working by adding this in...
	lesson_being_used = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	title = models.CharField(max_length=100,default='-')
	link = models.CharField(max_length=100,default='-')

	def __str__(self):
		return self.title

