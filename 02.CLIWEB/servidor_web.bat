@echo off
title Cliente Web RESTful - Monsters University
color 0B

echo.
echo ========================================
echo   CLIENTE WEB RESTFUL
echo   Monsters University
echo ========================================
echo.
echo [*] Iniciando servidor web en puerto 8000...
echo [*] La aplicacion estara disponible en:
echo.
echo     - Local:  http://localhost:8000
echo     - Red:    http://192.168.18.113:8000
echo.
echo [*] Servidor RESTful debe estar en:
echo     http://192.168.18.113:8080
echo.
echo [!] IMPORTANTE: Conecta tu movil a la misma red WiFi
echo.
echo ========================================
echo.

cd /d "%~dp0"
python -m http.server 8000

pause
