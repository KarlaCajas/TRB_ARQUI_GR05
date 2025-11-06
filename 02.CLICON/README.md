# 🎓 Cliente de Consola RESTful - Monsters University

Cliente de consola en Python para consumir servicios RESTful de conversión de unidades.

## 📋 Características

- ✅ **Login seguro** con usuario y contraseña (oculta con asteriscos)
- 🎨 **Imagen ASCII de Sullivan** de Monsters University (carga asíncrona)
- 🔧 **11 conversiones diferentes** organizadas por categorías:
  - 📏 Longitud (pulgadas, cm, km, metros, mm)
  - 🌡️ Temperatura (Celsius, Fahrenheit, Kelvin)
  - ⚖️ Masa (kg, gramos, miligramos, toneladas)
- 🎨 **Interfaz colorida** en consola
- ⚡ **Validación de errores** y manejo de excepciones

## 🔐 Credenciales

- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## 🚀 Instalación

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Instalar las dependencias:**
```powershell
pip install -r requirements.txt
```

## ▶️ Ejecución

1. **Asegúrate de que el servidor RESTful esté ejecutándose:**
   - El servidor debe estar corriendo en: `http://localhost:8080/WS_ConersionUnidades_RESTFULL`

2. **Ejecuta el cliente:**
```powershell
python cliente_restful.py
```

3. **Ingresa las credenciales:**
   - Usuario: `MONSTER`
   - Contraseña: `Monster9`

4. **Selecciona una opción del menú** y realiza conversiones.

## 📖 Uso

### Pantalla de Login
```
    🔐 SISTEMA DE CONVERSIÓN DE UNIDADES - LOGIN 🔐
    
    [Imagen ASCII de Sullivan]
    
    👤 Usuario: MONSTER
    🔑 Contraseña: *********
    
    ✅ ¡Login exitoso! Bienvenido, MONSTER!
```

### Menú Principal
```
📏 CONVERSIONES DE LONGITUD:
  1. Pulgadas a Centímetros
  2. Centímetros a Pulgadas
  3. Kilómetros a Metros
  4. Metros a Centímetros
  5. Centímetros a Milímetros

🌡️  CONVERSIONES DE TEMPERATURA:
  6. Celsius a Fahrenheit
  7. Fahrenheit a Celsius
  8. Celsius a Kelvin

⚖️  CONVERSIONES DE MASA:
  9. Kilogramos a Gramos
  10. Gramos a Miligramos
  11. Toneladas a Kilogramos

  0. 🚪 Salir
```

## 🔧 Tecnologías Utilizadas

- **Python 3**
- **requests** - Para consumir servicios RESTful
- **asyncio** - Para carga asíncrona de la imagen ASCII
- **getpass** - Para ocultar la contraseña con asteriscos

## 📝 Notas

- La contraseña se valida con asteriscos para mayor seguridad visual
- La imagen de Sullivan se carga de forma asíncrona
- El sistema tiene 3 intentos de login antes de bloquear el acceso
- Todas las conversiones se realizan mediante peticiones GET al servidor RESTful
- El cliente maneja errores de conexión, timeout y respuestas inválidas

## 👥 Autor

**Equipo MONSTER** - Monsters University 🎓

## 📄 Licencia

Este proyecto es parte del curso de Arquitectura de Software.
