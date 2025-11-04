@echo off
echo ========================================
echo    INSTALADOR - Cliente SOAP GR05
echo ========================================
echo.

echo [1/2] Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en PATH
    echo Por favor instala Python 3.7 o superior desde python.org
    pause
    exit /b 1
)

echo.
echo [2/2] Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo.
echo ========================================
echo    INSTALACION COMPLETADA CON EXITO
echo ========================================
echo.
echo Para ejecutar el cliente, usa:
echo     python cliente_soap.py
echo.
echo Credenciales:
echo     Usuario: MONSTER
echo     Contrasena: Monster9
echo.
pause
