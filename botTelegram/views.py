from django.shortcuts import render
from models import Trafico, Vehiculo, Operador
from datetime import datetime
# Create your views here.

def guardar_datos(request):
    contenido = leer_archivo().split('\n')
    # print(type(leer_archivo()))
    # contenido = str(leer_archivo()).split()
    print(contenido)
    if(int(contenido[0]) == 1):
        incidencia = Trafico(Ubicacion = contenido[1],
                             IntesidadTrafico = contenido[2],
                             Fecha = datetime.now())
        incidencia.save()
 
def leer_archivo():
    content = open('informacion.txt', 'r')
    contenido = content.read()
    content.close
    return contenido