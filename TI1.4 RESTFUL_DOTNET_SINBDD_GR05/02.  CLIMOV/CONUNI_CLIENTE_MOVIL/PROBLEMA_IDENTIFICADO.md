# ⚠️ PROBLEMA IDENTIFICADO

## ❌ El servidor NO está ejecutándose

He probado conectarme a tu servidor en `http://192.168.10.104:5014` y **no responde**.

---

## ✅ SOLUCIÓN (Sigue estos pasos EN ORDEN)

### Paso 1: Inicia tu Servidor .NET ⚡

**Abre una nueva ventana de PowerShell y ejecuta:**

```powershell
# Navega a tu proyecto del servidor
cd "C:\ruta\a\tu\proyecto\servidor"

# Ejecuta el servidor
dotnet run --urls "http://0.0.0.0:5014"
```

**Debes ver algo como:**
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://0.0.0.0:5014
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
```

⚠️ **IMPORTANTE:** Deja esta ventana abierta. El servidor debe estar ejecutándose todo el tiempo que uses la app.

---

### Paso 2: Verifica que el Servidor Funciona 🧪

**En OTRA ventana de PowerShell, ejecuta:**

```powershell
Invoke-WebRequest -Uri "http://localhost:5014/api/ConversionUnidades_Controlador" -Method Get
```

**Si ves un código de respuesta 200 o algún contenido, ¡funciona! ✅**

---

### Paso 3: Prueba una Conversión desde PowerShell 🧮

```powershell
$body = @{
    tipoConversion = "Temperatura"
    unidadOrigen = "Celsius"
    unidadDestino = "Fahrenheit"
    valor = 25
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5014/api/ConversionUnidades_Controlador" -Method Post -Body $body -ContentType "application/json"
```

**Deberías ver:**
```
resultado mensaje              exito
--------- -------              -----
     77.0 Conversión exitosa    True
```

---

### Paso 4: Desactiva el Firewall (Temporal) 🔥

**Ejecuta PowerShell como ADMINISTRADOR:**

```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

Después de probar, vuelve a activarlo:
```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

---

### Paso 5: Instala el Nuevo APK en tu Celular 📱

```powershell
cd "c:\Users\karly\Documents\VIII SEMESTRE\Arquitectura\ejemplos\REST_SIN_BDD_DOTNET_GR09\REST_SIN_BDD_DOTNET_GR09\CONUNI_CLIENTE_MOVIL"

adb install -r app\build\outputs\apk\debug\app-debug.apk
```

---

### Paso 6: Prueba la App 🎯

1. Abre la app en tu celular
2. Login: `MONSTER` / `Monster 9`
3. Selecciona "Temperatura"
4. Selecciona "Celsius a Fahrenheit"
5. Ingresa: `25`
6. Presiona "CONVERTIR"
7. Deberías ver: **77.0 Fahrenheit** ✅

---

## 🔍 ¿Por qué se demora mucho?

El timeout es ahora de **5 segundos** (antes era 10). Si se demora:

1. **Servidor no responde** - Verifica que esté ejecutándose
2. **Firewall bloquea** - Desactívalo temporalmente
3. **Red diferente** - Ambos deben estar en la misma WiFi

---

## 💡 Mensajes de Error Mejorados

Ahora la app te dirá exactamente qué pasó:

- ❌ **"Tiempo de espera agotado"** → Servidor no responde a tiempo
- ❌ **"No se puede conectar al servidor"** → Servidor apagado o firewall bloqueando
- ❌ **"No se encuentra el servidor"** → IP incorrecta

---

## 📋 Checklist Final

Antes de usar la app, verifica:

- [ ] ✅ Servidor ejecutándose (ventana de PowerShell abierta)
- [ ] ✅ Servidor responde en localhost (probado con PowerShell)
- [ ] ✅ Firewall desactivado temporalmente
- [ ] ✅ PC y celular en la misma red WiFi (192.168.10.x)
- [ ] ✅ APK actualizado instalado en el celular

---

## 🚀 Comando Todo-en-Uno

**Para probar rápidamente si el servidor funciona:**

```powershell
# Probar GET
try { 
    $r = Invoke-WebRequest -Uri "http://192.168.10.104:5014/api/ConversionUnidades_Controlador" -Method Get -TimeoutSec 3
    Write-Host "✅ Servidor OK!" -ForegroundColor Green
} catch { 
    Write-Host "❌ Servidor NO responde - Inícialo con:" -ForegroundColor Red
    Write-Host 'dotnet run --urls "http://0.0.0.0:5014"' -ForegroundColor Yellow
}
```

---

## 📖 Archivos de Ayuda

- **`SOLUCION_ERROR_CONEXION.md`** - Guía completa para resolver errores
- **`probar-servidor.ps1`** - Script automático para probar el servidor
- **`CONFIGURACION_SERVIDOR.md`** - Cómo configurar el servidor .NET

---

¡Sigue estos pasos y tu app funcionará perfectamente! 🎉

**Recuerda: El servidor SIEMPRE debe estar ejecutándose para que la app funcione.**
