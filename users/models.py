from django.db import models
from django.contrib.auth.models import User
from tokens.models import Token
from accounts.models import Account

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens = models.ManyToManyField(Token)
    accounts = models.ManyToManyField(Account)

    def __str__(self):
        return self.user.username
