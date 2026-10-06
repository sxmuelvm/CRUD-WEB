// Foco automatico en el primer campo visible del contenido
const primerCampo = document.querySelector("main input:not([type=hidden])");
if (primerCampo) {
    primerCampo.focus();
}