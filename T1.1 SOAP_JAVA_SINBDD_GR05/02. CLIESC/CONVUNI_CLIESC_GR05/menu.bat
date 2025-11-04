@echo off
title Cliente SOAP - Conversor de Unidades GR05
color 0A

:menu
cls
echo ============================================================
echo    CLIENTE SOAP - CONVERSOR DE UNIDADES
echo    Grupo: GR05
echo ============================================================
echo.
echo    [1] Instalar Dependencias
echo    [2] Probar Conexion con Servicio SOAP
echo    [3] Ejecutar Cliente de Escritorio
echo    [4] Ver Informacion del Proyecto
echo    [5] Ver Guia de Uso
echo    [6] Abrir WSDL en Navegador
echo    [0] Salir
echo.
echo ============================================================
set /p opcion="Selecciona una opcion: "

if "%opcion%"=="1" goto instalar
if "%opcion%"=="2" goto probar
if "%opcion%"=="3" goto ejecutar
if "%opcion%"=="4" goto info
if "%opcion%"=="5" goto guia
if "%opcion%"=="6" goto wsdl
if "%opcion%"=="0" goto salir
goto menu

:instalar
cls
echo ============================================================
echo    INSTALANDO DEPENDENCIAS
echo ============================================================
echo.
pip install zeep
echo.
echo ============================================================
echo    INSTALACION COMPLETADA
echo ============================================================
pause
goto menu

:probar
cls
echo ============================================================
echo    PROBANDO CONEXION CON SERVICIO SOAP
echo ============================================================
echo.
python test_conexion.py
pause
goto menu

:ejecutar
cls
echo ============================================================
echo    INICIANDO CLIENTE DE ESCRITORIO
echo ============================================================
echo.
echo Credenciales:
echo    Usuario: MONSTER
echo    Contrasena: Monster9
echo.
python cliente_soap.py
pause
goto menu

:info
cls
echo ============================================================
echo    INFORMACION DEL PROYECTO
echo ============================================================
echo.
python INFO_PROYECTO.py
pause
goto menu

:guia
cls
start GUIA_USO.md
goto menu

:wsdl
cls
start http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
goto menu

:salir
cls
echo.
echo Gracias por usar el Cliente SOAP GR05
echo.
exit
