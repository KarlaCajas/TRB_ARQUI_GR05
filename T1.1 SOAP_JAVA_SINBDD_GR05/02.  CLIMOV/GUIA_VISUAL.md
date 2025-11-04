# 📱 Guía Visual Rápida - Cliente Android SOAP

## 🎯 Objetivo
Crear una aplicación Android que se conecte a tu servicio SOAP y permita login con credenciales.

---

## 📋 PARTE 1: PREPARACIÓN (5 minutos)

### ✅ Checklist antes de empezar:
```
□ Android Studio instalado
□ Servicio SOAP corriendo en http://localhost:8080
□ Java JDK instalado
□ Conexión a Internet (para descargar dependencias)
```

---

## 🚀 PARTE 2: ABRIR EL PROYECTO

### Paso 1: Abrir Android Studio
```
Android Studio → Open → Navegar a:
c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02. CLIMOV
```

### Paso 2: Esperar sincronización de Gradle
```
Verás en la parte inferior:
"Gradle sync in progress..." 
↓
Espera...
↓
"Gradle sync finished" ✓
```

---

## 📟 PARTE 3A: EJECUTAR EN EMULADOR (Más fácil)

### Opción recomendada para pruebas rápidas

#### Paso 1: Crear emulador
```
Tools → Device Manager → Create Device
↓
Selecciona: Pixel 5
↓
Selecciona: API 30 (Android 11) - x86_64
↓
Finish
```

#### Paso 2: Ejecutar
```
1. Verifica que el servicio SOAP esté corriendo
2. Selecciona el emulador en el dropdown
3. Click en Run ▶️
4. Espera a que inicie
```

#### Paso 3: Login
```
Usuario: MONSTER
Contraseña: Monster9
↓
Click en INGRESAR
↓
✓ Pantalla principal
```

### 🔍 URL usada en emulador:
```
http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI
(10.0.2.2 = localhost de tu PC)
```

---

## 📱 PARTE 3B: EJECUTAR EN CELULAR (Requiere configuración)

### Para conectar desde tu dispositivo físico

#### Paso 1: Configurar tu celular
```
Ajustes → Acerca del teléfono
↓
Toca 7 veces "Número de compilación"
↓
Vuelve a Ajustes → Opciones de desarrollador
↓
Activa "Depuración USB"
```

#### Paso 2: Obtener tu IP local
```powershell
# En PowerShell:
ipconfig

# Busca "Dirección IPv4": 192.168.X.X
# Anota esta IP
```

#### Paso 3: Configurar Firewall
```powershell
# PowerShell como ADMINISTRADOR:
New-NetFirewallRule -DisplayName "SOAP Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow

# O ejecuta:
.\configurar-firewall.ps1
```

#### Paso 4: Modificar el código
```java
// Archivo: app/src/main/java/com/gr05/conuniclient/LoginActivity.java

// Busca línea 22:
private static final String SOAP_URL_DEVICE = "http://192.168.1.5:8080/ConUni_Soap_Java_GR05/CONUNI";
// Cambia 192.168.1.5 por TU IP

// Busca línea 33:
soapClient = new SOAPClient(SOAP_URL_EMULATOR);
// Cambia por:
soapClient = new SOAPClient(SOAP_URL_DEVICE);
```

#### Paso 5: Conectar y ejecutar
```
1. Conecta tu celular por USB
2. Autoriza la depuración USB en el celular
3. Asegúrate de estar en la misma WiFi
4. Selecciona tu dispositivo en Android Studio
5. Click en Run ▶️
```

#### Paso 6: Verificar conexión
```
Desde el navegador de tu celular, visita:
http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl

Si ves XML → ✓ Todo bien
Si no carga → ✗ Problema de red/firewall
```

---

## 🎨 ESTRUCTURA DEL PROYECTO

```
CONUNIClient/
├── 📄 LoginActivity.java       ← Login con credenciales
├── 📄 MainActivity.java        ← Pantalla después del login
├── 📄 SOAPClient.java          ← Cliente para llamadas SOAP
├── 📄 activity_login.xml       ← Diseño de login
├── 📄 activity_main.xml        ← Diseño pantalla principal
├── 📄 AndroidManifest.xml      ← Permisos y configuración
└── 📄 network_security_config  ← Permite HTTP
```

---

## 🔐 CREDENCIALES

```
Usuario:    MONSTER
Contraseña: Monster9
```

**¡IMPORTANTE!** Las credenciales están "quemadas" en el código (líneas 20-21 de LoginActivity.java)

---

## 🎯 FLUJO DE LA APP

```
1. App inicia
   ↓
2. Pantalla de Login
   ↓
3. Usuario ingresa: MONSTER / Monster9
   ↓
4. App valida credenciales (hardcoded)
   ↓
5. [OPCIONAL] Llama al servicio SOAP
   ↓
6. Login exitoso
   ↓
7. Pantalla principal
   ↓
8. Botón "Cerrar Sesión" → Vuelve a Login
```

---

## 📊 COMPARACIÓN: EMULADOR vs DISPOSITIVO

| Característica | Emulador | Dispositivo Físico |
|----------------|----------|-------------------|
| Configuración | ✅ Fácil | ⚠️ Media |
| Velocidad | 🐢 Media | 🚀 Rápida |
| Realismo | 📱 Simulado | 📱 Real |
| URL | 10.0.2.2 | Tu IP local |
| Firewall | No requiere | Sí requiere |
| WiFi | No requiere | Sí requiere |
| USB | No requiere | Sí requiere |

**Recomendación:** Usa emulador para desarrollo y dispositivo para pruebas finales.

---

## 🔧 TROUBLESHOOTING RÁPIDO

### ❌ "No puede conectar al servicio"
```
EMULADOR:
- Verifica que uses 10.0.2.2 (no localhost)
- Verifica que el servicio SOAP esté corriendo

DISPOSITIVO:
- Verifica que estés en la misma WiFi
- Verifica la IP con ipconfig
- Verifica el firewall
```

### ❌ "Gradle sync failed"
```
- Verifica conexión a internet
- File → Invalidate Caches / Restart
```

### ❌ "SDK not found"
```
File → Project Structure → SDK Location
→ Android Studio descargará el SDK automáticamente
```

### ❌ App se cierra al hacer login
```
- Revisa Logcat (tag: SOAPClient)
- Verifica que el servicio SOAP esté accesible
```

---

## 📁 ARCHIVOS DE AYUDA INCLUIDOS

| Archivo | Descripción |
|---------|-------------|
| 📄 README.md | Documentación completa |
| 📄 QUICKSTART.md | Guía rápida de inicio |
| 📄 COMO_ABRIR.md | Cómo abrir en Android Studio |
| 📄 WSDL_ADAPTATION.md | Adaptar a tu WSDL |
| 📄 POWERSHELL_COMMANDS.md | Comandos útiles |
| 📄 SUMMARY.md | Resumen del proyecto |
| 📄 verificar-entorno.ps1 | Script de verificación |
| 📄 configurar-firewall.ps1 | Script de firewall |

---

## ⏱️ TIEMPO ESTIMADO

| Tarea | Tiempo |
|-------|--------|
| Abrir proyecto en Android Studio | 2-5 min |
| Sincronización de Gradle | 3-10 min |
| Crear emulador | 5-10 min |
| Ejecutar en emulador | 2-3 min |
| Configurar para dispositivo | 10-15 min |
| **TOTAL (emulador)** | **15-30 min** |
| **TOTAL (dispositivo)** | **25-45 min** |

---

## ✅ VERIFICACIÓN FINAL

Antes de decir "está listo", verifica:

```
□ App se instala sin errores
□ Pantalla de login se ve correctamente
□ Campos de usuario/contraseña funcionan
□ Login con credenciales correctas funciona
□ Login con credenciales incorrectas muestra error
□ Pantalla principal muestra nombre de usuario
□ Botón "Cerrar Sesión" funciona
□ [OPCIONAL] Servicio SOAP responde correctamente
```

---

## 🎓 PARA ENTREGAR

1. ✅ Proyecto funcionando en emulador
2. ✅ Capturas de pantalla:
   - Pantalla de login
   - Login exitoso
   - Pantalla principal
   - (Opcional) Logs de Logcat mostrando llamada SOAP
3. ✅ Video corto (opcional):
   - Mostrando el flujo completo de login
4. ✅ Proyecto funcionando en celular (bonus)

---

## 🚀 COMANDOS RÁPIDOS

### Ejecutar script de verificación:
```powershell
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"
.\verificar-entorno.ps1
```

### Configurar firewall (como Admin):
```powershell
.\configurar-firewall.ps1
```

### Ver tu IP:
```powershell
ipconfig | Select-String "IPv4"
```

### Verificar servicio SOAP:
```powershell
Test-NetConnection -ComputerName localhost -Port 8080
```

---

## 📞 RECURSOS ADICIONALES

- **WSDL del servicio:** http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
- **Documentación kSOAP2:** https://github.com/simpligility/ksoap2-android
- **Android Developers:** https://developer.android.com/

---

**¡Éxito con tu proyecto! 🎉**

*Desarrollado para: TI1.1 SOAP_JAVA_SINBDD_GR05*  
*Grupo: G5*  
*Fecha: 3 de noviembre de 2025*
