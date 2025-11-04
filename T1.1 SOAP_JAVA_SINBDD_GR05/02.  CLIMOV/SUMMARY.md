# 📱 Cliente Android SOAP - CONUNI

## ✅ Proyecto Completado

### 🎯 Credenciales de Acceso
- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

### 📂 Estructura del Proyecto
```
02. CLIMOV/
├── app/
│   ├── src/main/
│   │   ├── java/com/gr05/conuniclient/
│   │   │   ├── LoginActivity.java       ✅ Pantalla de login
│   │   │   ├── MainActivity.java        ✅ Pantalla principal
│   │   │   └── SOAPClient.java          ✅ Cliente SOAP
│   │   ├── res/
│   │   │   ├── layout/
│   │   │   │   ├── activity_login.xml   ✅ UI Login
│   │   │   │   └── activity_main.xml    ✅ UI Principal
│   │   │   ├── values/
│   │   │   │   ├── strings.xml          ✅ Textos
│   │   │   │   ├── colors.xml           ✅ Colores
│   │   │   │   └── themes.xml           ✅ Temas
│   │   │   └── xml/
│   │   │       └── network_security_config.xml ✅ Config HTTP
│   │   └── AndroidManifest.xml          ✅ Manifest con permisos
│   └── build.gradle                     ✅ Dependencias
├── build.gradle                         ✅ Config proyecto
├── settings.gradle                      ✅ Config módulos
├── gradle.properties                    ✅ Properties
├── .gitignore                           ✅ Git ignore
├── README.md                            ✅ Documentación completa
├── QUICKSTART.md                        ✅ Guía rápida
└── WSDL_ADAPTATION.md                   ✅ Guía adaptación WSDL
```

## 🚀 Pasos para Ejecutar

### 📟 En Emulador (Más fácil)
1. Abre el proyecto en Android Studio
2. Asegúrate de que tu servicio SOAP esté corriendo en `http://localhost:8080`
3. Crea un emulador Android (API 30+)
4. Presiona Run ▶️
5. Login con: `MONSTER` / `Monster9`

**✓ Ya está configurado para usar `10.0.2.2` (localhost del emulador)**

### 📱 En Dispositivo Físico (Requiere configuración adicional)

#### 1️⃣ Obtén tu IP:
```powershell
ipconfig
```
Anota tu IPv4 (ej: `192.168.1.5`)

#### 2️⃣ Modifica `LoginActivity.java` línea 33:
```java
// Cambiar de:
soapClient = new SOAPClient(SOAP_URL_EMULATOR);

// A:
soapClient = new SOAPClient(SOAP_URL_DEVICE);
```

#### 3️⃣ Actualiza la IP en línea 22:
```java
private static final String SOAP_URL_DEVICE = "http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI";
```

#### 4️⃣ Configura el Firewall (PowerShell como Admin):
```powershell
New-NetFirewallRule -DisplayName "SOAP Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow
```

#### 5️⃣ Conecta tu celular:
- Habilita depuración USB
- Conecta por USB
- Autoriza la depuración
- Asegúrate de estar en la misma WiFi
- Presiona Run ▶️ en Android Studio

#### 6️⃣ Verifica la conexión:
Desde el navegador de tu celular:
```
http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
```
Si ves el XML, ¡todo bien!

## 🔧 Tecnologías Usadas

| Componente | Tecnología |
|------------|-----------|
| Lenguaje | Java |
| Framework | Android SDK |
| Cliente SOAP | kSOAP2-Android 3.6.4 |
| UI | Material Design Components |
| Min SDK | API 24 (Android 7.0) |
| Target SDK | API 34 (Android 14) |
| Build System | Gradle |

## 📋 Características

✅ Login con credenciales quemadas  
✅ Validación de campos  
✅ Cliente SOAP genérico y extensible  
✅ Soporte para HTTP (no solo HTTPS)  
✅ Manejo de errores de red  
✅ Interfaz Material Design  
✅ Compatible con emulador y dispositivo físico  
✅ AsyncTask para operaciones en segundo plano  
✅ SharedPreferences para mantener sesión  
✅ Logs detallados para debugging  

## 📖 Documentación Disponible

| Archivo | Descripción |
|---------|-------------|
| `README.md` | Documentación completa con troubleshooting |
| `QUICKSTART.md` | Guía rápida de inicio |
| `WSDL_ADAPTATION.md` | Cómo adaptar a tu WSDL específico |

## 🎨 Pantallas

### Login Screen
- Input de usuario
- Input de contraseña (con toggle de visibilidad)
- Botón de ingreso
- Progress indicator durante carga
- Validación de campos vacíos
- Mensajes de error/éxito

### Main Screen
- Mensaje de bienvenida
- Nombre del usuario logueado
- Estado de conexión al servicio
- Botón de cerrar sesión

## 🔐 Seguridad

⚠️ **IMPORTANTE:** Este proyecto es para fines educativos.

En producción deberías:
- Implementar autenticación real contra el servicio
- Usar HTTPS en lugar de HTTP
- No almacenar credenciales en texto plano
- Implementar tokens de sesión
- Cifrar datos sensibles

## 🐛 Troubleshooting Común

| Problema | Causa | Solución |
|----------|-------|----------|
| No conecta en emulador | Usando localhost | Usa `10.0.2.2` |
| No conecta en celular | No están en la misma red | Verifica WiFi |
| Firewall bloquea | Puerto cerrado | Ejecuta comando de firewall |
| HTTP no permitido | Política Android | Ya configurado en el proyecto |
| App muy lenta | Emulador ARM | Usa x86_64 con HAXM |

## 🔍 Verificar Instalación

Para verificar que todo está bien configurado:

1. **Revisa el AndroidManifest.xml** → Debe tener permisos de Internet
2. **Revisa network_security_config.xml** → Debe permitir cleartext
3. **Revisa build.gradle (app)** → Debe incluir ksoap2-android
4. **Revisa LoginActivity.java** → Credenciales correctas
5. **Revisa SOAPClient.java** → URL del servicio correcta

## 📞 URLs Importantes

| Descripción | URL |
|-------------|-----|
| WSDL del servicio | http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl |
| URL para emulador | http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI |
| URL para dispositivo | http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI |

## 🎓 Para el Profesor

Este proyecto demuestra:
- ✅ Consumo de servicios SOAP desde Android
- ✅ Arquitectura de aplicación móvil básica
- ✅ Manejo de operaciones asíncronas
- ✅ Interfaz de usuario moderna (Material Design)
- ✅ Configuración de seguridad de red
- ✅ Manejo de sesiones
- ✅ Buenas prácticas de logging y debugging

## 📊 Métricas del Proyecto

- **Líneas de código Java:** ~400
- **Archivos XML:** 8
- **Actividades:** 2
- **Dependencias externas:** 5
- **Tiempo estimado de setup:** 5-10 minutos
- **APIs Android usadas:** Material, ConstraintLayout, SharedPreferences

---

**Proyecto:** TI1.1 SOAP_JAVA_SINBDD_GR05  
**Grupo:** G5  
**Componente:** Cliente Móvil Android  
**Versión:** 1.0.0  
**Fecha:** 3 de noviembre de 2025  
**Estado:** ✅ Completo y listo para usar
