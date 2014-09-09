from django.db import models
from students.models import Student

class Phone_Student(models.Model):
	phone 		= models.CharField(max_length=10)
	student_id 	= models.ForeignKey(Student)

	def __unicode__(self):
		return self.phone