# 🚀 Cómo Abrir el Proyecto en Android Studio

## Método 1: Desde Android Studio (Recomendado)

1. **Abre Android Studio**

2. **En la pantalla de bienvenida:**
   - Click en **"Open"**
   - O si ya tienes un proyecto abierto: **File > Open**

3. **Navega a la carpeta:**
   ```
   c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV
   ```

4. **Selecciona la carpeta y click en OK**

5. **Espera a que Gradle sincronice** (primera vez puede tardar 2-5 minutos)
   - Verás "Gradle sync in progress..." en la parte inferior
   - Espera a que aparezca "Gradle sync finished"

6. **¡Listo!** El proyecto está abierto y listo para compilar

## Método 2: Desde el Explorador de Archivos

1. **Navega a:**
   ```
   c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV
   ```

2. **Doble click en cualquiera de estos archivos:**
   - `build.gradle`
   - `settings.gradle`

3. **Selecciona "Android Studio"** cuando Windows pregunte con qué abrir

4. **Espera la sincronización de Gradle**

## Método 3: Desde la Línea de Comandos

```powershell
# Navegar a la carpeta
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"

# Abrir con Android Studio (si está en el PATH)
studio .

# O con ruta completa (ajusta según tu instalación)
& "C:\Program Files\Android\Android Studio\bin\studio64.exe" .
```

## 🔧 Después de Abrir el Proyecto

### 1. Verificar SDK de Android
Si es la primera vez que usas Android Studio:

1. Ve a **File > Project Structure** (o presiona `Ctrl+Alt+Shift+S`)
2. En **SDK Location**, verifica que tengas un SDK configurado
3. Si no, Android Studio te ofrecerá descargarlo automáticamente

### 2. Descargar Dependencias
Si falta alguna dependencia, Android Studio te mostrará un banner:
- Click en **"Sync Now"** o **"Download"**
- Espera a que se complete la descarga

### 3. Configurar Emulador (Opcional)
Si no tienes un emulador configurado:

1. Ve a **Tools > Device Manager** (o presiona el ícono de teléfono en la barra)
2. Click en **"Create Device"**
3. Selecciona un dispositivo (recomendado: **Pixel 5**)
4. Selecciona una imagen del sistema:
   - API Level: **30** o superior (Android 11+)
   - Tipo: **x86_64** (más rápido)
   - Click en **Download** si no la tienes
5. Click en **Next > Finish**

## ▶️ Ejecutar la Aplicación

### En Emulador:
1. Asegúrate de que tu **servicio SOAP esté corriendo** en `http://localhost:8080`
2. Selecciona tu emulador en el dropdown (junto al botón Run)
3. Click en el botón **Run** (▶️) o presiona `Shift+F10`
4. Espera a que el emulador inicie y la app se instale

### En Dispositivo Físico:
1. Conecta tu celular por USB
2. Habilita **Depuración USB** en tu celular
3. Autoriza la conexión cuando te lo pida
4. **IMPORTANTE:** Modifica la URL en `LoginActivity.java` (ver README.md)
5. Selecciona tu dispositivo en el dropdown
6. Click en **Run** (▶️)

## 🐛 Problemas Comunes al Abrir

### "Gradle sync failed"
**Causa:** No hay conexión a internet o problema con dependencias

**Soluciones:**
1. Verifica tu conexión a internet
2. Ve a **File > Invalidate Caches / Restart**
3. Intenta de nuevo

### "SDK not found"
**Causa:** No tienes Android SDK instalado

**Solución:**
1. Ve a **File > Project Structure > SDK Location**
2. Android Studio te ofrecerá descargar el SDK
3. Acepta y espera la descarga

### "Failed to find Build Tools"
**Causa:** Faltan herramientas de compilación

**Solución:**
1. Ve a **Tools > SDK Manager**
2. En la pestaña **SDK Tools**
3. Marca **Android SDK Build-Tools**
4. Click en **Apply > OK**

### El proyecto se ve vacío o sin estructura
**Causa:** Vista incorrecta en el Project Explorer

**Solución:**
1. En el panel izquierdo (Project Explorer)
2. Cambia la vista de **"Project"** a **"Android"** usando el dropdown
3. Ahora deberías ver: `app > java > com.gr05.conuniclient`

### Gradle tarda mucho en sincronizar
**Causa:** Primera sincronización descarga muchas dependencias

**Solución:**
- Es normal, especialmente la primera vez
- Puede tardar 5-15 minutos dependiendo de tu internet
- Solo déjalo terminar

### "This version of Android Studio is old"
**Causa:** Android Studio desactualizado

**Solución:**
1. Ve a **Help > Check for Updates**
2. O descarga la última versión de: https://developer.android.com/studio

## 📁 Verificar que Abriste el Proyecto Correcto

Deberías ver esta estructura en el Project Explorer (vista Android):

```
📁 app
  📁 manifests
    📄 AndroidManifest.xml
  📁 java
    📁 com.gr05.conuniclient
      📄 LoginActivity
      📄 MainActivity
      📄 SOAPClient
  📁 res
    📁 layout
      📄 activity_login.xml
      📄 activity_main.xml
    📁 values
      📄 colors.xml
      📄 strings.xml
      📄 themes.xml
    📁 xml
      📄 network_security_config.xml
📄 build.gradle (Project)
📄 build.gradle (Module: app)
```

## ✅ Checklist Final

Antes de ejecutar, verifica:

- [ ] Android Studio abrió el proyecto correctamente
- [ ] Gradle sync completado sin errores
- [ ] No hay errores rojos en los archivos Java
- [ ] Emulador configurado O dispositivo conectado
- [ ] Servicio SOAP corriendo en `http://localhost:8080`
- [ ] Si usas dispositivo físico: IP actualizada en `LoginActivity.java`

## 🎯 Siguiente Paso

Una vez abierto el proyecto:
1. Lee el **README.md** para instrucciones completas
2. Ejecuta **verificar-entorno.ps1** para verificar tu entorno
3. Presiona **Run** y prueba la aplicación

---

**¿Sigues teniendo problemas?**
Consulta el archivo **README.md** sección "Solución de Problemas"
