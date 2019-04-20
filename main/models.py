from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("send the email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None, is_staff=True, is_admin=True):
        user = self.create_user(email, password=password,
                                is_staff=True, is_admin=True)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=20, null=True,
                              blank=False, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.email}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()


class Signup(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    organization = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)

    