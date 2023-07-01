from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "password",
        "password_repeat"
    ]
