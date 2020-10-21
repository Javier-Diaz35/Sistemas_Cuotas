from django import forms
from django.forms import ModelForm
from .models import Alumno, Curso, Cuota, Esquema_Cuota

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

class EsquemaForm(ModelForm):

    class Meta:
        model = Esquema_Cuota
        fields = ['year', 'monto', 'numeromes']

