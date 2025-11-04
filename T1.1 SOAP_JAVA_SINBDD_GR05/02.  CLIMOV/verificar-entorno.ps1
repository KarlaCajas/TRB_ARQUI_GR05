Write-Host "=== Verificacion del Entorno SOAP Client Android ===" -ForegroundColor Green

Write-Host "`n1. Verificando IP local..." -ForegroundColor Yellow
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*"} | Select-Object -First 1).IPAddress
Write-Host "   IP: $ip" -ForegroundColor Cyan

Write-Host "`n2. Verificando puerto 8080..." -ForegroundColor Yellow
$port = Get-NetTCPConnection -LocalPort 8080 -State Listen -ErrorAction SilentlyContinue
if ($port) {
    Write-Host "   Checkmark Puerto 8080 esta abierto" -ForegroundColor Green
} else {
    Write-Host "   X Puerto 8080 no esta en escucha" -ForegroundColor Red
}

Write-Host "`n3. Verificando regla de firewall..." -ForegroundColor Yellow
$rule = Get-NetFirewallRule -DisplayName "SOAP Server 8080" -ErrorAction SilentlyContinue
if ($rule) {
    Write-Host "   Checkmark Regla de firewall existe" -ForegroundColor Green
} else {
    Write-Host "   X Regla de firewall no configurada" -ForegroundColor Red
    Write-Host "   Ejecuta como Admin: New-NetFirewallRule -DisplayName 'SOAP Server 8080' -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow" -ForegroundColor Yellow
}

Write-Host "`n4. Verificando servicio SOAP..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl" -TimeoutSec 5 -UseBasicParsing
    Write-Host "   Checkmark Servicio SOAP responde correctamente" -ForegroundColor Green
} catch {
    Write-Host "   X No se puede acceder al servicio SOAP" -ForegroundColor Red
    Write-Host "   Asegurate de que el servicio este corriendo" -ForegroundColor Yellow
}

Write-Host "`n5. Verificando estructura del proyecto..." -ForegroundColor Yellow
$projectPath = "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"
if (Test-Path $projectPath) {
    Write-Host "   Checkmark Proyecto existe en: $projectPath" -ForegroundColor Green
    
    $mainFiles = @(
        "app\src\main\java\com\gr05\conuniclient\LoginActivity.java",
        "app\src\main\java\com\gr05\conuniclient\MainActivity.java",
        "app\src\main\java\com\gr05\conuniclient\SOAPClient.java",
        "app\build.gradle",
        "build.gradle"
    )
    
    foreach ($file in $mainFiles) {
        $fullPath = Join-Path $projectPath $file
        if (Test-Path $fullPath) {
            Write-Host "   Checkmark $file" -ForegroundColor Green
        } else {
            Write-Host "   X Falta: $file" -ForegroundColor Red
        }
    }
} else {
    Write-Host "   X Proyecto no encontrado" -ForegroundColor Red
}

Write-Host "`n=== Resumen ===" -ForegroundColor Green
Write-Host "Credenciales de login:" -ForegroundColor White
Write-Host "  Usuario: MONSTER" -ForegroundColor Cyan
Write-Host "  Password: Monster9" -ForegroundColor Cyan
Write-Host "`nURLs configuradas:" -ForegroundColor White
Write-Host "  Para emulador: http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI" -ForegroundColor Cyan
Write-Host "  Para dispositivo fisico: http://${ip}:8080/ConUni_Soap_Java_GR05/CONUNI" -ForegroundColor Cyan

Write-Host "`nPresiona cualquier tecla para continuar..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
