# 📚 Índice de Documentación - Cliente Android SOAP

Bienvenido al proyecto **Cliente Móvil Android para Servicio SOAP CONUNI**

## 🎯 ¿Por dónde empiezo?

### Si es tu primera vez:
1. 👉 **[GUIA_VISUAL.md](GUIA_VISUAL.md)** - Guía visual paso a paso
2. 👉 **[COMO_ABRIR.md](COMO_ABRIR.md)** - Cómo abrir el proyecto en Android Studio
3. 👉 **[QUICKSTART.md](QUICKSTART.md)** - Configuración rápida

### Si quieres ver todos los detalles:
👉 **[README.md](README.md)** - Documentación completa

---

## 📖 Documentos Disponibles

### 🚀 Inicio Rápido
| Documento | Descripción | Tiempo |
|-----------|-------------|--------|
| **[GUIA_VISUAL.md](GUIA_VISUAL.md)** | Guía visual con diagramas y pasos | 10 min |
| **[QUICKSTART.md](QUICKSTART.md)** | Configuración rápida para empezar | 5 min |
| **[COMO_ABRIR.md](COMO_ABRIR.md)** | Cómo abrir en Android Studio | 5 min |

### 📚 Documentación Completa
| Documento | Descripción | Cuándo usar |
|-----------|-------------|-------------|
| **[README.md](README.md)** | Documentación completa del proyecto | Para referencia completa |
| **[SUMMARY.md](SUMMARY.md)** | Resumen ejecutivo del proyecto | Para entender qué hace |
| **[WSDL_ADAPTATION.md](WSDL_ADAPTATION.md)** | Cómo adaptar a tu WSDL | Si necesitas personalizar |

### 🔧 Herramientas y Scripts
| Archivo | Descripción | Cómo usar |
|---------|-------------|-----------|
| **[verificar-entorno.ps1](verificar-entorno.ps1)** | Verifica configuración | `.\verificar-entorno.ps1` |
| **[configurar-firewall.ps1](configurar-firewall.ps1)** | Configura firewall (Admin) | `.\configurar-firewall.ps1` |
| **[POWERSHELL_COMMANDS.md](POWERSHELL_COMMANDS.md)** | Comandos útiles PowerShell | Referencia |

---

## 🎯 Rutas Rápidas por Objetivo

### Objetivo: "Quiero ejecutar la app YA"
```
1. GUIA_VISUAL.md → Parte 2 (Abrir proyecto)
2. GUIA_VISUAL.md → Parte 3A (Ejecutar en emulador)
3. Login con: MONSTER / Monster9
✅ Listo!
```

### Objetivo: "Quiero ejecutar en mi celular"
```
1. GUIA_VISUAL.md → Parte 3B (Ejecutar en celular)
2. Ejecutar: configurar-firewall.ps1
3. Modificar LoginActivity.java con tu IP
4. Conectar celular y ejecutar
✅ Listo!
```

### Objetivo: "Tengo problemas para abrir el proyecto"
```
1. COMO_ABRIR.md → Sección completa
2. COMO_ABRIR.md → "Problemas Comunes al Abrir"
✅ Solución encontrada!
```

### Objetivo: "Quiero adaptar el código a mi WSDL"
```
1. WSDL_ADAPTATION.md → Analizar tu WSDL
2. WSDL_ADAPTATION.md → Modificar SOAPClient.java
3. WSDL_ADAPTATION.md → Ejemplo Completo
✅ Código adaptado!
```

### Objetivo: "La app no conecta al servicio"
```
1. README.md → "Solución de Problemas"
2. Ejecutar: verificar-entorno.ps1
3. Si usa celular: configurar-firewall.ps1
✅ Problema resuelto!
```

---

## 📋 Credenciales del Sistema

```
Usuario:    MONSTER
Contraseña: Monster9
```

---

## 🌐 URLs Importantes

| Tipo | URL |
|------|-----|
| **WSDL** | http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl |
| **Emulador** | http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI |
| **Dispositivo** | http://[TU_IP]:8080/ConUni_Soap_Java_GR05/CONUNI |

---

## 🗂️ Estructura del Proyecto

```
📁 Cliente Android SOAP (02. CLIMOV)
│
├── 📱 Código Fuente
│   ├── app/src/main/java/com/gr05/conuniclient/
│   │   ├── LoginActivity.java       → Pantalla de login
│   │   ├── MainActivity.java        → Pantalla principal
│   │   └── SOAPClient.java          → Cliente SOAP
│   │
│   ├── app/src/main/res/layout/
│   │   ├── activity_login.xml       → UI Login
│   │   └── activity_main.xml        → UI Principal
│   │
│   └── app/src/main/res/xml/
│       └── network_security_config.xml → Config HTTP
│
├── 📚 Documentación
│   ├── INDEX.md                     → Este archivo
│   ├── README.md                    → Documentación completa
│   ├── GUIA_VISUAL.md              → Guía visual paso a paso
│   ├── QUICKSTART.md               → Guía rápida
│   ├── COMO_ABRIR.md               → Abrir en Android Studio
│   ├── SUMMARY.md                   → Resumen ejecutivo
│   ├── WSDL_ADAPTATION.md          → Adaptar a tu WSDL
│   └── POWERSHELL_COMMANDS.md      → Comandos útiles
│
├── 🔧 Scripts
│   ├── verificar-entorno.ps1       → Verificar configuración
│   └── configurar-firewall.ps1     → Configurar firewall
│
└── ⚙️ Configuración
    ├── build.gradle                 → Config Gradle (proyecto)
    ├── settings.gradle              → Config módulos
    ├── app/build.gradle            → Config Gradle (app)
    ├── AndroidManifest.xml         → Manifest y permisos
    └── .gitignore                   → Git ignore
```

---

## 🎓 Glosario de Términos

| Término | Significado |
|---------|-------------|
| **SOAP** | Protocolo para intercambio de información en servicios web |
| **WSDL** | Descripción del servicio web (XML) |
| **kSOAP2** | Librería Android para consumir servicios SOAP |
| **Emulador** | Dispositivo Android virtual en tu PC |
| **ADB** | Android Debug Bridge (herramienta de debugging) |
| **Gradle** | Sistema de compilación para Android |
| **API Level** | Versión de Android SDK |
| **10.0.2.2** | IP especial que el emulador usa para localhost |

---

## 🎯 Checklist de Verificación

### Antes de ejecutar:
```
□ Android Studio instalado
□ Proyecto abierto correctamente
□ Gradle sync completado
□ Servicio SOAP corriendo en localhost:8080
□ Emulador configurado O celular conectado
□ Si usa celular: Firewall configurado
□ Si usa celular: IP actualizada en código
```

### Después de ejecutar:
```
□ App se instaló sin errores
□ Login funciona con MONSTER / Monster9
□ Pantalla principal se muestra
□ Cerrar sesión funciona
□ [Opcional] Llamadas SOAP funcionan
```

---

## 📞 Soporte

### Problemas comunes → README.md sección "Solución de Problemas"

### Comandos útiles → POWERSHELL_COMMANDS.md

### Adaptación del código → WSDL_ADAPTATION.md

---

## 🎨 Características del Proyecto

✅ Login con credenciales quemadas  
✅ Cliente SOAP genérico  
✅ Interfaz Material Design  
✅ Soporte HTTP (no solo HTTPS)  
✅ Compatible emulador y dispositivo físico  
✅ Manejo de errores  
✅ Sesión persistente  
✅ Logs para debugging  

---

## 📊 Información del Proyecto

| Propiedad | Valor |
|-----------|-------|
| **Nombre** | CONUNIClient |
| **Paquete** | com.gr05.conuniclient |
| **Min SDK** | API 24 (Android 7.0) |
| **Target SDK** | API 34 (Android 14) |
| **Lenguaje** | Java |
| **Build System** | Gradle |
| **Librería SOAP** | kSOAP2-Android 3.6.4 |

---

## 🚀 Empezar Ahora

### Para principiantes:
```powershell
# 1. Abrir PowerShell en la carpeta del proyecto
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"

# 2. Verificar entorno
.\verificar-entorno.ps1

# 3. Leer la guía visual
# Abre: GUIA_VISUAL.md
```

### Para avanzados:
```powershell
# 1. Configurar firewall (Admin)
.\configurar-firewall.ps1

# 2. Abrir en Android Studio
studio .

# 3. Run ▶️
```

---

## 📝 Notas Finales

- Este proyecto es **educativo**, no incluye seguridad de producción
- Las credenciales están **hardcoded** (quemadas en el código)
- El servicio usa **HTTP**, no HTTPS
- Para producción, implementa autenticación real y HTTPS

---

## 🎓 Para el Profesor

Este proyecto demuestra:
- ✅ Consumo de servicios SOAP desde Android
- ✅ Arquitectura de app móvil básica
- ✅ Manejo de operaciones asíncronas
- ✅ Interfaz moderna (Material Design)
- ✅ Configuración de seguridad de red
- ✅ Documentación completa y profesional

---

**¡Todo listo para empezar! 🚀**

*Proyecto: TI1.1 SOAP_JAVA_SINBDD_GR05*  
*Grupo: G5*  
*Fecha: 3 de noviembre de 2025*  
*Estado: ✅ Completo*

---

## 🗺️ Mapa de Navegación

```
START HERE
    ↓
¿Primera vez?
    ↓
  Sí → GUIA_VISUAL.md
    ↓
  Problemas abriendo proyecto?
    ↓
  Sí → COMO_ABRIR.md
    ↓
  ¿Ejecutar en emulador o celular?
    ↓
  Emulador → GUIA_VISUAL.md (Parte 3A)
  Celular  → GUIA_VISUAL.md (Parte 3B) + configurar-firewall.ps1
    ↓
  ¿Problemas de conexión?
    ↓
  Sí → README.md (Troubleshooting) + verificar-entorno.ps1
    ↓
  ¿Necesitas personalizar?
    ↓
  Sí → WSDL_ADAPTATION.md
    ↓
  ✅ PROYECTO FUNCIONANDO
```

---

**Última actualización:** 3 de noviembre de 2025
