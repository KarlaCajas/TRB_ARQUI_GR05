# Cliente Web SOAP con Flask

Cliente web interactivo con interfaz gráfica para consumir el servicio SOAP de .NET.

## Características

- 🔐 **Sistema de Login**: Autenticación con usuario y contraseña
- 🎨 **Interfaz Moderna**: Diseño responsive y atractivo con gradientes
- 🔷 **Arte ASCII de Sulivan**: Personaje de Monsters University en la pantalla de login
- 🔄 **Conversiones en Tiempo Real**: 
  - Temperatura (Celsius, Fahrenheit, Kelvin)
  - Masa (Kilogramos, Libras, Onzas)
  - Longitud (Metros, Pies, Kilómetros, Millas)
- 📱 **Responsive Design**: Funciona en desktop, tablet y móvil
- 🛡️ **Sesiones Seguras**: Control de acceso con Flask sessions

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Servidor .NET SOAP ejecutándose en `http://localhost:63393/Service.svc`

## Instalación

1. **Instalar las dependencias:**

```powershell
cd 02.CLIWEB
pip install -r requirements.txt
```

## Configuración

1. Asegúrate de que el servidor .NET esté ejecutándose en `http://localhost:63393/Service.svc`
2. Verifica que la URL del WSDL esté accesible: `http://localhost:63393/Service.svc?wsdl`

## Uso

### Ejecutar la aplicación web:

```powershell
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

### Credenciales de Login:
- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## Estructura del Proyecto

```
02.CLIWEB/
├── app.py                      # Aplicación Flask principal
├── requirements.txt            # Dependencias de Python
├── README.md                   # Este archivo
└── templates/                  # Plantillas HTML
    ├── base.html              # Plantilla base con estilos
    ├── login.html             # Página de login
    └── dashboard.html         # Panel de conversiones
```

## Funcionalidades

### 1. Pantalla de Login
- Formulario de autenticación
- Arte ASCII de Sulivan de Monsters University
- Validación de credenciales
- Mensajes de error/éxito

### 2. Dashboard de Conversiones
- **Conversiones de Temperatura:**
  - Celsius a Fahrenheit
  - Fahrenheit a Celsius
  - Celsius a Kelvin

- **Conversiones de Masa:**
  - Kilogramos a Libras
  - Libras a Kilogramos
  - Kilogramos a Onzas

- **Conversiones de Longitud:**
  - Metros a Pies
  - Pies a Metros
  - Kilómetros a Millas

### 3. Características de Seguridad
- Sistema de sesiones con Flask
- Decorador `@login_required` para proteger rutas
- Logout seguro

## Capturas de Funcionalidad

### Pantalla de Login
- Formulario elegante con gradiente morado
- Arte ASCII de Sulivan
- Campos de usuario y contraseña
- Credenciales visibles para prueba

### Dashboard
- Tres tarjetas con categorías de conversión
- Opciones de radio para seleccionar tipo de conversión
- Campo numérico para ingresar valor
- Botón de conversión destacado
- Resultados mostrados con alertas de éxito
- Header con nombre de usuario y botón de logout

## Tecnologías Utilizadas

- **Backend:** Flask 3.0.0
- **SOAP Client:** Zeep 4.3.2
- **Frontend:** HTML5, CSS3 (Vanilla)
- **Diseño:** CSS Grid, Flexbox, Gradientes
- **Sesiones:** Flask Sessions

## API Endpoints

- `GET /` - Redirección al login o dashboard
- `GET /login` - Muestra formulario de login
- `POST /login` - Procesa autenticación
- `GET /logout` - Cierra sesión
- `GET /dashboard` - Panel principal (requiere login)
- `POST /convertir` - Realiza conversión SOAP (requiere login)

## Troubleshooting

### Error de conexión SOAP
```
✗ No se pudo conectar con el servicio SOAP
```
**Solución:** Verifica que el servidor .NET esté ejecutándose en el puerto 63393

### Error de módulos no encontrados
```
ModuleNotFoundError: No module named 'flask'
```
**Solución:** Instala las dependencias con `pip install -r requirements.txt`

### Error de puerto en uso
```
OSError: [Errno 48] Address already in use
```
**Solución:** Cambia el puerto en `app.py` o detén la aplicación que usa el puerto 5000

## Personalización

### Cambiar credenciales de login
Edita en `app.py`:
```python
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"
```

### Cambiar puerto del servidor
Edita en `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Cambia 5000 por el puerto deseado
```

### Cambiar URL del servicio SOAP
Edita en `app.py`:
```python
WSDL_URL = "http://localhost:63393/Service.svc?wsdl"
```

## Modo Producción

Para ejecutar en producción, usa un servidor WSGI como Gunicorn:

```powershell
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Notas de Seguridad

⚠️ **IMPORTANTE para Producción:**
- Cambia `app.secret_key` por una clave segura aleatoria
- No uses `debug=True` en producción
- Implementa HTTPS/SSL
- Usa variables de entorno para credenciales
- Implementa limitación de intentos de login
- Agrega CSRF protection

## Licencia

Proyecto educativo - 2025
