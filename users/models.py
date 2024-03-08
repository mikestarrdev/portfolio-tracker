from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.user.username if self.user else ""
