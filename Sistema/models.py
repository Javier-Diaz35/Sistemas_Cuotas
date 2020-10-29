from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import datetime

class Curso(models.Model):
    nombre = models.CharField(max_length=15, null=False, blank=False)
    division = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.division


class Alumno(models.Model):
    nombre = models.CharField(max_length=20, null=True, validators=[MinLengthValidator(4)])
    apellido = models.CharField(max_length=20, null=True, validators=[MinLengthValidator(4)])
    celular = models.CharField(max_length=20, null=True)
    dni = models.CharField(max_length=10, unique=True, null=True, validators=[MinLengthValidator(8)])
    matricula = models.CharField(max_length=20, unique=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False, blank=False)
    oculto = models.BooleanField(default=False)
    beca = models.BooleanField(default=False)
    mediaBeca = models.BooleanField(default=False)

    def __str__(self):
        return self.apellido + ' ' + self.nombre



class Cuota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=False, blank=False)
    year = models.IntegerField(null=False, default=0)
    monto = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    numeromes = models.IntegerField(null=False, blank=False)
    fechaPago = models.DateField(null=True, blank=True)
    pago = models.BooleanField(default=False)

    def verificar_cuotas(verificalumno):
        año = datetime.date.today().year
        cuotas_del_año = Esquema_Cuota.objects.filter(year = año)
        for cuota in cuotas_del_año:
                if not Cuota.objects.filter(year = año, alumno = verificalumno, numeromes = cuota.numeromes).exists():
                    nueva_cuota = Cuota.objects.create(alumno = verificalumno, year = año, monto = cuota.monto, numeromes = cuota.numeromes)
                    print(verificalumno.mediaBeca)
                    nueva_cuota.save()
                    print('cuota generada') 
                    print(cuota.numeromes)
                print('verificando cuotas...')
                print(verificalumno)
                return True

    def __str__(self):
        return self.monto
            

class Esquema_Cuota(models.Model):
    year = models.IntegerField(null=False, default=0)
    monto = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    numeromes = models.IntegerField(null=False, blank=False)



    def __str__(self):
        return str(self.monto)








    
