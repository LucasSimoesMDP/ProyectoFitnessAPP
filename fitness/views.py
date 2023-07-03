from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.

def index(request):
    return render(request, "index.html")

def my_profile(request):
    return render(request,"my_profile.html")

def subir_rutina(request):
    return render(request, "subir_rutina1.html")

def subir_rutina_p2(request):
        return render(request, "subir_rutina2.html")

def subir_rutina_p3(request):
        return render(request, "subir_rutina3.html")