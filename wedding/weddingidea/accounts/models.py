from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# from appName.models import table_name

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user =  self.model(
                email=self.normalize_email(email),
                username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        user =  self.create_user(
                email=self.normalize_email(email),
                username=username,
                password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser):

    category_choices = [
        ('couple', 'Couple'),
        ('vendor', 'Vendor'),
        ('wedding_planner', 'Wedding Planner')
    ]

    email            = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username         = models.CharField(max_length=30,unique=True)
    date_joined      = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login       = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_staff         = models.BooleanField(default=False)
    is_superuser     = models.BooleanField(default=False)
    name_of_event = models.CharField(max_length=50)
    date_of_event = models.DateTimeField(null=True, blank=True)
    wedding_category = models.CharField(
        max_length=16, choices=category_choices, default='couple')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True