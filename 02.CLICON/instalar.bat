@echo off
chcp 65001 > nul
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║  🎓 Cliente RESTful - Monsters University - INSTALADOR 🎓   ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 📦 Instalando dependencias de Python...
echo.

pip install -r requirements.txt

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ ¡Instalación completada con éxito!
    echo.
    echo 📝 Para ejecutar el cliente, usa: run_cliente.bat
    echo    O ejecuta directamente: python cliente_restful.py
    echo.
) else (
    echo.
    echo ❌ Error en la instalación.
    echo    Verifica que Python y pip estén instalados correctamente.
    echo.
)

pause
