from django.db import models
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contract_address = models.CharField(max_length=225)
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=10)
    decimals = models.IntegerField()

    def __str__(self):
        return self.name
