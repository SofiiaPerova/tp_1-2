from djoser.email import PasswordResetEmail
from django.urls import reverse
from django.conf import settings
from djoser.email import PasswordChangedConfirmationEmail
from djoser.serializers import SendEmailResetSerializer

class CustomPasswordResetEmail(PasswordResetEmail):
    class CustomPasswordResetEmail(PasswordResetEmail):
        def get_context_data(self):
            context = super().get_context_data()
            domain = 'http://localhost:8080/'
            context['url'] = f"{domain}{context['url']}"
            return context