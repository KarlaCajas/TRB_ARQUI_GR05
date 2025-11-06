package ec.edu.monster.vista;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;
import ec.edu.monster.R;
import android.graphics.drawable.GradientDrawable;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Obtener referencia a los botones
        Button btnTransformaciones = findViewById(R.id.btnIrTransformaciones);
        Button btnCerrarSesion = findViewById(R.id.btnCerrarSesion);

        // Paleta de colores moderna y atractiva
        int colorBtnTransform = Color.parseColor("#6200EE");  // Morado moderno
        int colorBtnCerrar = Color.parseColor("#03DAC6");    // Verde azulado
        int colorTextLight = Color.WHITE;
        int colorBorder = Color.parseColor("#3700B3");       // Borde morado oscuro
        int colorBorderCerrar = Color.parseColor("#018786"); // Borde verde oscuro

        // Estilo para el botón de Transformaciones (Degradado morado)
        GradientDrawable shapeTransform = new GradientDrawable();
        shapeTransform.setShape(GradientDrawable.RECTANGLE);
        shapeTransform.setCornerRadius(24);
        shapeTransform.setColors(new int[]{
                Color.parseColor("#7F39FB"),  // Morado claro
                Color.parseColor("#6200EE")   // Morado oscuro
        });
        shapeTransform.setOrientation(GradientDrawable.Orientation.LEFT_RIGHT);
        shapeTransform.setStroke(4, colorBorder);
        btnTransformaciones.setBackground(shapeTransform);
        btnTransformaciones.setTextColor(colorTextLight);
        btnTransformaciones.setTextSize(18);
        btnTransformaciones.setElevation(8);  // Sombra suave

        // Estilo para el botón de Cerrar Sesión (Degradado verde azulado)
        GradientDrawable shapeCerrar = new GradientDrawable();
        shapeCerrar.setShape(GradientDrawable.RECTANGLE);
        shapeCerrar.setCornerRadius(24);
        shapeCerrar.setColors(new int[]{
                Color.parseColor("#03DAC6"),  // Verde azulado claro
                Color.parseColor("#018786")   // Verde azulado oscuro
        });
        shapeCerrar.setOrientation(GradientDrawable.Orientation.LEFT_RIGHT);
        shapeCerrar.setStroke(4, colorBorderCerrar);
        btnCerrarSesion.setBackground(shapeCerrar);
        btnCerrarSesion.setTextColor(Color.BLACK);  // Texto negro para mejor contraste
        btnCerrarSesion.setTextSize(18);
        btnCerrarSesion.setElevation(8);

        // Ajustar padding para mejor aspecto
        int paddingHorizontal = 40;
        int paddingVertical = 20;
        btnTransformaciones.setPadding(paddingHorizontal, paddingVertical, paddingHorizontal, paddingVertical);
        btnCerrarSesion.setPadding(paddingHorizontal, paddingVertical, paddingHorizontal, paddingVertical);

        // Listeners manteniendo la funcionalidad original
        btnTransformaciones.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, TransformacionesActivity.class);
            startActivity(intent);
        });

        btnCerrarSesion.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });
    }
}