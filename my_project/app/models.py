from django.db import models

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50)
    pret = models.FloatField(db_index=True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, null=True, blank=True)
    imagine = models.FileField(null=True, blank=True)