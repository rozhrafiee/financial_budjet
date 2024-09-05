from django.db import models
class Title(models.Model):
    title = models.CharField()
    budget = models.PositiveBigIntegerField()
    payed_price = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.title

class Budejet(models.Model):
    pass
    

    