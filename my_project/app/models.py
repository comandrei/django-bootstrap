from django.db import models

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50)
    pret = models.FloatField()
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024)
    imagine = models.FileField()