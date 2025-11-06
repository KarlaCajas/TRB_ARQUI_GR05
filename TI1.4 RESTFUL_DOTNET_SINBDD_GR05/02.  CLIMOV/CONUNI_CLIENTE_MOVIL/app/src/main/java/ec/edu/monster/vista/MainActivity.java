package ec.edu.monster.vista;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import ec.edu.monster.R;

public class MainActivity extends AppCompatActivity {

    private CardView cardTemperatura, cardMasa, cardLongitud;
    private FloatingActionButton btnSalir;
    private TextView tvNombreUsuario;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar vistas
        cardTemperatura = findViewById(R.id.cardTemperatura);
        cardMasa = findViewById(R.id.cardMasa);
        cardLongitud = findViewById(R.id.cardLongitud);
        btnSalir = findViewById(R.id.btnSalir);
        tvNombreUsuario = findViewById(R.id.tvNombreUsuario);

        // Obtener nombre de usuario del intent
        String nombreUsuario = getIntent().getStringExtra("NOMBRE_USUARIO");
        if (nombreUsuario != null && !nombreUsuario.isEmpty()) {
            tvNombreUsuario.setText(nombreUsuario);
        }

        // Listeners
        cardTemperatura.setOnClickListener(v -> abrirConversiones("Temperatura"));
        cardMasa.setOnClickListener(v -> abrirConversiones("Masa"));
        cardLongitud.setOnClickListener(v -> abrirConversiones("Longitud"));

        btnSalir.setOnClickListener(v -> mostrarDialogoSalir());
    }

    private void abrirConversiones(String tipo) {
        Intent intent = new Intent(MainActivity.this, TransformacionesActivity.class);
        intent.putExtra("TIPO_CONVERSION", tipo);
        startActivity(intent);
    }

    private void mostrarDialogoSalir() {
        new AlertDialog.Builder(this)
                .setTitle("Salir")
                .setMessage("¿Desea cerrar sesión?")
                .setPositiveButton("Sí", (dialog, which) -> {
                    Intent intent = new Intent(MainActivity.this, LoginActivity.class);
                    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                    startActivity(intent);
                    finish();
                })
                .setNegativeButton("No", null)
                .show();
    }

    @Override
    public void onBackPressed() {
        mostrarDialogoSalir();
    }
}
