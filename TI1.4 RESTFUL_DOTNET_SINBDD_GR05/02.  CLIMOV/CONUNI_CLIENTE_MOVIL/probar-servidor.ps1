# Script para probar el servidor REST
# Ejecuta este script para verificar que tu servidor está funcionando

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Probador de Servidor REST - MONSTER  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar IP actual
Write-Host "1. Verificando tu IP actual..." -ForegroundColor Yellow
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -like "*Wi-Fi*" -and $_.IPAddress -like "192.168.*"}).IPAddress
if ($ip) {
    Write-Host "   ✅ Tu IP es: $ip" -ForegroundColor Green
} else {
    Write-Host "   ❌ No se encontró IP de WiFi" -ForegroundColor Red
    $ip = Read-Host "   Por favor ingresa tu IP manualmente"
}
Write-Host ""

# 2. Probar servidor con GET
Write-Host "2. Probando servidor con GET..." -ForegroundColor Yellow
$url = "http://$ip:5014/api/ConversionUnidades_Controlador"
Write-Host "   URL: $url" -ForegroundColor Gray

try {
    $response = Invoke-WebRequest -Uri $url -Method Get -TimeoutSec 3
    Write-Host "   ✅ Servidor responde correctamente!" -ForegroundColor Green
    Write-Host "   Código: $($response.StatusCode)" -ForegroundColor Gray
} catch {
    Write-Host "   ❌ Error al conectar:" -ForegroundColor Red
    Write-Host "   $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "   Posibles causas:" -ForegroundColor Yellow
    Write-Host "   - El servidor no está ejecutándose" -ForegroundColor Yellow
    Write-Host "   - El firewall está bloqueando el puerto 5014" -ForegroundColor Yellow
    Write-Host "   - El servidor no está escuchando en 0.0.0.0:5014" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   Para iniciar el servidor, ejecuta:" -ForegroundColor Cyan
    Write-Host "   cd TuProyectoServidor" -ForegroundColor White
    Write-Host '   dotnet run --urls "http://0.0.0.0:5014"' -ForegroundColor White
    exit
}
Write-Host ""

# 3. Probar conversión de temperatura
Write-Host "3. Probando conversión de temperatura (25°C a °F)..." -ForegroundColor Yellow

$body = @{
    tipoConversion = "Temperatura"
    unidadOrigen = "Celsius"
    unidadDestino = "Fahrenheit"
    valor = 25
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -TimeoutSec 3
    Write-Host "   ✅ Conversión exitosa!" -ForegroundColor Green
    Write-Host "   Resultado: $($response.resultado)°F" -ForegroundColor Green
    Write-Host "   Mensaje: $($response.mensaje)" -ForegroundColor Gray
} catch {
    Write-Host "   ❌ Error en la conversión:" -ForegroundColor Red
    Write-Host "   $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# 4. Probar conversión de masa
Write-Host "4. Probando conversión de masa (2 kg a g)..." -ForegroundColor Yellow

$body = @{
    tipoConversion = "Masa"
    unidadOrigen = "Kilogramos"
    unidadDestino = "Gramos"
    valor = 2
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -TimeoutSec 3
    Write-Host "   ✅ Conversión exitosa!" -ForegroundColor Green
    Write-Host "   Resultado: $($response.resultado) g" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Error en la conversión" -ForegroundColor Red
}
Write-Host ""

# 5. Probar conversión de longitud
Write-Host "5. Probando conversión de longitud (5 km a m)..." -ForegroundColor Yellow

$body = @{
    tipoConversion = "Longitud"
    unidadOrigen = "Kilómetros"
    unidadDestino = "Metros"
    valor = 5
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -TimeoutSec 3
    Write-Host "   ✅ Conversión exitosa!" -ForegroundColor Green
    Write-Host "   Resultado: $($response.resultado) m" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Error en la conversión" -ForegroundColor Red
}
Write-Host ""

# Resumen
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  RESUMEN" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Tu servidor está en: http://$ip:5014" -ForegroundColor White
Write-Host ""
Write-Host "Para que la app Android funcione:" -ForegroundColor Yellow
Write-Host "1. Edita ApiService.java línea 22:" -ForegroundColor White
Write-Host '   private static final String BASE_URL = "http://' -NoNewline -ForegroundColor Gray
Write-Host $ip -NoNewline -ForegroundColor Green
Write-Host ':5014/api/ConversionUnidades_Controlador";' -ForegroundColor Gray
Write-Host ""
Write-Host "2. Edita network_security_config.xml:" -ForegroundColor White
Write-Host '   <domain includeSubdomains="true">' -NoNewline -ForegroundColor Gray
Write-Host $ip -NoNewline -ForegroundColor Green
Write-Host '</domain>' -ForegroundColor Gray
Write-Host ""
Write-Host "3. Recompila el APK:" -ForegroundColor White
Write-Host '   .\gradlew assembleDebug' -ForegroundColor Gray
Write-Host ""
Write-Host "4. Instala en tu celular:" -ForegroundColor White
Write-Host '   adb install -r app\build\outputs\apk\debug\app-debug.apk' -ForegroundColor Gray
Write-Host ""
Write-Host "¡Listo! 🎉" -ForegroundColor Green
Write-Host ""

# Preguntar si desea desactivar el firewall
Write-Host "¿Deseas desactivar temporalmente el firewall? (S/N): " -ForegroundColor Yellow -NoNewline
$respuesta = Read-Host

if ($respuesta -eq "S" -or $respuesta -eq "s") {
    Write-Host ""
    Write-Host "Desactivando firewall..." -ForegroundColor Yellow
    try {
        Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
        Write-Host "✅ Firewall desactivado temporalmente" -ForegroundColor Green
        Write-Host ""
        Write-Host "⚠️  Recuerda volver a activarlo después:" -ForegroundColor Red
        Write-Host "   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True" -ForegroundColor White
    } catch {
        Write-Host "❌ Error: Ejecuta PowerShell como Administrador" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
