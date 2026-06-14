from rest_framework import serializers
from django_app import models as m
from rest_framework.validators import ValidationError
import re
from user_app.serializers import UserInformationsSerializer

class BloodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model  = m.BloodGroup
        fields = ["id", 'name']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.District
        fields = ['id', 'name']

class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Upazila
        fields = ['id', 'name']

class DonorProfileSerializer(serializers.ModelSerializer):
    user = UserInformationsSerializer(read_only=True)
    blood_group_name = serializers.ReadOnlyField(source="blood_group.name")
    district_name = serializers.ReadOnlyField(source="district.name")
    upazila_name = serializers.ReadOnlyField(source="upazila.name")

    class Meta:
        model = m.DonorProfile
        fields = [
            'id',
            'user',
            'blood_group',
            'blood_group_name',
            'last_donation_date',
            'district',
            'district_name',
            'upazila',
            'upazila_name',
            'full_address',
            'available',
            'total_donations'
        ]
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        user_exists = m.DonorProfile.objects.filter(user=validated_data['user']).exists()

        if user_exists:
            raise ValidationError("Your donor profile already created.")
        
        return super().create(validated_data)
    
class BloodRequestSerializer(serializers.ModelSerializer):
    # Read-only nested details for display
    user = UserInformationsSerializer(read_only=True)
    blood_group_name = serializers.ReadOnlyField(source='blood_group.name')
    district_name = serializers.ReadOnlyField(source='district.name')
    upazila_name = serializers.ReadOnlyField(source='upazila.name')
    
    class Meta:
        model = m.BloodRequest
        fields = "__all__"
        read_only_fields = ['id', 'user']