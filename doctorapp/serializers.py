from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("__all__")



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("__all__")
        
        
        
class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = ("__all__")
        