# Cliente de Escritorio - Calculadora de Conversión de Unidades

Calculadora de escritorio desarrollada en Python con interfaz gráfica (Tkinter) para realizar conversiones de unidades de temperatura, masa y longitud.

## 🚀 Características

- ✅ **Sistema de Login** con credenciales hardcodeadas
- 🔐 Usuario: `MONSTER` / Contraseña: `Monster9`
- 🌡️ **Conversiones de Temperatura** (Celsius, Fahrenheit, Kelvin)
- ⚖️ **Conversiones de Masa** (kg, gramos, miligramos, toneladas)
- 📏 **Conversiones de Longitud** (km, metros, centímetros, milímetros)
- 💻 Interfaz gráfica intuitiva con Tkinter
- 🎨 Diseño moderno y profesional
- 📊 Resultados con unidades incluidas

## 📋 Requisitos Previos

- Python 3.7 o superior
- Tkinter (incluido por defecto en Python)

## 🔧 Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**

```powershell
pip install -r requirements.txt
```

O instalar manualmente:

```powershell
pip install requests
```

## ▶️ Ejecución

### Método 1: Ejecutar el archivo principal

```powershell
python app.py
```

### Método 2: Usar el script automático

```powershell
ejecutar.bat
```

O simplemente haz doble clic en `ejecutar.bat`

## 🗂️ Estructura del Proyecto

```
02. CLIESC/
├── app.py                 # Aplicación principal
├── login_window.py        # Ventana de autenticación
├── main_window.py         # Calculadora de conversiones
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## 📖 Descripción de Archivos

### `app.py`
Archivo principal que integra el flujo completo de la aplicación:
1. Muestra la ventana de login
2. Si el login es exitoso, abre la calculadora de conversiones
3. Cierra la aplicación correctamente

### `login_window.py`
Ventana de autenticación con:
- Campos para usuario y contraseña
- Validación de credenciales hardcodeadas
- Interfaz moderna y centrada

**Credenciales válidas:**
- Usuario: `MONSTER`
- Contraseña: `Monster9`

### `main_window.py`
Calculadora de conversiones con:
- Selección de categoría (Temperatura, Masa, Longitud)
- Selección de tipo de conversión específica
- Campo de entrada para el valor
- Botón de conversión
- Visualización del resultado con unidades

## 🎯 Uso de la Aplicación

### 1. Login
1. Ejecutar `python app.py`
2. Ingresar usuario: **MONSTER**
3. Ingresar contraseña: **Monster9**
4. Clic en "Iniciar Sesión"

### 2. Calculadora de Conversiones

#### Realizar una conversión:
1. Seleccionar una **categoría** (Temperatura, Masa o Longitud)
2. Elegir el **tipo de conversión** específica
3. Ingresar el **valor** a convertir
4. Clic en "� CONVERTIR" o presionar Enter
5. Ver el **resultado** con sus unidades

#### Ejemplo:
```
Categoría: Temperatura
Conversión: Celsius a Fahrenheit
Valor: 25
Resultado: 25 °C = 77.00 °F
```

#### Limpiar campos:
- Clic en "🗑️ Limpiar"

## 🔄 Conversiones Disponibles

### 🌡️ Temperatura
| Conversión | Fórmula | Ejemplo |
|------------|---------|---------|
| Celsius → Fahrenheit | F = (C × 9/5) + 32 | 0°C = 32°F |
| Fahrenheit → Celsius | C = (F - 32) × 5/9 | 32°F = 0°C |
| Celsius → Kelvin | K = C + 273.15 | 0°C = 273.15K |

### ⚖️ Masa
| Conversión | Factor | Ejemplo |
|------------|--------|---------|
| Kilogramos → Gramos | × 1000 | 1 kg = 1000 g |
| Gramos → Miligramos | × 1000 | 1 g = 1000 mg |
| Toneladas → Kilogramos | × 1000 | 1 t = 1000 kg |

### 📏 Longitud
| Conversión | Factor | Ejemplo |
|------------|--------|---------|
| Kilómetros → Metros | × 1000 | 1 km = 1000 m |
| Metros → Centímetros | × 100 | 1 m = 100 cm |
| Centímetros → Milímetros | × 10 | 1 cm = 10 mm |

## ⚠️ Solución de Problemas

### Error "No module named 'requests'"
**Solución:**
```powershell
pip install requests
```

### Error "No module named 'tkinter'"
**Solución:** Tkinter viene incluido con Python. Si falta:
- En Windows: Reinstalar Python asegurándose de marcar "tcl/tk and IDLE"
- En Linux: `sudo apt-get install python3-tk`
- En Mac: Viene incluido por defecto

### La ventana no se muestra
**Solución:**
- Verifica que Python esté correctamente instalado
- Asegúrate de estar ejecutando Python 3.7 o superior
- Intenta ejecutar `python main_window.py` directamente

## 💡 Características Técnicas

- **Lenguaje:** Python 3.7+
- **GUI:** Tkinter
- **Arquitectura:** Aplicación standalone (sin servidor)
- **Cálculos:** Locales (no requiere conexión)

## 👨‍💻 Autor

Calculadora de conversiones desarrollada para facilitar cálculos de unidades comunes

## 📝 Notas

- Las credenciales están hardcodeadas en `login_window.py`
- Todas las conversiones se realizan localmente (sin servidor)
- La interfaz es responsiva y se adapta al contenido
- Incluye validación de campos y manejo de errores
- Los resultados se muestran con 2 decimales de precisión

## 🔒 Seguridad

⚠️ **Advertencia:** Este es un cliente de demostración con credenciales hardcodeadas. No usar en producción sin implementar un sistema de autenticación real.

---

**¡Listo para usar!** 🎉
