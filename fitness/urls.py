from django.urls import path
from .views import register,my_profile,index,subir_rutina, subir_rutina_p2, subir_rutina_p3,login,after_first_login
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('index/',views.after_first_login,name='index-after-fistlogin'),
    path('register/',views.register, name='register'),
    path('my_profile/', views.my_profile, name = 'my_profile'),
    path('subir_rutina1/',views.subir_rutina, name= 'subir_rutina1'),
    path('subir_rutina2/',views.subir_rutina_p2, name= 'subir_rutina2'),
    path('subir_rutina3/',views.subir_rutina_p3, name= 'subir_rutina3'),
]