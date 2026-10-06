const filtro = document.getElementById("filtro");
const filas = document.querySelectorAll("#tabla tbody tr");

// Minusculas y sin tildes, para que "cafe" encuentre "Café"
function normalizar(texto) {
    return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

// Texto de la fila sin la celda de acciones (la que contiene enlaces)
function textoDeFila(fila) {
    return Array.from(fila.cells)
        .filter((celda) => !celda.querySelector("a"))
        .map((celda) => celda.textContent)
        .join(" ");
}

filtro.addEventListener("input", () => {
    const texto = normalizar(filtro.value.trim());
    filas.forEach((fila) => {
        fila.hidden = !normalizar(textoDeFila(fila)).includes(texto);
    });
});