# Configuración del Servidor .NET

## 📋 Instrucciones para configurar tu servidor REST en .NET

### 1. Configurar CORS en Program.cs

Agrega esto en tu archivo `Program.cs` (o `Startup.cs` si es .NET 5 o anterior):

```csharp
var builder = WebApplication.CreateBuilder(args);

// Agregar servicios
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// ✅ IMPORTANTE: Configurar CORS
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

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// ✅ IMPORTANTE: Usar CORS antes de Authorization
app.UseCors();

app.UseAuthorization();

app.MapControllers();

app.Run();
```

### 2. Configurar la URL para escuchar en todas las interfaces

En `Properties/launchSettings.json`, asegúrate de que tu aplicación escuche en todas las interfaces de red:

```json
{
  "profiles": {
    "TuProyecto": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "http://0.0.0.0:5014",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

O usa este comando para ejecutar tu servidor:
```bash
dotnet run --urls "http://0.0.0.0:5014"
```

### 3. Crear el Controlador

Crea un archivo llamado `ConversionUnidades_Controlador.cs` en la carpeta `Controllers` y copia el código del archivo `SERVIDOR_DOTNET_CODIGO.cs`.

### 4. Desactivar el Firewall de Windows (Temporalmente para pruebas)

**Opción 1: Agregar regla de firewall**
1. Abre "Firewall de Windows Defender con seguridad avanzada"
2. Clic en "Reglas de entrada"
3. Clic en "Nueva regla..."
4. Selecciona "Puerto" → Siguiente
5. Selecciona "TCP" y escribe "5014" → Siguiente
6. Selecciona "Permitir la conexión" → Siguiente
7. Marca todas las opciones → Siguiente
8. Dale un nombre como "DotNet API Port 5014" → Finalizar

**Opción 2: Desactivar temporalmente (Solo para pruebas)**
```powershell
# Ejecuta PowerShell como Administrador
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

Para volver a activar:
```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

### 5. Verificar la IP de tu PC

Abre PowerShell o CMD y ejecuta:
```bash
ipconfig
```

Busca tu IP en la sección "Adaptador de LAN inalámbrica Wi-Fi":
```
Dirección IPv4. . . . . . . . . . . . . . : 192.168.10.104
```

### 6. Ejecutar el Servidor

```bash
cd TuProyecto
dotnet run --urls "http://0.0.0.0:5014"
```

Deberías ver algo como:
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://0.0.0.0:5014
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
```

### 7. Probar el Servidor

**Desde tu PC (navegador):**
```
http://localhost:5014/api/ConversionUnidades_Controlador
```

**Desde tu celular (en el mismo WiFi):**
```
http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

**Usando PowerShell (POST):**
```powershell
$body = @{
    tipoConversion = "Temperatura"
    unidadOrigen = "Celsius"
    unidadDestino = "Fahrenheit"
    valor = 25
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5014/api/ConversionUnidades_Controlador" -Method Post -Body $body -ContentType "application/json"
```

**Usando cURL:**
```bash
curl -X POST http://localhost:5014/api/ConversionUnidades_Controlador \
  -H "Content-Type: application/json" \
  -d "{\"tipoConversion\":\"Temperatura\",\"unidadOrigen\":\"Celsius\",\"unidadDestino\":\"Fahrenheit\",\"valor\":25}"
```

### 8. Configurar la App Android

Si tu servidor está en:
```
http://192.168.10.104:5014
```

Entonces en el archivo `ApiService.java` debe estar:
```java
private static final String BASE_URL = "http://192.168.10.104:5014/api/ConversionUnidades_Controlador";
```

### 🔧 Solución de Problemas

#### Problema: "No connection could be made because the target machine actively refused it"
- ✅ Verifica que el servidor esté ejecutándose
- ✅ Verifica que esté escuchando en `0.0.0.0` o tu IP local
- ✅ Verifica el firewall

#### Problema: "Connection timed out"
- ✅ Ambos dispositivos deben estar en la misma red WiFi
- ✅ Verifica la IP con `ipconfig`
- ✅ Desactiva el firewall temporalmente

#### Problema: Error 404
- ✅ Verifica que la ruta del controlador sea correcta
- ✅ El nombre del controlador debe ser exactamente `ConversionUnidades_Controlador`

#### Problema: Error de CORS
- ✅ Asegúrate de haber configurado CORS en `Program.cs`
- ✅ `app.UseCors()` debe estar antes de `app.UseAuthorization()`

### 📝 Ejemplo Completo de Request/Response

**Request:**
```json
POST http://192.168.10.104:5014/api/ConversionUnidades_Controlador
Content-Type: application/json

{
    "tipoConversion": "Temperatura",
    "unidadOrigen": "Celsius",
    "unidadDestino": "Fahrenheit",
    "valor": 25.0
}
```

**Response (Éxito):**
```json
{
    "resultado": 77.0,
    "mensaje": "Conversión exitosa",
    "exito": true
}
```

**Response (Error):**
```json
{
    "resultado": 0.0,
    "mensaje": "Conversión no soportada: Celsius a Libras",
    "exito": false
}
```

### 🚀 Lista de Verificación

- [ ] CORS configurado en Program.cs
- [ ] Controlador creado con el nombre exacto
- [ ] Servidor ejecutándose con `--urls "http://0.0.0.0:5014"`
- [ ] Firewall desactivado o regla creada
- [ ] Ambos dispositivos en la misma red WiFi
- [ ] IP verificada con `ipconfig`
- [ ] API probada desde navegador
- [ ] Archivo `ApiService.java` tiene la IP correcta
- [ ] Archivo `network_security_config.xml` tiene la IP correcta

¡Tu servidor debería estar listo para funcionar con la app móvil! 🎉
