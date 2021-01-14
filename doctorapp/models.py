from django.db import models
from django.contrib.auth.models import User
from patientapp.models import Patient
from django.contrib.auth.models import AbstractUser


class Doctor(AbstractUser):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	blood = models.CharField(max_length=10)
	status = models.BooleanField(default = 0)
	department = models.CharField(max_length=30 , default = "")
	salary = models.IntegerField(default = 10000)
	

# Ordonnance
class Prescription(models.Model):
	prescription = models.CharField(max_length=200)
	symptoms = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)
	docter = models.ForeignKey(Doctor,on_delete = models.CASCADE,unique = False)
	prescripted_date = models.DateField(auto_now = True) 
	outstanding = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)
 