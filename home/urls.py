#Se deberia crear un archivo URLS por cada app que creamos, por eso las URLS ahora están acá.

from django.urls import path
# from ..home import views #el punto indica que estamos importando desde la misma ubicación en la que está este archivo (modificado a dos puntos por el cambio del archivo VIEWS que ahora está en la carpeta HOME)
from home import views #Le sacamos los .. ya que no son necesarios y es mejor indicarle a python que acceda al PAQUETE home y no a la carpeta. En el archivo SETTINGS le pusimos que HOME es una aplicacion, por lo que lo toma como paquete.

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),#sacar los arguemtnos de nombre y apellido si sacamos los arg en crear_persona   
    path('about/', views.about, name='about'),
]