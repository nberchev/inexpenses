from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('validate-username/', views.UsernameValidationView.as_view(), name='validate-username'),
]
