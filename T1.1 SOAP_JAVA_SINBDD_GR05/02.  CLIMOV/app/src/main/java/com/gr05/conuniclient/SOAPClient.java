package com.gr05.conuniclient;

import android.os.AsyncTask;
import android.util.Log;

import org.ksoap2.SoapEnvelope;
import org.ksoap2.serialization.SoapObject;
import org.ksoap2.serialization.SoapSerializationEnvelope;
import org.ksoap2.transport.HttpTransportSE;

/**
 * Cliente SOAP para consumir el servicio CONUNI
 * IMPORTANTE: Para el emulador usar 10.0.2.2 en lugar de localhost
 * Para dispositivo físico usar la IP local de tu PC (ej: 192.168.x.x)
 */
public class SOAPClient {
    
    private static final String TAG = "SOAPClient";
    
    // Para emulador: usar 10.0.2.2
    // Para dispositivo físico: cambiar por la IP de tu PC en la red local
    private static final String NAMESPACE = "http://ws.conuni.com/";
    private String SOAP_URL;
    
    public SOAPClient(String serverUrl) {
        this.SOAP_URL = serverUrl;
    }
    
    /**
     * Interface para callback de resultados
     */
    public interface SOAPCallback {
        void onSuccess(String result);
        void onError(String error);
    }
    
    /**
     * Método genérico para llamar a operaciones SOAP
     */
    public void callSOAPMethod(String methodName, String paramName, String paramValue, SOAPCallback callback) {
        new SOAPTask(methodName, paramName, paramValue, callback).execute();
    }
    
    /**
     * AsyncTask para ejecutar llamadas SOAP en segundo plano
     */
    private class SOAPTask extends AsyncTask<Void, Void, String> {
        
        private String methodName;
        private String paramName;
        private String paramValue;
        private SOAPCallback callback;
        private String errorMessage = null;
        
        public SOAPTask(String methodName, String paramName, String paramValue, SOAPCallback callback) {
            this.methodName = methodName;
            this.paramName = paramName;
            this.paramValue = paramValue;
            this.callback = callback;
        }
        
        @Override
        protected String doInBackground(Void... voids) {
            try {
                // Crear el objeto SOAP
                SoapObject request = new SoapObject(NAMESPACE, methodName);
                
                // Agregar parámetros si existen
                if (paramName != null && paramValue != null) {
                    request.addProperty(paramName, paramValue);
                }
                
                // Crear el envelope SOAP
                SoapSerializationEnvelope envelope = new SoapSerializationEnvelope(SoapEnvelope.VER11);
                envelope.setOutputSoapObject(request);
                envelope.dotNet = false;
                
                // Configurar transporte HTTP
                HttpTransportSE transport = new HttpTransportSE(SOAP_URL, 30000);
                transport.debug = true;
                
                // Realizar la llamada SOAP
                String soapAction = NAMESPACE + methodName;
                transport.call(soapAction, envelope);
                
                // Obtener la respuesta
                Object response = envelope.getResponse();
                
                Log.d(TAG, "SOAP Response: " + response.toString());
                Log.d(TAG, "Request XML: " + transport.requestDump);
                Log.d(TAG, "Response XML: " + transport.responseDump);
                
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
    
    /**
     * Método de prueba para validar conexión al servicio
     */
    public void testConnection(SOAPCallback callback) {
        // Ajusta este método según los métodos disponibles en tu WSDL
        callSOAPMethod("testMethod", null, null, callback);
    }
}
