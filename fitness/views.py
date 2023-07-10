from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User


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

def register(request):
    user_count = User.objects.count()
    if request.POST:
         email = request.POST['email'].lower()
         fullname = request.POST['fullname'].lower().title()
         username = request.POST['username'].lower()
         password1 = request.POST['password']
         password2 = request.POST['password2']

        #  Si las contrasenas son diferentes, enviar mensaje de error
         if password1 != password2:
              return render() 

         for i in range(user_count):
            if username in User.objects.get(username):
                 pass
                 

        # Utilizo la clase de usuario predefinida de Django
         user = User.objects.create_user(username=username, email=email, password=password1, fullname = fullname)


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