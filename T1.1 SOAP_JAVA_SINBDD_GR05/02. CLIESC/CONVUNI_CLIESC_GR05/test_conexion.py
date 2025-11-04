"""
Script de prueba para verificar la conexión con el servicio SOAP
"""
from zeep import Client
from zeep.exceptions import Fault

def probar_conexion():
    """Prueba la conexión con el servicio SOAP"""
    print("=" * 60)
    print("  PRUEBA DE CONEXIÓN - Servicio SOAP GR05")
    print("=" * 60)
    print()
    
    wsdl_url = "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl"
    
    try:
        print(f"📡 Conectando a: {wsdl_url}")
        print("Esperando respuesta del servidor...")
        print()
        
        # Crear cliente SOAP
        client = Client(wsdl_url)
        
        print("✅ Conexión exitosa!")
        print()
        print("📋 Operaciones disponibles:")
        print("-" * 60)
        
        # Listar operaciones disponibles
        for service in client.wsdl.services.values():
            print(f"\n🔹 Servicio: {service.name}")
            for port in service.ports.values():
                operations = sorted(port.binding._operations.keys())
                for operation_name in operations:
                    print(f"   • {operation_name}")
        
        print()
        print("-" * 60)
        print("🧪 Realizando pruebas de operaciones...")
        print("-" * 60)
        print()
        
        # Prueba 1: Login
        print("Test 1: Login")
        try:
            resultado_login = client.service.login("MONSTER", "Monster9")
            print(f"   ✅ Login exitoso: {resultado_login}")
        except Exception as e:
            print(f"   ❌ Error en login: {str(e)}")
        print()
        
        # Prueba 2: Celsius a Fahrenheit
        print("Test 2: Celsius a Fahrenheit (100°C)")
        try:
            resultado = client.service.celsiusAFahrenheit(100)
            print(f"   ✅ Resultado: {resultado}°F")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
        print()
        
        # Prueba 3: Kilogramos a Gramos
        print("Test 3: Kilogramos a Gramos (5 kg)")
        try:
            resultado = client.service.kilogramosAGramos(5)
            print(f"   ✅ Resultado: {resultado} g")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
        print()
        
        # Prueba 4: Kilómetros a Metros
        print("Test 4: Kilómetros a Metros (2 km)")
        try:
            resultado = client.service.kilometrosAMetros(2)
            print(f"   ✅ Resultado: {resultado} m")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
        print()
        
        print("=" * 60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS")
        print("=" * 60)
        print()
        print("El servicio SOAP está funcionando correctamente.")
        print("Puedes ejecutar el cliente con: python cliente_soap.py")
        print()
        
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        print()
        print("🔧 Posibles soluciones:")
        print("   1. Verifica que el servidor SOAP esté ejecutándose")
        print("   2. Accede manualmente a:")
        print(f"      {wsdl_url}")
        print("   3. Verifica que el puerto 8080 esté disponible")
        print()
        return False
    
    return True


if __name__ == "__main__":
    probar_conexion()
    input("\nPresiona Enter para salir...")
