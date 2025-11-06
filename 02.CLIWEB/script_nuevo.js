// Configuración
const BASE_URL = "http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources";
const USUARIO_VALIDO = "MONSTER";
const PASSWORD_VALIDA = "Monster9";

let categoriaActual = "";

// Conversiones por categoría
const conversiones = {
    longitud: [
        { nombre: "Kilómetros → Metros", endpoint: "conversion/km-a-m", origen: "km", destino: "m" },
        { nombre: "Metros → Centímetros", endpoint: "conversion/m-a-cm", origen: "m", destino: "cm" },
        { nombre: "Centímetros → Milímetros", endpoint: "conversion/cm-a-mm", origen: "cm", destino: "mm" }
    ],
    temperatura: [
        { nombre: "Celsius → Fahrenheit", endpoint: "conversion/celsius-a-fahrenheit", origen: "°C", destino: "°F" },
        { nombre: "Fahrenheit → Celsius", endpoint: "conversion/fahrenheit-a-celsius", origen: "°F", destino: "°C" },
        { nombre: "Celsius → Kelvin", endpoint: "conversion/celsius-a-kelvin", origen: "°C", destino: "K" }
    ],
    masa: [
        { nombre: "Kilogramos → Gramos", endpoint: "conversion/kg-a-gramos", origen: "kg", destino: "g" },
        { nombre: "Gramos → Miligramos", endpoint: "conversion/gramos-a-miligramos", origen: "g", destino: "mg" },
        { nombre: "Toneladas → Kilogramos", endpoint: "conversion/toneladas-a-kg", origen: "t", destino: "kg" }
    ]
};

// ========== LOGIN ==========

function validarLogin() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    if (username === USUARIO_VALIDO && password === PASSWORD_VALIDA) {
        cambiarPantalla("loginScreen", "categoryScreen");
    } else {
        alert("❌ Credenciales incorrectas");
        document.getElementById("password").value = "";
    }
}

// ========== NAVEGACIÓN ==========

function cambiarPantalla(desde, hacia) {
    document.getElementById(desde).classList.remove("active");
    document.getElementById(hacia).classList.add("active");
}

function seleccionarCategoria(categoria) {
    categoriaActual = categoria;
    
    const select = document.getElementById("conversion");
    select.innerHTML = "<option value=''>-- Seleccione una conversión --</option>";
    
    conversiones[categoria].forEach((conv, index) => {
        const option = document.createElement("option");
        option.value = index;
        option.textContent = conv.nombre;
        select.appendChild(option);
    });
    
    cambiarPantalla("categoryScreen", "conversionScreen");
}

function volverACategorias() {
    document.getElementById("valor").value = "";
    document.getElementById("conversion").value = "";
    cambiarPantalla("conversionScreen", "categoryScreen");
}

function volverAConvertir() {
    document.getElementById("valor").value = "";
    cambiarPantalla("resultScreen", "conversionScreen");
}

function cerrarSesion() {
    if (confirm("¿Cerrar sesión?")) {
        document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
        document.getElementById("loginScreen").classList.add("active");
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
        document.getElementById("valor").value = "";
        document.getElementById("conversion").value = "";
        categoriaActual = "";
    }
}

// ========== CONVERSIÓN ==========

function realizarConversion() {
    const conversionIndex = document.getElementById("conversion").value;
    const valor = document.getElementById("valor").value;
    
    if (conversionIndex === "") {
        alert("⚠️ Seleccione una conversión");
        return;
    }
    
    if (!valor || isNaN(valor)) {
        alert("⚠️ Ingrese un valor válido");
        return;
    }
    
    const conversion = conversiones[categoriaActual][conversionIndex];
    const url = `${BASE_URL}/${conversion.endpoint}/${valor}`;
    
    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error("HTTP " + response.status);
            return response.text();
        })
        .then(data => {
            const resultado = parseFloat(data);
            
            document.getElementById("resultadoValor").textContent = 
                `${resultado.toFixed(4)} ${conversion.destino}`;
            document.getElementById("resultadoFormula").textContent = 
                `${valor} ${conversion.origen} = ${resultado.toFixed(4)} ${conversion.destino}`;
            
            cambiarPantalla("conversionScreen", "resultScreen");
        })
        .catch(error => {
            alert("❌ ERROR: " + error.message + "\n\nURL: " + url);
        });
}

// ========== EVENT LISTENERS ==========

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("username").addEventListener("keypress", function(e) {
        if (e.key === "Enter") document.getElementById("password").focus();
    });
    
    document.getElementById("password").addEventListener("keypress", function(e) {
        if (e.key === "Enter") validarLogin();
    });
    
    document.getElementById("valor").addEventListener("keypress", function(e) {
        if (e.key === "Enter") realizarConversion();
    });
});
