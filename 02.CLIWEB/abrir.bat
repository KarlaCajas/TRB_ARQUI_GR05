@echo off
chcp 65001 > nul
cls
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║     🌐 Cliente Web RESTful - Monsters University 🌐         ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Abriendo aplicación web en el navegador...
echo.
echo 📝 Credenciales:
echo    Usuario: MONSTER
echo    Contraseña: Monster9
echo.

start index.html

echo ✅ Aplicación abierta en el navegador predeterminado.
echo.
echo 💡 Si necesitas un servidor local, ejecuta:
echo    python -m http.server 8000
echo.
pause
