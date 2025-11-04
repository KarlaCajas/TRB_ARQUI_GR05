"""
Script de prueba para verificar el funcionamiento del cliente
"""
from api_client import APIClient

def test_conexion():
    """Prueba la conexión con el servidor"""
    print("=" * 60)
    print("PRUEBA DE CONEXIÓN CON EL SERVIDOR")
    print("=" * 60)
    
    api = APIClient()
    print(f"\nIntentando conectar con: {api.base_url}")
    
    if api.verificar_conexion():
        print("✅ Conexión exitosa!")
        print("\n--- Obteniendo conversiones ---")
        resultado = api.obtener_todas()
        
        if resultado["success"]:
            print(f"✅ {resultado['message']}")
            if resultado["data"]:
                print(f"📊 Total de conversiones: {len(resultado['data'])}")
                print("\nPrimeras conversiones:")
                for i, item in enumerate(resultado["data"][:3], 1):
                    print(f"\n  {i}. {item.get('tipoConversion', 'N/A')}")
                    print(f"     {item.get('unidadOrigen', 'N/A')} -> {item.get('unidadDestino', 'N/A')}")
                    print(f"     Factor: {item.get('factorConversion', 'N/A')}")
            else:
                print("ℹ️  No hay conversiones registradas")
        else:
            print(f"❌ {resultado['message']}")
    else:
        print("❌ No se pudo conectar con el servidor")
        print("\n⚠️  IMPORTANTE:")
        print("   1. Verifica que el servidor .NET esté ejecutándose")
        print("   2. Confirma que la URL sea: http://localhost:5014/api/ConversionUnidades_Controlador")
        print("   3. Revisa que no haya firewall bloqueando el puerto 5014")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_conexion()
