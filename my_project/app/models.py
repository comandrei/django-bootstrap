from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50, unique=True)
    pret = models.FloatField(db_index=True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, null=True, blank=True, help_text="Introduceti o descriere")
    imagine = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Produs {self.titlu} "
    
    @property
    def rating(self):
        rating = 0
        recenzii = self.recenzie_set.all()
        for recenzie in recenzii:
            rating +=recenzie.rating
        try:
            return rating // len(recenzii)
        except ZeroDivisionError:
            return 0

    

class Recenzie(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    titlu = models.CharField(max_length=10)
    descriere = models.CharField(max_length=100)


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
    an = models.IntegerField(default=1)

    email = None

    def __str__(self):
        return f"Student {self.nume}"


class Elev(models.Model):
    class Meta:
        unique_together = [("nume", "prenume")]

    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    an = models.IntegerField(default=1)
    cursuri = models.ManyToManyField(Curs, through='ElevCurs')


class ElevCurs(models.Model):
    elev = models.ForeignKey(Elev, on_delete=models.CASCADE)
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE)
    nota = models.IntegerField(default=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class PostManager(models.Manager):

    def active(self):
        acum = now()
        return self.filter(visible_from__lte=acum).filter(models.Q(end_on__gte=acum) | models.Q(end_on__isnull=True))

class Post(models.Model):
    class Meta:
        ordering = ('-updated', )

    titlu = models.CharField(max_length=50)
    continut = models.CharField(max_length=300)
    visible_from = models.DateTimeField()
    end_on = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

# Post.objects.filter(visible_from__lte=acum).filter(Q(end_on__gte=acum) | Q(end_on__isnull=True))
# Post.objects.active() - same as above
    
