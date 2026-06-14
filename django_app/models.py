from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class District(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Upazila(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class BloodGroup(models.Model):
    name = models.CharField(max_length=3)
    def __str__(self):
        return self.name
    
class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_user')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='donor_blood_group')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='donor_district')
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE, related_name='donor_upazila')
    full_address = models.TextField(null=False, blank=False)
    last_donation_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    total_donations = models.PositiveIntegerField(default=0)

class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='request_blood_group')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='request_district')
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE, related_name='request_upazila')
    hospital_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    required_date = models.DateField()
    blood_units = models.PositiveIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_user")

    def __str__(self):
        return self.patient_name