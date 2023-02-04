from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    sal=models.FloatField()
    design=models.CharField(max_length=100)
    company=models.CharField(max_length=100)

# Create your models here.
