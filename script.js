async function obtenerFrase() {
    const respuesta = await fetch("http://127.0.0.1:5000/api/frase");
    const data = await respuesta.json();
    document.getElementById("frase").textContent = data.frase;
}