package ec.edu.monster.vista;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import ec.edu.monster.R;
import ec.edu.monster.controlador.LoginController;

public class LoginActivity extends AppCompatActivity {
    private EditText etUsername, etPassword;
    private Button btnLogin;
    private LoginController loginController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login); // Muestra login

        etUsername = findViewById(R.id.etUsername);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);

        loginController = new LoginController();

        // Estilo para EditTexts
        etUsername.setBackgroundColor(Color.parseColor("#88000000")); // Negro semitransparente
        etUsername.setTextColor(Color.WHITE);
        etUsername.setHintTextColor(Color.LTGRAY);

        etPassword.setBackgroundColor(Color.parseColor("#88000000"));
        etPassword.setTextColor(Color.WHITE);
        etPassword.setHintTextColor(Color.LTGRAY);

        // Estilo para botón de login
        btnLogin.setBackgroundColor(Color.parseColor("#4CAF50")); // Verde suave
        btnLogin.setTextColor(Color.WHITE);

        btnLogin.setOnClickListener(v -> {
            String user = etUsername.getText().toString();
            String pass = etPassword.getText().toString();

            if (loginController.autenticar(user, pass)) {
                startActivity(new Intent(this, MainActivity.class));
                finish();
            } else {
                Toast.makeText(this, "Credenciales inválidas", Toast.LENGTH_SHORT).show();
            }
        });
    }
}