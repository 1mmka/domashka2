from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    avatar = models.ImageField(upload_to='avatars',verbose_name='Фотография')
    
    def __str__(self):
        return self.username