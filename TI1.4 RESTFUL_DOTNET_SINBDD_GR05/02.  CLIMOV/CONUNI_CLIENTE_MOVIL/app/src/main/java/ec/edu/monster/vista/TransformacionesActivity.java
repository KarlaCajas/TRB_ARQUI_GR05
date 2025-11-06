package ec.edu.monster.vista;

import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.AdapterView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

import ec.edu.monster.R;
import ec.edu.monster.controlador.ApiService;
import ec.edu.monster.modelo.ConversionRequest;
import ec.edu.monster.modelo.ConversionResponse;

public class TransformacionesActivity extends AppCompatActivity {

    private TextView tvTitulo, tvResultado;
    private Spinner spinnerConversion;
    private EditText etValor;
    private Button btnConvertir, btnVolver, btnLimpiar;
    private ImageButton btnAtras;
    private ProgressBar progressBar;
    private ImageView ivIconoResultado, ivIconoCategoria;
    
    private String tipoConversion;
    private ApiService apiService;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_transformaciones);

        // Obtener el tipo de conversión
        tipoConversion = getIntent().getStringExtra("TIPO_CONVERSION");

        // Inicializar vistas
        tvTitulo = findViewById(R.id.tvTitulo);
        spinnerConversion = findViewById(R.id.spinnerConversion);
        etValor = findViewById(R.id.etValor);
        btnConvertir = findViewById(R.id.btnConvertir);
        btnLimpiar = findViewById(R.id.btnLimpiar);
        btnVolver = findViewById(R.id.btnVolver);
        btnAtras = findViewById(R.id.btnAtras);
        tvResultado = findViewById(R.id.tvResultado);
        progressBar = findViewById(R.id.progressBar);
        ivIconoResultado = findViewById(R.id.ivIconoResultado);
        ivIconoCategoria = findViewById(R.id.ivIconoCategoria);

        // Inicializar servicio API
        apiService = new ApiService();

        // Configurar título
        tvTitulo.setText("Conversión de " + tipoConversion);

        // Configurar spinner según el tipo
        configurarSpinner();
        
        // Configurar iconos iniciales
        actualizarIcono();
        actualizarIconoCategoria();
        
        // Listener para cambiar icono al seleccionar conversión
        spinnerConversion.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                actualizarIcono();
            }
            
            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });

        // Listeners
        btnConvertir.setOnClickListener(v -> realizarConversion());
        btnLimpiar.setOnClickListener(v -> limpiarCampos());
        btnVolver.setOnClickListener(v -> finish());
        btnAtras.setOnClickListener(v -> finish());
    }
    
    private void limpiarCampos() {
        etValor.setText("");
        tvResultado.setText("Ingrese los datos y presione CONVERTIR");
        etValor.requestFocus();
    }
    
    private void actualizarIcono() {
        int iconoResId;
        switch (tipoConversion) {
            case "Temperatura":
                iconoResId = R.drawable.ic_temperature;
                break;
            case "Masa":
                iconoResId = R.drawable.ic_weight;
                break;
            case "Longitud":
                iconoResId = R.drawable.ic_ruler;
                break;
            default:
                iconoResId = R.drawable.ic_result;
        }
        if (ivIconoResultado != null) {
            ivIconoResultado.setImageResource(iconoResId);
        }
    }
    
    private void actualizarIconoCategoria() {
        int iconoResId;
        switch (tipoConversion) {
            case "Temperatura":
                iconoResId = R.drawable.ic_temperature;
                break;
            case "Masa":
                iconoResId = R.drawable.ic_weight;
                break;
            case "Longitud":
                iconoResId = R.drawable.ic_ruler;
                break;
            default:
                iconoResId = R.drawable.ic_result;
        }
        if (ivIconoCategoria != null) {
            ivIconoCategoria.setImageResource(iconoResId);
        }
    }

    private void configurarSpinner() {
        List<String> opciones = new ArrayList<>();
        
        switch (tipoConversion) {
            case "Temperatura":
                opciones.add("Celsius a Fahrenheit");
                opciones.add("Fahrenheit a Celsius");
                opciones.add("Celsius a Kelvin");
                break;
            case "Masa":
                opciones.add("Kilogramos a Gramos");
                opciones.add("Gramos a Miligramos");
                opciones.add("Toneladas a Kilogramos");
                break;
            case "Longitud":
                opciones.add("Kilómetros a Metros");
                opciones.add("Metros a Centímetros");
                opciones.add("Centímetros a Milímetros");
                break;
        }

        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, 
                android.R.layout.simple_spinner_item, opciones);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerConversion.setAdapter(adapter);
    }

    private void realizarConversion() {
        String valorStr = etValor.getText().toString().trim();
        
        if (valorStr.isEmpty()) {
            Toast.makeText(this, "Por favor ingrese un valor", Toast.LENGTH_SHORT).show();
            return;
        }

        double valor;
        try {
            valor = Double.parseDouble(valorStr);
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Valor inválido", Toast.LENGTH_SHORT).show();
            return;
        }

        String conversionSeleccionada = spinnerConversion.getSelectedItem().toString();
        String[] partes = obtenerUnidades(conversionSeleccionada);
        
        if (partes == null) {
            Toast.makeText(this, "Error al procesar conversión", Toast.LENGTH_SHORT).show();
            return;
        }

        String unidadOrigen = partes[0];
        String unidadDestino = partes[1];

        // Crear request
        ConversionRequest request = new ConversionRequest(tipoConversion, unidadOrigen, unidadDestino, valor);

        // Mostrar loading
        progressBar.setVisibility(View.VISIBLE);
        btnConvertir.setEnabled(false);
        tvResultado.setText("");

        // Llamar a la API
        apiService.realizarConversion(request, new ApiService.ApiCallback() {
            @Override
            public void onSuccess(ConversionResponse response) {
                progressBar.setVisibility(View.GONE);
                btnConvertir.setEnabled(true);
                
                String nombreUnidadCompleto = obtenerNombreUnidadCompleto(unidadDestino, response.getResultado());
                String resultado = String.format("Resultado: %.4f %s", 
                        response.getResultado(), nombreUnidadCompleto);
                tvResultado.setText(resultado);
                tvResultado.setVisibility(View.VISIBLE);
            }

            @Override
            public void onError(String error) {
                progressBar.setVisibility(View.GONE);
                btnConvertir.setEnabled(true);
                Toast.makeText(TransformacionesActivity.this, 
                        "Error: " + error, Toast.LENGTH_LONG).show();
            }
        });
    }
    
    private String obtenerNombreUnidadCompleto(String unidadBase, double valor) {
        String nombre;
        
        // Normalizar a minúsculas para comparación
        String unidad = unidadBase.toLowerCase();
        
        switch (unidad) {
            // Temperatura
            case "celsius":
                nombre = "grados Celsius";
                break;
            case "fahrenheit":
                nombre = "grados Fahrenheit";
                break;
            case "kelvin":
                nombre = "Kelvin";
                break;
            
            // Masa
            case "kilogramo":
                nombre = "kilogramos";
                break;
            case "gramo":
                nombre = "gramos";
                break;
            case "miligramo":
                nombre = "miligramos";
                break;
            case "tonelada":
                nombre = "toneladas";
                break;
            
            // Longitud
            case "kilometro":
                nombre = "kilómetros";
                break;
            case "metro":
                nombre = "metros";
                break;
            case "centimetro":
                nombre = "centímetros";
                break;
            case "milimetro":
                nombre = "milímetros";
                break;
            
            default:
                nombre = unidadBase;
        }
        
        return nombre;
    }

    private String[] obtenerUnidades(String conversion) {
        String[] unidades = new String[2];
        
        switch (conversion) {
            // Temperatura
            case "Celsius a Fahrenheit":
                unidades[0] = "Celsius";
                unidades[1] = "Fahrenheit";
                break;
            case "Fahrenheit a Celsius":
                unidades[0] = "Fahrenheit";
                unidades[1] = "Celsius";
                break;
            case "Celsius a Kelvin":
                unidades[0] = "Celsius";
                unidades[1] = "Kelvin";
                break;
            
            // Masa - CORREGIDO: singular y sin acentos
            case "Kilogramos a Gramos":
                unidades[0] = "Kilogramo";
                unidades[1] = "Gramo";
                break;
            case "Gramos a Miligramos":
                unidades[0] = "Gramo";
                unidades[1] = "Miligramo";
                break;
            case "Toneladas a Kilogramos":
                unidades[0] = "Tonelada";
                unidades[1] = "Kilogramo";
                break;
            
            // Longitud - CORREGIDO: singular y sin acentos
            case "Kilómetros a Metros":
                unidades[0] = "Kilometro";
                unidades[1] = "Metro";
                break;
            case "Metros a Centímetros":
                unidades[0] = "Metro";
                unidades[1] = "Centimetro";
                break;
            case "Centímetros a Milímetros":
                unidades[0] = "Centimetro";
                unidades[1] = "Milimetro";
                break;
            
            default:
                return null;
        }
        
        return unidades;
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (apiService != null) {
            apiService.shutdown();
        }
    }
}
