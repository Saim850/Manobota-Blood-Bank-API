from django.contrib import admin
from user_app.models import User
from django_app.models import DonorProfile

admin.site.register(User)
admin.site.register(DonorProfile)