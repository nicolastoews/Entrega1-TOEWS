from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect #new import
from home.forms import BusquedaPersona, PersonaFormulario

from home.models import Persona

def crear_persona(request):
    if request.method == 'POST':
        formulario = PersonaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now()) #lo crea vacio no se por que
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save() #guarda a la persona creada en la DB, si esto no está, la persona no queda guardad.
                            #no olvidar los save de cada objeto
            # return render(request,'home/ver_persona.html', {}) #Este te trae solo los datos que acabas de ingresar
            return redirect('ver_personas') #este te manda directamente a ver_personas mostrando todos los datos
    formulario = PersonaFormulario()
    return render(request,'home/crear_persona.html', {'formulario': formulario}) #new, reemplaza las 3 lineas de arriba

def ver_personas(request):
    nombre = request.GET.get('nombre')
    if nombre:
        personas = Persona.objects.filter(nombre__icontains = nombre)
    else:
        personas = Persona.objects.all() #trae todos los objetos de Persona que estén en la DB
    formulario = BusquedaPersona()
    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario}) #new, reemplaza las 3 lineas de arriba

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')