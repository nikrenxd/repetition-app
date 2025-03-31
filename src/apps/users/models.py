from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.db import models

from src.apps.users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=155, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class UserStatistic(models.Model):
    total_decks = models.PositiveIntegerField(default=0)
    completed_decks = models.PositiveIntegerField(default=0)
    completed_decks_percentage = models.PositiveIntegerField(default=0)

    user = models.OneToOneField(
        User,
        related_name="user_statistics",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "users_user_statistic"
