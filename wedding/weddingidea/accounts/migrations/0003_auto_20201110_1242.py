# Generated by Django 3.1.3 on 2020-11-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_event',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='person2_first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='person2_last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
