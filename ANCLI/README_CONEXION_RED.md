# 📱 Cliente Android - Conversiones MONSTER

Cliente Android nativo en Kotlin con Jetpack Compose para consumir el servicio web Flask.

## 🌐 Configuración de Red

### Tu IP Local Actual
```
192.168.18.113
```

### Configuración del Servidor Flask
El servidor ya está configurado para aceptar conexiones externas:
- `host='0.0.0.0'` permite conexiones desde cualquier dispositivo en la red
- Puerto: `5000`

### URL del Servicio
```
http://192.168.18.113:5000
```

## ⚙️ Configuración de la Aplicación Android

### 1. Archivo RetrofitClient.kt
La configuración cambia según dónde ejecutes la app:

**Para EMULADOR de Android:**
```kotlin
private const val BASE_URL = "http://10.0.2.2:5000/"
```
> 💡 `10.0.2.2` es una IP especial que el emulador usa para acceder al `localhost` de tu PC.

**Para CELULAR FÍSICO:**
```kotlin
private const val BASE_URL = "http://192.168.18.113:5000/"
```
> 💡 Usa tu IP real de la red local. Tu celular debe estar en la misma WiFi que tu PC.

### 2. Permisos en AndroidManifest.xml
✅ Ya agregados:
- `INTERNET` - Para realizar peticiones HTTP
- `ACCESS_NETWORK_STATE` - Para verificar conectividad
- `usesCleartextTraffic="true"` - Para permitir HTTP (no HTTPS)

### 3. Dependencias (build.gradle.kts)
✅ Ya agregadas:
- **Retrofit 2.9.0** - Cliente HTTP para Android
- **Gson Converter** - Para parsear JSON
- **OkHttp Logging Interceptor** - Para debug de peticiones
- **Coroutines** - Para llamadas asíncronas
- **ViewModel Compose** - Para manejo de estado

## 🚀 Pasos para Ejecutar

### En tu Computadora (Windows)

1. **Verifica tu IP** (si cambió):
   ```powershell
   ipconfig | Select-String -Pattern "IPv4"
   ```
   Anota la IPv4 que empiece con `192.168.x.x`

2. **Inicia el servidor SOAP .NET**:
   - Debe estar corriendo en `http://localhost:63393/Service.svc`

3. **Inicia el servidor Flask**:
   ```powershell
   cd "c:\ARQUITECTURA\TI1.2 SOAP_DOTNET_SINBDD_GRO#5\02.CLIWEB"
   python app.py
   ```
   
   Deberías ver:
   ```
   ✓ Servidor web iniciando en http://localhost:5000
   * Running on http://192.168.18.113:5000
   ```

4. **Verifica que el firewall permita conexiones** (solo si usas celular físico):
   ```powershell
   # Agregar regla para permitir puerto 5000
   New-NetFirewallRule -DisplayName "Flask Server" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
   ```

---

## 📱 OPCIÓN A: Usar Emulador de Android

### Ventajas
✅ No necesitas un dispositivo físico  
✅ Más fácil de depurar  
✅ No requiere configuración de red  

### Configuración

1. **Verifica la IP en RetrofitClient.kt**:
   ```kotlin
   private const val BASE_URL = "http://10.0.2.2:5000/"
   ```

2. **En Android Studio**:
   - Ve a `Tools → Device Manager`
   - Crea o selecciona un emulador (recomendado: Pixel 5 API 34)
   - Presiona ▶️ para iniciar el emulador

3. **Ejecuta la app**:
   - Click en el botón ▶️ Run
   - Selecciona tu emulador
   - Espera a que compile e instale

### Limitación
⚠️ El emulador no puede acceder directamente a IPs de tu red (192.168.x.x), por eso usamos `10.0.2.2`

---

## 📱 OPCIÓN B: Usar Celular Físico (Recomendado para pruebas reales)

### Ventajas
✅ Pruebas en dispositivo real  
✅ Mejor rendimiento  
✅ Puedes moverte libremente (sin cable USB después de la instalación)  

### Requisitos
1. Tu celular Android
2. Cable USB para conectar a la PC
3. Tu celular y PC en la **misma red WiFi**

### Pasos para Configurar

#### 1️⃣ Habilitar Opciones de Desarrollador en tu Celular

1. Ve a **Configuración** → **Acerca del teléfono**
2. Busca **Número de compilación** (o **Build number**)
3. Toca 7 veces sobre él
4. Verás el mensaje: "Ahora eres desarrollador"

#### 2️⃣ Activar Depuración USB

1. Ve a **Configuración** → **Sistema** → **Opciones de desarrollador**
2. Activa **Depuración USB**
3. (Opcional) Activa **Instalación por USB** para facilitar instalaciones

#### 3️⃣ Conectar tu Celular a Android Studio

1. **Conecta tu celular a la PC** con cable USB
2. En tu celular aparecerá: "¿Permitir depuración USB?"
   - Marca "Permitir siempre desde este equipo"
   - Toca **Permitir**
3. En **Android Studio**, deberías ver tu dispositivo en la lista desplegable de dispositivos

#### 4️⃣ Verificar que estén en la Misma Red WiFi

1. **En tu PC**:
   ```powershell
   ipconfig
   ```
   Anota tu IPv4 (ejemplo: `192.168.18.113`)

2. **En tu celular**:
   - Ve a **Configuración** → **WiFi**
   - Toca en la red conectada
   - Verifica que la IP empiece con el mismo rango (ejemplo: `192.168.18.x`)

#### 5️⃣ Actualizar la IP en RetrofitClient.kt

1. Abre el archivo:
   ```
   ANCLI/app/src/main/java/com/example/andcli/network/RetrofitClient.kt
   ```

2. **Cambia la IP de emulador a tu IP real**:
   ```kotlin
   // ANTES (para emulador):
   private const val BASE_URL = "http://10.0.2.2:5000/"
   
   // DESPUÉS (para celular físico):
   private const val BASE_URL = "http://192.168.18.113:5000/"
   ```
   > ⚠️ Usa TU IP real, no copies exactamente este ejemplo

3. **Guarda el archivo** (Ctrl + S)

#### 6️⃣ Probar la Conexión desde el Navegador

Antes de ejecutar la app, verifica que tu celular pueda alcanzar el servidor:

1. Abre **Chrome** (o cualquier navegador) en tu celular
2. Navega a: `http://192.168.18.113:5000`
3. Deberías ver la página de login del cliente web Flask
4. Si no carga, revisa:
   - ¿El servidor Flask está corriendo?
   - ¿Tu celular está en la misma WiFi?
   - ¿El firewall está bloqueando la conexión?

#### 7️⃣ Ejecutar la App en tu Celular

1. En **Android Studio**, haz clic en **Build → Rebuild Project**
2. Espera a que compile
3. Presiona el botón ▶️ **Run**
4. Selecciona tu dispositivo físico de la lista
5. Espera a que se instale y se abra la app

#### 8️⃣ Prueba la App

1. Ingresa las credenciales:
   - Usuario: `MONSTER`
   - Contraseña: `Monster9`
2. Selecciona una categoría (MASA, LONGITUD, TEMPERATURA)
3. Elige un tipo de conversión
4. Ingresa un valor y presiona "Convertir"

---

## 🔄 Cambiar entre Emulador y Celular Físico

### Para volver al Emulador:

1. Abre `RetrofitClient.kt`
2. Cambia la IP:
   ```kotlin
   private const val BASE_URL = "http://10.0.2.2:5000/"
   ```
3. **Build → Rebuild Project**
4. Ejecuta en el emulador

### Para usar tu Celular:

1. Abre `RetrofitClient.kt`
2. Cambia la IP:
   ```kotlin
   private const val BASE_URL = "http://192.168.18.113:5000/"
   ```
3. **Build → Rebuild Project**
4. Ejecuta en tu dispositivo físico

---

## 🔐 Credenciales

```
Usuario: MONSTER
Contraseña: Monster9
```

## 📱 Funcionalidades de la App

1. **Pantalla de Login**:
   - 🎨 Imagen de Sullivan con border radius
   - 🔵 Colores azules de Monsters University
   - 🔐 Validación con el servidor Flask
   - 🍪 Manejo de sesión con cookies

2. **Dashboard**:
   - ⚖️ MASA (kg↔lb, kg↔oz)
   - 📏 LONGITUD (m↔ft, km↔mi)
   - 🌡️ TEMPERATURA (°C↔°F, °C↔K)
   - ✨ Botones y cards con colores de Sullivan
   - ✅ Resultados en cards verdes
   - ❌ Errores en cards rojos

3. **Características**:
   - ✅ UI moderna con Material Design 3
   - ✅ Jetpack Compose
   - ✅ Manejo de estado con ViewModel
   - ✅ Indicadores de carga
   - ✅ Manejo de errores
   - ✅ Sesión persistente

---

## 🔍 Solución de Problemas

### ❌ Error: "No se puede conectar al servidor"

**Si usas EMULADOR:**
- Verifica que la URL sea `http://10.0.2.2:5000/`
- Asegúrate que el servidor Flask esté corriendo

**Si usas CELULAR FÍSICO:**

1. **Verifica que el servidor Flask esté corriendo**:
   ```powershell
   # Debería responder
   Invoke-WebRequest http://localhost:5000
   ```

2. **Verifica que tu dispositivo esté en la misma red**:
   - Ve a Configuración → WiFi en tu teléfono
   - Debe estar conectado a la misma red que tu PC
   - La IP debe empezar con el mismo rango (192.168.18.x)

3. **Prueba desde el navegador del celular**:
   - Abre Chrome en tu celular
   - Navega a: `http://192.168.18.113:5000`
   - Si no carga, hay un problema de red

4. **Verifica el Firewall de Windows**:
   ```powershell
   # Ver reglas existentes
   Get-NetFirewallRule -DisplayName "Flask*"
   
   # Agregar regla si no existe
   New-NetFirewallRule -DisplayName "Flask Server Port 5000" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
   ```

5. **Desactiva temporalmente el firewall para probar**:
   - Panel de Control → Windows Defender Firewall
   - Desactivar firewall de red privada
   - Prueba la conexión
   - Vuelve a activarlo después

### ❌ Error: "Credenciales incorrectas"

1. Verifica que el servidor Flask esté actualizado con los endpoints `/api/login` y `/api/convertir`
2. Asegúrate de usar:
   - Usuario: `MONSTER` (en mayúsculas)
   - Contraseña: `Monster9` (con M mayúscula)

### ❌ Error: "Cleartext HTTP traffic not permitted"

✅ Ya solucionado con `android:usesCleartextTraffic="true"` en AndroidManifest.xml

### ❌ Mi IP cambió

1. Obtén la nueva IP:
   ```powershell
   ipconfig | Select-String "IPv4"
   ```

2. Actualiza `RetrofitClient.kt`:
   ```kotlin
   private const val BASE_URL = "http://TU_NUEVA_IP:5000/"
   ```

3. **Build → Rebuild Project** en Android Studio

### ❌ El dispositivo no aparece en Android Studio

1. Verifica que la depuración USB esté activada
2. Desconecta y reconecta el cable USB
3. En el celular, cambia el modo USB:
   - Desliza desde arriba → Toca "USB para transferencia de archivos"
   - Cambia a "Transferencia de archivos" o "PTP"
4. Ejecuta en terminal:
   ```powershell
   # Si tienes adb instalado
   adb devices
   ```

---

## 📂 Estructura del Proyecto

```
ANCLI/app/src/main/java/com/example/andcli/
├── MainActivity.kt          # Pantallas Login y Dashboard (UI con colores de Sullivan)
├── data/
│   └── Models.kt           # Modelos de datos (LoginResponse, ConversionResponse)
├── network/
│   ├── ApiService.kt       # Definición de endpoints (/api/login, /api/convertir)
│   └── RetrofitClient.kt   # Configuración Retrofit (⚠️ CAMBIAR IP AQUÍ)
└── viewmodel/
    └── MainViewModel.kt    # Lógica de negocio y estado

ANCLI/app/src/main/res/
└── drawable/
    └── login_solivan.jpg   # Imagen de Sullivan para login
```

---

## 🎯 Resumen Rápido

### Para Emulador:
```kotlin
// RetrofitClient.kt
private const val BASE_URL = "http://10.0.2.2:5000/"
```
✅ Más fácil, no requiere configuración de red

### Para Celular Físico:
```kotlin
// RetrofitClient.kt
private const val BASE_URL = "http://192.168.18.113:5000/"  // Tu IP real
```
✅ Requisitos:
1. Depuración USB activada
2. Celular y PC en la misma WiFi
3. Firewall permitiendo puerto 5000
4. Probar primero desde navegador del celular

---

## ✅ Lista de Verificación

Antes de ejecutar, verifica:

- [ ] Servidor SOAP .NET corriendo (puerto 63393)
- [ ] Servidor Flask corriendo (puerto 5000)
- [ ] IP correcta en RetrofitClient.kt (10.0.2.2 para emulador, 192.168.x.x para celular)
- [ ] Dispositivo/emulador conectado y visible en Android Studio
- [ ] Si usas celular: mismo WiFi que la PC
- [ ] Si usas celular: probado desde navegador del celular
- [ ] Gradle sincronizado en Android Studio
- [ ] Permisos de Internet en AndroidManifest.xml
- [ ] Firewall permite puerto 5000 (para celular físico)

---

## 💡 Notas Importantes

- **Emulador**: Usa `10.0.2.2` (IP especial para localhost de tu PC)
- **Celular**: Usa tu IP real `192.168.x.x` (misma red WiFi obligatorio)
- **IP Dinámica**: Si reinicias tu router, tu IP puede cambiar
- **Firewall**: Windows puede bloquear conexiones desde tu celular
- **HTTP vs HTTPS**: Usamos HTTP simple para desarrollo local
- **Puerto**: Cambiamos de 8000 a 5000 (puerto por defecto de Flask)

---

## 🎨 Nueva Interfaz con Colores de Sullivan

La app ahora incluye:











- 🔵 Color azul principal: `#0066CC` (Monsters University)
- 🔵 Color azul claro: `#4DA6FF`
- 🤍 Fondo blanco limpio
- 🟢 Cards de resultado verdes
- 🔴 Cards de error rojos
- 🖼️ Imagen de Sullivan con border radius en login
- 📦 Todos los botones y cards con esquinas redondeadas
- 🎯 Emojis decorativos en toda la interfaz

---

¡Listo para usar! 🎉
