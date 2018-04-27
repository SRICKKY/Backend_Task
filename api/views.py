from rest_framework import viewsets

from ola_app.models import Rider,Driver

from . import serializers


class RiderViewSet(viewsets.ModelViewSet):
	queryset = Rider.objects.all()
	serializer_class = serializers.RiderSerializer

class DriverViewSet(viewsets.ModelViewSet):
	queryset = Driver.objects.all()
	serializer_class = serializers.DriverSerializer