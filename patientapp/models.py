from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	email = models.CharField(max_length=50,unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	dateOfBirth = models.DateField()
	blood = models.CharField(max_length=10)
	medical = models.CharField(max_length=100)

 