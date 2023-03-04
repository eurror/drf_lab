from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('activate/<str:email>/<str:activation_code>/', views.ActivationView.as_view()),
]
