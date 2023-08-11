from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users


class LandlordRegistrationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "email", "is_landlord", "password1", "password2"]
