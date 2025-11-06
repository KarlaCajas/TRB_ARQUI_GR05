# Cliente Móvil Android - Conversor de Unidades

## 📱 Descripción
Aplicación móvil Android que se conecta a un servidor REST en .NET para realizar conversiones de unidades.

## 🔐 Credenciales de Login
- **Usuario:** MONSTER
- **Contraseña:** Monster 9

## 🔄 Conversiones Soportadas

### Temperatura
- Celsius a Fahrenheit (C → F)
- Fahrenheit a Celsius (F → C)
- Celsius a Kelvin (C → K)

### Masa
- Kilogramos a Gramos (kg → g)
- Gramos a Miligramos (g → mg)
- Toneladas a Kilogramos (t → kg)

### Longitud
- Kilómetros a Metros (km → m)
- Metros a Centímetros (m → cm)
- Centímetros a Milímetros (cm → mm)

## 🌐 Configuración del Servidor

### URL del Servidor
El archivo `ApiService.java` está configurado para usar:
```
http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

### Cambiar la URL del Servidor
Si necesitas cambiar la IP, edita el archivo:
`app/src/main/java/ec/edu/monster/controlador/ApiService.java`

Línea 17:
```java
private static final String BASE_URL = "http://192.168.10.104:5014/api/ConversionUnidades_Controlador";
```

### Para usar con Emulador Android
Si usas el emulador de Android Studio, usa `10.0.2.2` en lugar de `localhost`:
```java
private static final String BASE_URL = "http://10.0.2.2:5014/api/ConversionUnidades_Controlador";
```

## 📋 Formato de la API REST (Servidor .NET)

### Endpoint
```
POST http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

### Request Body (JSON)
```json
{
    "tipoConversion": "Temperatura",
    "unidadOrigen": "Celsius",
    "unidadDestino": "Fahrenheit",
    "valor": 25.0
}
```

### Response Body (JSON)
```json
{
    "resultado": 77.0,
    "mensaje": "Conversión exitosa",
    "exito": true
}
```

## 🎨 Estructura de la Aplicación

### Pantallas
1. **LoginActivity** - Pantalla de inicio de sesión
2. **MainActivity** - Menú principal con 3 categorías
3. **TransformacionesActivity** - Pantalla de conversión

### Paquetes
- `ec.edu.monster.vista` - Actividades (UI)
- `ec.edu.monster.modelo` - Modelos de datos
- `ec.edu.monster.controlador` - Servicios y lógica

## 🚀 Cómo Ejecutar

### Requisitos
- Android Studio
- SDK de Android (API 24 o superior)
- Servidor REST .NET ejecutándose en `http://192.168.10.104:5014`

### Pasos
1. Abre el proyecto en Android Studio
2. Sincroniza Gradle (Sync Now)
3. Asegúrate de que tu servidor .NET esté ejecutándose
4. Verifica que tu dispositivo/emulador pueda acceder a la IP del servidor
5. Ejecuta la aplicación (Run > Run 'app')

### Probar Conectividad
Desde el dispositivo/emulador, abre el navegador y accede a:
```
http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

Si ves una respuesta o error del servidor, la conexión está funcionando.

## 🔧 Configuración del Servidor .NET

### Valores de Unidades Esperados por el Servidor

#### Temperatura
- `"Celsius"`, `"Fahrenheit"`, `"Kelvin"`

#### Masa
- `"Kilogramos"`, `"Gramos"`, `"Miligramos"`, `"Toneladas"`

#### Longitud
- `"Kilómetros"`, `"Metros"`, `"Centímetros"`, `"Milímetros"`

### Ejemplo de Controlador .NET (C#)

```csharp
[ApiController]
[Route("api/[controller]")]
public class ConversionUnidades_Controlador : ControllerBase
{
    [HttpPost]
    public IActionResult ConvertirUnidades([FromBody] ConversionRequest request)
    {
        try
        {
            double resultado = 0;
            
            // Conversiones de Temperatura
            if (request.TipoConversion == "Temperatura")
            {
                if (request.UnidadOrigen == "Celsius" && request.UnidadDestino == "Fahrenheit")
                    resultado = (request.Valor * 9/5) + 32;
                else if (request.UnidadOrigen == "Fahrenheit" && request.UnidadDestino == "Celsius")
                    resultado = (request.Valor - 32) * 5/9;
                else if (request.UnidadOrigen == "Celsius" && request.UnidadDestino == "Kelvin")
                    resultado = request.Valor + 273.15;
            }
            // Conversiones de Masa
            else if (request.TipoConversion == "Masa")
            {
                if (request.UnidadOrigen == "Kilogramos" && request.UnidadDestino == "Gramos")
                    resultado = request.Valor * 1000;
                else if (request.UnidadOrigen == "Gramos" && request.UnidadDestino == "Miligramos")
                    resultado = request.Valor * 1000;
                else if (request.UnidadOrigen == "Toneladas" && request.UnidadDestino == "Kilogramos")
                    resultado = request.Valor * 1000;
            }
            // Conversiones de Longitud
            else if (request.TipoConversion == "Longitud")
            {
                if (request.UnidadOrigen == "Kilómetros" && request.UnidadDestino == "Metros")
                    resultado = request.Valor * 1000;
                else if (request.UnidadOrigen == "Metros" && request.UnidadDestino == "Centímetros")
                    resultado = request.Valor * 100;
                else if (request.UnidadOrigen == "Centímetros" && request.UnidadDestino == "Milímetros")
                    resultado = request.Valor * 10;
            }
            
            return Ok(new ConversionResponse
            {
                Resultado = resultado,
                Mensaje = "Conversión exitosa",
                Exito = true
            });
        }
        catch (Exception ex)
        {
            return BadRequest(new ConversionResponse
            {
                Resultado = 0,
                Mensaje = ex.Message,
                Exito = false
            });
        }
    }
}

public class ConversionRequest
{
    public string TipoConversion { get; set; }
    public string UnidadOrigen { get; set; }
    public string UnidadDestino { get; set; }
    public double Valor { get; set; }
}

public class ConversionResponse
{
    public double Resultado { get; set; }
    public string Mensaje { get; set; }
    public bool Exito { get; set; }
}
```

### Configurar CORS en .NET (Program.cs o Startup.cs)

```csharp
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

// ...

app.UseCors();
```

## 🐛 Solución de Problemas

### Error de Conexión
1. Verifica que el servidor .NET esté ejecutándose
2. Verifica que ambos dispositivos estén en la misma red WiFi
3. Desactiva el firewall temporalmente en tu PC
4. Verifica la IP con `ipconfig` en Windows

### Error 404
- Verifica que la URL del endpoint sea correcta
- Verifica que el controlador en .NET tenga la ruta correcta

### Error de JSON
- Verifica que los nombres de las propiedades coincidan exactamente (mayúsculas/minúsculas)
- En .NET, usa `[JsonPropertyName("propiedad")]` si es necesario

## 📱 Capturas de Pantalla
La aplicación incluye:
- ✅ Login con validación
- ✅ Menú principal con cards coloridas
- ✅ Conversiones dinámicas según categoría
- ✅ Resultados claros con iconos
- ✅ Botón de volver y cerrar sesión
- ✅ Diseño moderno con Material Design

## 👨‍💻 Autor
Desarrollado para el curso de Arquitectura - VIII Semestre
