from django import forms
from django.forms import ModelForm
from .models import Alumno, Curso, Cuota, Esquema_Cuota
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class AlumnoForm(ModelForm):


    #nombre = forms.CharField(min_length=3, max_length=7)

    class Meta:
        model = Alumno
        fields = ['apellido', 'nombre', 'dni', 'celular', 'curso', 'matricula', 'beca', 'mediaBeca']
        fields_required = ['apellido', 'nombre', 'dni', 'celular', 'curso']
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'dni' : 'DNI',
            'celular' : 'Celular',
            'curso' : 'Curso',
            'matricula' : 'Matricula',
            'beca' : 'Beca Completa',
            'mediaBeca' : 'Media Beca'
        }

        widgets = {
            'nombre' : forms.TextInput(
                attrs= {
                    'minlength':3,
                    'maxlength':7,
                    'pattern': '[-a-zA-Z0]+$',
                    'class': 'form-control',
                    'placeholder': 'Nombre/s del alumno',
                    'id': 'id_nombre',                    
                }),

            'apellido' : forms.TextInput(
                attrs={
                    'minlength':4,
                    'maxlength':10,
                    'pattern': '[-a-zA-Z0]+$',
                    'class': 'form-control',
                    'placeholder': 'Apellido/s del alumno',
                    'id': 'id_apellido'
                }),

            'celular' : forms.NumberInput(
                attrs={
                    'minlength':5,
                    'maxvalue':10,
                    'pattern': '[-a-zA-Z0]+$',
                    'class': 'form-control',
                    'placeholder': '3546435111',
                    'id': 'id_telefono'
                }),

            'dni' : forms.NumberInput(
                attrs={
                    
                    'class': 'form-control',
                    'placeholder': 'dni',
                    'id': 'id_dni'
                }),

            'matricula' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '00000001',
                    'id': 'id_matricula'
                }),
            
            'curso' : forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'id_curso'
                }),
        }

class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = ['nombre', 'division']

        labels = {
            'nombre' : 'Nombre',
            'division' : 'Division',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'minlength':5,
                    'minlength':6,
                    'pattern': '[-a-zA-Z0]+$',
                    'class': 'form-control',
                    'placeholder': 'Primero',
                    'id': 'id_nombre',
                }
            ),

            'division' : forms.TextInput(
                attrs={
                    'minlenght':1,
                    'maxlength':4,
                    'pattern': '[-a-zA-Z0]+$',
                    'class': 'form-control',
                    'placeholder': 'A',
                    'id': 'id_division'
                }
            )
        }

class CuotaForm(ModelForm):



    class Meta:
        model = Cuota
        fields = ['alumno', 'monto', 'numeromes', 'year']
        widgets = {
            'year': forms.SelectDateWidget(years=range(2020, 2030),
                attrs={
                    'class': 'form-control',    
                }
            )
        }

class EsquemaForm(ModelForm):

    class Meta:
        model = Esquema_Cuota
        fields = ['year', 'monto', 'numeromes']

        labels = {
            'year' : 'Año de la cuota',
            'monto' : 'Monto',
            'numeromes' : 'Numero del mes',
        }

        widgets = {
            'year' : forms.NumberInput(
                attrs={
                    'minvalue':4,
                    'maxvalue':4,
                    'pattern': '[A-Za-z\ ]{5,80}',
                    'class' : 'form-control',
                    'placeholder': '2000',
                    'id': 'id_year'
                }
            ),

            'monto' : forms.NumberInput(
                attrs={
                    'minvalue':3,
                    'maxvalue':6,
                    'pattern': '[A-Za-z\ ]{5,80}',
                    'class' : 'form-control',
                    'placeholder': '800',
                    'id': 'id_monto'
                }
            ),

            'numeromes' : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder': '01',
                    'id': 'id_numeromes'
                }
            )
        }

class FormilarioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormilarioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widgets.attrs['class'] = 'form-control'
        self.fields['username'].widgets.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widgets.attrs['class'] = 'formcontrol'
        self.fields['password'].widgets.attrs['placeholder'] = 'Contraseña'

class CustomUserCreationForm(UserCreationForm):
    pass
