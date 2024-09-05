from django.db import models
class Companies(models.Model):
    title = models.CharField()
    stock = models.BigIntegerField()
    date = models.DateField()
    
class Totalbalance(models.Model):
    total_balance = models.BigIntegerField()    
