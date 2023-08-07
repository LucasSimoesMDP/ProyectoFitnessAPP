from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
import json
from django.views.decorators.csrf import csrf_exempt
import ast

def login_view(request,*args, **kwargs):
           
    context = {}

    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login        
        return redirect('index-firstroutine')   

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email'].lower()
            password = form.cleaned_data['password']
            if '@' in username_or_email:
                cuenta = get_user_model().objects.get(email=username_or_email)
                cuenta = authenticate(username = cuenta.get_username(), password = password)  
            else:
                cuenta = authenticate(username = username_or_email, password = password) 
            if cuenta is not None:
                login(request,cuenta)
            #  Si el usuario ya inició sesión anteriormente, 
            # que lo lleve al menu index si ya tiene una rutina grabada
            # Si nunca hizo una rutina, lo deberia llevar a index after first login  
                return redirect('index-firstroutine')
            else:
                form.add_error(None,'Credenciales invalidas')
        else:            
            #  Guardo el mensaje de error
            context['form'] = form                       
    return render(request, 'login.html', context)           

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login        
        return redirect('index-firstroutine')      

    # Variable para guardar futuro mensaje de error
    context = {}   

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username').lower()
             contrasena = form.cleaned_data.get('password1')
             cuenta = authenticate(username = username, password = contrasena)
             login(request, cuenta)       
             return redirect('index-firstroutine')
        else: 
             #  Guardo el mensaje de error
             context['form'] = form                       
    return render(request, "register.html", context)

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        #  Si el usuario ya inició sesión anteriormente, 
        # que lo lleve al menu index si ya tiene una rutina grabada
        # Si nunca hizo una rutina, lo deberia llevar a index after first login        
        return redirect('index-firstroutine')   
    return render(request, "index.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def my_profile(request):
    return render(request,"my_profile.html")

@login_required
@csrf_exempt
def subir_rutina(request):
    return render(request, "subir_rutina1.html")

@login_required
@csrf_exempt
def subir_rutina_p2(request):
    if request.method == 'POST':
        fecha_vencimiento_gym = request.body.decode('utf-8')
        # Dias que el usuario va al Gym
        dias_de_gym = request.POST.getlist('dias')
        if 'dias' not in fecha_vencimiento_gym:
        # Fecha de vencimiento del gym (OPCIONAL)
            if fecha_vencimiento_gym != 'null':
                print('La fecha de vencimiento es',fecha_vencimiento_gym)
    return render(request, "subir_rutina2.html",{'days': dias_de_gym})

# Funcion para guardar informacion de la parte 2 de la rutina
@login_required
@csrf_exempt
def save_routine_daily_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ejercicios = data['Ejercicios']
        dias = ast.literal_eval(data['Dias'])
        print(ejercicios)
        print(type(ejercicios))
        # Como dias = ['Lunes', 'Martes', 'Miercoles'] es un string y NO es una lista
        # Me queda ahora guardar los ejercicios en la database del user con el model 
        # que cree y pasar al dia siguiente --> ejercicios[i] agarra todos los ejercicios 
        # con las condiciones 
        dias.remove(dias[0])
        print(dias)
        # Para pasar al dia siguiente debo mandar a subir rutina2 la lista quitando el valor del dia 
    return render(request,"subir_rutina2",{'days': dias})

@login_required
def subir_rutina_p3(request):
    return render(request, "subir_rutina3.html")

@login_required
def after_first_login(request):
    return render(request,"index-firstroutine.html")