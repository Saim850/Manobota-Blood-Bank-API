from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_app import views as dv
from user_app import views as uv

router = DefaultRouter()

router.register('register', uv.UserRegisterView, basename="register")
router.register('my-donor-profile', dv.MyProfileViewSet, basename='my-donor-profile')
router.register('blood-group', dv.BloodGroupViewSet)
router.register('donor', dv.DonorProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
