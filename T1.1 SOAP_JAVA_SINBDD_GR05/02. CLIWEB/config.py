# Configuración del Cliente Web SOAP
# Este archivo contiene configuraciones opcionales

# Configuración del Servidor
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

# URL del Servicio SOAP
WSDL_URL = 'http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl'

# Credenciales (Solo para desarrollo - No usar en producción)
USUARIO_VALIDO = 'MONSTER'
CONTRASENA_VALIDA = 'Monster9'

# Timeout para peticiones SOAP (segundos)
SOAP_TIMEOUT = 30
