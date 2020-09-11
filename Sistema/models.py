from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=15, null=False, blank=False)
    division = models.CharField(max_length=5, unique=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.division


class Alumno(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    apellido = models.CharField(max_length=20, null=True)
    celular = models.CharField(max_length=20, null=True)
    dni = models.CharField(max_length=20, unique=True, null=True)
    matricula = models.CharField(max_length=20, unique=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)
    oculto = models.BooleanField(default=False)
    beca = models.BooleanField(default=False)
    mediaBeca = models.BooleanField(default=False)

    def __str__(self):
        return self.apellido + ' ' + self.nombre



class Cuota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateField(auto_now=True, null=False, blank=False)
    monto = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    numeromes = models.CharField(max_length=2, null=False)

    def __str__(self):
        return self.numeromes

class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False, blank=False)
    cuotaEstablecida = models.ForeignKey(Cuota, on_delete=models.CASCADE, null=False, blank=False)
    fechaPago = models.DateField(auto_now=True, null=False, blank=False)
    total = models.CharField(max_length=20, blank=False, null=True) 

    def __str__(self):
        return self.cuotaEstablecida    

class Recibo(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False, blank=False)
    cuotaEstablecida = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2) 
    montoPagar = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    fechaPago = models.DateField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return self.montoPagar









    
