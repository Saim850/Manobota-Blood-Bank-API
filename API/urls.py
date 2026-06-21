from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_app import views as dv
from user_app import views as uv

router = DefaultRouter()

router.register('register', uv.UserRegisterView, basename="register")
router.register('blood-group', dv.BloodGroupViewSet)
router.register('district', dv.DistrictViewSet)
router.register('upazila', dv.UpazilaViewSet)
router.register('user-info', uv.UserInformationsViewSet, basename="user-info")
router.register('donor', dv.DonorProfileViewSet)
router.register('my-donor-profile', dv.MyProfileViewSet, basename='my-donor-profile')
router.register('blood-request', dv.BloodRequestViewSet, basename="blood-request")
router.register('my-blood-request', dv.MyBloodRequestViewSet, basename="my-blood-request")
router.register('forgot-password', uv.DeleteUserViewSet, basename='forgot-password')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
