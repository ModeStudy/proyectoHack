from django.db import models

class Trafico(models.Model):
    Ubicacion = models.CharField(max_length=200)
    IntensidadTrafico = models.IntegerField(default=0)
    Fecha = models.DateTimeField(default=None)

    def __str__(self):
        return self.Ubicacion


    def __str__(self):
        return str(self.IntensidadTrafico)
    
    def __str__(self):
        return str(self.Fecha)

class Accidentes(models.Model):
    Ubicacion = models.CharField(max_length=200)
    GravedadAccidente = models.IntegerField(default=0)
    Fecha = models.DateTimeField(default=None)

    def __str__(self):
        return self.Ubicacion


    def __str__(self):
        return str(self.GravedadAccidente)
    
    def __str__(self):
        return str(self.Fecha)
    
class Gasolina(models.Model):
    PorcentajeGasolina = models.DecimalField(decimal_places=2, max_digits=5)
    DineroDisponible = models.DecimalField(decimal_places=2, max_digits=6)
    Ubicacion = models.CharField(max_length=200)
    Fecha = models.DateTimeField(default=None)

    def __str__(self):
        return self.Ubicacion

    def __str__(self):
        return self.DineroDisponible
    
    def __str__(self):
        return str(self.PorcentajeGasolina)
    
    def __str__(self):
        return str(self.Fecha)

class Asaltos(models.Model):
    Ubicacion = models.CharField(max_length=200)
    Fecha = models.DateTimeField(default=None)
    PerdidasEconomicas = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    IsAsaltoArmado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Ubicacion


    def __str__(self):
        return str(self.Fecha)
    
    def __str__(self):
        return str(self.PerdidasEconomicas)
    
    def __str__(self):
        return str(self.IsAsaltoArmado)
    
class Clima(models.Model):
    Ubicacion = models.CharField(max_length=200)
    TipoClima = models.CharField(max_length=50)
    Fecha = models.DateTimeField(default=None)
    IsNecesidadHotel = models.BooleanField(default=False)

    def __str__(self):
        return self.Ubicacion
    
    def __str__(self):
        return str(self.TipoClima)
    
    def __str__(self):
        return str(self.Fecha)
    
    def __str__(self):
        return str(self.IsNecesidadHotel)
        
class FallaMecanica(models.Model):
    Ubicacion = models.CharField(max_length=200)
    Fecha = models.DateTimeField(default=None)
    Falla = models.CharField(max_length=100)

    def __str__(self):
        return self.Ubicacion
    
    def __str__(self):
        return str(self.Fecha)
    
    def __str__(self):
        return self.Falla

class Documentacion(models.Model):
    Fecha = models.DateTimeField(default=None)
    TipoDocumentacion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Fecha)
    
    def __str__(self):
        return self.TipoDocumentacion

    

class Vehiculo(models.Model):
    Matricula = models.CharField(max_length=20)
    Tonelaje = models.DecimalField
    Trafico = models.ForeignKey(Trafico, on_delete=models.CASCADE)
    Accidente = models.ForeignKey(Accidentes, on_delete=models.CASCADE)
    Gas = models.ForeignKey(Gasolina, on_delete=models.CASCADE)
    Asalto = models.ForeignKey(Asaltos, on_delete=models.CASCADE)
    CLima = models.ForeignKey(Clima, on_delete=models.CASCADE)
    FalloMecanico = models.ForeignKey(FallaMecanica, on_delete=models.CASCADE)
    Documentacion = models.ForeignKey(Documentacion, on_delete=models.CASCADE)
    
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