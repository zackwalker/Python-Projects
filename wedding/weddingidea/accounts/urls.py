from django.urls import path
from .views import update_profile

urlpatterns = [
    path('register/', update_profile, name='register'),
]
