from django.db import models
from django.contrib.auth.models import User
class Companies(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField()
    stock = models.BigIntegerField()
    date = models.DateField()
    
class Totalbalance(models.Model):
    total_balance = models.BigIntegerField()    
