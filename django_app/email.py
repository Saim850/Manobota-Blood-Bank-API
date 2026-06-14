# your_app/email.py
from djoser import email
from django.conf import settings

class CustomPasswordResetEmail(email.PasswordResetEmail):
    def get_context_value(self):
        context = super().get_context_value()

        uid = context.get('uid')
        token = context.get('token')

        reset_url = f"{settings.FRONTEND_URL}/reset-password?uid={uid}&token={token}"

        context['reset_password_url'] = reset_url
        return context