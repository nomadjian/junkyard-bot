from django.contrib.auth.models import BaseUserManager
import datetime

class UserManager(BaseUserManager):
    def create_user(self,login,password=None, is_staff=False, is_superuser=False):
        user = self.model(login=login)
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_active = True
        user.save(using=self.db)
        return user
    
    def create_superuser(self, login, password=None):
        user = self.create_user(login, password, is_staff=True, is_superuser=True)
        return user