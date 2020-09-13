from django.shortcuts import render, redirect
from .models import Alumno, Curso, Cuota, Pago
from .forms import AlumnoForm, CursoForm, CuotaForm, PagoForm


def home(request):

    return render (request, 'Sistema/home.html')


def listado_alumno(request):
    alumnos = Alumno.objects.filter(oculto=False)
    data = {
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
            formulario.save()
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
    data = {
        'alumnos':alumnos     
        }
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
    data = {
        'form':PagoForm()

    }
    if request.method == 'POST':
        formulario = PagoForm(request.POST)
        print(formulario)
        if formulario.is_valid():  
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'Sistema/nuevo_pago.html', data)


def historial(request):
    pagos = Pago.objects.all()
    data = {
        'pagos':pagos
        }
    return render(request, 'Sistema/historial.html', data)
