# Cliente de Escritorio SOAP con Tkinter

Cliente de escritorio (GUI) con interfaz gráfica para consumir el servicio SOAP de .NET.

## Características

- 🖥️ **Interfaz Gráfica Nativa**: Aplicación de escritorio con Tkinter
- 🔐 **Sistema de Login**: Autenticación con usuario y contraseña
- 🎨 **Diseño Moderno**: Interfaz limpia con colores corporativos
- 🔷 **Arte ASCII de Sulivan**: Personaje de Monsters University en la pantalla de login (sin código async)
- 🔄 **Conversiones en Tiempo Real**: 
  - Temperatura (Celsius, Fahrenheit, Kelvin)
  - Masa (Kilogramos, Libras, Onzas)
  - Longitud (Metros, Pies, Kilómetros, Millas)
- 📊 **Panel de Resultados**: Visualización clara de las conversiones
- 🛡️ **Sesión Segura**: Control de acceso con validación de credenciales

## Requisitos Previos

- Python 3.7 o superior (con Tkinter incluido)
- pip (gestor de paquetes de Python)
- Servidor .NET SOAP ejecutándose en `http://localhost:63393/Service.svc`

## Instalación

1. **Instalar las dependencias:**

```powershell
cd 02.CLISEC
pip install -r requirements.txt
```

**Nota:** Tkinter viene incluido con Python en Windows. No requiere instalación adicional.

## Configuración

1. Asegúrate de que el servidor .NET esté ejecutándose en `http://localhost:63393/Service.svc`
2. Verifica que la URL del WSDL esté accesible: `http://localhost:63393/Service.svc?wsdl`

## Uso

### Ejecutar la aplicación de escritorio:

```powershell
python cliente_escritorio.py
```

### Credenciales de Login:
- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## Estructura del Proyecto

```
02.CLISEC/
├── cliente_escritorio.py   # Aplicación Tkinter principal
├── requirements.txt         # Dependencias de Python
└── README.md               # Este archivo
```

## Funcionalidades

### 1. Pantalla de Login
- Formulario de autenticación elegante
- Arte ASCII de Sulivan de Monsters University (sin animación)
- Validación de credenciales
- Mensajes de error/éxito con MessageBox
- Diseño centrado y responsive

### 2. Dashboard de Conversiones
- **Header:** Título de la aplicación con botón de logout
- **Tres Secciones de Conversión:**
  - 🌡️ **Temperatura**: Celsius/Fahrenheit/Kelvin
  - ⚖️ **Masa**: Kilogramos/Libras/Onzas
  - 📏 **Longitud**: Metros/Pies/Kilómetros/Millas
- **Panel de Resultados:** Muestra los resultados de las conversiones
- **Radio Buttons:** Selección intuitiva del tipo de conversión
- **Entrada de Datos:** Campo numérico para ingresar valores
- **Botones de Conversión:** Un botón por cada categoría

### 3. Características de la Interfaz
- Diseño en grid con 4 secciones principales
- Colores corporativos (morado/azul)
- Efectos hover en botones
- Tecla Enter para confirmar acciones
- Ventana centrada automáticamente
- Tamaño fijo 900x700 píxeles

## Tecnologías Utilizadas

- **GUI Framework:** Tkinter (incluido con Python)
- **SOAP Client:** Zeep 4.3.2
- **HTTP Requests:** Requests 2.32.5
- **XML Parsing:** lxml 6.0.2

## Conversiones Disponibles

### Temperatura
- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Celsius → Kelvin

### Masa
- Kilogramos → Libras
- Libras → Kilogramos
- Kilogramos → Onzas

### Longitud
- Metros → Pies
- Pies → Metros
- Kilómetros → Millas

## Troubleshooting

### Error de conexión SOAP
```
Error: No se pudo conectar con el servicio SOAP
```
**Solución:** Verifica que el servidor .NET esté ejecutándose en el puerto 63393

### Error de Tkinter
```
ModuleNotFoundError: No module named 'tkinter'
```
**Solución:** En Windows, Tkinter viene incluido con Python. Reinstala Python si es necesario.

En Linux:
```bash
sudo apt-get install python3-tk
```

### Ventana no se muestra correctamente
**Solución:** Actualiza los drivers de video o ejecuta en modo compatibilidad

## Atajos de Teclado

- **Enter** en campo de contraseña → Iniciar sesión
- **Enter** en campo de valor → Realizar conversión
- **Alt+F4** → Cerrar aplicación

## Personalización

### Cambiar credenciales de login
Edita en `cliente_escritorio.py`:
```python
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"
```

### Cambiar colores
Edita en el método `__init__`:
```python
self.color_primary = "#667eea"
self.color_secondary = "#764ba2"
```

### Cambiar URL del servicio SOAP
Edita en `cliente_escritorio.py`:
```python
WSDL_URL = "http://localhost:63393/Service.svc?wsdl"
```

### Cambiar tamaño de ventana
Edita en el método `__init__`:
```python
self.root.geometry("900x700")  # Cambia a las dimensiones deseadas
```

## Ventajas del Cliente de Escritorio

✅ **No requiere navegador** - Aplicación nativa de Windows  
✅ **Rápido y ligero** - Sin overhead de servidor web  
✅ **Interfaz familiar** - Diseño tipo aplicación Windows  
✅ **Offline-first** - Solo necesita conexión al servicio SOAP  
✅ **Sin dependencias web** - No requiere Flask ni servidor HTTP  

## Comparación con otros clientes

| Característica | Consola | Web | Escritorio |
|---------------|---------|-----|------------|
| Interfaz Gráfica | ❌ | ✅ | ✅ |
| Requiere Navegador | ❌ | ✅ | ❌ |
| Portable | ✅ | ❌ | ✅ |
| Fácil de usar | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## Capturas de Pantalla

### Pantalla de Login
- Ventana centrada 500x600 píxeles
- Arte ASCII de Sulivan
- Campos de usuario y contraseña
- Botón de inicio de sesión con efecto hover
- Panel informativo con credenciales

### Dashboard
- Header con título y botón de logout
- Grid 2x2 con 4 secciones
- 3 secciones de conversión (Temperatura, Masa, Longitud)
- 1 panel de resultados
- Radio buttons para selección
- Botones de conversión estilizados

## Notas Importantes

⚠️ **Tkinter** es la biblioteca estándar de Python para interfaces gráficas. Viene incluida con Python en Windows, no requiere instalación adicional.

⚠️ **Sin código async**: La imagen de Sulivan se muestra directamente sin animación ni código asíncrono.

⚠️ **Threading**: La aplicación usa el hilo principal de Tkinter. No se requieren hilos adicionales para la imagen.

## Licencia

Proyecto educativo - 2025

## Autor

Sistema - Cliente SOAP con Tkinter
