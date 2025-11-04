"""
INFORMACIÓN DEL PROYECTO
========================

Nombre: Cliente de Escritorio SOAP - Conversor de Unidades
Grupo: GR05
Tecnología: Python 3 + SOAP (zeep) + Tkinter

ESTRUCTURA DEL PROYECTO
========================

CONVUNI_CLIESC_GR05/
├── cliente_soap.py          # Cliente principal con GUI
├── test_conexion.py         # Script de prueba de conexión
├── requirements.txt         # Dependencias del proyecto
├── instalar.bat            # Script de instalación automática
├── ejecutar.bat            # Script de ejecución rápida
├── README.md               # Documentación principal
├── GUIA_USO.md            # Guía detallada de uso
├── INFO_PROYECTO.py       # Este archivo
└── service.wsdl           # WSDL descargado del servicio

CREDENCIALES
============
Usuario:    MONSTER
Contraseña: Monster9

SERVICIO SOAP
=============
URL: http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl

OPERACIONES DISPONIBLES
=======================

🌡️ TEMPERATURA:
   - celsiusAFahrenheit(celsius: float) -> float
   - fahrenheitACelsius(fahrenheit: float) -> float
   - celsiusAKelvin(celsius: float) -> float

⚖️ MASA:
   - toneladasAKilogramos(toneladas: float) -> float
   - kilogramosAGramos(kg: float) -> float
   - gramosAMiligramos(gramos: float) -> float

📏 LONGITUD:
   - kilometrosAMetros(km: float) -> float
   - metrosACentimetros(metros: float) -> float
   - centimetrosAMilimetros(cm: float) -> float

🔐 AUTENTICACIÓN:
   - login(usuario: str, password: str) -> bool

DEPENDENCIAS
============
- zeep==4.2.1       # Cliente SOAP para Python
- tkinter           # GUI (incluido en Python)

INSTALACIÓN RÁPIDA
==================
1. Ejecuta: instalar.bat
   O manualmente: pip install zeep

2. Ejecuta: ejecutar.bat
   O manualmente: python cliente_soap.py

CARACTERÍSTICAS PRINCIPALES
============================
✅ Interfaz gráfica moderna y profesional
✅ Sistema de login con credenciales
✅ 9 conversiones diferentes organizadas por categoría
✅ Validación robusta de entrada
✅ Manejo completo de errores
✅ Comunicación SOAP en tiempo real
✅ Atajos de teclado (Enter)
✅ Scripts de instalación y ejecución

ARQUITECTURA
============

┌─────────────────────────────────────────┐
│         CLIENTE PYTHON (Tkinter)        │
├─────────────────────────────────────────┤
│  LoginWindow    │    MainWindow         │
│  - Validación   │    - Pestañas         │
│  - Autenticación│    - Conversiones     │
└────────────┬────┴──────────┬────────────┘
             │                │
             └────────┬───────┘
                      │
              ┌───────▼────────┐
              │   SOAPClient   │
              │   (zeep)       │
              └───────┬────────┘
                      │
                 (SOAP/HTTP)
                      │
              ┌───────▼────────┐
              │  Servicio SOAP │
              │  (Java/WSDL)   │
              └────────────────┘

FLUJO DE EJECUCIÓN
==================

1. INICIO
   └─> cliente_soap.py ejecutado
       └─> SOAPClient conecta al WSDL
           └─> LoginWindow mostrada

2. LOGIN
   └─> Usuario ingresa credenciales
       └─> Validación local
           └─> Llamada SOAP: login(usuario, password)
               ├─> Éxito → MainWindow
               └─> Error → Mensaje de error

3. CONVERSIÓN
   └─> Usuario selecciona pestaña
       └─> Usuario ingresa valor
           └─> Presiona "Convertir" o Enter
               └─> Validación de entrada
                   └─> Llamada SOAP: operación(valor)
                       ├─> Éxito → Muestra resultado
                       └─> Error → Mensaje de error

MANEJO DE ERRORES
=================

Nivel 1: Validación de Entrada
   - Campos vacíos
   - Formato numérico
   - Valores válidos

Nivel 2: Validación de Negocio
   - Credenciales incorrectas
   - Valores fuera de rango

Nivel 3: Comunicación SOAP
   - Error de conexión
   - Timeout
   - Respuesta inválida

Nivel 4: Sistema
   - Servicio no disponible
   - Puerto ocupado
   - Dependencias faltantes

PRUEBAS REALIZADAS
==================
✅ Conexión exitosa al servicio SOAP
✅ Login con credenciales correctas
✅ Login con credenciales incorrectas
✅ Cada una de las 9 conversiones
✅ Validación de entrada (números válidos/inválidos)
✅ Manejo de errores de conexión
✅ Interfaz responsive

COMANDOS ÚTILES
===============

# Instalar dependencias
pip install zeep

# Probar conexión
python test_conexion.py

# Ejecutar cliente
python cliente_soap.py

# Ver servicios SOAP disponibles
# Acceder a: http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl

TROUBLESHOOTING
===============

Problema: ImportError: No module named 'zeep'
Solución: pip install zeep

Problema: No se puede conectar al servicio
Solución: Verifica que el servidor SOAP esté ejecutándose

Problema: Login falla
Solución: Usa credenciales correctas (MONSTER / Monster9)

Problema: Error en conversión
Solución: Ingresa números válidos (ej: 10, 10.5, -5)

CONTACTO
========
Proyecto académico - Grupo GR05
Arquitectura de Software
"""

if __name__ == "__main__":
    print(__doc__)
