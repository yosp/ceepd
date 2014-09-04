from django.db import models

class Student(models.Model):
	sex_choices = (
			('M','Masculino'),
			('F','Femenino'),
					)

	id_student	= models.IntegerField()
	first_name 	= models.CharField(max_length=255)
	last_name 	= models.CharField(max_length=255)
	address 	= models.CharField(max_length=255, blank=True)
	birthday 	= models.DateField()
	photo 		= models.ImageField(upload_to='students')
	sex 		= models.CharField(max_length=1,
									choices=sex_choices)

	def __unicode__(self):
		return ('%(fname)s %(lname)s') % {'fname': self.first_name,  'lname': self.last_name}