from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    icon = models.ImageField(upload_to = 'upload',blank=True)
    is_goulmet = models.BooleanField(default=False)

    def __str__(self):
        return self.username