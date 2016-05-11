from django.db import models

# Create your models here.

class Driver(models.Model):
    lastname = models.CharField(max_length=255, verbose_name='Nom')
    firstname = models.CharField(max_length=255, verbose_name='Prenom')
    phone = models.CharField(max_length=10, verbose_name='Telephone', blank=True, null=True)
