# Cliente de Escritorio SOAP - Conversor de Unidades
## Grupo GR05

### 📋 Descripción
Cliente de escritorio desarrollado en Python con interfaz gráfica (Tkinter) que consume el servicio web SOAP para conversión de unidades.

### 🔧 Requisitos
- Python 3.7 o superior
- Servicio SOAP ejecutándose en: `http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl`

### 📦 Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

### 🚀 Ejecución

1. **Asegúrate de que el servicio SOAP esté ejecutándose**

2. **Ejecutar el cliente:**
```bash
python cliente_soap.py
```

### 🔐 Credenciales de Acceso
- **Usuario:** MONSTER
- **Contraseña:** Monster9

### ✨ Funcionalidades

#### Conversiones de Temperatura:
- Celsius → Fahrenheit
- Fahrenheit → Celsius
- Celsius → Kelvin

#### Conversiones de Masa:
- Toneladas → Kilogramos
- Kilogramos → Gramos
- Gramos → Miligramos

#### Conversiones de Longitud:
- Kilómetros → Metros
- Metros → Centímetros
- Centímetros → Milímetros

### 📱 Uso de la Aplicación

1. **Login:**
   - Ingresa las credenciales (Usuario: MONSTER, Contraseña: Monster9)
   - Presiona "INGRESAR" o tecla Enter

2. **Ventana Principal:**
   - Selecciona la pestaña de la categoría deseada (Temperatura, Masa, Longitud)
   - Ingresa el valor a convertir
   - Presiona "Convertir" o tecla Enter
   - El resultado se mostrará automáticamente

### 🏗️ Arquitectura

```
cliente_soap.py
├── SOAPClient          # Clase para comunicación con servicio SOAP
├── LoginWindow         # Ventana de autenticación
└── MainWindow          # Ventana principal con conversiones
```

### 🔌 Conexión con el Servicio

El cliente se conecta al servicio SOAP utilizando la biblioteca `zeep`, que maneja:
- Parsing del WSDL
- Generación automática de métodos
- Serialización/Deserialización de mensajes SOAP
- Manejo de excepciones

### 📝 Notas Técnicas

- **Librería SOAP:** zeep 4.2.1
- **GUI Framework:** tkinter (incluido en Python)
- **Validación:** Credenciales validadas localmente y en el servicio
- **Manejo de Errores:** Captura y muestra errores de conexión y conversión

### 🐛 Solución de Problemas

**Error de conexión al servicio:**
- Verifica que el servidor SOAP esté ejecutándose
- Confirma que la URL sea correcta: `http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl`

**Error al instalar zeep:**
```bash
pip install --upgrade pip
pip install zeep
```

**Tkinter no disponible (Linux):**
```bash
sudo apt-get install python3-tk
```

### 👥 Grupo
GR05 - Arquitectura de Software

### 📄 Licencia
Proyecto académico - Uso educativo
