from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=30)
    ani = models.IntegerField()
