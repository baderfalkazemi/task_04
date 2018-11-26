from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	opening_time = models.TimeField(default="01:45:33")
	closing_time = models.TimeField(default="01:45:33")

	def __str__(self):
		return self.name
