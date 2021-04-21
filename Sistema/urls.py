from django.urls import path
from .views import home, listado_alumno, nuevo_alumno, modificar_alumno, ocultar_alumno,listado_alumnos_oculto, listado_curso, nuevo_curso, modificar_curso, nueva_cuota, listado_cuota, modificar_cuota, listado_pago, nuevo_pago, ultimos_cobros, desocultar_alumno, list_esquema_cuota, nuevo_esquema, impagar_cuota, eliminar_alumno, historial, informes, importar, eliminar_curso, importar_listado

urlpatterns = [
    path('', home, name="home"),
    #Alumnos
    path('listado-alumno', listado_alumno, name="listado_alumnos"),
    path('nuevo-alumno', nuevo_alumno, name="nuevo_alumno"),
    path('modificar-alumno/<int:pk>', modificar_alumno, name="modificar_alumno"),
    path('ocultar-alumno/<int:pk>', ocultar_alumno , name='ocultar_alumno'),
    path('listado-alumno-oculto', listado_alumnos_oculto, name="listado_alumnos_oculto"),
    path('desocultar-alumno/<int:pk>', desocultar_alumno, name="desocultar_alumno"),
    path('eliminar-alumno/<int:pk>', eliminar_alumno, name="eliminar_alumno"),
    #Cursos
    path('listado-curso', listado_curso, name="listado_curso"),
    path('nuevo-curso', nuevo_curso, name="nuevo_curso"),
    path('modificar-curso/<int:pk>', modificar_curso, name="modificar_curso"),
    path('eliminar-curso/<int:pk>', eliminar_curso, name="eliminar_curso"),
    #Cuota
    path('listado-cuota', listado_cuota, name="listado_cuota"),
    path('nuevo-cuota', nueva_cuota, name="nueva_cuota"),
    path('modificar-cuota/<int:pk>', modificar_cuota, name="modificar_cuota"),
    path('impagar_cuota/<int:pk>', impagar_cuota, name="impagar_cuota"),
    #Pago
    path('listado-pago', listado_pago, name="listado_pago"),
    path('nuevo-pago', nuevo_pago, name="nuevo_pago"),
    path('ultimos-cobros', ultimos_cobros, name="ultimos_cobros"),
    #Esquema
    path('list-esquema-cuota', list_esquema_cuota, name="listado_esquema_cuota"),
    path('nuevo-esquema', nuevo_esquema, name="nuevo_esquema"),

    path('historial', historial, name="historial"),

    path('informes', informes, name="informes"),

    path('import', importar , name='import'),

    path('importar-listado', importar_listado, name='importar_listado'),

]
