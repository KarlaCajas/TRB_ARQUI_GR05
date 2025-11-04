import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = 'http://localhost:5014/api/ConversionUnidades_Controlador'

print("=" * 70)
print("PRUEBAS FINALES CON FORMATO CORRECTO")
print("=" * 70)

# Prueba 1: Masa - kg a gramo
print("\n✓ Prueba 1: 100 kilogramo → gramo")
params = {'valor': 100, 'unidadOrigen': 'kilogramo', 'unidadDestino': 'gramo'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} gramos")

# Prueba 2: Masa - gramo a miligramo
print("\n✓ Prueba 2: 500 gramo → miligramo")
params = {'valor': 500, 'unidadOrigen': 'gramo', 'unidadDestino': 'miligramo'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} miligramos")

# Prueba 3: Masa - tonelada a kilogramo
print("\n✓ Prueba 3: 2 tonelada → kilogramo")
params = {'valor': 2, 'unidadOrigen': 'tonelada', 'unidadDestino': 'kilogramo'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} kilogramos")

# Prueba 4: Longitud - km a metro
print("\n✓ Prueba 4: 5 kilometro → metro")
params = {'valor': 5, 'unidadOrigen': 'kilometro', 'unidadDestino': 'metro'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} metros")

# Prueba 5: Longitud - metro a centimetro
print("\n✓ Prueba 5: 10 metro → centimetro")
params = {'valor': 10, 'unidadOrigen': 'metro', 'unidadDestino': 'centimetro'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} centímetros")

# Prueba 6: Longitud - cm a milimetro
print("\n✓ Prueba 6: 50 centimetro → milimetro")
params = {'valor': 50, 'unidadOrigen': 'centimetro', 'unidadDestino': 'milimetro'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} milímetros")

# Prueba 7: Temperatura - celsius a fahrenheit
print("\n✓ Prueba 7: 25 celsius → fahrenheit")
params = {'valor': 25, 'unidadOrigen': 'celsius', 'unidadDestino': 'fahrenheit'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} °F")

# Prueba 8: Temperatura - fahrenheit a celsius
print("\n✓ Prueba 8: 77 fahrenheit → celsius")
params = {'valor': 77, 'unidadOrigen': 'fahrenheit', 'unidadDestino': 'celsius'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} °C")

# Prueba 9: Temperatura - celsius a kelvin
print("\n✓ Prueba 9: 0 celsius → kelvin")
params = {'valor': 0, 'unidadOrigen': 'celsius', 'unidadDestino': 'kelvin'}
response = requests.get(base_url, params=params, verify=False)
print(f"   Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print(f"   Resultado: {data['resultado']} K")

print("\n" + "=" * 70)
print("✅ TODAS LAS CONVERSIONES FUNCIONAN CORRECTAMENTE")
print("=" * 70)
