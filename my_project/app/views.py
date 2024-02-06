from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse

from .models import Produs, Question, Answer, Recenzie
from .forms import ContactForm
from django.db.models import F


# Create your views here.
def salut(request):
    produse = Produs.objects.all().select_related("producator").prefetch_related("recenzie_set").order_by("-created")[:3]
    return render(request, "index.html", {"produse": produse})

def lista_produse(request):
    produse = Produs.objects.all().select_related("producator").prefetch_related("recenzie_set")
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lt=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    #produse = produse.order_by("pret") # Pret crescator
    #produse = produse.order_by("-pret") # Pret descrescator
    produse = produse.order_by("-pret", "-titlu") # Pret descrescator, in caz de egalitate de pret sorteaza dupa titlu


    # for produs in produse:
    #     produs.pret += 1
    #     produs.save()
    
    #produse.update(pret=F('pret')+1)

    return render(request, "produse.html", {"produse": produse})


def produs(request, id):
    try:
        produs = Produs.objects.get(id=id)
        #recenzii = Recenzie.objects.filter(produs=produs) # echivalent cu linia de mai jos
        recenzii = produs.recenzie_set.all()
        recenzii_str = [recenzie.titlu for recenzie in recenzii]
    except Produs.DoesNotExist:
        return HttpResponse("404")
    return render(request, "produs.html", {"produs": produs})


def quiz(request):
    question = Question.objects.first()
    text = question.text
    raspunsuri_relationate = question.answer_set.all()
    raspunsuri = [(answer.value, answer.corect, answer.question.text) for answer in raspunsuri_relationate]
    return HttpResponse(f"{text} <br/> {raspunsuri}")


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["subiect"]
        mesaj = request.POST["mesaj"]
        send_mail(subject, mesaj, from_email="contact@siit.ro", recipient_list=[email])
    return render(request, "contact.html", {"form": form})