from django.contrib import admin
from .models import Cuota, Alumno, Curso, Esquema_Cuota

admin.site.register(Esquema_Cuota)
admin.site.register(Cuota)
admin.site.register(Alumno)
admin.site.register(Curso)

