# Cliente SOAP en Python

Cliente de consola en Python para consumir el servicio SOAP de .NET.

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Instalar las dependencias:**

```powershell
pip install -r requirements.txt
```

O instalar manualmente:

```powershell
pip install zeep requests lxml
```

## Configuración

1. Asegúrate de que el servidor .NET esté ejecutándose en `http://localhost:63393/Service.svc`
2. Verifica que la URL del WSDL esté accesible: `http://localhost:63393/Service.svc?wsdl`

## Uso

### Ejecutar el cliente:

```powershell
python cliente_soap.py
```

### Funcionalidades disponibles:

El cliente proporciona las siguientes conversiones:

#### Conversiones de Temperatura:
- Celsius a Fahrenheit
- Fahrenheit a Celsius
- Celsius a Kelvin

#### Conversiones de Masa:
- Kilogramos a Libras
- Libras a Kilogramos
- Kilogramos a Onzas

#### Conversiones de Longitud:
- Metros a Pies
- Pies a Metros
- Kilómetros a Millas

#### Métodos de Prueba:
- GetData: Prueba básica con un valor entero
- GetDataUsingDataContract: Prueba con objeto complejo

## Estructura del Proyecto

```
02.CLICON/
├── cliente_soap.py      # Cliente SOAP principal
├── requirements.txt     # Dependencias de Python
└── README.md           # Este archivo
```

## Troubleshooting

### Error de conexión
- Verifica que el servidor .NET esté ejecutándose
- Comprueba que el puerto 63393 esté disponible
- Asegúrate de que no haya firewall bloqueando la conexión

### Error de importación de zeep
```powershell
pip install --upgrade zeep
```

### Error de lxml en Windows
Si tienes problemas instalando lxml, intenta:
```powershell
pip install --upgrade pip
pip install lxml
```

## Ejemplo de Uso

```
============================================================
         CLIENTE SOAP - SERVICIO DE CONVERSIONES           
============================================================

--- CONVERSIONES DE TEMPERATURA ---
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Celsius a Kelvin
...

Seleccione una opción: 1
Ingrese temperatura en Celsius: 25

✓ 25.0°C = 77.00°F
```

## Notas

- El cliente usa la librería `zeep` para consumir servicios SOAP
- Todas las conversiones se realizan en el servidor .NET
- El cliente es interactivo y fácil de usar desde la consola
