from django.db import models

class Course(models.Model):
	sections_choices = (
						('A','Diurno'),
						('B','Tarde'),
						('N','N/A'),
						)

	id_course 	= models.IntegerField()
	section 	= models.CharField(max_length=1, choices=sections_choices)
	name		= models.CharField(max_length=100)
	description	= models.CharField(max_length=100)
	amount		= models.DecimalField(max_digits=8, decimal_places=2)