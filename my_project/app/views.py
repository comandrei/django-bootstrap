from django.shortcuts import render
from django.http import HttpResponse

from .models import Produs

# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def lista_produse(request):
    produse = Produs.objects.all()
    produse_formatat = [
        f"<li>{produs.titlu} - {produs.pret} - {produs.stoc}</li>"
        for produs in produse
    ]
    response_string = "<ol>"
    response_string += "".join(produse_formatat)
    response_string += "</ol>"
    return HttpResponse(response_string)