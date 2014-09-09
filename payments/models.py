from django.db import models

from students.models import Student

# Esta clase contiene los conceptos de pagos
class Payment_Concept(models.Model):
	id_payment_concept 	= models.PositiveIntegerField()
	description 		= models.CharField(max_length=60)

# Esta clase es para crear los pagos de los estudiantes
class Payment(models.Model):
	months_choices = (
						('1','Enero'),
						('2','Febrero'),
						('3','Marzo'),
						('4','Abril'),
						('5','Mayo'),
						('6','Junio'),
						('7','Julio'),
						('8','Agosto'),
						('9','Septiembre'),
						('10','Octubre'),
						('11','Noviembre'),
						('12','Diciembre'),
						)

	id_payment 	= models.PositiveIntegerField()
	amount 		= models.DecimalField(max_digits=8, decimal_places=2)
	month 		= models.CharField(max_length=2, choices=months_choices)
	year_period = models.CharField(max_length=9)
	date_pay 	= models.DateTimeField(auto_now_add=True, editable=False)
	id_payment_concept = models.ForeignKey(Payment_Concept)