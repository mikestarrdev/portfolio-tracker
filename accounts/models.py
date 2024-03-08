from django.contrib.auth.models import User
from django.db import models
from tokens.models import Token

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=225)
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.address} - {self.token.name}"
