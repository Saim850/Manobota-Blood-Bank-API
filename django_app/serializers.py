from rest_framework import serializers
from django_app import models as m
from rest_framework.validators import ValidationError
import re

class BloodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model  = m.BloodGroup
        fields = ["id", 'name']

class DonorProfileSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.name")
    user_email = serializers.ReadOnlyField(source="user.email")
    user_phone = serializers.ReadOnlyField(source="user.phone_number")
    blood_group_name = serializers.ReadOnlyField(source="blood_group.name")

    class Meta:
        model = m.DonorProfile
        fields = [
            'id',
            'user',
            'user_name',
            'user_email',
            'user_phone',
            'blood_group',
            'blood_group_name',
            'last_donation_date',
            'district',
            'upazila',
            'village',
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