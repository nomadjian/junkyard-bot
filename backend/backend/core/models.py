from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from core.managers import UserManager


class User(AbstractBaseUser):
    login = models.CharField(verbose_name='Логин', unique=True, max_length=64)
    is_staff = models.BooleanField(verbose_name='Сотрудник')
    is_active = models.BooleanField(verbose_name='Активен')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.login
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    


# Create your models here.
