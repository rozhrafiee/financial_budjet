from django.db import models
from django.contrib.auth.models import User
class SavingPlan(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    monthly_saving = models.PositiveBigIntegerField()
    target = models.IntegerField()
    start_month = models.PositiveIntegerField()
    
class TotalSaving(models.Model):
    totel_saving = models.PositiveBigIntegerField()    