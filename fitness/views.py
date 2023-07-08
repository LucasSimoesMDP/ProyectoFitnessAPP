from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import models


# Create your views here.


def index(request):
    return render(request, "index.html")

def login(request):
      return render(request, "login.html")

def register(request):
      return render(request, "register.html")

# @login_required
# def logout(request):
#       return

@login_required
def my_profile(request):
    return render(request,"my_profile.html")

@login_required
def subir_rutina(request):
    return render(request, "subir_rutina1.html")

@login_required
def subir_rutina_p2(request):
        return render(request, "subir_rutina2.html")

@login_required
def subir_rutina_p3(request):
        return render(request, "subir_rutina3.html")

@login_required
def after_first_login(request):
      return render(request,"index-after-firstlogin.html")