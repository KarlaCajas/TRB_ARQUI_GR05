# 🌐 Configuración para Acceso en Red Local

## 📍 Información de la Red

**IP del Servidor:** `192.168.18.113`
**Puerto del Servidor:** `8080`

## 🔗 URLs de Acceso

### Desde localhost (tu PC):
```
http://localhost:8080/WS_ConersionUnidades_RESTFULL/webresources
```

### Desde otros dispositivos en la red (Android, móviles, otras PCs):
```
http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources
```

## 📱 Para Emulador de Android Studio:

### AVD (Android Virtual Device - Emulador estándar):
```
http://10.0.2.2:8080/WS_ConersionUnidades_RESTFULL/webresources
```
**Nota:** `10.0.2.2` es la IP especial que el emulador usa para referirse al localhost de tu PC.

### Genymotion (si lo usas):
```
http://10.0.3.2:8080/WS_ConersionUnidades_RESTFULL/webresources
```

### Dispositivo Android Físico conectado a la misma WiFi:
```
http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources
```

## ✅ Verificación

### Verificar que el servidor esté escuchando en todas las interfaces:

1. El servidor Payara/GlassFish debe estar configurado para escuchar en `0.0.0.0` (todas las interfaces)
2. Esto ya está configurado por defecto en Payara

### Probar la conexión desde otro dispositivo:

Abre un navegador en tu teléfono o en el emulador y navega a:
```
http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources/application.wadl
```

Deberías ver el archivo WADL (descripción del servicio).

## 🔥 Configurar Firewall de Windows (si es necesario):

Si no puedes acceder desde otros dispositivos, ejecuta estos comandos en PowerShell como Administrador:

```powershell
# Permitir el puerto 8080 en el firewall
New-NetFirewallRule -DisplayName "Payara Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow
```

## 🎨 Endpoints de Conversión:

### Longitud:
- `GET /conversion/pulgadas-a-cm/{valor}`
- `GET /conversion/cm-a-pulgadas/{valor}`
- `GET /conversion/km-a-m/{valor}`
- `GET /conversion/m-a-cm/{valor}`
- `GET /conversion/cm-a-mm/{valor}`

### Temperatura:
- `GET /conversion/celsius-a-fahrenheit/{valor}`
- `GET /conversion/fahrenheit-a-celsius/{valor}`
- `GET /conversion/celsius-a-kelvin/{valor}`

### Masa:
- `GET /conversion/kg-a-gramos/{valor}`
- `GET /conversion/gramos-a-miligramos/{valor}`
- `GET /conversion/toneladas-a-kg/{valor}`

## 📝 Ejemplo de Uso en Android:

```java
// URL para el emulador AVD
String BASE_URL = "http://10.0.2.2:8080/WS_ConersionUnidades_RESTFULL/webresources";

// URL para dispositivo físico en la misma red
// String BASE_URL = "http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources";

// Ejemplo de petición
String endpoint = BASE_URL + "/conversion/celsius-a-fahrenheit/25";
```

## 🎯 Credenciales:
- **Usuario:** MONSTER
- **Contraseña:** Monster9

## 🌈 Colores del tema Sullivan (para Android):

```xml
<!-- Sullivan Blue Scheme -->
<color name="sullivan_primary">#4A90E2</color>
<color name="sullivan_primary_dark">#2E5C8A</color>
<color name="sullivan_accent">#64B5F6</color>
<color name="sullivan_background">#E8F4F8</color>
<color name="sullivan_text">#1E3A5F</color>
<color name="sullivan_light">#B3D9F2</color>
<color name="sullivan_white">#FFFFFF</color>
<color name="sullivan_green">#27AE60</color>
<color name="sullivan_orange">#FF9800</color>
<color name="sullivan_red">#E74C3C</color>
```
