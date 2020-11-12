from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# from appName.models import table_name
# Create your models here.

class Profile(models.Model):

    category_choices = [
        ('couple', 'Couple'),
        ('vendor', 'Vendor'),
        ('wedding_planner', 'Wedding Planner')
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', blank=True)
    name_of_event = models.CharField(max_length=50, null=True, blank=True)
    date_of_event = models.DateTimeField(null=True, blank=True)
    wedding_category = models.CharField(
        max_length=16, choices=category_choices, default='couple', null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # else:
    #     instance.profile.save()
