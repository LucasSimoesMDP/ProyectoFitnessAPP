from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm


# Create your views here.
def index(request):
    return render(request, "index.html")

def login_view(request,*args, **kwargs):
           
    context = {}

    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login        
        return redirect('index.html')   

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            is_email = '@' in form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            if is_email:
                email = form.cleaned_data['username_or_email']
                cuenta = authenticate(email = email, password = password)  
            else:
                username = form.cleaned_data['username_or_email']
                cuenta = authenticate(username = username, password = password)  
            login(request,cuenta)
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login  
            return render(request, "index-firstroutine.html")
        else:            
            #  Guardo el mensaje de error
            context['form'] = form                       
    return render(request, "login.html", context)   

        

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login        
        return redirect('index.html')      

    # Variable para guardar futuro mensaje de error
    context = {}   

    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username').lower()
             contrasena = form.cleaned_data.get('password1')
             cuenta = authenticate(username = username, password = contrasena)
             login(request, cuenta)       
             return redirect(request, "index-firstroutine.html")
        else: 
             #  Guardo el mensaje de error
             context['form'] = form                       
    return render(request, "register.html", context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('index.html')

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
    return render(request,"index-firstroutine.html")