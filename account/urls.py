from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="user_registration"),
    path('mentor-register/', views.MentorRegistrationView.as_view(), name="mentor_registration"),
    path('activate/<str:email>/<str:activation_code>/', views.ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
