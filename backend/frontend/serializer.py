from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = ["site_name", "welcome_message"]
