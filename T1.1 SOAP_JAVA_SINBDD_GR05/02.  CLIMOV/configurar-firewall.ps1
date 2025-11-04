# Script para configurar firewall para el servicio SOAP
# DEBE EJECUTARSE COMO ADMINISTRADOR

Write-Host "=== Configuracion de Firewall para SOAP Server ===" -ForegroundColor Green

# Verificar si se ejecuta como administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "`nERROR: Este script debe ejecutarse como Administrador" -ForegroundColor Red
    Write-Host "Haz click derecho en PowerShell y selecciona 'Ejecutar como administrador'" -ForegroundColor Yellow
    Write-Host "`nPresiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit
}

Write-Host "`n1. Verificando si ya existe la regla..." -ForegroundColor Yellow
$existingRule = Get-NetFirewallRule -DisplayName "SOAP Server 8080" -ErrorAction SilentlyContinue

if ($existingRule) {
    Write-Host "   La regla ya existe. ¿Deseas eliminarla y crearla de nuevo? (S/N)" -ForegroundColor Yellow
    $response = Read-Host
    if ($response -eq "S" -or $response -eq "s") {
        Remove-NetFirewallRule -DisplayName "SOAP Server 8080"
        Write-Host "   Regla anterior eliminada" -ForegroundColor Cyan
    } else {
        Write-Host "   Manteniendo regla existente" -ForegroundColor Cyan
        Write-Host "`nPresiona cualquier tecla para salir..."
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        exit
    }
}

Write-Host "`n2. Creando regla de firewall para puerto 8080..." -ForegroundColor Yellow
try {
    New-NetFirewallRule -DisplayName "SOAP Server 8080" `
                        -Direction Inbound `
                        -LocalPort 8080 `
                        -Protocol TCP `
                        -Action Allow `
                        -Profile Any `
                        -Enabled True
    
    Write-Host "   Checkmark Regla creada exitosamente" -ForegroundColor Green
} catch {
    Write-Host "   X Error al crear la regla: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "`nPresiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit
}

Write-Host "`n3. Verificando la regla..." -ForegroundColor Yellow
$newRule = Get-NetFirewallRule -DisplayName "SOAP Server 8080"
if ($newRule) {
    Write-Host "   Checkmark Regla verificada" -ForegroundColor Green
    Write-Host "`n   Detalles de la regla:" -ForegroundColor Cyan
    Write-Host "   - Nombre: $($newRule.DisplayName)" -ForegroundColor White
    Write-Host "   - Estado: $($newRule.Enabled)" -ForegroundColor White
    Write-Host "   - Direccion: $($newRule.Direction)" -ForegroundColor White
    Write-Host "   - Accion: $($newRule.Action)" -ForegroundColor White
} else {
    Write-Host "   X No se pudo verificar la regla" -ForegroundColor Red
}

Write-Host "`n4. Verificando conectividad al puerto 8080..." -ForegroundColor Yellow
$port = Get-NetTCPConnection -LocalPort 8080 -State Listen -ErrorAction SilentlyContinue
if ($port) {
    Write-Host "   Checkmark Hay un servicio escuchando en el puerto 8080" -ForegroundColor Green
    $process = Get-Process -Id $port.OwningProcess
    Write-Host "   Proceso: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Cyan
} else {
    Write-Host "   ! No hay ningun servicio escuchando en el puerto 8080" -ForegroundColor Yellow
    Write-Host "   Asegurate de iniciar tu servidor SOAP antes de ejecutar la app" -ForegroundColor Yellow
}

Write-Host "`n=== Configuracion Completa ===" -ForegroundColor Green
Write-Host "`nAhora tu PC deberia permitir conexiones entrantes en el puerto 8080" -ForegroundColor White
Write-Host "Tu dispositivo Android podra conectarse al servicio SOAP" -ForegroundColor White

Write-Host "`nSiguientes pasos:" -ForegroundColor Yellow
Write-Host "1. Asegurate de que tu servicio SOAP este corriendo" -ForegroundColor White
Write-Host "2. Conecta tu celular a la misma red WiFi que tu PC" -ForegroundColor White
Write-Host "3. Obtén tu IP con: ipconfig" -ForegroundColor White
Write-Host "4. Actualiza la IP en LoginActivity.java" -ForegroundColor White
Write-Host "5. Ejecuta la app en tu celular" -ForegroundColor White

Write-Host "`n¿Deseas ver tu IP local ahora? (S/N)" -ForegroundColor Yellow
$showIp = Read-Host
if ($showIp -eq "S" -or $showIp -eq "s") {
    Write-Host "`nTu IP local es:" -ForegroundColor Cyan
    $ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*"} | Select-Object -First 1).IPAddress
    Write-Host "   $ip" -ForegroundColor Green
    Write-Host "`nUsa esta IP en LoginActivity.java:" -ForegroundColor White
    Write-Host "   private static final String SOAP_URL_DEVICE = `"http://${ip}:8080/ConUni_Soap_Java_GR05/CONUNI`";" -ForegroundColor Cyan
}

Write-Host "`nPresiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
