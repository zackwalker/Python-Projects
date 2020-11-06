from django.db import models

# Create your models here.


class Couple(models.Model):
    person1_first_name = models.CharField(max_length=50)
    person1_last_name = models.CharField(max_length=50)
    person2_first_name = models.CharField(max_length=50)
    person2_last_name = models.CharField(max_length=50)
    date_of_event = models.DateTimeField()
