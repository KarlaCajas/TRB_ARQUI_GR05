# Guía Rápida de Configuración

## Para Emulador

1. Abre el proyecto en Android Studio
2. Crea un emulador Android (API 30+)
3. Asegúrate de que tu servicio SOAP esté corriendo en `http://localhost:8080`
4. Ejecuta la app (▶️)
5. Login con:
   - Usuario: `MONSTER`
   - Contraseña: `Monster9`

## Para Dispositivo Físico

### Paso 1: Obtener tu IP local
```powershell
ipconfig
```
Anota tu dirección IPv4 (ej: 192.168.1.5)

### Paso 2: Modificar LoginActivity.java
```java
// Línea 33, cambiar de:
soapClient = new SOAPClient(SOAP_URL_EMULATOR);

// A:
soapClient = new SOAPClient(SOAP_URL_DEVICE);

// Y en línea 22, cambiar la IP:
private static final String SOAP_URL_DEVICE = "http://192.168.1.5:8080/ConUni_Soap_Java_GR05/CONUNI";
```

### Paso 3: Configurar Firewall
```powershell
# Como Administrador:
New-NetFirewallRule -DisplayName "SOAP Server 8080" -Direction Inbound -LocalPort 8080 -Protocol TCP -Action Allow
```

### Paso 4: Conectar celular
1. Habilita depuración USB en tu celular
2. Conecta por USB y autoriza
3. Asegúrate de estar en la misma red WiFi
4. Ejecuta la app desde Android Studio

### Paso 5: Verificar conexión
Desde el navegador del celular, visita:
```
http://TU_IP:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
```

Si ves el XML del WSDL, ¡todo está listo!

## Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| No conecta en emulador | Usa `10.0.2.2` en lugar de `localhost` |
| No conecta en celular | Verifica que estés en la misma WiFi |
| Firewall bloquea | Ejecuta el comando de firewall como admin |
| App muy lenta | Usa emulador x86_64 con HAXM |
| HTTP no permitido | Ya está configurado en el proyecto |

## Estructura de Archivos Importante

```
LoginActivity.java  → Maneja el login y conexión SOAP
SOAPClient.java     → Cliente genérico para llamadas SOAP
MainActivity.java   → Pantalla después del login exitoso
network_security_config.xml → Permite HTTP (no solo HTTPS)
```

## Personalizar para tu WSDL

Si tu servicio tiene métodos específicos, edita `SOAPClient.java`:

```java
public void tuMetodo(String param, SOAPCallback callback) {
    callSOAPMethod("nombreMetodo", "nombreParam", param, callback);
}
```

Luego usa en LoginActivity:
```java
soapClient.tuMetodo(valor, callback);
```
