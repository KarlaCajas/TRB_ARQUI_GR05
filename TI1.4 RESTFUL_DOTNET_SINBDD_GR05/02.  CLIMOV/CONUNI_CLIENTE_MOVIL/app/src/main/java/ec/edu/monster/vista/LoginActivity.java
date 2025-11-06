package ec.edu.monster.vista;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import ec.edu.monster.R;

public class LoginActivity extends AppCompatActivity {
    
    private EditText etUsuario, etPassword;
    private Button btnLogin;

    private static final String USUARIO_CORRECTO = "MONSTER";
    private static final String PASSWORD_CORRECTO = "Monster9";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        // Inicializar vistas
        etUsuario = findViewById(R.id.etUsuario);
        etPassword = findViewById(R.id.etPassword);
        btnLogin = findViewById(R.id.btnLogin);

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                validarLogin();
            }
        });
    }

    private void validarLogin() {
        String usuario = etUsuario.getText().toString().trim();
        String password = etPassword.getText().toString();

        if (usuario.isEmpty() || password.isEmpty()) {
            Toast.makeText(this, "Por favor complete todos los campos", Toast.LENGTH_SHORT).show();
            return;
        }

        if (usuario.equals(USUARIO_CORRECTO) && password.equals(PASSWORD_CORRECTO)) {
            Toast.makeText(this, "¡Bienvenido!", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(LoginActivity.this, MainActivity.class);
            intent.putExtra("NOMBRE_USUARIO", USUARIO_CORRECTO);
            startActivity(intent);
            finish();
        } else {
            Toast.makeText(this, "Usuario o contraseña incorrectos", Toast.LENGTH_SHORT).show();
            etPassword.setText("");
        }
    }
}
