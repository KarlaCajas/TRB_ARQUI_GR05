@echo off
echo ========================================
echo    CLIENTE SOAP - Conversor de Unidades
echo    Grupo: GR05
echo ========================================
echo.
echo Iniciando cliente...
echo.
python cliente_soap.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo ejecutar el cliente
    echo Verifica que las dependencias esten instaladas
    echo Ejecuta: instalar.bat
    echo.
    pause
)
