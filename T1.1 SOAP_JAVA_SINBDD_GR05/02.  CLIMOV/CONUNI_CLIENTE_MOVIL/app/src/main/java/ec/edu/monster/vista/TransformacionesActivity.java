package ec.edu.monster.vista;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.HashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import ec.edu.monster.R;
import ec.edu.monster.controlador.TransformacionController;

public class TransformacionesActivity extends AppCompatActivity {

    private static final String TAG = "TransformacionesActivity";
    
    private LinearLayout layoutCategorias;
    private LinearLayout layoutConversiones;
    private LinearLayout layoutBotonesConversion;
    private LinearLayout layoutResultado;
    private EditText etValor;
    private TextView tvResultado;
    private Button btnConvertir;
    private Button btnVolver;
    
    private String categoriaSeleccionada = "";
    private String conversionSeleccionada = "";
    
    private ExecutorService executorService;
    private TransformacionController controller;
    
    // Mapas para las conversiones
    private HashMap<String, String[]> conversionesMap;
    private HashMap<String, String> metodoMap;
    private HashMap<String, String> unidadMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_transformaciones);

        executorService = Executors.newSingleThreadExecutor();
        controller = new TransformacionController();
        
        inicializarVistas();
        inicializarMapas();
        configurarEventos();
    }

    private void inicializarVistas() {
        layoutCategorias = findViewById(R.id.layoutCategorias);
        layoutConversiones = findViewById(R.id.layoutConversiones);
        layoutBotonesConversion = findViewById(R.id.layoutBotonesConversion);
        layoutResultado = findViewById(R.id.layoutResultado);
        etValor = findViewById(R.id.etValor);
        tvResultado = findViewById(R.id.tvResultado);
        btnConvertir = findViewById(R.id.btnConvertir);
        btnVolver = findViewById(R.id.btnVolver);
    }

    private void inicializarMapas() {
        conversionesMap = new HashMap<>();
        conversionesMap.put("MASA", new String[]{
            "Kilogramos → Gramos",
            "Gramos → Miligramos", 
            "Toneladas → Kilogramos"
        });
        conversionesMap.put("LONGITUD", new String[]{
            "Kilómetros → Metros",
            "Metros → Centímetros",
            "Centímetros → Milímetros"
        });
        conversionesMap.put("TEMPERATURA", new String[]{
            "Celsius → Fahrenheit",
            "Fahrenheit → Celsius",
            "Celsius → Kelvin"
        });

        metodoMap = new HashMap<>();
        metodoMap.put("Kilogramos → Gramos", "convertirKilogramosAGramos");
        metodoMap.put("Gramos → Miligramos", "convertirGramosAMiligramos");
        metodoMap.put("Toneladas → Kilogramos", "convertirToneladasAKilogramos");
        metodoMap.put("Kilómetros → Metros", "convertirKilometrosAMetros");
        metodoMap.put("Metros → Centímetros", "convertirMetrosACentimetros");
        metodoMap.put("Centímetros → Milímetros", "convertirCentimetrosAMilimetros");
        metodoMap.put("Celsius → Fahrenheit", "convertirCelsiusAFahrenheit");
        metodoMap.put("Fahrenheit → Celsius", "convertirFahrenheitACelsius");
        metodoMap.put("Celsius → Kelvin", "convertirCelsiusAKelvin");

        unidadMap = new HashMap<>();
        unidadMap.put("Kilogramos → Gramos", "g");
        unidadMap.put("Gramos → Miligramos", "mg");
        unidadMap.put("Toneladas → Kilogramos", "kg");
        unidadMap.put("Kilómetros → Metros", "m");
        unidadMap.put("Metros → Centímetros", "cm");
        unidadMap.put("Centímetros → Milímetros", "mm");
        unidadMap.put("Celsius → Fahrenheit", "°F");
        unidadMap.put("Fahrenheit → Celsius", "°C");
        unidadMap.put("Celsius → Kelvin", "K");
    }

    private void configurarEventos() {
        // Botones de categoría con iconos
        Button btnMasa = findViewById(R.id.btnMasa);
        btnMasa.setCompoundDrawablesWithIntrinsicBounds(R.drawable.ic_masa, 0, 0, 0);
        btnMasa.setCompoundDrawablePadding(24);
        btnMasa.setOnClickListener(v -> mostrarConversiones("MASA"));
        
        Button btnLongitud = findViewById(R.id.btnLongitud);
        btnLongitud.setCompoundDrawablesWithIntrinsicBounds(R.drawable.ic_longitud, 0, 0, 0);
        btnLongitud.setCompoundDrawablePadding(24);
        btnLongitud.setOnClickListener(v -> mostrarConversiones("LONGITUD"));
        
        Button btnTemperatura = findViewById(R.id.btnTemperatura);
        btnTemperatura.setCompoundDrawablesWithIntrinsicBounds(R.drawable.ic_temperatura, 0, 0, 0);
        btnTemperatura.setCompoundDrawablePadding(24);
        btnTemperatura.setOnClickListener(v -> mostrarConversiones("TEMPERATURA"));
        
        // Botón volver
        btnVolver.setOnClickListener(v -> volverACategorias());
        
        // Botón convertir
        btnConvertir.setOnClickListener(v -> realizarConversion());
        
        // Botón cerrar sesión
        findViewById(R.id.btnCerrarSesion).setOnClickListener(v -> {
            Intent intent = new Intent(TransformacionesActivity.this, LoginActivity.class);
            intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
            startActivity(intent);
            finish();
        });
    }

    private void mostrarConversiones(String categoria) {
        categoriaSeleccionada = categoria;
        layoutCategorias.setVisibility(View.GONE);
        layoutConversiones.setVisibility(View.VISIBLE);
        layoutResultado.setVisibility(View.GONE);
        
        // Limpiar botones anteriores
        layoutBotonesConversion.removeAllViews();
        
        // Crear botones de conversión
        String[] conversiones = conversionesMap.get(categoria);
        if (conversiones != null) {
            for (String conversion : conversiones) {
                Button btnConversion = new Button(this);
                LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                );
                params.setMargins(0, 0, 0, 16);
                btnConversion.setLayoutParams(params);
                btnConversion.setText(conversion);
                btnConversion.setTextColor(Color.BLACK);
                btnConversion.setBackgroundColor(Color.WHITE);
                btnConversion.setAllCaps(false);
                btnConversion.setPadding(32, 32, 32, 32);
                btnConversion.setElevation(4f);
                
                btnConversion.setOnClickListener(v -> {
                    conversionSeleccionada = conversion;
                    resaltarBotonSeleccionado(btnConversion);
                });
                
                layoutBotonesConversion.addView(btnConversion);
            }
        }
    }

    private void resaltarBotonSeleccionado(Button botonSeleccionado) {
        // Resetear todos los botones
        for (int i = 0; i < layoutBotonesConversion.getChildCount(); i++) {
            View child = layoutBotonesConversion.getChildAt(i);
            if (child instanceof Button) {
                child.setBackgroundColor(Color.WHITE);
            }
        }
        // Resaltar el seleccionado
        botonSeleccionado.setBackgroundColor(Color.parseColor("#1976D2"));
        botonSeleccionado.setTextColor(Color.WHITE);
    }

    private void volverACategorias() {
        layoutCategorias.setVisibility(View.VISIBLE);
        layoutConversiones.setVisibility(View.GONE);
        layoutResultado.setVisibility(View.GONE);
        etValor.setText("");
        conversionSeleccionada = "";
    }

    private void realizarConversion() {
        if (conversionSeleccionada.isEmpty()) {
            Toast.makeText(this, "Seleccione un tipo de conversión", Toast.LENGTH_SHORT).show();
            return;
        }

        String valorStr = etValor.getText().toString().trim();
        if (valorStr.isEmpty()) {
            Toast.makeText(this, "Ingrese un valor", Toast.LENGTH_SHORT).show();
            return;
        }

        try {
            double valor = Double.parseDouble(valorStr);
            String unidad = unidadMap.get(conversionSeleccionada);
            
            executorService.execute(() -> {
                try {
                    String resultado = null;
                    
                    // Llamar al método correcto según la conversión
                    switch (conversionSeleccionada) {
                        case "Kilogramos → Gramos":
                            resultado = controller.convertirKilogramosAGramos(valor);
                            break;
                        case "Gramos → Miligramos":
                            resultado = controller.convertirGramosAMiligramos(valor);
                            break;
                        case "Toneladas → Kilogramos":
                            resultado = controller.convertirToneladasAKilogramos(valor);
                            break;
                        case "Kilómetros → Metros":
                            resultado = controller.convertirKilometrosAMetros(valor);
                            break;
                        case "Metros → Centímetros":
                            resultado = controller.convertirMetrosACentimetros(valor);
                            break;
                        case "Centímetros → Milímetros":
                            resultado = controller.convertirCentimetrosAMilimetros(valor);
                            break;
                        case "Celsius → Fahrenheit":
                            resultado = controller.convertirCelsiusAFahrenheit(valor);
                            break;
                        case "Fahrenheit → Celsius":
                            resultado = controller.convertirFahrenheitACelsius(valor);
                            break;
                        case "Celsius → Kelvin":
                            resultado = controller.convertirCelsiusAKelvin(valor);
                            break;
                    }
                    
                    final String resultadoFinal = resultado;
                    Log.d(TAG, "Resultado del servicio: " + resultado);
                    
                    runOnUiThread(() -> {
                        try {
                            if (resultadoFinal != null && !resultadoFinal.isEmpty()) {
                                // Limpiar y parsear el resultado
                                String resultadoLimpio = resultadoFinal.replaceAll("[^0-9.-]", "");
                                double resultadoNumerico = Double.parseDouble(resultadoLimpio);
                                
                                // Formatear con 4 decimales y nombre completo de unidad
                                tvResultado.setText(String.format("%.4f %s", resultadoNumerico, unidad));
                                layoutResultado.setVisibility(View.VISIBLE);
                            } else {
                                mostrarError("Error: respuesta vacía del servidor");
                            }
                        } catch (NumberFormatException e) {
                            Log.e(TAG, "Error al parsear: " + resultadoFinal, e);
                            mostrarError("Error al procesar resultado: " + resultadoFinal);
                        }
                    });
                } catch (Exception e) {
                    Log.e(TAG, "Error en conversión", e);
                    runOnUiThread(() -> mostrarError("Error: " + e.getMessage()));
                }
            });
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Ingrese un número válido", Toast.LENGTH_SHORT).show();
        }
    }

    private void mostrarError(String mensaje) {
        runOnUiThread(() -> {
            Toast.makeText(this, mensaje, Toast.LENGTH_LONG).show();
            layoutResultado.setVisibility(View.GONE);
        });
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (executorService != null && !executorService.isShutdown()) {
            executorService.shutdown();
        }
    }
}
