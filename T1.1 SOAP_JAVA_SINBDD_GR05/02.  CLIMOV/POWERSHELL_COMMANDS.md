# 🔧 Comandos Útiles para Windows PowerShell

## 📡 Verificar Servicio SOAP

### Ver tu IP local
```powershell
ipconfig | Select-String -Pattern "IPv4"
```

### Probar conexión al servicio desde PowerShell
```powershell
# Probar si el servicio está escuchando
Test-NetConnection -ComputerName localhost -Port 8080

# Descargar el WSDL
Invoke-WebRequest -Uri "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl" -OutFile "servicio.wsdl"

# Ver el WSDL en pantalla
(Invoke-WebRequest -Uri "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl").Content
```

## 🔥 Configurar Firewall

### Agregar regla para permitir puerto 8080
```powershell
# Como Administrador
New-NetFirewallRule -DisplayName "SOAP Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow
```

### Verificar si la regla existe
```powershell
Get-NetFirewallRule -DisplayName "SOAP Server 8080"
```

### Ver todas las reglas del puerto 8080
```powershell
Get-NetFirewallPortFilter | Where-Object LocalPort -eq 8080 | Get-NetFirewallRule
```

### Eliminar la regla (si necesitas)
```powershell
Remove-NetFirewallRule -DisplayName "SOAP Server 8080"
```

### Desactivar temporalmente el firewall (NO RECOMENDADO)
```powershell
# Como Administrador - solo para pruebas
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

# Reactivar después
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

## 📱 Android Debug Bridge (ADB)

### Verificar si tu dispositivo está conectado
```powershell
# Si tienes Android SDK instalado
adb devices
```

### Ver logs del dispositivo en tiempo real
```powershell
adb logcat | Select-String -Pattern "SOAPClient"
```

### Instalar APK manualmente
```powershell
adb install -r "ruta\a\tu\app.apk"
```

### Ver IP del dispositivo Android
```powershell
adb shell ip addr show wlan0
```

## 🌐 Red y Conectividad

### Ver todas las interfaces de red con sus IPs
```powershell
Get-NetIPAddress -AddressFamily IPv4 | Select-Object InterfaceAlias, IPAddress
```

### Ver configuración de red completa
```powershell
Get-NetIPConfiguration
```

### Hacer ping a tu dispositivo Android (si conoces su IP)
```powershell
Test-Connection -ComputerName 192.168.1.XXX -Count 4
```

### Ver puertos abiertos en tu PC
```powershell
Get-NetTCPConnection -LocalPort 8080 -State Listen
```

### Ver todos los puertos en escucha
```powershell
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"} | Select-Object LocalPort, OwningProcess | Sort-Object LocalPort
```

## 📂 Gestión de Proyecto

### Navegar a la carpeta del proyecto
```powershell
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"
```

### Ver estructura del proyecto
```powershell
tree /F
```

### Buscar archivos Java
```powershell
Get-ChildItem -Recurse -Filter "*.java" | Select-Object FullName
```

### Contar líneas de código
```powershell
(Get-Content -Path "app\src\main\java\com\gr05\conuniclient\*.java" | Measure-Object -Line).Lines
```

### Abrir Android Studio desde PowerShell
```powershell
# Si está en el PATH
studio .

# O ruta completa (ajusta según tu instalación)
& "C:\Program Files\Android\Android Studio\bin\studio64.exe" .
```

## 🛠️ Gradle (si tienes Gradle instalado)

### Limpiar proyecto
```powershell
.\gradlew clean
```

### Compilar proyecto
```powershell
.\gradlew build
```

### Compilar e instalar en dispositivo conectado
```powershell
.\gradlew installDebug
```

### Ver dependencias
```powershell
.\gradlew dependencies
```

## 🔍 Debugging y Troubleshooting

### Ver procesos usando el puerto 8080
```powershell
Get-Process -Id (Get-NetTCPConnection -LocalPort 8080).OwningProcess
```

### Matar proceso que usa el puerto 8080
```powershell
# Obtener el PID
$pid = (Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue).OwningProcess
if ($pid) {
    Stop-Process -Id $pid -Force
    Write-Host "Proceso $pid terminado"
} else {
    Write-Host "No hay proceso usando el puerto 8080"
}
```

### Ver logs del sistema
```powershell
Get-EventLog -LogName System -Newest 50 | Where-Object {$_.Source -like "*Firewall*"}
```

### Verificar conectividad a una IP específica y puerto
```powershell
Test-NetConnection -ComputerName 192.168.1.5 -Port 8080 -InformationLevel Detailed
```

## 📦 Gestión de APK

### Crear APK debug desde línea de comandos
```powershell
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"
.\gradlew assembleDebug
```

### Ubicación del APK generado
```powershell
# Usualmente está en:
Get-Item "app\build\outputs\apk\debug\*.apk"
```

### Copiar APK al escritorio
```powershell
Copy-Item "app\build\outputs\apk\debug\app-debug.apk" "$env:USERPROFILE\Desktop\CONUNIClient.apk"
```

## 🔄 Git (si usas control de versiones)

### Inicializar repositorio
```powershell
git init
```

### Ver estado
```powershell
git status
```

### Agregar todos los archivos
```powershell
git add .
```

### Hacer commit
```powershell
git commit -m "Cliente Android SOAP inicial"
```

## 💡 Tips Útiles

### Crear alias para comandos comunes
```powershell
# Agregar a tu perfil de PowerShell
Set-Alias -Name testsoap -Value {Test-NetConnection -ComputerName localhost -Port 8080}
```

### Ver tu perfil de PowerShell
```powershell
notepad $PROFILE
```

### Recargar perfil sin cerrar PowerShell
```powershell
. $PROFILE
```

## 🎯 Script de Verificación Completo

Copia y pega este script para verificar todo:

```powershell
Write-Host "=== Verificación del Entorno SOAP Client Android ===" -ForegroundColor Green

Write-Host "`n1. Verificando IP local..." -ForegroundColor Yellow
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*"} | Select-Object -First 1).IPAddress
Write-Host "   IP: $ip" -ForegroundColor Cyan

Write-Host "`n2. Verificando puerto 8080..." -ForegroundColor Yellow
$port = Get-NetTCPConnection -LocalPort 8080 -State Listen -ErrorAction SilentlyContinue
if ($port) {
    Write-Host "   ✓ Puerto 8080 está abierto" -ForegroundColor Green
} else {
    Write-Host "   ✗ Puerto 8080 no está en escucha" -ForegroundColor Red
}

Write-Host "`n3. Verificando regla de firewall..." -ForegroundColor Yellow
$rule = Get-NetFirewallRule -DisplayName "SOAP Server 8080" -ErrorAction SilentlyContinue
if ($rule) {
    Write-Host "   ✓ Regla de firewall existe" -ForegroundColor Green
} else {
    Write-Host "   ✗ Regla de firewall no configurada" -ForegroundColor Red
    Write-Host "   Ejecuta: New-NetFirewallRule -DisplayName 'SOAP Server 8080' -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow" -ForegroundColor Yellow
}

Write-Host "`n4. Verificando servicio SOAP..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl" -TimeoutSec 5 -UseBasicParsing
    Write-Host "   ✓ Servicio SOAP responde correctamente" -ForegroundColor Green
} catch {
    Write-Host "   ✗ No se puede acceder al servicio SOAP" -ForegroundColor Red
    Write-Host "   Asegúrate de que el servicio esté corriendo" -ForegroundColor Yellow
}

Write-Host "`n5. Verificando estructura del proyecto..." -ForegroundColor Yellow
$projectPath = "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"
if (Test-Path $projectPath) {
    Write-Host "   ✓ Proyecto existe en: $projectPath" -ForegroundColor Green
    
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
            Write-Host "   ✓ $file" -ForegroundColor Green
        } else {
            Write-Host "   ✗ Falta: $file" -ForegroundColor Red
        }
    }
} else {
    Write-Host "   ✗ Proyecto no encontrado" -ForegroundColor Red
}

Write-Host "`n=== Resumen ===" -ForegroundColor Green
Write-Host "IP para usar en dispositivo físico: $ip" -ForegroundColor Cyan
Write-Host "URL para emulador: http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI" -ForegroundColor Cyan
Write-Host "URL para dispositivo: http://${ip}:8080/ConUni_Soap_Java_GR05/CONUNI" -ForegroundColor Cyan
```

Guarda este script como `verificar-entorno.ps1` y ejecútalo:
```powershell
.\verificar-entorno.ps1
```

---

**Nota:** Algunos comandos requieren permisos de administrador. Abre PowerShell como administrador cuando sea necesario.
