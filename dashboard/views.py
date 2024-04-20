from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest
from botTelegram.models import Trafico, Accidentes, Gasolina, Asaltos, Clima, FallaMecanica, Documentacion

# Create your views here.
def dashboard(request):
    plantilla = loader.get_template('dashboard/index.html')
    total_trafico = Trafico.objects.count()
    total_accidentes = Accidentes.objects.count()
    total_gasolina = Gasolina.objects.count()
    total_asaltos = Asaltos.objects.count()
    total_clima = Clima.objects.count()
    total_FallaMecanica = FallaMecanica.objects.count()
    total_documentacion = Documentacion.objects.count()
    context = { 'total_trafico' : total_trafico, 'total_accidentes': total_accidentes, 'total_gasolina' : total_gasolina,
               'total_asaltos' : total_asaltos, 'total_clima' : total_clima, 'total_FallaMecanica' : total_FallaMecanica,
               'total_documentacion' : total_documentacion}
    return HttpResponse(plantilla.render(context=context, request=request))
    

"""personajes = Personaje.objects.all()
    plantilla = loader.get_template('personajes/galeria.html')
    context = {
        'personajes': personajes,
    }
    return HttpResponse(plantilla.render(context=context, request=request))"""