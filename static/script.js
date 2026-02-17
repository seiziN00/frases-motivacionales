const frase = document.getElementById("frase");

async function obtenerFrase() {
    try {
        const res = await fetch("http://127.0.0.1:5000/api/frase");
        const data = await res.json();
        frase.textContent = data.frase;
        cargarStats();
    } catch {
        frase.textContent = "Error al obtener frase";
    }
}



async function agregarFrase() {
    const texto = document.getElementById("nuevaFrase").value;
    
    await fetch("http://127.0.0.1:5000/api/frase", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ frase: texto })
    });

    document.getElementById("nuevaFrase").value = "";
    cargarStats();
}

async function cargarStats() {
    const res = await fetch("http://127.0.0.1:5000/api/stats");
    const data = await res.json();
    document.getElementById("stats").textContent =
        "Total frases: " + data.total_frases;
}