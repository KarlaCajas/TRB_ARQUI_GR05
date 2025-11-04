import requests
import urllib3

# Deshabilitar advertencias SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("=" * 60)
print("PROBANDO DIFERENTES MÉTODOS")
print("=" * 60)

# URL del servidor
base_url = 'http://localhost:5014/api/ConversionUnidades_Controlador'

# Método 1: GET con query parameters
print("\n1. GET con query parameters:")
params = {
    'tipo': 'longitud',
    'valor': 100,
    'deUnidad': 'metro',
    'aUnidad': 'centimetro'
}
try:
    response = requests.get(base_url, params=params, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:300]}")
except Exception as e:
    print(f"   Error: {e}")

# Método 2: POST con form data
print("\n2. POST con form data (application/x-www-form-urlencoded):")
data = {
    'tipo': 'longitud',
    'valor': 100,
    'deUnidad': 'metro',
    'aUnidad': 'centimetro'
}
try:
    response = requests.post(base_url, data=data, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:300]}")
except Exception as e:
    print(f"   Error: {e}")

# Método 3: GET en http (puerto 5014)
print("\n3. GET en puerto HTTP 5014:")
base_url_http = 'http://localhost:5014/api/ConversionUnidades_Controlador'
try:
    response = requests.get(base_url_http, params=params)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:300]}")
except Exception as e:
    print(f"   Error: {e}")

# Método 4: POST en http con form data
print("\n4. POST en puerto HTTP 5014 con form data:")
try:
    response = requests.post(base_url_http, data=data)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text[:300]}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 60)
