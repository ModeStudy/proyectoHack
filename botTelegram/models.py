from django.db import models

class Trafico(models.Model):
    Ubicacion = models.CharField(max_length=200)
    IntensidadTrafico = models.IntegerField
    Fecha = models.DateTimeField

    def __str__(self):
        return self.Ubicacion


    def __str__(self):
        return str(self.IntensidadTrafico)
    
    def __str__(self):
        return str(self.Fecha)


class Vehiculo(models.Model):
    Matricula = models.CharField(max_length=20)
    Tonelaje = models.DecimalField
    Trafico = models.ForeignKey(Trafico, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Matricula
    
    def __str__(self):
        return str(self.Tonelaje)
    

class Operador(models.Model):
    Nombre = models.CharField(max_length=150)
    Edad = models.IntegerField
    Licencia = models.CharField(max_length=100)
    Vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

    def __str__(self):
        return str(self.Edad)
    def __str__(self):
        return str(self.Licencia)