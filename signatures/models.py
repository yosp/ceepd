from django.db import models

from courses.models import Course

class Signature(models.Model):
	id_signature	= models.PositiveIntegerField()
	description 	= models.CharField(max_length=60)


class Signature_Course(models.Model):
	id_signature 	= models.ForeignKey(Signature)
	id_course 		= models.ForeignKey(Course)