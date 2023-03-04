from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from . import serializers


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MentorRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.MentorRegistrationSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(
            email=email,
            activation_code=activation_code).first()
        if not user:
            return Response('User not found', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Account is activated', status=200)
