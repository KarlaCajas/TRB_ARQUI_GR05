@echo off
REM Script para ejecutar el Cliente de Escritorio

echo ============================================================
echo   Cliente de Escritorio - Sistema de Conversion de Unidades
echo ============================================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor, instala Python 3.7 o superior
    pause
    exit /b 1
)

echo [1/3] Verificando Python...
python --version
echo.

echo [2/3] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)
echo.

echo [3/3] Iniciando aplicacion...
echo.
echo ============================================================
echo   CREDENCIALES DE LOGIN:
echo   Usuario: MONSTER
echo   Contrasena: Monster9
echo ============================================================
echo.

python app.py

echo.
echo ============================================================
echo   Aplicacion cerrada
echo ============================================================
pause
