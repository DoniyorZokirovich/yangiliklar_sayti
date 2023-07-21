from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin

class OzimizUserManager(UserManager):
    def create_user(self, username, password=None, is_staff = False, is_superuser = False, is_active = True,**extra_fields):
        user = self.model(username=username,
                          password=password,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          is_active=is_active,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,  password=None, **extra_fields):
        return self.create_user(username=username,password=password,is_superuser=True, is_staff=True, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=123,blank=True,null=True)
    username = models.CharField(max_length=40,unique=True)
    phone = models.CharField(max_length=123,blank=True,null=True)
    oferta = models.BooleanField(default=True)


    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    object = OzimizUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS   = []
