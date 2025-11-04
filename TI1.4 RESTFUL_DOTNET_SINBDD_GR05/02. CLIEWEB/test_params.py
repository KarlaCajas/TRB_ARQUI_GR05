import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = 'http://localhost:5014/api/ConversionUnidades_Controlador'

print("=" * 70)
print("PROBANDO DIFERENTES FORMATOS DE PARÁMETROS")
print("=" * 70)

# Prueba 1: Nombres actuales
print("\n1. Probando con deUnidad/aUnidad:")
params1 = {
    'tipo': 'masa',
    'valor': 100,
    'deUnidad': 'kilogramo',
    'aUnidad': 'gramo'
}
try:
    response = requests.get(base_url, params=params1, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

# Prueba 2: Nombres en inglés
print("\n2. Probando con fromUnit/toUnit:")
params2 = {
    'type': 'masa',
    'value': 100,
    'fromUnit': 'kilogramo',
    'toUnit': 'gramo'
}
try:
    response = requests.get(base_url, params=params2, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

# Prueba 3: Nombres cortos
print("\n3. Probando con de/a:")
params3 = {
    'tipo': 'masa',
    'valor': 100,
    'de': 'kilogramo',
    'a': 'gramo'
}
try:
    response = requests.get(base_url, params=params3, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

# Prueba 4: Con unidadOrigen/unidadDestino
print("\n4. Probando con unidadOrigen/unidadDestino:")
params4 = {
    'tipo': 'masa',
    'valor': 100,
    'unidadOrigen': 'kilogramo',
    'unidadDestino': 'gramo'
}
try:
    response = requests.get(base_url, params=params4, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

# Prueba 5: Sin tipo, solo unidades
print("\n5. Probando sin tipo:")
params5 = {
    'valor': 100,
    'deUnidad': 'kilogramo',
    'aUnidad': 'gramo'
}
try:
    response = requests.get(base_url, params=params5, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

# Prueba 6: Temperatura
print("\n6. Probando temperatura con celsius/fahrenheit:")
params6 = {
    'tipo': 'temperatura',
    'valor': 25,
    'deUnidad': 'celsius',
    'aUnidad': 'fahrenheit'
}
try:
    response = requests.get(base_url, params=params6, verify=False)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.text}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 70)
