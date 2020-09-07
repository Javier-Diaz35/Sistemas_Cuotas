from django import forms
from django.forms import ModelForm
from .models import Alumno, Curso, Cuota, Pago

class AlumnoForm(ModelForm):

    class Meta:
        model = Alumno
        fields = ['apellido', 'nombre', 'dni', 'celular', 'curso', 'matricula']

class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = ['nombre', 'division']

class CuotaForm(ModelForm):

    class Meta:
        model = Cuota
        fields = ['alumno', 'monto', 'numeromes']

class PagoForm(ModelForm):

    
    class Meta:
        model = Pago
        fields = ['alumno', 'cuotaEstablecida']