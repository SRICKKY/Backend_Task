from django.db import models

# Create your models here.
class Rider(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	mobile_number = models.CharField(max_length=12)


	def __str__(self):
		return self.name



class Driver(models.Model):
	name = models.CharField(max_length=30)
	mobile_number = models.CharField(max_length=20)
	booked_to = models.OneToOneField(Rider, on_delete=models.CASCADE)
	is_available = models.BooleanField(default=False)


	def __str__(self):
		return self.name

