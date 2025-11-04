# 🐍 Cliente de Consola Python - Conversor de Unidades

Cliente de consola desarrollado en Python para realizar conversiones de unidades (Masa, Longitud y Temperatura) conectado a la API RESTful desarrollada en .NET.

## 📋 Requisitos Previos

- Python 3.7 o superior
- Servidor .NET ejecutándose en `http://localhost:5014` (opcional - el cliente puede funcionar sin conexión)
- Librería `requests` (se instala automáticamente con requirements.txt)

## 🚀 Instalación

1. **Navegar a la carpeta del proyecto:**
   ```powershell
   cd "c:\Arquitectura G5\TI1.4 RESTFUL_DOTNET_SINBDD_GR05\02. CLICON"
   ```

2. **Instalar las dependencias:**
   ```powershell
   pip install -r requirements.txt
   ```

## 🔧 Configuración

### Credenciales de Acceso (Hardcoded)
El cliente tiene las siguientes credenciales configuradas:
- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

### URL del Servidor
- **Base URL:** `http://localhost:5014`
- **Endpoint:** `/api/ConversionUnidades_Controlador`

## ▶️ Ejecución

Para ejecutar el cliente de consola:

```powershell
python cliente_api.py
```

## 📖 Funcionalidades

El cliente ofrece tres categorías de conversiones:

### 1. ⚖️ Conversiones de MASA
- Kilogramos → Gramos
- Gramos → Miligramos
- Toneladas → Kilogramos

### 2. 📏 Conversiones de LONGITUD
- Kilómetros → Metros
- Metros → Centímetros
- Centímetros → Milímetros

### 3. 🌡️ Conversiones de TEMPERATURA
- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Celsius → Kelvin

### 4. � Verificación de Conexión
Verifica si el servidor .NET está disponible y responde correctamente.

## 🎯 Ejemplo de Uso

```
==================================================
🚀 CONVERSOR DE UNIDADES
==================================================
Cliente para API RESTful .NET
Servidor: http://localhost:5014
==================================================

🔌 Verificando conexión con el servidor...
✅ Servidor conectado correctamente en http://localhost:5014

==================================================
🔐 Iniciando sesión como: MONSTER
==================================================
✅ Login exitoso!
Usuario autenticado: MONSTER

==================================================
🌐 CONVERSOR DE UNIDADES
==================================================
👤 Usuario: MONSTER
� Servidor: http://localhost:5014
==================================================
1. ⚖️  Conversiones de MASA
2. � Conversiones de LONGITUD
3. 🌡️  Conversiones de TEMPERATURA
4. 🔌 Verificar conexión con servidor
5. 🚪 Cerrar sesión y salir
==================================================

👉 Seleccione una opción:
```

## 🏗️ Estructura del Código

### Clase `ClienteConversionUnidades`

La clase principal que encapsula toda la lógica:

- **`__init__(base_url)`**: Constructor con conversiones predefinidas
- **`verificar_conexion_servidor()`**: Verifica disponibilidad del servidor
- **`login(usuario, contrasena)`**: Maneja la autenticación
- **`verificar_autenticacion()`**: Verifica si el usuario está autenticado
- **`convertir_temperatura(valor, tipo)`**: Realiza conversiones de temperatura
- **`realizar_conversion(valor, categoria, opcion)`**: Ejecuta conversión y envía al servidor

### Funciones de Menú

- **`menu_conversiones_masa(cliente)`**: Menú interactivo de conversiones de masa
- **`menu_conversiones_longitud(cliente)`**: Menú interactivo de conversiones de longitud
- **`menu_conversiones_temperatura(cliente)`**: Menú interactivo de conversiones de temperatura
- **`menu_principal(cliente)`**: Menú principal de la aplicación
- **`main()`**: Función principal que inicia el programa

## 🔐 Seguridad

> **Nota:** Las credenciales están hardcoded en el código para propósitos de desarrollo y testing. En un entorno de producción, se deben utilizar variables de entorno o un sistema de configuración seguro.

## 🛠️ Personalización

### Cambiar la URL del Servidor

Editar la línea en `cliente_api.py`:
```python
cliente = ClienteConversionUnidades("http://localhost:PUERTO")
```

### Agregar Nuevas Conversiones

Puedes agregar conversiones editando los diccionarios en el constructor `__init__`:

```python
self.conversiones_masa = {
    "6": {"nombre": "Nuevaconversión", "origen": "unidad1", "destino": "unidad2", "factor": 1.234}
}
```

## ❗ Manejo de Errores

El cliente maneja los siguientes tipos de errores:

- ✅ **Conexión rechazada**: Cuando el servidor no está ejecutándose (permite continuar offline)
- ✅ **Errores HTTP**: El cliente informa pero continúa funcionando
- ✅ **Errores de entrada**: Validación de datos numéricos
- ✅ **Autenticación**: Verifica que el usuario esté autenticado
- ✅ **Timeout**: Maneja tiempos de espera en conexión

## 📝 Notas Adicionales

1. **El cliente funciona incluso sin servidor**: Las conversiones se realizan localmente, el servidor solo registra las operaciones.

2. **Verificación de conexión**: Al iniciar, verifica automáticamente la conexión con el servidor.

3. **Conversiones de temperatura**: Utilizan fórmulas específicas en lugar de factores de multiplicación.

4. **Interrupción del programa**: Puedes usar `Ctrl+C` para salir del programa en cualquier momento.

## 🐛 Troubleshooting

### Error: "No se pudo conectar al servidor"
- El cliente funcionará de todos modos para realizar conversiones
- Si quieres registrar en el servidor, verifica que esté ejecutándose
- Confirma que el puerto sea el correcto (5014)
- Usa la opción 4 del menú para verificar conexión

### Error: "Módulo 'requests' no encontrado"
- Ejecuta: `pip install requests`
- O instala desde requirements.txt: `pip install -r requirements.txt`

### Servidor no registra conversiones
- Verifica que el endpoint esté correctamente configurado en .NET
- Revisa que el controlador acepte POST con los campos correctos
- Asegúrate de que no haya CORS bloqueando las peticiones

## 🎓 Conversiones Disponibles

### Masa
| Conversión | Factor |
|------------|--------|
| kg → g | ×1000 |
| g → mg | ×1000 |
| t → kg | ×1000 |

### Longitud
| Conversión | Factor |
|------------|--------|
| km → m | ×1000 |
| m → cm | ×100 |
| cm → mm | ×10 |

### Temperatura
| Conversión | Fórmula |
|------------|---------|
| °C → °F | (°C × 9/5) + 32 |
| °F → °C | (°F - 32) × 5/9 |
| °C → K | °C + 273.15 |

## 📄 Licencia

Este proyecto es parte del curso TI1.4 - Arquitectura G5.

## 👥 Autor

Generado para el proyecto RESTFUL_DOTNET_SINBDD_GR05
