# Cómo Adaptar el Cliente al WSDL Real

## 1. Analizar tu WSDL

Primero, abre tu WSDL en el navegador:
```
http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
```

Busca estos elementos importantes:

### targetNamespace
```xml
<definitions targetNamespace="http://ws.conuni.com/">
```
Este es tu **NAMESPACE** (ya está configurado en SOAPClient.java)

### Operaciones disponibles
```xml
<portType name="...">
    <operation name="validarUsuario">
        <input message="..."/>
        <output message="..."/>
    </operation>
    <operation name="obtenerDatos">
        <input message="..."/>
        <output message="..."/>
    </operation>
</portType>
```

### Mensajes y parámetros
```xml
<message name="validarUsuario">
    <part name="usuario" type="xsd:string"/>
    <part name="password" type="xsd:string"/>
</message>
```

## 2. Modificar SOAPClient.java

### Ejemplo 1: Método con un solo parámetro

Si tu WSDL tiene un método `obtenerUsuario` que recibe un `id`:

```java
// Agregar en SOAPClient.java
public void obtenerUsuario(String id, SOAPCallback callback) {
    callSOAPMethod("obtenerUsuario", "id", id, callback);
}
```

### Ejemplo 2: Método con múltiples parámetros

Si tu método `validarUsuario` recibe `usuario` y `password`:

```java
// Agregar en SOAPClient.java
public void validarUsuario(String usuario, String password, SOAPCallback callback) {
    new SOAPTaskMultiParam("validarUsuario", usuario, password, callback).execute();
}

// Agregar esta clase interna
private class SOAPTaskMultiParam extends AsyncTask<Void, Void, String> {
    private String methodName;
    private String usuario;
    private String password;
    private SOAPCallback callback;
    private String errorMessage = null;
    
    public SOAPTaskMultiParam(String methodName, String usuario, String password, SOAPCallback callback) {
        this.methodName = methodName;
        this.usuario = usuario;
        this.password = password;
        this.callback = callback;
    }
    
    @Override
    protected String doInBackground(Void... voids) {
        try {
            SoapObject request = new SoapObject(NAMESPACE, methodName);
            request.addProperty("usuario", usuario);
            request.addProperty("password", password);
            
            SoapSerializationEnvelope envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
            envelope.setOutputSoapObject(request);
            envelope.dotNet = false;
            
            HttpTransportSE transport = new HttpTransportSE(SOAP_URL, 30000);
            transport.debug = true;
            
            String soapAction = NAMESPACE + methodName;
            transport.call(soapAction, envelope);
            
            Object response = envelope.getResponse();
            Log.d(TAG, "SOAP Response: " + response.toString());
            
            return response.toString();
        } catch (Exception e) {
            errorMessage = "Error SOAP: " + e.getMessage();
            Log.e(TAG, errorMessage, e);
            return null;
        }
    }
    
    @Override
    protected void onPostExecute(String result) {
        if (result != null && callback != null) {
            callback.onSuccess(result);
        } else if (callback != null) {
            callback.onError(errorMessage != null ? errorMessage : "Error desconocido");
        }
    }
}
```

### Ejemplo 3: Método sin parámetros

```java
public void listarTodos(SOAPCallback callback) {
    callSOAPMethod("listarTodos", null, null, callback);
}
```

## 3. Usar en LoginActivity.java

### Reemplazar la simulación con llamada real

Busca el método `testSOAPConnection` (línea ~70) y reemplaza:

```java
private void testSOAPConnection(String username) {
    // OPCIÓN A: Si tienes método validarUsuario con 2 parámetros
    String password = etPassword.getText().toString().trim();
    soapClient.validarUsuario(username, password, new SOAPClient.SOAPCallback() {
        @Override
        public void onSuccess(String result) {
            runOnUiThread(() -> {
                showLoading(false);
                // Parsear resultado si es necesario
                if (result.contains("true") || result.equals("1")) {
                    loginSuccess(username);
                } else {
                    Toast.makeText(LoginActivity.this, R.string.login_error, Toast.LENGTH_SHORT).show();
                }
            });
        }
        
        @Override
        public void onError(String error) {
            runOnUiThread(() -> {
                showLoading(false);
                Toast.makeText(LoginActivity.this, R.string.network_error + "\n" + error, Toast.LENGTH_LONG).show();
            });
        }
    });
    
    // OPCIÓN B: Si solo tienes método obtenerUsuario
    soapClient.obtenerUsuario(username, new SOAPClient.SOAPCallback() {
        @Override
        public void onSuccess(String result) {
            runOnUiThread(() -> {
                showLoading(false);
                // Validar que el usuario existe
                if (result != null && !result.isEmpty() && !result.equals("null")) {
                    loginSuccess(username);
                } else {
                    Toast.makeText(LoginActivity.this, R.string.login_error, Toast.LENGTH_SHORT).show();
                }
            });
        }
        
        @Override
        public void onError(String error) {
            runOnUiThread(() -> {
                showLoading(false);
                Toast.makeText(LoginActivity.this, R.string.network_error, Toast.LENGTH_SHORT).show();
            });
        }
    });
}
```

## 4. Agregar más funcionalidades en MainActivity

### Ejemplo: Listar datos

En `MainActivity.java`, puedes agregar más funcionalidades:

```java
private SOAPClient soapClient;
private TextView tvDatos;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    
    initViews();
    loadUserInfo();
    setupListeners();
    
    // Inicializar cliente SOAP
    soapClient = new SOAPClient("http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI");
    
    // Cargar datos
    cargarDatos();
}

private void cargarDatos() {
    soapClient.listarTodos(new SOAPClient.SOAPCallback() {
        @Override
        public void onSuccess(String result) {
            runOnUiThread(() -> {
                tvDatos.setText("Datos: " + result);
            });
        }
        
        @Override
        public void onError(String error) {
            runOnUiThread(() -> {
                Toast.makeText(MainActivity.this, "Error: " + error, Toast.LENGTH_SHORT).show();
            });
        }
    });
}
```

## 5. Parsear Respuestas XML Complejas

Si tu SOAP devuelve XML complejo, puedes parsearlo:

```java
import org.xmlpull.v1.XmlPullParser;
import org.xmlpull.v1.XmlPullParserFactory;
import java.io.StringReader;

private void parsearRespuesta(String xmlResponse) {
    try {
        XmlPullParserFactory factory = XmlPullParserFactory.newInstance();
        XmlPullParser parser = factory.newPullParser();
        parser.setInput(new StringReader(xmlResponse));
        
        int eventType = parser.getEventType();
        String currentTag = null;
        
        while (eventType != XmlPullParser.END_DOCUMENT) {
            switch (eventType) {
                case XmlPullParser.START_TAG:
                    currentTag = parser.getName();
                    break;
                    
                case XmlPullParser.TEXT:
                    String text = parser.getText();
                    if (currentTag != null && !text.trim().isEmpty()) {
                        Log.d(TAG, currentTag + ": " + text);
                        // Procesar según el tag
                    }
                    break;
            }
            eventType = parser.next();
        }
    } catch (Exception e) {
        Log.e(TAG, "Error parseando XML", e);
    }
}
```

## 6. Ejemplo Completo con WSDL Real

Supongamos que tu WSDL tiene estos métodos:

```xml
<operation name="login">
    <input><part name="user" type="string"/><part name="pass" type="string"/></input>
    <output><part name="return" type="boolean"/></output>
</operation>

<operation name="getUser">
    <input><part name="userId" type="int"/></input>
    <output><part name="return" type="string"/></output>
</operation>

<operation name="getAllUsers">
    <input/>
    <output><part name="return" type="string"/></output>
</operation>
```

### Implementación en SOAPClient.java:

```java
public void login(String user, String pass, SOAPCallback callback) {
    new LoginTask(user, pass, callback).execute();
}

public void getUser(int userId, SOAPCallback callback) {
    callSOAPMethod("getUser", "userId", String.valueOf(userId), callback);
}

public void getAllUsers(SOAPCallback callback) {
    callSOAPMethod("getAllUsers", null, null, callback);
}

private class LoginTask extends AsyncTask<Void, Void, String> {
    private String user, pass;
    private SOAPCallback callback;
    private String errorMessage = null;
    
    public LoginTask(String user, String pass, SOAPCallback callback) {
        this.user = user;
        this.pass = pass;
        this.callback = callback;
    }
    
    @Override
    protected String doInBackground(Void... voids) {
        try {
            SoapObject request = new SoapObject(NAMESPACE, "login");
            request.addProperty("user", user);
            request.addProperty("pass", pass);
            
            SoapSerializationEnvelope envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
            envelope.setOutputSoapObject(request);
            envelope.dotNet = false;
            
            HttpTransportSE transport = new HttpTransportSE(SOAP_URL, 30000);
            String soapAction = NAMESPACE + "login";
            transport.call(soapAction, envelope);
            
            Object response = envelope.getResponse();
            return response.toString();
        } catch (Exception e) {
            errorMessage = e.getMessage();
            return null;
        }
    }
    
    @Override
    protected void onPostExecute(String result) {
        if (result != null && callback != null) {
            callback.onSuccess(result);
        } else if (callback != null) {
            callback.onError(errorMessage != null ? errorMessage : "Error desconocido");
        }
    }
}
```

## 7. Debugging

Para ver las peticiones y respuestas SOAP completas:

```java
// En SOAPClient.java, en el método doInBackground:
transport.debug = true;
transport.call(soapAction, envelope);

Log.d(TAG, "=== REQUEST ===");
Log.d(TAG, transport.requestDump);
Log.d(TAG, "=== RESPONSE ===");
Log.d(TAG, transport.responseDump);
```

Luego revisa el Logcat en Android Studio filtrando por "SOAPClient".

## 8. Checklist de Adaptación

- [ ] Verificar el namespace en el WSDL
- [ ] Listar todas las operaciones disponibles
- [ ] Identificar parámetros de entrada de cada operación
- [ ] Identificar tipo de respuesta de cada operación
- [ ] Crear métodos en SOAPClient.java para cada operación
- [ ] Modificar LoginActivity para usar el método real de validación
- [ ] Probar cada método con logs para verificar request/response
- [ ] Manejar errores específicos de tu servicio
- [ ] Parsear respuestas complejas si es necesario

---

Con esta guía podrás adaptar el cliente a cualquier servicio SOAP que tengas definido en tu WSDL.
