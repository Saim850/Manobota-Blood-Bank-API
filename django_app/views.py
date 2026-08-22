from rest_framework.viewsets import ModelViewSet
from django_app import models as m
from django_app import serializers as s
from rest_framework import permissions as p, filters as f
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from django_app.permissions import IsUserOrReadOnly, IsAdminOrReadOnly
from django_app.paganations import CustomPagination

class BloodGroupViewSet(ModelViewSet):
    queryset = m.BloodGroup.objects.all()
    serializer_class = s.BloodGroupSerializer
    permission_classes = [IsAdminOrReadOnly]

class MyProfileViewSet(ModelViewSet):
    serializer_class = s.DonorProfileSerializer
    permission_classes = [IsUserOrReadOnly, p.IsAuthenticated]
    def get_queryset(self):
        return m.DonorProfile.objects.filter(user=self.request.user).all()

class DonorProfileViewSet(ModelViewSet):
    queryset = queryset = m.DonorProfile.objects.select_related('user', 'blood_group').all()
    serializer_class = s.DonorProfileSerializer
    permission_classes = [IsUserOrReadOnly]

    filter_backends = [DjangoFilterBackend, f.SearchFilter, f.OrderingFilter]
    filterset_fields = ['blood_group', 'available']

    pagination_class = CustomPagination