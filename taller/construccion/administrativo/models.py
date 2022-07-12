
from django.db import models

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    
    tipo_opciones = (('Residencial', 'Residencial'),
                ('Comercial','Comercial'))
    
    tipo = models.CharField(max_length=30 ,choices=tipo_opciones)

    

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_cantidad_cuartos(self):
        valor = [t.numero_cuartos for t in self.los_departamentos.all()]
        valor = sum(valor)
        return valor
    
    def obtener_costo_departamentos(self):
        valor = [t.costo for t in self.los_departamentos.all()]
        valor = sum(valor)
        return valor


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=30)
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="los_departamentos")

    def __str__(self):
        return "%s %s %s %s" % (self.nombre_propietario,
                self.costo,
                self.numero_cuartos,
                self.edificio)