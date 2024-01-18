from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50, unique=True)
    pret = models.FloatField(db_index=True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, null=True, blank=True, help_text="Introduceti o descriere")
    imagine = models.FileField(null=True, blank=True)


class Favorit(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Question(models.Model):
    text = models.CharField(max_length=50)

class Answer(models.Model):
    value = models.CharField(max_length=10)
    corect = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=15)
    adresa = models.CharField(max_length=100)
    oras = models.CharField(max_length=20)
    cnp = models.CharField(max_length=13, null=True, blank=True)


class Curs(models.Model):
    nume = models.CharField(max_length=10)
    descriere = models.CharField(max_length=50)

    def __str__(self):
        return f"Curs {self.nume}"


class Student(models.Model):
    nume = models.CharField(max_length=30)
    telefon = models.CharField(max_length=100)
    cursuri = models.ManyToManyField(Curs)

    email = None

    def __str__(self):
        return f"Student {self.nume}"

