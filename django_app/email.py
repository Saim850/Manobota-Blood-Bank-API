from djoser import email

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "email/password_reset.html"

    def get_subject(self):
        return "Reset your manobota blood bank password";

    def get_context_data(self):
        context = super().get_context_data()

        context["url"] = f"https://manobota-blood-bank-client.vercel.app/reset-password-confirm/{context['uid']}/{context['token']}"

        return context