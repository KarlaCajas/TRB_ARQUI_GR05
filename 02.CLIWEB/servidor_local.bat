@echo off
chcp 65001 > nul
cls
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║   🌐 Servidor Local - Cliente Web RESTful 🌐               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Iniciando servidor local en puerto 8000...
echo.
echo 📝 Accede a la aplicación en:
echo    http://localhost:8000
echo.
echo 💡 Credenciales:
echo    Usuario: MONSTER
echo    Contraseña: Monster9
echo.
echo ⚠️  Presiona Ctrl+C para detener el servidor
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
echo.

python -m http.server 8000
