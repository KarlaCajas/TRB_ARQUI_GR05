@echo off
echo ========================================
echo   CONFIGURAR FIREWALL PARA PAYARA SERVER
echo ========================================
echo.
echo Este script creara una regla en el Firewall de Windows
echo para permitir conexiones entrantes al puerto 8080
echo.
echo IMPORTANTE: Ejecuta este archivo como ADMINISTRADOR
echo.
pause

echo.
echo Creando regla de firewall...
netsh advfirewall firewall add rule name="Payara Server 8080" dir=in action=allow protocol=TCP localport=8080

if %errorlevel% equ 0 (
    echo.
    echo ✓ Regla de firewall creada exitosamente
    echo.
    echo Ahora prueba desde tu movil:
    echo http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL
) else (
    echo.
    echo ✗ Error al crear la regla
    echo Asegurate de ejecutar este archivo como ADMINISTRADOR
)

echo.
pause
