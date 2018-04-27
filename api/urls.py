from django.urls import path,include

from api.views import RiderViewSet,DriverViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('rider',RiderViewSet)
router.register('driver',DriverViewSet)

urlpatterns = [
	path('rest-auth/',include('rest_auth.urls')),
	path('rest-auth/registration/',include('rest_auth.registration.urls')),
]

urlpatterns += router.urls