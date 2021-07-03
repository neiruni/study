from django.db import models

# Create your models here.
class FruitsList(models.Model):
    id = models.AutoField(primary_key=True)
    fruitsName = models.CharField(max_length=20)
    memo = models.CharField(max_length=200)