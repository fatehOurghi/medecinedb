from django.db import models
from django.contrib.auth.models import User
from patientapp.models import Patient
from django.contrib.auth.models import AbstractUser
import datetime


class Doctor(AbstractUser):
	GENDER = ((0, 'Male'), (1, 'Female'))
	BLOOD = (
		(0, "A+"),
		(1, "A-"),
		(2, "B+"),
		(3, "B-"),
		(4, "AB+"),
		(5, "AB-"),
		(6, "O+"),
  		(7, "O-"),
	)
	phone = models.CharField(max_length=10,default="")
	gender = models.CharField(max_length=6, choices=GENDER)
	address = models.CharField(max_length=200, default="")
	date_of_birth = models.DateField(null=True, blank=True)
	blood = models.CharField(max_length=3, choices=BLOOD)
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
 