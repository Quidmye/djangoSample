from django.db import models

# Create your models here.

class ComputerModel(models.Model):

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    memory = models.IntegerField()
    frequency = models.FloatField()
    diagonal = models.FloatField()
