from rest_framework.viewsets import ModelViewSet
from django_app import models as m
from django_app import serializers as s
from rest_framework import permissions as p, filters as f
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from django_app.permissions import IsUserOrReadOnly, IsAdminOrReadOnly
from django_app.paganations import CustomPagination
from django.utils import timezone


class BloodGroupViewSet(ModelViewSet):
    queryset = m.BloodGroup.objects.all()
    serializer_class = s.BloodGroupSerializer
    permission_classes = [IsAdminOrReadOnly]

class DistrictViewSet(ModelViewSet):
    queryset = m.District.objects.all()
    serializer_class = s.DistrictSerializer
    permission_classes = [IsAdminOrReadOnly]

class UpazilaViewSet(ModelViewSet):
    queryset = m.Upazila.objects.all()
    serializer_class = s.UpazilaSerializer
    permission_classes = [IsAdminOrReadOnly]

class MyProfileViewSet(ModelViewSet):
    serializer_class = s.DonorProfileSerializer
    permission_classes = [IsUserOrReadOnly, p.IsAuthenticated]
    def get_queryset(self):
        return m.DonorProfile.objects.filter(user=self.request.user).all()

class DonorProfileViewSet(ModelViewSet):
    queryset = queryset = m.DonorProfile.objects.select_related('user', 'blood_group', 'district', 'upazila').all()
    serializer_class = s.DonorProfileSerializer
    permission_classes = [IsUserOrReadOnly]

    filter_backends = [DjangoFilterBackend, f.SearchFilter, f.OrderingFilter]
    filterset_fields = ['blood_group', 'district', 'upazila', 'last_donation_date', 'available']
    
    pagination_class = CustomPagination

class BloodRequestViewSet(ModelViewSet):
    def get_queryset(self):
        m.BloodRequest.objects.filter(
            required_date__lt=timezone.now().date()
        ).delete()

        return m.BloodRequest.objects.all()

    serializer_class = s.BloodRequestSerializer
    permission_classes = [IsUserOrReadOnly]

    filter_backends = [DjangoFilterBackend, f.SearchFilter, f.OrderingFilter]
    filterset_fields = ['blood_group', 'district', 'upazila', 'hospital_name']
    
    search_fields = ['patient_name', 'hospital_name', 'contact_number']
    
    ordering_fields = ['id', 'patient_name', 'hospital_name']
    ordering = ['-id']
    
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """Save the blood request with the current user as creator"""
        serializer.save(user=self.request.user)

class MyBloodRequestViewSet(ModelViewSet):
    permission_classes = [IsUserOrReadOnly, p.IsAuthenticated]
    serializer_class = s.BloodRequestSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        return m.BloodRequest.objects.filter(user=self.request.user.id).all()