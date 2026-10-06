const formBorrar = document.getElementById("form-borrar");

if (formBorrar) {
    formBorrar.addEventListener("submit", (e) => {
        if (!confirm("¿Seguro que desea borrar este producto?")) {
            e.preventDefault();
        }
    });
}