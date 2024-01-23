from django.shortcuts import render
from django.http import HttpResponse

from .models import Produs, Question, Answer

# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def lista_produse(request):
    if "pret_maxim" in request.GET:
        produse = Produs.objects.filter(pret__lt=int(request.GET["pret_maxim"]))
    elif "search" in request.GET:
        produse = Produs.objects.filter(titlu__icontains=request.GET["search"])
    else:
        produse = Produs.objects.all()
    produse_formatat = [
        f"<li>{produs.titlu} - {produs.pret} - {produs.stoc}</li>"
        for produs in produse
    ]
    response_string = "<ol>"
    response_string += "".join(produse_formatat)
    response_string += "</ol>"
    return HttpResponse(response_string)

def produs(request):
    return HttpResponse("")


def quiz(request):
    question = Question.objects.first()
    text = question.text
    raspunsuri_relationate = question.answer_set.all()
    raspunsuri = [(answer.value, answer.corect, answer.question.text) for answer in raspunsuri_relationate]
    return HttpResponse(f"{text} <br/> {raspunsuri}") 