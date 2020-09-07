function confirmarEliminacion(pk){

    swal({
        title: "Esta seguro?",
        text: "El alumno se va a dar de baja y no se va poder deshacer la accion",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          window.location.href = "/ocultar_alumno/" + pk + "/";
        } else {
          swal("Your imaginary file is safe!");
        }
      });
}