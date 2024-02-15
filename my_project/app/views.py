import json 

from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .decorators import is_staff
from .forms import *
from .models import Produs, Question, Answer, Recenzie


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
        form = ContactForm(request.POST)
        if form.is_valid():
            subiect = form.cleaned_data["subiect"]
            mesaj = form.cleaned_data["mesaj"]
            email = form.cleaned_data["email"]
            copie = form.cleaned_data["trimite_copie"]
            copie_text = f"{type(copie)}, {copie}"
            print(type(copie), copie)
            send_mail(subiect, mesaj+copie_text, from_email="contact@siit.ro", recipient_list=[email])
            return redirect("/")
    return render(request, "contact.html", {"form": form})


def custom_login(request):
    form = CustomLoginForm()
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            login(request, form.authenticate_user)
            return redirect("/")

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect("/")


@is_staff
@login_required
def adauga_produs(request):
    formular = ProdusForm()
    if request.method == "POST":
        formular = ProdusForm(request.POST)
        if formular.is_valid():
            formular.save()
            return redirect(reverse("pagina-produse"))
    return render(request, "adauga_produs.html", {"form": formular})

def editare_produs(request, produs_id):
    produs = get_object_or_404(Produs, id=produs_id)
    formular = ProdusForm(instance=produs)
    if request.method == "POST":
        formular = ProdusForm(request.POST, instance=produs)
        if formular.is_valid():
            formular.save()
            return redirect(reverse("pagina-produse"))
    return render(request, "adauga_produs.html", {"form": formular})

#editare_produs(request, id=7)
#editare_produs(request, produs_id=7)
from django.views.generic import UpdateView

class ProdusUpdateView(UpdateView):
    model = Produs
    form_class = ProdusForm
    template_name = "adauga_produs.html"
    success_url = reverse_lazy("pagina-produse")



def api_view(request):
    raspuns = {
        "cheie": "valoare"
    }
    return HttpResponse(json.dumps(raspuns), content_type="application/json")