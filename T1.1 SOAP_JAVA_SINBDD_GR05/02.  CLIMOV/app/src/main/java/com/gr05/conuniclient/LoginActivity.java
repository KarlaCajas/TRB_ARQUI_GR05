package com.gr05.conuniclient;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;

/**
 * Activity de Login con credenciales quemadas
 * Usuario: MONSTER
 * Contraseña: Monster9
 */
public class LoginActivity extends AppCompatActivity {
    
    // Credenciales quemadas
    private static final String VALID_USERNAME = "MONSTER";
    private static final String VALID_PASSWORD = "Monster9";
    
    private TextInputEditText etUsername, etPassword;
    private MaterialButton btnLogin;
    private View progressBar;
    
    // Para emulador: 10.0.2.2
    // Para dispositivo físico: cambiar por IP de tu PC (ej: 192.168.1.5)
    private static final String SOAP_URL_EMULATOR = "http://10.0.2.2:8080/ConUni_Soap_Java_GR05/CONUNI";
    private static final String SOAP_URL_DEVICE = "http://192.168.1.5:8080/ConUni_Soap_Java_GR05/CONUNI";
    
    private SOAPClient soapClient;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        
        // Verificar si ya está logueado
        if (isLoggedIn()) {
            navigateToMain();
            return;
        }
        
        initViews();
        setupListeners();
        
        // Inicializar cliente SOAP (usar URL del emulador por defecto)
        // Cambiar a SOAP_URL_DEVICE si vas a probar en dispositivo físico
        soapClient = new SOAPClient(SOAP_URL_EMULATOR);
    }
    
    private void initViews() {
        etUsername = findViewById(R.id.etUsername);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);
        progressBar = findViewById(R.id.progressBar);
    }
    
    private void setupListeners() {
        btnLogin.setOnClickListener(v -> attemptLogin());
    }
    
    private void attemptLogin() {
        // Obtener valores
        String username = etUsername.getText().toString().trim();
        String password = etPassword.getText().toString().trim();
        
        // Validar campos vacíos
        if (TextUtils.isEmpty(username) || TextUtils.isEmpty(password)) {
            Toast.makeText(this, R.string.empty_fields, Toast.LENGTH_SHORT).show();
            return;
        }
        
        // Validar credenciales
        if (username.equals(VALID_USERNAME) && password.equals(VALID_PASSWORD)) {
            showLoading(true);
            
            // Intentar conectar con el servicio SOAP
            testSOAPConnection(username);
        } else {
            Toast.makeText(this, R.string.login_error, Toast.LENGTH_SHORT).show();
        }
    }
    
    private void testSOAPConnection(String username) {
        // Aquí puedes llamar a un método real de tu servicio SOAP
        // Por ahora, simulamos una conexión exitosa
        
        // Ejemplo de llamada SOAP (descomentar y ajustar según tu WSDL):
        /*
        soapClient.callSOAPMethod("validarUsuario", "usuario", username, new SOAPClient.SOAPCallback() {
            @Override
            public void onSuccess(String result) {
                runOnUiThread(() -> {
                    showLoading(false);
                    loginSuccess(username);
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
        */
        
        // Simulación: login exitoso después de 1 segundo
        btnLogin.postDelayed(() -> {
            showLoading(false);
            loginSuccess(username);
        }, 1000);
    }
    
    private void loginSuccess(String username) {
        // Guardar sesión
        saveLoginSession(username);
        
        // Mostrar mensaje
        Toast.makeText(this, R.string.login_success, Toast.LENGTH_SHORT).show();
        
        // Navegar a MainActivity
        navigateToMain();
    }
    
    private void showLoading(boolean show) {
        progressBar.setVisibility(show ? View.VISIBLE : View.GONE);
        btnLogin.setEnabled(!show);
        etUsername.setEnabled(!show);
        etPassword.setEnabled(!show);
    }
    
    private void saveLoginSession(String username) {
        SharedPreferences prefs = getSharedPreferences("LoginPrefs", MODE_PRIVATE);
        prefs.edit()
                .putBoolean("isLoggedIn", true)
                .putString("username", username)
                .apply();
    }
    
    private boolean isLoggedIn() {
        SharedPreferences prefs = getSharedPreferences("LoginPrefs", MODE_PRIVATE);
        return prefs.getBoolean("isLoggedIn", false);
    }
    
    private void navigateToMain() {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
        finish();
    }
}
