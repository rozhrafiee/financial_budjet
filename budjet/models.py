from django.db import models
from django.contrib.auth.models import User
class Title(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)    
    title = models.CharField()
    budget = models.PositiveBigIntegerField()
    payed_price = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.title

class Budejet(models.Model):
    budjet = models.IntegerField()
    

    