from django.shortcuts import render, redirect
from .models import Alumno, Curso, Cuota, Esquema_Cuota
from .forms import AlumnoForm, CursoForm, CuotaForm, EsquemaForm
from django.core.exceptions import ObjectDoesNotExist
import datetime


def home(request):

    return render (request, 'Sistema/home.html')


def listado_alumno(request):
    alumnos = Alumno.objects.filter(oculto=False).order_by('apellido')
    cursos = Curso.objects.all()
    data = {
        'cursos':cursos,
        'alumnos':alumnos     
        }
    return render(request, 'Sistema/listado_alumnos.html', data)


def nuevo_alumno(request):
    data = {
        'form':AlumnoForm()

    }
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST)
        print(formulario)
        if formulario.is_valid():  
            nuevoalumno = formulario.save()
            Cuota.verificar_cuotas(nuevoalumno)
            data['mensaje'] = "Guardado Correctamente"
        else:
            data['mensaje'] = formulario.errors
    return render(request, 'Sistema/nuevo_alumno.html', data)

def modificar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    template = 'Sistema/modificar_alumno.html'
    formulario = AlumnoForm(request.POST or None, instance=alumno)

    if formulario.is_valid():
        formulario.save()
        return redirect("listado_alumnos")
    
    data = {
        'form':formulario
    }

    return render(request, template, data)

def ocultar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    alumno.oculto = True
    alumno.save()

    return redirect("listado_alumnos")

def desocultar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    alumno.oculto = False
    alumno.save()

    return redirect("listado_alumnos")

def listado_alumnos_oculto(request):
    alumnos = Alumno.objects.filter(oculto=True)
    orden = request.POST['ordenar']
    data = {
        'alumnos':alumnos
        }
    if request.method == 'POST':
        if request.POST.get('ordenar'):
            if orden == 1:
                alumnos = Alumno.objects.filter(oculto=True).order_by('apellido')
            if orden == 2:
                alumnos = Alumno.objects.filter(oculto=True).order_by('-apellido')

    return render(request, 'Sistema/alumnos_ocultos.html', data)

def listado_curso(request):
    cursos = Curso.objects.all()
    data = {
        'cursos':cursos
        }
    return render(request, 'Sistema/listado_cursos.html', data)

def nuevo_curso(request):
    data = {
        'form':CursoForm()

    }
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        print(formulario)
        if formulario.is_valid():  
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'Sistema/nuevo_curso.html', data)

def modificar_curso(request, pk):
    curso = Curso.objects.get(pk = pk)
    template = 'Sistema/modificar_curso.html'
    formulario = CursoForm(request.POST or None, instance=curso)

    if formulario.is_valid():
        formulario.save()
        return redirect("listado_cursos")
    
    data = {
        'form':formulario
    }

    return render(request, template, data)

def listado_cuota(request):
    cuotas = Cuota.objects.all()
    data = {
        'cuotas':cuotas
        }
    return render(request, 'Sistema/listado_cuotas.html', data)

def nueva_cuota(request):
    data = {
        'form':CuotaForm()

    }
    if request.method == 'POST':
        formulario = CuotaForm(request.POST)
        print(formulario)
        if formulario.is_valid():  
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'Sistema/nueva_cuota.html', data)

def modificar_cuota(request, pk):
    cuota = Cuota.objects.get(pk = pk)
    template = 'Sistema/modificar_cuota.html'
    formulario = CuotaForm(request.POST or None, instance=cuota)

    if formulario.is_valid():
        formulario.save()
        return redirect("listado_cuota")
    
    data = {
        'form':formulario
    }

    return render(request, template, data)

def listado_pago(request):
    pagos = Pago.objects.all()
    data = {
        'pagos':pagos
        }
    return render(request, 'Sistema/listado_pago.html', data)

def ultimos_cobros(request):
    pagos = Pago.objects.all()
    data = {
        'pagos':pagos
        }
    return render(request, 'Sistema/ultimos_cobros.html', data)

def nuevo_pago(request):
    cursos = Curso.objects.all()
    data = {
        'cursos':cursos,
        'form':CuotaForm()

    }
    if request.method == 'POST':
        idcurso = request.POST['seleccionCurso']
        alumnos = Alumno.objects.filter(curso = idcurso)
        cuotas = Cuota.objects.filter(alumno = alumnos)
        #print(alumnos)
        data['cursoseleccionado'] = True
        data['cursoid'] = int(idcurso)
        data['alumnos'] = alumnos
        data['cuotas'] = cuotas
        try: 
            idalumno = request.POST.get('seleccionAlumno', 0)
            if idalumno != 0:
                data['alumoseleccionado'] = True
                data['alumnoid'] = int(idalumno)
                idcuota = request.POST.get('seleccionMes', 0)
                if idcuota != 0:
                    data['cuotaseleccionado'] = True
                    data['cuotaid'] = int(idcuota)
                    
        except ObjectDoesNotExist:
            pass
                #formulario = PagoForm(request.POST)
                #if formulario.is_valid():
                #    formulario.save()
                #    data['mensaje'] = "Guardado Correctamente"

    return render(request, 'Sistema/nuevo_pago.html', data)


def list_esquema_cuota(request):
    esquema = Esquema_Cuota.objects.all()
    data = {
        'esquemas':esquema
        }
    return render(request, 'Sistema/list_esquema_cuota.html', data)

def nuevo_esquema(request):
    data = {
        'form':EsquemaForm()

    }
    if request.method == 'POST':
        formulario = EsquemaForm(request.POST)
        if formulario.is_valid():  
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'Sistema/nuevo_esquema.html', data)
