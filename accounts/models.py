from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .manage import *
import uuid


class User(AbstractBaseUser):
    username = None
    # UUID = models.UUIDField(primary_key=True, unique=True,
    #                         default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=100, unique=True,
                             verbose_name='Phone Number')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permition?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes,always
        return True

    def save(self, *args, **kwargs):
        self.username = self.phone
        return super().save(*args, **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
