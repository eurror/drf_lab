from rest_framework import serializers
from django.contrib.auth import get_user_model

from .utils import send_activation_code


User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(is_active=True, **validated_data)
        # send_activation_code(user.email, user.activation_code)
        return user


class MentorRegistrationSerializer(serializers.ModelSerializer):
    experience = serializers.ChoiceField(
            required=True,
            help_text='Каким видом преподавания вы занимались раньше?',
            choices=(
                ('лично, частным образом', 'лично, частным образом'),
                ('лично, профессионально', 'лично, профессионально'),
                ('онлайн', 'онлайн'),
                ('другое', 'другое'),
            )
        )
    audience = serializers.ChoiceField(
            required=True,
            help_text='Есть ли у вас аудитория, с которой вы хотите поделиться своим курсом?',
            choices=(
                ('в настоящий момент нет', 'в настоящий момент нет'),
                ('у меня маленькая аудитория', 'у меня маленькая аудитория'),
                ('у меня достаточная аудитория', 'у меня достаточная аудитория'),
            )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'experience',
            'audience',
        )

    def create(self, validated_data):
        user = User.objects.create_user(is_mentor=True, **validated_data)
        # send_activation_code(user.email, user.activation_code)
        return user
