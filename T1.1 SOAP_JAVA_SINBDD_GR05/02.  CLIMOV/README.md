# Cliente Móvil Android para Servicio SOAP CONUNI

Aplicación Android que consume el servicio web SOAP CONUNI con autenticación mediante credenciales.

## 📋 Credenciales de Acceso

- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## 🚀 Configuración del Proyecto

### Requisitos Previos

1. **Android Studio** (versión Arctic Fox o superior)
2. **JDK 8** o superior
3. **Servicio SOAP** corriendo en `http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI`

### Estructura del Proyecto

```
CONUNIClient/
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/gr05/conuniclient/
│   │       │   ├── LoginActivity.java      # Pantalla de login
│   │       │   ├── MainActivity.java       # Pantalla principal
│   │       │   └── SOAPClient.java         # Cliente SOAP
│   │       ├── res/
│   │       │   ├── layout/
│   │       │   │   ├── activity_login.xml  # UI Login
│   │       │   │   └── activity_main.xml   # UI Principal
│   │       │   ├── values/
│   │       │   │   ├── strings.xml
│   │       │   │   ├── colors.xml
│   │       │   │   └── themes.xml
│   │       │   └── xml/
│   │       │       └── network_security_config.xml
│   │       └── AndroidManifest.xml
│   └── build.gradle
├── build.gradle
├── settings.gradle
└── gradle.properties
```

## 📱 Ejecutar en Emulador

### 1. Abrir el Proyecto en Android Studio

```bash
# Navegar a la carpeta del proyecto
cd "c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02.  CLIMOV"

# Abrir con Android Studio
# File > Open > Seleccionar esta carpeta
```

### 2. Configurar el Emulador

1. En Android Studio, ve a **Tools > Device Manager**
2. Crea un nuevo dispositivo virtual:
   - Dispositivo: Pixel 5 o similar
   - API Level: 30 o superior (Android 11+)
   - Configuración: x86_64 para mejor rendimiento

### 3. Configurar la URL del Servicio

**IMPORTANTE:** El emulador de Android usa `10.0.2.2` para acceder a `localhost` de tu PC.

La configuración ya está lista en `LoginActivity.java`:

```java
private static final String SOAP_URL_EMULATOR = "http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI";
```

### 4. Ejecutar la Aplicación

1. Asegúrate de que tu **servicio SOAP esté corriendo** en `http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI`
2. Selecciona el emulador creado
3. Haz clic en el botón **Run** (▶️) en Android Studio
4. Espera a que se compile e instale la aplicación
5. La app se abrirá automáticamente en el emulador

### 5. Probar el Login

1. Ingresa las credenciales:
   - Usuario: `MONSTER`
   - Contraseña: `Monster9`
2. Presiona el botón **INGRESAR**
3. Deberías ver la pantalla principal con el mensaje de bienvenida

## 📲 Ejecutar en Dispositivo Físico

### 1. Habilitar Modo Desarrollador en tu Celular

**Para Android:**
1. Ve a **Ajustes > Acerca del teléfono**
2. Toca 7 veces sobre **Número de compilación**
3. Vuelve a Ajustes y busca **Opciones de desarrollador**
4. Habilita **Depuración USB**

### 2. Conectar el Dispositivo

1. Conecta tu celular a la PC con un cable USB
2. Autoriza la depuración USB en tu celular (aparecerá un diálogo)
3. En Android Studio, tu dispositivo aparecerá en la lista de dispositivos

### 3. Configurar la IP de tu PC

**IMPORTANTE:** Debes cambiar la URL del servicio para que apunte a la IP local de tu PC.

#### Obtener la IP de tu PC:

```powershell
# En PowerShell, ejecuta:
ipconfig
```

Busca la **Dirección IPv4** de tu adaptador de red (ej: `192.168.1.5`)

#### Modificar el código:

En `LoginActivity.java`, cambia la línea:

```java
// Busca esta línea (aproximadamente línea 33):
soapClient = new SOAPClient(SOAP_URL_EMULATOR);

// Cámbiala por:
soapClient = new SOAPClient(SOAP_URL_DEVICE);

// Y actualiza la IP en SOAP_URL_DEVICE (línea 22):
private static final String SOAP_URL_DEVICE = "http://TU_IP_AQUI:8080/ConUni_Soap_Java_GR05/CONUNI";
// Por ejemplo: "http://192.168.1.5:8080/ConUni_Soap_Java_GR05/CONUNI"
```

### 4. Conectar el Celular a la Misma Red WiFi

Asegúrate de que:
- Tu PC y tu celular estén en la **misma red WiFi**
- El **firewall de Windows** permita conexiones en el puerto 8080

#### Permitir conexión en el Firewall:

```powershell
# Ejecutar como Administrador en PowerShell:
New-NetFirewallRule -DisplayName "SOAP Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow
```

### 5. Verificar la Conexión

Antes de ejecutar la app, verifica que tu celular puede acceder al servicio:

1. Abre el navegador de tu celular
2. Visita: `http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl`
3. Deberías ver el XML del WSDL

### 6. Ejecutar la Aplicación

1. Selecciona tu dispositivo físico en Android Studio
2. Haz clic en **Run** (▶️)
3. La app se instalará y ejecutará en tu celular
4. Prueba el login con las credenciales

## 🔧 Solución de Problemas

### Error: "Unable to connect to SOAP service"

**Causa:** La app no puede conectarse al servicio SOAP.

**Soluciones:**

1. **En Emulador:**
   - Verifica que el servicio esté corriendo en `http://localhost:8080`
   - Usa `10.0.2.2` en lugar de `localhost`

2. **En Dispositivo Físico:**
   - Verifica que estés en la misma red WiFi
   - Verifica que la IP sea correcta con `ipconfig`
   - Desactiva temporalmente el firewall para probar
   - Verifica que el servicio SOAP esté escuchando en todas las interfaces (0.0.0.0) y no solo en localhost

### Error: "Cleartext HTTP traffic not permitted"

**Causa:** Android bloquea tráfico HTTP no seguro por defecto.

**Solución:** Ya está configurado en el proyecto mediante `network_security_config.xml` y `android:usesCleartextTraffic="true"` en el manifest.

### El emulador es muy lento

**Soluciones:**
- Usa una imagen de sistema **x86_64** en lugar de ARM
- Habilita **Hardware Acceleration** en la configuración del emulador
- Asigna más RAM al emulador (2GB o más)
- Asegúrate de tener **Intel HAXM** o **AMD Hypervisor** instalado

### La app se cierra al hacer login

**Causas posibles:**
- Error de conexión al servicio SOAP
- NetworkOnMainThreadException (ya solucionado con AsyncTask)

**Solución:**
- Revisa los logs en Android Studio (Logcat)
- Busca excepciones marcadas con el tag "SOAPClient"

## 📚 Dependencias Utilizadas

```gradle
// Cliente SOAP para Android
implementation 'com.google.code.ksoap2-android:ksoap2-android:3.6.4'

// Material Design Components
implementation 'com.google.android.material:material:1.10.0'

// AndroidX
implementation 'androidx.appcompat:appcompat:1.6.1'
implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
```

## 🔐 Seguridad

**ADVERTENCIA:** Este proyecto usa credenciales quemadas en el código solo para propósitos educativos. En un entorno de producción:

- Usa autenticación real contra el servicio SOAP
- Implementa tokens de sesión
- Usa HTTPS en lugar de HTTP
- No almacenes credenciales en texto plano

## 📞 Soporte

Para más información sobre el servicio SOAP, consulta el WSDL en:
```
http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
```

## 📝 Notas Adicionales

### Personalizar la interfaz del cliente SOAP

Si necesitas llamar a métodos específicos de tu servicio SOAP, edita `SOAPClient.java`:

```java
// Ejemplo de método personalizado
public void validarUsuario(String usuario, SOAPCallback callback) {
    callSOAPMethod("validarUsuario", "usuario", usuario, callback);
}
```

Y luego úsalo en `LoginActivity.java`:

```java
soapClient.validarUsuario(username, new SOAPClient.SOAPCallback() {
    @Override
    public void onSuccess(String result) {
        // Manejar respuesta exitosa
        loginSuccess(username);
    }
    
    @Override
    public void onError(String error) {
        // Manejar error
        Toast.makeText(LoginActivity.this, error, Toast.LENGTH_SHORT).show();
    }
});
```

### Logs y Debugging

Para ver los logs de las peticiones SOAP:
1. Abre **Logcat** en Android Studio
2. Filtra por el tag "SOAPClient"
3. Verás el XML de request y response de cada llamada

---

**Desarrollado para:** Arquitectura G5 - TI1.1 SOAP_JAVA_SINBDD_GR05  
**Versión:** 1.0  
**Fecha:** 3 de noviembre de 2025
