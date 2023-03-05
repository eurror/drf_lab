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
            'is_mentor',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
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
            'is_mentor',
            'experience',
            'audience',
        )

    def update(self, validated_data):
        user = User.objects.update(**validated_data)
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(
        min_length=4, required=True
    )
    new_password = serializers.CharField(
        min_length=4, required=True
    )
    new_password_confirm = serializers.CharField(
        min_length=4, required=True
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'new_password_confirm')

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.pop('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError('Password don\'t match')
        return attrs

    def validate_old_password(self, old_password):
        user = self.context['request'].user

        if not user.check_password(old_password):
            raise serializers.ValidationError('You entered wrong password')
        return old_password

    def set_new_password(self):
        user = self.context['request'].user
        new_password = self.validated_data.get('new_password')
        user.set_password(new_password)
        user.save()
