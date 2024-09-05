from django.db import models
class SavingPlan(models.Model):
    title = models.CharField()
    monthly_saving = models.PositiveBigIntegerField()
    target = models.CharField()
    start_month = models.PositiveIntegerField()
    
class TotalSaving(models.Model):
    totel_saving = models.PositiveBigIntegerField()    