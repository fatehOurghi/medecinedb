from rest_framework import serializers
from .models import *


class DoctorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = Doctor
        fields = ('username', 'password', 'first_name', 'last_name', 'gender', 'date_of_birth')        
        
        
class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = ("__all__")
        