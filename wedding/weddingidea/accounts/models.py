from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# from appName.models import table_name
# Create your models here.


class Profile(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null=True, blank=True)
    name_of_event = models.CharField(max_length=50, null=True,blank=True)
    date_of_event = models.DateTimeField(null=True, blank=True)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person2_first_name = models.CharField(max_length=50, null=True)
    person2_last_name = models.CharField(max_length=50, null=True)
    date_of_event = models.DateTimeField(null=True)
>>>>>>> a1cc382631312f64c6dd56057d48ea35206c7fa9

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
<<<<<<< HEAD
    instance.Profile.save()

=======
>>>>>>> a1cc382631312f64c6dd56057d48ea35206c7fa9

# post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
