from django.urls import path
from .views import my_profile,index,subir_rutina, subir_rutina_p2
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_profile/', views.my_profile, name = 'my_profile'),
    path('subir_rutina1/',views.subir_rutina, name= 'subir_rutina1'),
    path('subir_rutina2/',views.subir_rutina_p2, name= 'subir_rutina2')
]