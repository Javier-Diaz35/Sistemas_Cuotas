function confirmarEliminarAlumno(id) {
  
  Swal.fire({
    title: '¿Estas seguro?',
    text: "El alumno sera enviado a la lista de dados de baja, podra eliminarlo definitivamente desde ahi",
    icon: 'ALERTA',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, estoy de acuerdo',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      window.location.href = "/ocultar_alumno/" + id + "/";

    }
  });
}

$('#exampleModal').modal('show');

