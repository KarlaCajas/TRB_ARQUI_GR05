package com.example.andclie.ui.screens

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.draw.alpha
import com.example.andclie.R
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import java.net.URL

val SullivanSuccess = Color(0xFF27AE60)
val SullivanSuccessLight = Color(0xFFE8F8F5)
val SullivanWarning = Color(0xFFFF9800)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ConversionScreen(
    onLogout: () -> Unit
) {
    var selectedCategory by remember { mutableStateOf("") }
    var selectedConversion by remember { mutableStateOf("") }
    var inputValue by remember { mutableStateOf("") }
    var resultText by remember { mutableStateOf("Ingrese los datos y presione CONVERTIR") }
    var isLoading by remember { mutableStateOf(false) }
    var expandedCategory by remember { mutableStateOf(false) }
    var expandedConversion by remember { mutableStateOf(false) }
    
    val scope = rememberCoroutineScope()

    val categories = listOf("Longitud", "Temperatura", "Masa")
    
    val conversions = mapOf(
        "Longitud" to listOf(
            "Kilómetros → Metros" to "conversion/km-a-m",
            "Metros → Centímetros" to "conversion/m-a-cm",
            "Centímetros → Milímetros" to "conversion/cm-a-mm"
        ),
        "Temperatura" to listOf(
            "Celsius → Fahrenheit" to "conversion/celsius-a-fahrenheit",
            "Fahrenheit → Celsius" to "conversion/fahrenheit-a-celsius",
            "Celsius → Kelvin" to "conversion/celsius-a-kelvin"
        ),
        "Masa" to listOf(
            "Kilogramos → Gramos" to "conversion/kg-a-gramos",
            "Gramos → Miligramos" to "conversion/gramos-a-miligramos",
            "Toneladas → Kilogramos" to "conversion/toneladas-a-kg"
        )
    )

    Box(
        modifier = Modifier.fillMaxSize()
    ) {
        // Imagen de fondo
        Image(
            painter = painterResource(id = R.drawable.background_sullivan),
            contentDescription = "Background",
            modifier = Modifier
                .fillMaxSize()
                .alpha(0.2f),
            contentScale = ContentScale.Crop
        )
        
        // Contenido sobre el fondo
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(SullivanBackground.copy(alpha = 0.85f))
        ) {
        // Header
        Card(
            modifier = Modifier.fillMaxWidth(),
            colors = CardDefaults.cardColors(containerColor = SullivanPrimary),
            shape = RoundedCornerShape(0.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Text(
                    text = "🔧 CONVERSOR DE UNIDADES 🔧",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.Bold,
                    color = Color.White
                )
                Text(
                    text = "Sistema de conversiones",
                    fontSize = 12.sp,
                    color = Color.White
                )
            }
        }

        // Contenido principal
        Column(
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Card de configuración
            Card(
                modifier = Modifier.fillMaxWidth(),
                colors = CardDefaults.cardColors(containerColor = SullivanCardBackground),
                elevation = CardDefaults.cardElevation(defaultElevation = 4.dp),
                shape = RoundedCornerShape(16.dp)
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(20.dp),
                    verticalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    Text(
                        text = "📊 Configuración de Conversión",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold,
                        color = SullivanPrimaryDark
                    )

                    // Dropdown Categoría
                    ExposedDropdownMenuBox(
                        expanded = expandedCategory,
                        onExpandedChange = { expandedCategory = !expandedCategory }
                    ) {
                        OutlinedTextField(
                            value = selectedCategory,
                            onValueChange = {},
                            readOnly = true,
                            label = { Text("📂 Categoría") },
                            trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expandedCategory) },
                            modifier = Modifier
                                .fillMaxWidth()
                                .menuAnchor(),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedBorderColor = SullivanPrimary,
                                unfocusedBorderColor = Color.LightGray
                            )
                        )
                        ExposedDropdownMenu(
                            expanded = expandedCategory,
                            onDismissRequest = { expandedCategory = false }
                        ) {
                            categories.forEach { category ->
                                DropdownMenuItem(
                                    text = { Text(category) },
                                    onClick = {
                                        selectedCategory = category
                                        selectedConversion = ""
                                        expandedCategory = false
                                    }
                                )
                            }
                        }
                    }

                    // Dropdown Conversión
                    if (selectedCategory.isNotEmpty()) {
                        ExposedDropdownMenuBox(
                            expanded = expandedConversion,
                            onExpandedChange = { expandedConversion = !expandedConversion }
                        ) {
                            OutlinedTextField(
                                value = selectedConversion,
                                onValueChange = {},
                                readOnly = true,
                                label = { Text("🔄 Tipo de Conversión") },
                                trailingIcon = { ExposedDropdownMenuDefaults.TrailingIcon(expanded = expandedConversion) },
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .menuAnchor(),
                                colors = OutlinedTextFieldDefaults.colors(
                                    focusedBorderColor = SullivanPrimary,
                                    unfocusedBorderColor = Color.LightGray
                                )
                            )
                            ExposedDropdownMenu(
                                expanded = expandedConversion,
                                onDismissRequest = { expandedConversion = false }
                            ) {
                                conversions[selectedCategory]?.forEach { (name, _) ->
                                    DropdownMenuItem(
                                        text = { Text(name) },
                                        onClick = {
                                            selectedConversion = name
                                            expandedConversion = false
                                        }
                                    )
                                }
                            }
                        }
                    }

                    // Campo de valor
                    OutlinedTextField(
                        value = inputValue,
                        onValueChange = { inputValue = it },
                        label = { Text("🔢 Valor a Convertir") },
                        modifier = Modifier.fillMaxWidth(),
                        singleLine = true,
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedBorderColor = SullivanPrimary,
                            unfocusedBorderColor = Color.LightGray
                        )
                    )

                    // Botones
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Button(
                            onClick = {
                                scope.launch {
                                    performConversion(
                                        selectedCategory,
                                        selectedConversion,
                                        inputValue,
                                        conversions,
                                        onResult = { resultText = it },
                                        onLoadingChange = { isLoading = it }
                                    )
                                }
                            },
                            modifier = Modifier
                                .weight(1f)
                                .height(50.dp),
                            colors = ButtonDefaults.buttonColors(containerColor = SullivanSuccess),
                            enabled = !isLoading
                        ) {
                            if (isLoading) {
                                CircularProgressIndicator(
                                    modifier = Modifier.size(20.dp),
                                    color = Color.White,
                                    strokeWidth = 2.dp
                                )
                            } else {
                                Text("✅ CONVERTIR", fontWeight = FontWeight.Bold)
                            }
                        }

                        Button(
                            onClick = {
                                selectedCategory = ""
                                selectedConversion = ""
                                inputValue = ""
                                resultText = "Ingrese los datos y presione CONVERTIR"
                            },
                            modifier = Modifier
                                .weight(1f)
                                .height(50.dp),
                            colors = ButtonDefaults.buttonColors(containerColor = SullivanWarning)
                        ) {
                            Text("🗑️ LIMPIAR", fontWeight = FontWeight.Bold)
                        }
                    }
                }
            }

            // Card de resultado
            Card(
                modifier = Modifier.fillMaxWidth(),
                colors = CardDefaults.cardColors(containerColor = SullivanSuccessLight),
                elevation = CardDefaults.cardElevation(defaultElevation = 4.dp),
                shape = RoundedCornerShape(16.dp)
            ) {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(20.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "✨ Resultado de la Conversión ✨",
                        fontSize = 14.sp,
                        fontWeight = FontWeight.Bold,
                        color = SullivanSuccess
                    )
                    Spacer(modifier = Modifier.height(12.dp))
                    Text(
                        text = resultText,
                        fontSize = 13.sp,
                        fontWeight = FontWeight.Bold,
                        color = SullivanSuccess,
                        textAlign = TextAlign.Center
                    )
                }
            }

            // Botones de footer
            Button(
                onClick = onLogout,
                modifier = Modifier
                    .fillMaxWidth()
                    .height(50.dp),
                colors = ButtonDefaults.buttonColors(containerColor = SullivanError)
            ) {
                Text("🚪 CERRAR SESIÓN", fontSize = 12.sp, fontWeight = FontWeight.Bold)
            }
        }
        }
    }
}

suspend fun performConversion(
    category: String,
    conversion: String,
    value: String,
    conversions: Map<String, List<Pair<String, String>>>,
    onResult: (String) -> Unit,
    onLoadingChange: (Boolean) -> Unit
) {
    if (category.isEmpty() || conversion.isEmpty() || value.isEmpty()) {
        onResult("⚠️ Complete todos los campos")
        return
    }

    val numValue = value.toDoubleOrNull()
    if (numValue == null) {
        onResult("❌ Valor inválido")
        return
    }

    onLoadingChange(true)

    try {
        val endpoint = conversions[category]?.find { it.first == conversion }?.second
        if (endpoint == null) {
            onResult("❌ Conversión no encontrada")
            onLoadingChange(false)
            return
        }

        val baseUrl = "http://192.168.18.113:8080/WS_ConersionUnidades_RESTFULL/webresources/"
        // IP de tu PC en la red de casa: 192.168.18.113
        // Para Universidad: 10.40.16.230
        val url = "$baseUrl$endpoint/$numValue"

        val result = withContext(Dispatchers.IO) {
            try {
                val connection = URL(url).openConnection()
                connection.connectTimeout = 5000
                connection.readTimeout = 5000
                connection.getInputStream().bufferedReader().use { it.readText() }
            } catch (e: Exception) {
                throw Exception("Error de conexión: ${e.message}")
            }
        }

        onResult("✅ $value → ${result.toDouble().let { "%.4f".format(it) }}\n\n$conversion")
    } catch (e: Exception) {
        onResult("❌ Error: ${e.message}\n\nVerifica que el servidor esté activo")
    } finally {
        onLoadingChange(false)
    }
}
