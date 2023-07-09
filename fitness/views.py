from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
      if request.method == 'POST':
        username_or_mail = request.POST['usernameormail']
        password = request.POST['password']

    #Filtro si el usuario escribio su username o su mail para iniciar sesion        
        
      else:
        return render(request, "login.html")

def register(request):
    if request.method == 'POST':
         email = request.POST['email']
         if len(email) == 0:
              pass
         fullname = request.POST['fullname']
         username = request.POST['username']
         password = request.POST['password']



        # Utilizo la clase de usuario predefinida de Django
         user = User.objects.create_user(username=username, email=email, password=password, fullname = fullname)
         return render(request, "index-after-firstlogin.html", {'user':user})
    else:                
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