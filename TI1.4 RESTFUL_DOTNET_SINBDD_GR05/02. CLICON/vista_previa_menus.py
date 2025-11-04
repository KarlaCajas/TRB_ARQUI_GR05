"""
DEMOSTRACIÓN VISUAL DEL MENÚ
Este archivo muestra cómo se ve la interfaz del cliente
"""

MENU_PRINCIPAL = """
==================================================
🌐 CONVERSOR DE UNIDADES
==================================================
👤 Usuario: MONSTER
🔗 Servidor: http://localhost:5014
==================================================
1. ⚖️  Conversiones de MASA
2. 📏 Conversiones de LONGITUD
3. 🌡️  Conversiones de TEMPERATURA
4. 🔌 Verificar conexión con servidor
5. 🚪 Cerrar sesión y salir
==================================================
"""

MENU_MASA = """
==================================================
⚖️  CONVERSIONES DE MASA
==================================================
1. Kilogramos a Gramos
2. Gramos a Miligramos
3. Toneladas a Kilogramos
0. ⬅️  Volver al menú principal
==================================================
"""

MENU_LONGITUD = """
==================================================
📏 CONVERSIONES DE LONGITUD
==================================================
1. Kilómetros a Metros
2. Metros a Centímetros
3. Centímetros a Milímetros
0. ⬅️  Volver al menú principal
==================================================
"""

MENU_TEMPERATURA = """
==================================================
🌡️  CONVERSIONES DE TEMPERATURA
==================================================
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
3. Celsius a Kelvin
0. ⬅️  Volver al menú principal
==================================================
"""

EJEMPLO_CONVERSION = """
==================================================
📊 RESULTADO DE LA CONVERSIÓN
==================================================
Tipo: Kilogramos a Libras
Valor original: 100 kilogramos
Resultado: 220.4620 libras
==================================================
✅ Conversión registrada en el servidor
"""

if __name__ == "__main__":
    print("=" * 60)
    print("VISTA PREVIA DE LOS MENÚS DEL CONVERSOR DE UNIDADES")
    print("=" * 60)
    
    print("\n📱 MENÚ PRINCIPAL:")
    print(MENU_PRINCIPAL)
    
    print("\n⚖️  MENÚ DE MASA:")
    print(MENU_MASA)
    
    print("\n📏 MENÚ DE LONGITUD:")
    print(MENU_LONGITUD)
    
    print("\n🌡️  MENÚ DE TEMPERATURA:")
    print(MENU_TEMPERATURA)
    
    print("\n✅ EJEMPLO DE CONVERSIÓN:")
    print(EJEMPLO_CONVERSION)
    
    print("\n" + "=" * 60)
    print("Para ver los menús reales, ejecuta: python cliente_api.py")
    print("=" * 60)
