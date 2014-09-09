from django.db import models

from students.models import Student
from signatures.models import Signature
from courses.models import Course

class Grade_Type(models.Model):
	grades_choices = (
						('G','General'),
						('C','Completivo'),
						('X','Extraordinario'),
						('E','Especial'),
					)

	id_grade_type 	= models.PositiveIntegerField()
	description 	= models.CharField(max_length=20,
										choices=grades_choices)
	
class grades_student(models.Model):
	grade 			= models.IntegerField()
	year_period 	= models.CharField(max_length=9)
	id_student 		= models.ForeignKey(Student)
	id_signature 	= models.ForeignKey(Signature)
	id_course 		= models.ForeignKey(Course)
	id_grade_type 	= models.ForeignKey(Grade_Type)