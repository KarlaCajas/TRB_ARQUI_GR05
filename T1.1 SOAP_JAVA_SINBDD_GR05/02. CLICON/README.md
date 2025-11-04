# Cliente SOAP en consola (Python)

## Resumen
Este pequeño cliente de consola consume el WSDL SOAP que indicaste:
http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl

## Requisitos
- Python 3.8+
- pip

## Instalación (PowerShell)
```powershell
# Desde la carpeta del proyecto
python -m pip install -r requirements.txt
```

## Uso
Ejecuta el script y realiza login con las credenciales quemadas:
- Usuario: MONSTER
- Contraseña: Monster9

```powershell
python client.py
```

El cliente intentará conectar al WSDL local, listará servicios/puertos/operaciones y te permitirá invocar una operación. Si una operación requiere parámetros, te pedirá un dict literal en Python con los parámetros (por ejemplo: {"id": 123, "name": "Juan"}).

## Notas
- Si el cliente no puede conectar al WSDL, comprueba que el servicio Java esté corriendo en http://localhost:8080 y que la ruta del WSDL sea accesible desde la máquina donde ejecutes el cliente.
- Este cliente no implementa autenticación HTTP o WS-Security; solo contiene un login local (credenciales quemadas) como gate de acceso antes de permitir llamadas al servicio.
