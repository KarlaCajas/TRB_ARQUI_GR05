// Configuración
// Para acceso desde móvil, usa la IP de tu PC en la red (Red de casa: 192.168.18.113)
// Para acceso local, usa localhost
const BASE_URL = "http://localhost:8080/WS_ConersionUnidades_RESTFULL/webresources";
const USUARIO_VALIDO = "MONSTER";
const PASSWORD_VALIDA = "Monster9";

let categoriaActual = '';

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

// ========== FUNCIONES DE LOGIN ==========

function validarLogin() {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    if (username === USUARIO_VALIDO && password === PASSWORD_VALIDA) {
        // Login exitoso - mostrar bienvenida
        alert('✅ ¡Bienvenido al Sistema!\n\n' + username + '\n\nSistema de Conversión de Unidades');
        
        // Ir a pantalla de categorías
        cambiarPantalla('loginScreen', 'categoryScreen');
    } else {
        // Login fallido
        alert('❌ Error de Login\n\nCredenciales incorrectas.\nIntenta nuevamente.');
        document.getElementById('password').value = '';
    }
}

// ========== NAVEGACIÓN ENTRE PANTALLAS ==========

function cambiarPantalla(pantallaActual, pantallaNueva) {
    document.getElementById(pantallaActual).classList.remove('active');
    document.getElementById(pantallaNueva).classList.add('active');
}

function seleccionarCategoria(categoria) {
    categoriaActual = categoria;
    
    // Actualizar el selector de conversiones
    const select = document.getElementById('conversion');
    select.innerHTML = '<option value="">-- Seleccione una conversión --</option>';
    
    conversiones[categoria].forEach((conv, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = conv.nombre;
        select.appendChild(option);
    });
    
    // Cambiar a pantalla de conversión
    cambiarPantalla('categoryScreen', 'conversionScreen');
}

function volverACategorias() {
    // Limpiar campos
    document.getElementById('valor').value = '';
    document.getElementById('conversion').value = '';
    
    cambiarPantalla('conversionScreen', 'categoryScreen');
}

function volverDesdResultado() {
    // Volver a la pantalla de categorías desde resultado
    // Resetear la categoría actual
    categoriaActual = '';
    
    // Cambiar pantalla directamente sin limpiar campos (no existen en esta pantalla)
    cambiarPantalla('resultScreen', 'categoryScreen');
}

function limpiarCampos() {
    const conversionSelect = document.getElementById('conversion');
    const valorInput = document.getElementById('valor');
    
    if (conversionSelect) {
        conversionSelect.innerHTML = '<option value="">-- Seleccione una conversión --</option>';
    }
    
    if (valorInput) {
        valorInput.value = '';
    }
    
    categoriaActual = '';
}

function cerrarSesion() {
    if (confirm('¿Está seguro que desea cerrar sesión?')) {
        // Volver a pantalla de login
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        document.getElementById('loginScreen').classList.add('active');
        
        // Resetear todos los formularios
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('valor').value = '';
        document.getElementById('conversion').value = '';
        categoriaActual = '';
    }
}

// ========== CONVERSIONES ==========

function realizarConversion() {
    const conversionIndex = document.getElementById('conversion').value;
    const valor = document.getElementById('valor').value;
    
    // Validaciones
    if (conversionIndex === '') {
        alert('⚠️ Por favor, selecciona un tipo de conversión.');
        return;
    }
    
    if (!valor || isNaN(valor)) {
        alert('⚠️ Por favor, ingresa un valor numérico válido.');
        return;
    }
    
    const conversion = conversiones[categoriaActual][conversionIndex];
    const url = `${BASE_URL}/${conversion.endpoint}/${valor}`;
    
    // Realizar petición
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            const resultado = parseFloat(data);
            
            // Actualizar pantalla de resultado
            document.getElementById('resultadoValor').textContent = 
                `${resultado.toFixed(4)} ${conversion.destino}`;
            document.getElementById('resultadoFormula').textContent = 
                `${valor} ${conversion.origen} = ${resultado.toFixed(4)} ${conversion.destino}`;
            
            // Cambiar a pantalla de resultado
            cambiarPantalla('conversionScreen', 'resultScreen');
        })
        .catch(error => {
            let mensaje = '';
            
            if (error.message.includes('Failed to fetch')) {
                mensaje = `❌ ERROR DE CONEXIÓN\n\nNo se puede conectar al servidor.\n\nVerifica que el servidor esté ejecutándose en:\n${BASE_URL}`;
            } else {
                mensaje = `❌ ERROR EN LA CONVERSIÓN\n\n${error.message}\n\nURL: ${url}`;
            }
            
            alert(mensaje);
        });
}

// ========== NAVEGACIÓN ENTRE PANTALLAS ==========

function volverAConvertir() {
    // Volver a la pantalla de selección
    document.getElementById('resultScreen').classList.remove('active');
    document.getElementById('selectionScreen').classList.add('active');
    
    // Limpiar campo de valor
    document.getElementById('valor').value = '';
}

function cerrarSesion() {
    if (confirm('¿Está seguro que desea cerrar sesión?')) {
        // Volver a pantalla de login
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });
        document.getElementById('loginScreen').classList.add('active');
        
        // Resetear todos los formularios
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        limpiarCampos();
    }
}

function limpiarCampos() {
    document.getElementById('categoria').value = '';
    document.getElementById('conversion').innerHTML = '<option value="">-- Primero seleccione una categoría --</option>';
    document.getElementById('valor').value = '';
}

// ========== UTILIDADES ==========

function mostrarMensaje(titulo, mensaje, tipo) {
    alert(`${titulo}\n\n${mensaje}`);
}

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    // Enter en login
    document.getElementById('username').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            document.getElementById('password').focus();
        }
    });
    
    document.getElementById('password').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            validarLogin();
        }
    });
    
    // Enter en valor
    document.getElementById('valor').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            realizarConversion();
        }
    });
});
