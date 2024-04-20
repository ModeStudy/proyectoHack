from django.shortcuts import render
from models import Trafico, Vehiculo, Operador, Accidentes, Gasolina, Asaltos, Clima, FallaMecanica, Documentacion
from datetime import datetime
# Create your views here.

def guardar_datos(request):
    contenido = leer_archivo().split('\n')
    # print(type(leer_archivo()))
    # contenido = str(leer_archivo()).split()
    print(contenido)
    if(int(contenido[0]) == 1):
        incidencia = Trafico(Ubicacion = contenido[1], IntensidadTrafico = contenido[2], Fecha = datetime.now())
        incidencia.save()
    
    if int(contenido[0] == 2):
        incidencia = Accidentes(Ubicacion = contenido[1], GravedadAccidente = contenido[2], Fecha = datetime.now())
        incidencia.save()
    
    if int(contenido[0] == 3):
        incidencia = Gasolina(PorcentajeGasolina = contenido[1], DineroDisponible = contenido[2], Ubicacion = contenido[3])
        incidencia.save()

    if int(contenido[0] == 4):
       incidencia = Asaltos(Ubicacion = contenido[1], Fecha = datetime.now(), PerdidasEconomicas = contenido[3])
       incidencia.save()

    if int(contenido[0] == 5):
       incidencia = Clima(Ubicacion = contenido[1], TipoClima = contenido[2], Fecha = datetime.now())
       incidencia.save()

    if int(contenido[0] == 6):
         incidencia = FallaMecanica(Ubicacion = contenido[1], Fecha = datetime.now(), Falla = contenido[3])
         incidencia.save()

    if int(contenido[0] == 7):
         incidencia = Documentacion(Fecha = datetime.now(), TipoDocumentacion = contenido[2])
         incidencia.save()

def respuestas():
    contenido = leer_archivo().split('\n')
    pass

def leer_archivo():
    content = open('informacion.txt', 'r')
    contenido = content.read()
    content.close
    return contenido