from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class BloodGroup(models.Model):
    name = models.CharField(max_length=3)
    def __str__(self):
        return self.name
    
class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_user')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='donor_blood_group')
    district = models.CharField(max_length=15);
    upazila = models.CharField(max_length=15);
    village = models.CharField(max_length=30);
    last_donation_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    total_donations = models.PositiveIntegerField(default=0)