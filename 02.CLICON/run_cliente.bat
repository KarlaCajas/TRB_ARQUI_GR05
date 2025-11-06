@echo off
chcp 65001 > nul
cls
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║   🎓 Iniciando Cliente RESTful - Monsters University 🎓     ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Ejecutando cliente...
echo.

python cliente_restful.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Error al ejecutar el cliente.
    echo    Verifica que hayas instalado las dependencias con: instalar.bat
    echo.
    pause
)
