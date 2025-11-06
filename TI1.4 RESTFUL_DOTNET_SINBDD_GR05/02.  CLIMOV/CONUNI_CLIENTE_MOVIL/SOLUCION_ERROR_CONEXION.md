# 🔧 Solución al Error de Conexión

## ❌ Error que ves:
```
Error: failed to connect to /192.168.10.104 (port 5014) from /192...
```

Este error significa que **la app no puede conectarse al servidor**.

---

## ✅ Solución Paso a Paso

### 1️⃣ Verificar que el Servidor esté Ejecutándose

**En tu PC, abre PowerShell/CMD y ejecuta:**

```powershell
cd TuProyectoServidor
dotnet run --urls "http://0.0.0.0:5014"
```

**Deberías ver algo como:**
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://0.0.0.0:5014
info: Microsoft.Hosting.Lifetime[0]
      Application started.
```

**Si ves esto, ¡el servidor está corriendo! ✅**

---

### 2️⃣ Probar el Servidor desde tu PC

**Abre el navegador en tu PC y visita:**
```
http://localhost:5014/api/ConversionUnidades_Controlador
```

O prueba con PowerShell:
```powershell
$body = @{
    tipoConversion = "Temperatura"
    unidadOrigen = "Celsius"
    unidadDestino = "Fahrenheit"
    valor = 25
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5014/api/ConversionUnidades_Controlador" -Method Post -Body $body -ContentType "application/json"
```

**Si funciona, deberías ver:**
```
resultado  mensaje                  exito
---------  -------                  -----
     77.0  Conversión exitosa        True
```

---

### 3️⃣ Verificar tu IP Actual

Tu IP puede haber cambiado. **Verifica con:**

```powershell
ipconfig
```

**Busca:**
```
Adaptador de LAN inalámbrica Wi-Fi:
   Dirección IPv4. . . . . . . . . . : 192.168.10.104
```

**⚠️ Si tu IP cambió:**

1. Anota la nueva IP (ejemplo: `192.168.10.105`)
2. Edita `ApiService.java` línea 22:
   ```java
   private static final String BASE_URL = "http://192.168.10.105:5014/api/ConversionUnidades_Controlador";
   ```
3. También edita `network_security_config.xml`:
   ```xml
   <domain includeSubdomains="true">192.168.10.105</domain>
   ```
4. Recompila el APK:
   ```powershell
   .\gradlew assembleDebug
   ```

---

### 4️⃣ Desactivar el Firewall (Temporal)

El firewall de Windows puede estar bloqueando la conexión.

**Ejecuta PowerShell como Administrador:**

```powershell
# Desactivar firewall temporalmente
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

**Después de probar, vuelve a activarlo:**
```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

**O crea una regla permanente:**
1. Abre "Firewall de Windows Defender con seguridad avanzada"
2. Clic en "Reglas de entrada" → "Nueva regla..."
3. Tipo: Puerto → TCP → 5014
4. Acción: Permitir la conexión
5. Perfil: Todos
6. Nombre: "DotNet API Port 5014"

---

### 5️⃣ Verificar que estén en la Misma Red WiFi

**Tu PC y tu celular DEBEN estar conectados a la MISMA red WiFi.**

**En tu PC:**
```powershell
ipconfig
```
Busca: `Adaptador de LAN inalámbrica Wi-Fi`

**En tu celular:**
- Ajustes → WiFi
- Verifica que estés conectado a: **repeater.com** (o la misma red que tu PC)

---

### 6️⃣ Probar desde tu Celular (Navegador)

**Antes de usar la app, prueba desde el navegador de tu celular:**

Abre el navegador y visita:
```
http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

**Si ves un JSON o algún mensaje, ¡la conexión funciona! ✅**

**Si no carga o da timeout:**
- ❌ El firewall está bloqueando
- ❌ No están en la misma red
- ❌ El servidor no está escuchando en 0.0.0.0

---

## 🎯 Checklist de Verificación

Marca cada paso:

- [ ] **Servidor ejecutándose** con `dotnet run --urls "http://0.0.0.0:5014"`
- [ ] **Servidor responde en PC** (probar con navegador en `localhost:5014`)
- [ ] **IP correcta** (verificar con `ipconfig`)
- [ ] **IP actualizada** en `ApiService.java` y `network_security_config.xml`
- [ ] **Firewall desactivado** o regla creada
- [ ] **Misma red WiFi** (PC y celular)
- [ ] **Servidor responde desde celular** (probar en navegador del celular)
- [ ] **APK actualizado** (recompilado después de cambiar IP)

---

## 🔄 Comandos Rápidos

### Verificar IP:
```powershell
ipconfig | Select-String "IPv4"
```

### Iniciar Servidor:
```powershell
cd "C:\TuProyectoServidor"
dotnet run --urls "http://0.0.0.0:5014"
```

### Probar Servidor:
```powershell
curl http://localhost:5014/api/ConversionUnidades_Controlador
```

### Recompilar APK:
```powershell
cd "c:\Users\karly\Documents\VIII SEMESTRE\Arquitectura\ejemplos\REST_SIN_BDD_DOTNET_GR09\REST_SIN_BDD_DOTNET_GR09\CONUNI_CLIENTE_MOVIL"
$env:JAVA_HOME = "C:\Program Files\Java\jdk-21"
.\gradlew clean assembleDebug
```

### Reinstalar APK:
```powershell
adb install -r app\build\outputs\apk\debug\app-debug.apk
```

---

## 🆘 Errores Comunes

### Error: "Connection refused"
**Causa:** Servidor no está ejecutándose  
**Solución:** Ejecuta `dotnet run --urls "http://0.0.0.0:5014"`

### Error: "Timeout"
**Causa:** Firewall bloqueando o diferente red WiFi  
**Solución:** Desactiva firewall y verifica misma red

### Error: "Unknown host"
**Causa:** IP incorrecta en la app  
**Solución:** Actualiza IP en `ApiService.java`

### Error: "Cannot assign requested address"
**Causa:** Servidor escuchando en 127.0.0.1 en lugar de 0.0.0.0  
**Solución:** Usa `--urls "http://0.0.0.0:5014"`

---

## 📝 Configuración del Servidor .NET (Importante)

Asegúrate de que tu `Program.cs` tenga CORS habilitado:

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

app.UseCors(); // ⚠️ IMPORTANTE: Antes de UseAuthorization
app.UseAuthorization();
app.MapControllers();

app.Run();
```

---

## ✅ Después de Solucionar

Una vez que funcione:

1. **Prueba una conversión:**
   - Login: MONSTER / Monster 9
   - Temperatura → Celsius a Fahrenheit
   - Valor: 25
   - Resultado esperado: 77°F

2. **Si funciona, todo está bien! 🎉**

3. **Para no tener este problema otra vez:**
   - Mantén siempre tu PC en la misma red WiFi
   - O configura una IP estática en tu PC
   - O usa el servidor en la nube (más avanzado)

---

## 🌐 Alternativa: Usar Emulador

Si tienes muchos problemas con el dispositivo físico, usa el emulador:

1. En `ApiService.java` cambia la IP a:
   ```java
   private static final String BASE_URL = "http://10.0.2.2:5014/api/ConversionUnidades_Controlador";
   ```

2. `10.0.2.2` es la IP especial que el emulador usa para acceder a `localhost` de tu PC

3. Recompila y ejecuta en el emulador

---

## 📞 Necesitas Ayuda?

Si después de seguir todos los pasos no funciona:

1. **Muestra el error exacto** que aparece
2. **Verifica:**
   - ¿El servidor está corriendo? (captura de pantalla)
   - ¿Qué dice `ipconfig`? (tu IP actual)
   - ¿Funciona en el navegador de tu celular?
3. **Intenta con el emulador** primero

---

¡Sigue estos pasos en orden y tu app funcionará! 🚀
