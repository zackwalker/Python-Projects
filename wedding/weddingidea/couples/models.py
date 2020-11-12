from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Couple(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))
