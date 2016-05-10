from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nom', unique=True)
    phone = models.CharField(max_length=10, verbose_name='Telephone')
