# Cliente Web Python - Sistema de Conversiones MONSTER

Cliente web desarrollado en Python con Flask para interactuar con la API RESTful .NET de conversión de unidades.

## 🚀 Características

- ✅ **Login seguro** con credenciales:
  - Usuario: `MONSTER`
  - Contraseña: `Monster9`

- 📊 **Menú de Conversiones**:
  - **Masa**: Kilogramos, gramos, libras, onzas
  - **Longitud**: Metros, kilómetros, pies, millas, centímetros, pulgadas
  - **Temperatura**: Celsius, Fahrenheit, Kelvin

- 🔗 **Conexión al Servidor .NET**:
  - URL del servidor: `https://localhost:7102`
  - Verificación automática del estado del servidor
  - Indicador visual de conexión en tiempo real

- 🎨 **Interfaz Moderna**:
  - Diseño responsivo con Bootstrap 5
  - Fondo personalizado con imagen `fondo6.jpg`
  - Animaciones suaves y efectos visuales

## 📋 Requisitos Previos

- Python 3.8 o superior
- Servidor .NET RESTful activo en `https://localhost:7102`

## 🔧 Instalación

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

1. **Asegúrate de que el servidor .NET esté ejecutándose**:
   - URL: `https://localhost:7102/api/ConversionUnidades_Controlador`

2. **Ejecuta la aplicación Flask**:
```bash
python app.py
```

3. **Abre tu navegador** en:
   - `http://localhost:3000`

## 🔐 Credenciales de Acceso

- **Usuario**: `MONSTER`
- **Contraseña**: `Monster9`

## 📁 Estructura del Proyecto

```
02. CLIEWEB/
│
├── app.py                          # Aplicación principal Flask
├── requirements.txt                # Dependencias Python
├── README.md                       # Este archivo
│
├── templates/                      # Plantillas HTML
│   ├── base.html                  # Plantilla base
│   ├── login.html                 # Página de login
│   ├── menu.html                  # Menú principal
│   ├── conversion_masa.html       # Conversión de masa
│   ├── conversion_longitud.html   # Conversión de longitud
│   └── conversion_temperatura.html # Conversión de temperatura
│
└── static/                         # Archivos estáticos
    └── imagenes/                   # Imágenes
        ├── fondo6.jpg             # Fondo principal
        └── logo_login.png         # Logo
```

## 🌐 Endpoints de la API

El cliente se conecta al siguiente endpoint del servidor .NET:

- **POST** `https://localhost:7102/api/ConversionUnidades_Controlador`

### Formato de petición:
```json
{
    "tipo": "masa|longitud|temperatura",
    "valor": 100,
    "deUnidad": "kilogramo",
    "aUnidad": "libra"
}
```

## 🎯 Uso de la Aplicación

1. **Login**: Ingresa con las credenciales proporcionadas
2. **Seleccionar conversión**: Elige entre Masa, Longitud o Temperatura
3. **Ingresar datos**: 
   - Valor numérico a convertir
   - Unidad de origen
   - Unidad de destino
4. **Convertir**: Presiona el botón "Convertir"
5. **Ver resultado**: El resultado se mostrará en pantalla

## 🔍 Verificación de Conexión

El menú principal incluye un indicador de estado del servidor que:
- ✅ Muestra "Conectado" si el servidor está activo
- ❌ Muestra "Desconectado" si hay problemas de conexión
- 🔄 Se actualiza automáticamente cada 10 segundos

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Iconos**: Font Awesome 6
- **HTTP Client**: Requests (Python)

## 📝 Notas Importantes

- El cliente está configurado para ignorar advertencias SSL (`verify=False`) ya que el servidor .NET usa HTTPS con certificado autofirmado
- El puerto por defecto del cliente es `3000`
- El servidor .NET debe estar ejecutándose antes de iniciar el cliente

## 🐛 Solución de Problemas

### Error de conexión al servidor
- Verifica que el servidor .NET esté activo
- Comprueba la URL: `https://localhost:7102`
- Asegúrate de que no haya firewalls bloqueando la conexión

### Error al instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 👨‍💻 Autor

Sistema desarrollado para el proyecto de Arquitectura G5

---
**¡MONSTER te da la bienvenida! 🐉**
