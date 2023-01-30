from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)

    def __repr__(self) -> str:
        return f"<Account [{self.id}] - {self.username}>"
