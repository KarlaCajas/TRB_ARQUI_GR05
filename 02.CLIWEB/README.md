# 🎓 Cliente Web (HTML/CSS/JS) RESTful - Monsters University (CLIWEB)

Cliente web con interfaz gráfica moderna para consumir servicios RESTful de conversión de unidades.

## 📋 Características

- 🌐 **Aplicación Web Completa** - HTML5, CSS3 y JavaScript vanilla
- ✅ **Login seguro** - Usuario y contraseña con validación
- 🎨 **Diseño moderno y responsive** - Funciona en desktop, tablet y móvil
- 💫 **Animaciones suaves** - Transiciones y efectos visuales
- 🔧 **11 conversiones diferentes** organizadas por categorías:
  - 📏 Longitud (pulgadas, cm, km, metros, mm)
  - 🌡️ Temperatura (Celsius, Fahrenheit, Kelvin)
  - ⚖️ Masa (kg, gramos, miligramos, toneladas)
- 📊 **ComboBox dinámicos** - Se actualizan según la categoría
- ⚡ **Validación en tiempo real** - Mensajes de error claros
- 📈 **Resultados detallados** - Información completa de la conversión
- 🎯 **Sin dependencias** - No requiere frameworks ni librerías externas

## 🔐 Credenciales

- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## 🚀 Instalación y Ejecución

### Método 1: Abrir directamente
1. Abre el archivo `index.html` en tu navegador web favorito
2. O haz doble clic en `abrir.bat` (Windows)

### Método 2: Servidor local (recomendado)
Si tienes problemas con CORS, usa un servidor local:

**Con Python:**
```powershell
# Python 3
python -m http.server 8000

# Luego abre: http://localhost:8000
```

**Con Node.js (http-server):**
```powershell
npx http-server -p 8000
```

**Con PHP:**
```powershell
php -S localhost:8000
```

## 📁 Estructura de Archivos

```
02.CLIWEB/
├── index.html      # Estructura HTML de la aplicación
├── styles.css      # Estilos y diseño
├── script.js       # Lógica y funcionalidad
├── abrir.bat       # Script para abrir en Windows
└── README.md       # Este archivo
```

## 📖 Uso

### 1. Pantalla de Login
- Ventana moderna con fondo degradado
- Campos para usuario y contraseña
- Contador de intentos (3 intentos disponibles)
- Botones "Ingresar" y "Cancelar"

### 2. Pantalla Principal
La aplicación web incluye:

**Header azul:**
- Logo de Monsters University
- Título del sistema

**Sección de Conversión:**
- **ComboBox de categoría**: Selecciona entre Longitud, Temperatura o Masa
- **ComboBox de conversión**: Se actualiza automáticamente según la categoría
- **Campo de valor**: Ingresa el número a convertir
- **Botón Convertir**: Realiza la conversión

**Área de Resultados:**
- Muestra información detallada de la conversión
- Código de colores (verde para éxito, rojo para error)
- URL del servidor y estado de conexión

**Footer:**
- Botón "Salir" para cerrar sesión
- Información de copyright

## 🎨 Características de Diseño

- **Colores profesionales** con degradados
- **Responsive Design** - Se adapta a cualquier tamaño de pantalla
- **Animaciones CSS** - Transiciones suaves y efectos hover
- **Sombras y profundidad** - Diseño Material Design
- **Tipografía moderna** - Segoe UI y Consolas

## 🔧 Tecnologías Utilizadas

- **HTML5** - Estructura semántica
- **CSS3** - Estilos modernos con Flexbox y animaciones
- **JavaScript (ES6+)** - Lógica y peticiones Fetch API
- **RESTful API** - Consumo de servicios HTTP

## 📝 Configuración

La URL del servidor se encuentra en `script.js`:

```javascript
const BASE_URL = "http://localhost:8080/WS_ConersionUnidades_RESTFULL/webresources";
```

Si tu servidor está en otra dirección, modifica esta constante.

## 🌐 Compatibilidad

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+
- ✅ Opera 76+

## 📱 Responsive

La aplicación es totalmente responsive:
- **Desktop**: Experiencia completa con diseño amplio
- **Tablet**: Adaptación de columnas y espaciado
- **Móvil**: Diseño vertical optimizado para pantallas pequeñas

## 🔒 Seguridad

- Validación de entrada en frontend
- Manejo de errores de red
- Timeout en peticiones
- Sanitización de datos

## 🐛 Solución de Problemas

### No se puede conectar al servidor
- Verifica que el servidor RESTful esté ejecutándose
- Asegúrate de que la URL en `script.js` sea correcta
- Revisa que no haya problemas de CORS

### Las conversiones no funcionan
- Abre la consola del navegador (F12) para ver errores
- Verifica la respuesta del servidor
- Comprueba que los endpoints estén disponibles

## 👥 Autor

**Equipo MONSTER** - Monsters University 🎓

## 📄 Licencia

Este proyecto es parte del curso de Arquitectura de Software.

---

🎓 **¡Bienvenido a Monsters University!** 🎓
