# Cliente Web Python - Sistema de Conversión de Unidades

Este es un cliente web desarrollado en Python usando Flask para realizar conversiones de unidades.

## 🔐 Credenciales de Acceso

- **Usuario**: `MONSTER`
- **Contraseña**: `Monster9`

## 📋 Requisitos Previos

- Python 3.8 o superior

## 🚀 Instalación

1. **Instalar las dependencias:**

```powershell
pip install Flask
```

## ▶️ Ejecución

1. **Ejecute la aplicación Flask:**

```powershell
python app.py
```

2. **Abra su navegador en:**

```
http://localhost:5000
```

## 📁 Estructura del Proyecto

```
02. CLIWEB/
│
├── app.py                  # Aplicación principal Flask
├── requirements.txt        # Dependencias Python
├── README.md              # Este archivo
│
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── login.html        # Página de login
│   ├── dashboard.html    # Dashboard principal
│   └── operacion.html    # Ejecutar operaciones SOAP
│
└── static/               # Archivos estáticos
    └── style.css        # Estilos CSS
```

## 🔧 Características

- ✅ Sistema de autenticación seguro
- ✅ **Conversión de Temperatura**: °C → °F, °F → °C, °C → K
- ✅ **Conversión de Masa**: kg → g, g → mg, t → kg
- ✅ **Conversión de Longitud**: km → m, m → cm, cm → mm
- ✅ Resultados con unidades claramente mostradas
- ✅ Fórmulas de conversión visibles
- ✅ Interfaz web moderna y responsiva
- ✅ Manejo de sesiones seguro

## 🛠️ Tecnologías Utilizadas

- **Flask**: Framework web de Python
- **HTML5/CSS3**: Interfaz de usuario
- **Jinja2**: Motor de plantillas

## 📝 Uso

### Sistema de Conversión de Unidades

1. **Iniciar sesión** con las credenciales (Usuario: MONSTER, Contraseña: Monster9)
2. **Seleccionar una categoría** de conversión desde el dashboard:
   - 🌡️ **Temperatura**: °C → °F, °F → °C, °C → K
   - ⚖️ **Masa**: kg → g, g → mg, t → kg
   - 📏 **Longitud**: km → m, m → cm, cm → mm
3. **Elegir el tipo de conversión** del menú desplegable
4. **Ingresar el valor** a convertir
5. **Ver el resultado** con:
   - Valor original con su unidad
   - Valor convertido con su unidad
   - Fórmula de conversión utilizada
6. **Cerrar sesión** cuando termine

Para más detalles sobre las conversiones, consulta [CONVERSIONES_SIMPLIFICADAS.md](CONVERSIONES_SIMPLIFICADAS.md)

## ⚠️ Notas Importantes

- Las credenciales están quemadas en el código (`app.py`)
- La aplicación se ejecuta en modo debug para desarrollo
- Para producción, debe configurar una `secret_key` más segura
- No requiere servicios externos ni SOAP

## 🔍 Solución de Problemas

### No puedo iniciar sesión
- Verifique que use las credenciales correctas:
  - Usuario: `MONSTER` (en mayúsculas)
  - Contraseña: `Monster9`

### Error al instalar Flask
```powershell
pip install --upgrade pip
pip install Flask
```

## 👨‍💻 Autor

Cliente Web SOAP - Monster University
Grupo 05
