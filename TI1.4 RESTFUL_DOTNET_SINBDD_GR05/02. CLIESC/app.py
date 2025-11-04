"""
Cliente de Escritorio para Sistema de Conversión de Unidades
Aplicación principal que integra login y ventana principal
"""
from login_window import LoginWindow
from main_window import MainWindow


def main():
    """Función principal de la aplicación"""
    print("=" * 60)
    print("Cliente de Escritorio - Sistema de Conversión de Unidades")
    print("=" * 60)
    print("\nIniciando aplicación...")
    
    # Loop principal para manejar login y logout
    continuar = True
    
    while continuar:
        # Mostrar ventana de login
        print("\n[1] Mostrando ventana de login...")
        login = LoginWindow()
        login_exitoso = login.ejecutar()
        
        if login_exitoso:
            print("\n✓ Login exitoso")
            print(f"✓ Usuario autenticado: {login.USUARIO_VALIDO}")
            
            # Mostrar ventana principal
            print("\n[2] Abriendo calculadora de conversiones...")
            app = MainWindow(usuario=login.USUARIO_VALIDO)
            cerrar_sesion = app.ejecutar()
            
            if cerrar_sesion:
                print("\n✓ Sesión cerrada correctamente")
                print("✓ Volviendo al login...")
                # El loop continúa y vuelve a mostrar el login
            else:
                print("\n✓ Aplicación cerrada correctamente")
                continuar = False
        else:
            print("\n✗ Login cancelado o fallido")
            print("✗ Aplicación terminada")
            continuar = False
    
    print("\n" + "=" * 60)
    print("Gracias por usar el sistema")
    print("=" * 60)


if __name__ == "__main__":
    main()
