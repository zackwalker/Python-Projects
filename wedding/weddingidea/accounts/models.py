from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# from appName.models import table_name
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null=True, blank=True)
    name_of_event = models.CharField(max_length=50, null=True,blank=True)
    date_of_event = models.DateTimeField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.Profile.save()


# post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
