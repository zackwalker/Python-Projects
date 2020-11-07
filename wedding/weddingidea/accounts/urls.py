from django.urls import path
from .views import UserRegistrationView, update_profile

urlpatterns = [
    path('register/', update_profile, name='register'),
]
