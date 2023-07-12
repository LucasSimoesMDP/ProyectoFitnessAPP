from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from .forms import RegistationForm


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
      if request.POST:
        username_or_mail = request.POST['usernameormail']
        password = request.POST['password']

    #Filtro si el usuario escribio su username o su mail para iniciar sesion        
        
      else:
        return render(request, "login.html")

def register(request, *args, **kwargs):
    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
         return redirect('index.html')      

    # Variable para guardar futuro mensaje de error
    contexto = {}   

    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
             form.save()
             email = form.cleaned_data.get('email').lower()
             contrasena = form.cleaned_data.get('password')
             cuenta = authenticate(email = email, password = contrasena)
             login(request, cuenta)       
             return render(request, "index-after-firstlogin.html")
        else: 
             #  Guardo el mensaje de error
             contexto['form'] = form           
    return render(request, "register.html", contexto)


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