from django.shortcuts import render, redirect
from .models import Alumno, Curso, Cuota, Esquema_Cuota
from .forms import AlumnoForm, CursoForm, CuotaForm, EsquemaForm, FormilarioLogin, CustomUserCreationForm
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.db.models import Q, Count
from django.core.paginator  import Paginator
from tablib import Dataset
from bootstrap_modal_forms.generic import BSModalCreateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, authenticate 
from django.contrib import messages

'''class Login(FormView):
    template_name = 'login.html'
    form_class = FormilarioLogin
    success_url = reverse_lazy('listado_alumnos')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    @login_required(login_url='/accounts/login')
    def home(request):

        return render (request, 'Sistema/login.html')

    @login_required(login_url='/accounts/login')
'''

def home(request):

    return render (request, 'Sistema/login.html')

@login_required
def listado_alumno(request):
    alumnos = Alumno.objects.filter(oculto=False)
    cursos = Curso.objects.all()

    if request.POST.get('apellido'):

        alumnos = Alumno.objects.filter(oculto=False).order_by('apellido')
    
    if request.POST.get('dni'):

        alumnos = Alumno.objects.filter(oculto=False).order_by('dni')
    

    paginator = Paginator(alumnos, 8)
    pagina = request.GET.get('page') or 1
    page_obj = paginator.get_page(pagina)
    alumnos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, alumnos.paginator.num_pages + 1)

    queryset = request.GET.get('buscar')
    if queryset:
        alumnos = Alumno.objects.filter(
            
            Q(nombre__icontains = queryset) | 
            Q(apellido__icontains = queryset)
            
            ).distinct()

    data = {
        'cursos':cursos,
        'page_obj': page_obj,
        'alumnos':alumnos  
        }

    return render(request, 'Sistema/listado_alumnos.html', data)

@login_required
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
    return render(request, 'Sistema/import_excel.html', data)

@login_required
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

@login_required
def ocultar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    alumno.oculto = True
    alumno.save()

    return redirect(to="listado_alumnos")

@login_required
def desocultar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    alumno.oculto = False
    alumno.save()

    return redirect("listado_alumnos")

@login_required
def eliminar_alumno(request, pk):
    alumno = Alumno.objects.get(pk = pk)
    alumno.delete()

    return redirect(request, 'Sistema/alumnos_ocultos.html')

@login_required
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

@login_required
def listado_curso(request):
    cursos = Curso.objects.all()
    data = {
        'cursos':cursos
        }
    return render(request, 'Sistema/listado_cursos.html', data)

@login_required
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

@login_required
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

@login_required
def eliminar_curso(request, pk):
    curso = Curso.objects.get(pk = pk)
    curso.delete()

    return redirect(request, 'Sistema/listado_cursos.html')

@login_required
def listado_cuota(request):
    cuotas = Cuota.objects.filter(pago = True)

    queryset = request.GET.get('buscar')
    if queryset:
        cuotas = Cuota.objects.filter(
            
            Q(alumno__nombre__icontains = queryset)            
            ).filter(pago = True).distinct()

    data = {
        'cuotas':cuotas
        }
    return render(request, 'Sistema/listado_cuotas.html', data)

@login_required
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

@login_required
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

@login_required
def listado_pago(request):
    pagos = Pago.objects.all()
    data = {
        'pagos':pagos
        }
    return render(request, 'Sistema/listado_pago.html', data)

@login_required
def ultimos_cobros(request):
    pagos = Pago.objects.all()
    data = {
        'pagos':pagos
        }
    return render(request, 'Sistema/ultimos_cobros.html', data)

@login_required
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

@login_required
def impagar_cuota(request, pk):
    cuotas = Cuota.objects.get(pk = pk)
    cuotas.pago = False
    cuotas.save()

    return redirect("listado_cuotas.html")

@login_required
def list_esquema_cuota(request):
    esquema = Esquema_Cuota.objects.all()
    data = {
        'esquemas':esquema
        }
    return render(request, 'Sistema/list_esquema_cuota.html', data)

@login_required
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

@login_required
def historial(request):
    año = datetime.date.today().year

    history = Cuota.objects.filter(year = año).order_by('alumno')

    queryset = request.GET.get('buscar')
    if queryset:
        history = Cuota.objects.filter(
            
            Q(alumno__nombre__icontains = queryset)            
            ).distinct()

    if request.POST.get('añolectivo') == "2020":
        history = Cuota.objects.filter(year = "2020").order_by('alumno')
    
    if request.POST.get('añolectivo') == "2021":
        history = Cuota.objects.filter(year = "2021").order_by('alumno')

    data = {
        'pagos':history
    }

    return render(request, 'Sistema/historial.html', data)

@login_required
def informes(request):

    return render(request, 'Sistema/informes.html', )

@login_required
def importar(request):
    #template = loader.get_template('export/importar.html')  
    if request.method == 'POST':  
        alumno_resource = AlumnoResource()
        dataset = Dataset()  
        #print(dataset)
        nuevos_alumnos = request.FILES['xlsfile']  
        #print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())  
        #print(dataset)
        result = alumno_resource.import_data(dataset, dry_run=True) # Test the data import  
        #print(result.has_errors())  
        if not result.has_errors(): 
            alumno_resource.import_data(dataset, dry_run=False) # Actually import now  


    return render(request, 'Sistema/importar.html')

@login_required
def import_excel(request):
    
    return render(modal, 'Sistema/import_excel.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Correctamente")
            return redirect(to="listado_alumnos")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
