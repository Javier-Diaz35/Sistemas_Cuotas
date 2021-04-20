from import_export import resource
from .models import Alumno

class AlumnoResource(resource.ModelResource):
    class Meta:
        model = Alumno
        