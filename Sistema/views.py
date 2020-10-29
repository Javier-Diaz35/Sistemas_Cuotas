from django.shortcuts import render, redirect
from .models import Alumno, Curso, Cuota, Esquema_Cuota
from .forms import AlumnoForm, CursoForm, CuotaForm, EsquemaForm
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.db.models import Q


def home(request):

    return render (request, 'Sistema/home.html')


def listado_alumno(request):
    alumnos = Alumno.objects.filter(oculto=False).order_by('apellido')
    cursos = Curso.objects.all()
    queryset = request.GET.get('buscar')
    if queryset:
        alumnos = Alumno.objects.filter(
            
            Q(nombre__icontains = queryset) | 
            Q(apellido__icontains = queryset)
            
            ).distinct()

    data = {
        'cursos':cursos,
        'alumnos':alumnos     
        }

    if request.method == 'POST':
        orden = request.POST['ordenar']
        data['ordenseleccionado'] = True
        if orden != 0:
            if orden == '1':
                alumno = Alumno.objects.filter(oculto=False).order_by('apellido')
                data['alumnos'] = alumno
            if orden == '2':
                alumno = Alumno.objects.filter(oculto=False).order_by('-apellido')
                data['alumnos'] = alumno
        idcurso = request.POST['ordencurso']
        if idcurso != 0:
            alumnos = Alumno.objects.filter(curso = idcurso, oculto=False)
            data['alumnos'] = alumnos
            data['cursoid'] = int(idcurso)

    return render(request, 'Sistema/listado_alumnos.html', data)


def nuevo_alumno(request):
    data = {
        'form':AlumnoForm()

    }
    if request.POST.get('becasi'):
            data['becaseleccion'] = True
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
    cursos = Curso.objects.all()
    alumnos = Alumno.objects.filter(oculto=True)
    queryset = request.GET.get('buscar')
    if queryset:
        alumnos = Alumno.objects.filter(oculto=True).filter(
            Q(nombre__icontains = queryset) | 
            Q(apellido__icontains = queryset)
            
            ).distinct()
    data = {
        'cursos':cursos,
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
    cuotas = Cuota.objects.filter(pago = True)
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
    #Se traen los datos de los modelos
    cursos = Curso.objects.all()
    data = {
        'cursos':cursos,
        'form':CuotaForm()

    }
    if request.method == 'POST':
        #El curso seleccionado se lo guarda en una variable
        #Encontrado el curso que se selecciono se busca el listadio de alumnos que esten en el curso seleccionado
        idcurso = request.POST['seleccionCurso']
        alumnos = Alumno.objects.filter(curso = idcurso)
        data['cursoseleccionado'] = True
        data['cursoid'] = int(idcurso)
        data['alumnos'] = alumnos
        try:
            #Se obtiene el alumno que se selecciono
            idalumno = request.POST.get('seleccionAlumno', 0)
            if idalumno != 0:
                print(idalumno)
                #Se busca el alumno que se selecciono en el listado
                #En caso de que el seleccionado no tenga las cuotas generadas se le generan en el momento
                alumno = Alumno.objects.get(pk = idalumno)
                Cuota.verificar_cuotas(alumno)
                data['alumoseleccionado'] = True
                data['alumnoid'] = int(idalumno)
                #Se obtiene cuota que pertenezca al alumno que se selecciono
                cuotas = Cuota.objects.filter(alumno = alumno, pago = False)
                data['cuotas'] = cuotas
                #Se obtieneel id de la cuota que se selecciono
                idcuota = request.POST.get('seleccionMes', 0)
                print('antes...')
                print(idcuota)
                if idcuota != '0':
                    data['cuotaseleccionado'] = True
                    data['cuotaid'] = int(idcuota)
                    print('despues')
                    print(idcuota)
                    if request.POST.get('boton'):
                        #En caso de que se haya seleccionado una cuota se muestra el boton
                        #Y se hace el guardado del nuevo pago
                        print('boton')
                        cuotaselect = Cuota.objects.get(pk = idcuota)
                        cuotaselect.pago = True
                        cuotaselect.fechaPago = datetime.date.today()
                        cuotaselect.save()
                        data['mensaje'] = "Guardado Correctamente"
        except ObjectDoesNotExist:
            pass
                #formulario = CuotaForm(request.POST)
                #if formulario.is_valid():
                #    formulario.save()
                #    data['mensaje'] = "Guardado Correctamente"

    return render(request, 'Sistema/nuevo_pago.html', data)

def impagar_cuota(request, pk):
    cuotas = Cuota.objects.get(pk = pk)
    cuotas.pago = False
    cuotas.save()

    return redirect("listado_cuotas.html")

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
