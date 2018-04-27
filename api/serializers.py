from rest_framework import serializers

from ola_app.models import Rider, Driver

class RiderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rider
		fields = ('name','email','mobile_number')

class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = ('name','mobile_number','booked_to','is_available')