package ec.edu.monster.controlador;

import android.os.Handler;
import android.os.Looper;
import android.util.Log;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import ec.edu.monster.modelo.ConversionRequest;
import ec.edu.monster.modelo.ConversionResponse;

public class ApiService {
    // URLs disponibles - puedes cambiar según tu ubicación
    // Para emulador (servidor local): http://10.0.2.2:5014/api/ConversionUnidades_Controlador
    // Para WiFi casa: http://192.168.10.104:5014/api/ConversionUnidades_Controlador
    // Para Universidad: http://10.40.17.85:5014/api/ConversionUnidades_Controlador
    
    private static final String BASE_URL = "http://10.40.17.85:5014/api/ConversionUnidades_Controlador"; // Universidad
    private static final int TIMEOUT = 5000; // 5 segundos
    
    private final ExecutorService executorService;
    private final Handler mainHandler;

    public ApiService() {
        this.executorService = Executors.newSingleThreadExecutor();
        this.mainHandler = new Handler(Looper.getMainLooper());
    }

    public interface ApiCallback {
        void onSuccess(ConversionResponse response);
        void onError(String error);
    }

    public void realizarConversion(ConversionRequest request, ApiCallback callback) {
        executorService.execute(() -> {
            HttpURLConnection connection = null;
            try {
                // Construir URL con parámetros GET - solo los que el servidor espera
                String urlWithParams = BASE_URL + 
                    "?valor=" + request.getValor() +
                    "&unidadOrigen=" + URLEncoder.encode(request.getUnidadOrigen(), "UTF-8") +
                    "&unidadDestino=" + URLEncoder.encode(request.getUnidadDestino(), "UTF-8");
                
                android.util.Log.d("ApiService", "URL: " + urlWithParams);
                
                URL url = new URL(urlWithParams);
                connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                connection.setRequestProperty("Accept", "application/json");
                connection.setConnectTimeout(TIMEOUT);
                connection.setReadTimeout(TIMEOUT);

                // Leer respuesta
                int responseCode = connection.getResponseCode();
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(), "UTF-8"));
                    StringBuilder response = new StringBuilder();
                    String line;
                    while ((line = br.readLine()) != null) {
                        response.append(line);
                    }
                    br.close();

                    // Parsear respuesta
                    JSONObject jsonResponse = new JSONObject(response.toString());
                    ConversionResponse conversionResponse = new ConversionResponse();
                    conversionResponse.setResultado(jsonResponse.getDouble("resultado"));
                    conversionResponse.setMensaje(jsonResponse.optString("mensaje", ""));
                    conversionResponse.setExito(jsonResponse.optBoolean("exito", true));

                    // Callback en el hilo principal
                    mainHandler.post(() -> callback.onSuccess(conversionResponse));
                } else {
                    String errorMsg = "Servidor no responde correctamente (código: " + responseCode + ")";
                    mainHandler.post(() -> callback.onError(errorMsg));
                }

            } catch (java.net.SocketTimeoutException e) {
                mainHandler.post(() -> callback.onError("Tiempo de espera agotado. Verifica que el servidor esté ejecutándose."));
            } catch (java.net.ConnectException e) {
                mainHandler.post(() -> callback.onError("No se puede conectar al servidor. Verifica:\n1. Servidor ejecutándose\n2. Misma red WiFi\n3. Firewall desactivado"));
            } catch (java.net.UnknownHostException e) {
                mainHandler.post(() -> callback.onError("No se encuentra el servidor en " + BASE_URL));
            } catch (Exception e) {
                mainHandler.post(() -> callback.onError("Error: " + e.getMessage()));
            } finally {
                if (connection != null) {
                    connection.disconnect();
                }
            }
        });
    }

    public void shutdown() {
        executorService.shutdown();
    }
}
