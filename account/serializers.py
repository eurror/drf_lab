from rest_framework import serializers
from django.contrib.auth import get_user_model

from .utils import send_activation_code


User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        min_length=4, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password_confirm',
        )

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        if password != password_confirm:
            return serializers.ValidationError("Passwords don't match!")
        return attrs

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user
