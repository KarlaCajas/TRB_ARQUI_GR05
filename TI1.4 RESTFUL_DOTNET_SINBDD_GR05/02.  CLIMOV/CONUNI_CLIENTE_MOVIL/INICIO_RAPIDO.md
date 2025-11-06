# 🚀 Guía Rápida de Inicio

## Pasos para ejecutar la aplicación

### 1️⃣ Preparar el Servidor .NET

1. Abre tu proyecto del servidor REST en Visual Studio o VS Code
2. Copia el código del archivo `SERVIDOR_DOTNET_CODIGO.cs` a tu controlador
3. Configura CORS (ver archivo `CONFIGURACION_SERVIDOR.md`)
4. Ejecuta el servidor:
   ```bash
   dotnet run --urls "http://0.0.0.0:5014"
   ```
5. Verifica que esté ejecutándose abriendo en el navegador:
   ```
   http://localhost:5014/api/ConversionUnidades_Controlador
   ```

### 2️⃣ Configurar el Cliente Android

1. Abre el proyecto en Android Studio
2. Espera a que Gradle sincronice automáticamente
3. Si hay errores, haz clic en: `File` → `Sync Project with Gradle Files`

### 3️⃣ Verificar la Configuración de Red

**Tu IP actual:** `192.168.10.104`

Verifica que estos archivos tengan tu IP correcta:

**Archivo 1:** `app/src/main/java/ec/edu/monster/controlador/ApiService.java`
```java
private static final String BASE_URL = "http://192.168.10.104:5014/api/ConversionUnidades_Controlador";
```

**Archivo 2:** `app/src/main/res/xml/network_security_config.xml`
```xml
<domain includeSubdomains="true">192.168.10.104</domain>
```

### 4️⃣ Ejecutar la Aplicación

**Opción A: Dispositivo Físico (Recomendado)**
1. Conecta tu celular por USB
2. Activa "Depuración USB" en Opciones de Desarrollador
3. Asegúrate de que tu celular esté en el MISMO WiFi que tu PC
4. En Android Studio: `Run` → `Run 'app'`
5. Selecciona tu dispositivo

**Opción B: Emulador Android**
1. Si usas emulador, cambia la IP en `ApiService.java`:
   ```java
   private static final String BASE_URL = "http://10.0.2.2:5014/api/ConversionUnidades_Controlador";
   ```
2. En Android Studio: `Run` → `Run 'app'`
3. Selecciona el emulador

### 5️⃣ Probar la Aplicación

1. **Login:**
   - Usuario: `MONSTER`
   - Contraseña: `Monster 9`

2. **Selecciona una categoría:**
   - Temperatura
   - Masa
   - Longitud

3. **Realiza una conversión:**
   - Selecciona el tipo de conversión
   - Ingresa un valor
   - Presiona "CONVERTIR"
   - Ve el resultado

4. **Navega:**
   - Usa el botón "VOLVER AL MENÚ" para regresar
   - Usa "CERRAR SESIÓN" para salir

---

## 🔥 Solución Rápida de Problemas

### ❌ Error: "Unable to resolve host" o "Connection refused"

**Solución 1: Verificar que el servidor esté ejecutándose**
```bash
# En PowerShell/CMD en tu PC
curl http://localhost:5014/api/ConversionUnidades_Controlador
```

**Solución 2: Desactivar Firewall temporalmente**
```powershell
# PowerShell como Administrador
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

**Solución 3: Verificar que ambos estén en la misma red WiFi**
- Tu PC debe estar conectada a: `repeater.com` (192.168.10.104)
- Tu celular debe estar en la MISMA red WiFi

### ❌ Error: "Failed to connect to /192.168.10.104:5014"

La IP puede haber cambiado. Verifica tu IP actual:
```bash
ipconfig
```

Busca: `Adaptador de LAN inalámbrica Wi-Fi` → `Dirección IPv4`

Si cambió, actualiza:
1. `ApiService.java` (línea 17)
2. `network_security_config.xml`

### ❌ Build Error: "Cannot resolve symbol"

1. `File` → `Invalidate Caches` → `Invalidate and Restart`
2. Espera que Gradle sincronice

### ❌ El servidor responde pero la app no muestra resultado

Verifica que tu servidor .NET retorne exactamente este formato JSON:
```json
{
    "resultado": 77.0,
    "mensaje": "Conversión exitosa",
    "exito": true
}
```

Los nombres deben ser **exactamente** esos (en minúsculas).

---

## ✅ Checklist Antes de Ejecutar

- [ ] Servidor .NET ejecutándose en puerto 5014
- [ ] PC y celular en la misma red WiFi (192.168.10.x)
- [ ] IP correcta en `ApiService.java` y `network_security_config.xml`
- [ ] Firewall desactivado o con regla para puerto 5014
- [ ] Gradle sincronizado en Android Studio
- [ ] USB Debugging activado (si usas dispositivo físico)

---

## 📱 Credenciales

**Usuario:** MONSTER  
**Contraseña:** Monster 9

---

## 🎯 URLs Importantes

**Servidor local (desde PC):**
```
http://localhost:5014/api/ConversionUnidades_Controlador
```

**Servidor desde celular:**
```
http://192.168.10.104:5014/api/ConversionUnidades_Controlador
```

**Servidor desde emulador:**
```
http://10.0.2.2:5014/api/ConversionUnidades_Controlador
```

---

## 🔄 Conversiones Disponibles

### Temperatura
- ✅ Celsius → Fahrenheit
- ✅ Fahrenheit → Celsius
- ✅ Celsius → Kelvin

### Masa
- ✅ Kilogramos → Gramos
- ✅ Gramos → Miligramos
- ✅ Toneladas → Kilogramos

### Longitud
- ✅ Kilómetros → Metros
- ✅ Metros → Centímetros
- ✅ Centímetros → Milímetros

---

## 🎨 Características de la App

✅ Login con validación  
✅ Menú con 3 categorías con iconos  
✅ Conversiones dinámicas  
✅ Resultados con formato claro  
✅ Botón de volver en cada pantalla  
✅ Cerrar sesión vuelve al login  
✅ Diseño moderno con Material Design  
✅ Colores y gradientes atractivos  
✅ Feedback visual (ProgressBar)  
✅ Manejo de errores  

---

¡Listo! Tu aplicación está completamente configurada y lista para funcionar! 🎉
