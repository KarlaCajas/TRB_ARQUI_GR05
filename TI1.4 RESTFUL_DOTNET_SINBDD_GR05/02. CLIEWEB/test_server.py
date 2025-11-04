import requests
import urllib3

# Deshabilitar advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL del servidor
API_BASE_URL = 'http://localhost:5014/api/ConversionUnidades_Controlador'

# Datos de prueba
data = {
    'tipo': 'longitud',
    'valor': 100,
    'deUnidad': 'metro',
    'aUnidad': 'centimetro'
}

print("=" * 60)
print("PRUEBA DE CONEXIÓN AL SERVIDOR .NET")
print("=" * 60)
print(f"\nURL: {API_BASE_URL}")
print(f"Datos a enviar: {data}\n")

try:
    # Intentar conexión GET primero
    print("1. Probando GET...")
    try:
        response = requests.get(API_BASE_URL, verify=False, timeout=5)
        print(f"   ✓ GET Status Code: {response.status_code}")
        print(f"   Response: {response.text[:200]}")
    except Exception as e:
        print(f"   ✗ Error en GET: {str(e)}")
    
    print("\n2. Probando POST con JSON...")
    response = requests.post(API_BASE_URL, json=data, verify=False, timeout=5)
    print(f"   ✓ POST Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print(f"   ✓ Respuesta exitosa:")
        print(f"   {response.json()}")
    elif response.status_code == 405:
        print(f"   ✗ Error 405: Método no permitido")
        print(f"   El servidor no acepta POST en este endpoint")
    else:
        print(f"   ✗ Error {response.status_code}")
        print(f"   Respuesta: {response.text[:200]}")
        
except requests.exceptions.ConnectionError:
    print("\n✗ ERROR: No se puede conectar al servidor")
    print("   Asegúrate de que el servidor .NET esté ejecutándose en:")
    print("   http://localhost:5014")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")

print("\n" + "=" * 60)
print("VERIFICANDO ENDPOINTS ALTERNATIVOS")
print("=" * 60)

# Probar URLs alternativas
urls_alternativas = [
    'http://localhost:5014/api/ConversionUnidades_Controlador',
    'http://localhost:5014'
]

for url in urls_alternativas:
    try:
        print(f"\nProbando: {url}")
        response = requests.get(url, verify=False, timeout=3)
        print(f"✓ Conectado! Status: {response.status_code}")
    except Exception as e:
        print(f"✗ No disponible: {str(e)}")

print("\n" + "=" * 60)
