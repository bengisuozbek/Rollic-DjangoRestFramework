from rest_framework import serializers
from .models import Users

class RollicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "username", "first_name", "last_name", "email", "phone", "password", "confirm_password"]
