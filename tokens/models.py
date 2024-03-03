from django.db import models

class Token(models.Model):
    contract_address = models.CharField(max_length=225)
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=10)
    decimals = models.IntegerField()

    def __str__(self):
        return self.name
