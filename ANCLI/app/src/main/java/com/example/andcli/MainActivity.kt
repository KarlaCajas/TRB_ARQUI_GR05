package com.example.andcli

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.PasswordVisualTransformation
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.andcli.ui.theme.ANDCLITheme
import com.example.andcli.viewmodel.MainViewModel

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            ANDCLITheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    MainApp(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}

@Composable
fun MainApp(modifier: Modifier = Modifier) {
    val viewModel: MainViewModel = viewModel()
    val uiState by viewModel.uiState.collectAsState()
    
    if (uiState.isLoggedIn) {
        DashboardScreen(viewModel = viewModel, uiState = uiState, modifier = modifier)
    } else {
        LoginScreen(viewModel = viewModel, uiState = uiState, modifier = modifier)
    }
}@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LoginScreen(viewModel: MainViewModel, uiState: com.example.andcli.viewmodel.ConversionState, modifier: Modifier = Modifier) {
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }
    
    // Colores de Sullivan (azul Monsters University)
    val sullivanBlue = Color(0xFF0066CC)
    
    Box(
        modifier = modifier.fillMaxSize()
    ) {
        // Imagen de fondo
        Image(
            painter = painterResource(id = R.drawable.background_monsters),
            contentDescription = "Fondo Monsters",
            modifier = Modifier.fillMaxSize(),
            contentScale = ContentScale.Crop,
            alpha = 0.8f // Más visible la imagen
        )
        
        // Contenido encima del fondo
        Column(
            modifier = Modifier
                .fillMaxSize()
                .background(Color.White.copy(alpha = 0.65f)) // Menos opaco para ver mejor el fondo
                .padding(32.dp)
                .verticalScroll(rememberScrollState()),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Título centrado
            Text(
                text = "🎓 MONSTERS\nUNIVERSITY",
                style = MaterialTheme.typography.headlineLarge,
                fontWeight = FontWeight.Bold,
                color = sullivanBlue,
                textAlign = androidx.compose.ui.text.style.TextAlign.Center
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            Text(
                text = "Conversiones de Unidades",
                style = MaterialTheme.typography.titleMedium,
                color = Color.Gray,
                textAlign = androidx.compose.ui.text.style.TextAlign.Center
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            OutlinedTextField(
                value = username,
                onValueChange = { username = it },
                label = { Text("Usuario") },
                singleLine = true,
                modifier = Modifier.fillMaxWidth(),
                enabled = !uiState.isLoading,
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = sullivanBlue,
                    focusedLabelColor = sullivanBlue,
                    unfocusedContainerColor = Color.White
                )
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            OutlinedTextField(
                value = password,
                onValueChange = { password = it },
                label = { Text("Contraseña 🔒") },
                singleLine = true,
                visualTransformation = PasswordVisualTransformation(),
                modifier = Modifier.fillMaxWidth(),
                enabled = !uiState.isLoading,
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = sullivanBlue,
                    focusedLabelColor = sullivanBlue,
                    unfocusedContainerColor = Color.White
                )
            )
            
            Spacer(modifier = Modifier.height(32.dp))
            
            Button(
                onClick = { viewModel.login(username, password) },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(56.dp),
                enabled = !uiState.isLoading && username.isNotEmpty() && password.isNotEmpty(),
                colors = ButtonDefaults.buttonColors(
                    containerColor = sullivanBlue,
                    contentColor = Color.White
                ),
                shape = RoundedCornerShape(12.dp)
            ) {
                if (uiState.isLoading) {
                    CircularProgressIndicator(
                        modifier = Modifier.size(24.dp),
                        color = Color.White
                    )
                } else {
                    Text("Ingresar", fontWeight = FontWeight.Bold)
                }
            }
            
            if (uiState.error.isNotEmpty()) {
                Spacer(modifier = Modifier.height(16.dp))
                Card(
                    colors = CardDefaults.cardColors(
                        containerColor = Color(0xFFFFEBEE)
                    ),
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(12.dp)
                ) {
                    Text(
                        text = uiState.error,
                        modifier = Modifier.padding(16.dp),
                        color = Color(0xFFC62828),
                        textAlign = androidx.compose.ui.text.style.TextAlign.Center
                    )
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DashboardScreen(viewModel: MainViewModel, uiState: com.example.andcli.viewmodel.ConversionState, modifier: Modifier = Modifier) {
    var selectedCategoria by remember { mutableStateOf("") }
    var selectedTipo by remember { mutableStateOf("") }
    var valor by remember { mutableStateOf("") }
    
    // Colores de Sullivan
    val sullivanBlue = Color(0xFF0066CC)
    val lightBlue = Color(0xFF4DA6FF)
    val veryLightBlue = Color(0xFFE3F2FD)
    
    val conversiones = mapOf(
        "MASA" to listOf(
            "kg_lb" to "Kilogramos → Libras",
            "lb_kg" to "Libras → Kilogramos",
            "kg_oz" to "Kilogramos → Onzas"
        ),
        "LONGITUD" to listOf(
            "m_ft" to "Metros → Pies",
            "ft_m" to "Pies → Metros",
            "km_mi" to "Kilómetros → Millas"
        ),
        "TEMPERATURA" to listOf(
            "celsius_fahrenheit" to "Celsius → Fahrenheit",
            "fahrenheit_celsius" to "Fahrenheit → Celsius",
            "celsius_kelvin" to "Celsius → Kelvin"
        )
    )
    
    Scaffold(
        topBar = {
            TopAppBar(
                title = { 
                    Text(
                        "🎓 Conversiones MONSTER",
                        fontWeight = FontWeight.Bold,
                        textAlign = androidx.compose.ui.text.style.TextAlign.Center,
                        modifier = Modifier.fillMaxWidth()
                    ) 
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = sullivanBlue,
                    titleContentColor = Color.White,
                    actionIconContentColor = Color.White
                ),
                actions = {
                    TextButton(onClick = { viewModel.logout() }) {
                        Text("Salir 👋", color = Color.White)
                    }
                }
            )
        }
    ) { paddingValues ->
        Box(
            modifier = Modifier.fillMaxSize()
        ) {
            // Imagen de fondo
            Image(
                painter = painterResource(id = R.drawable.background_monsters),
                contentDescription = "Fondo Monsters",
                modifier = Modifier.fillMaxSize(),
                contentScale = ContentScale.Crop,
                alpha = 0.6f // Más visible
            )
            
            // Contenido encima del fondo
            Column(
                modifier = modifier
                    .fillMaxSize()
                    .background(Color.White.copy(alpha = 0.75f)) // Menos opaco
                    .padding(paddingValues)
                    .padding(16.dp)
                    .verticalScroll(rememberScrollState())
            ) {
                Text(
                    text = "🔄 Conversión de Unidades",
                    style = MaterialTheme.typography.headlineSmall,
                    fontWeight = FontWeight.Bold,
                    color = sullivanBlue,
                    textAlign = androidx.compose.ui.text.style.TextAlign.Center,
                    modifier = Modifier.fillMaxWidth()
                )
            
            Spacer(modifier = Modifier.height(24.dp))
            
            Text(
                "Categoría:",
                fontWeight = FontWeight.SemiBold,
                color = sullivanBlue
            )
            
            Spacer(modifier = Modifier.height(8.dp))
            
            conversiones.keys.forEach { categoria ->
                ElevatedCard(
                    onClick = { 
                        selectedCategoria = categoria
                        selectedTipo = ""
                    },
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp),
                    colors = CardDefaults.elevatedCardColors(
                        containerColor = if (selectedCategoria == categoria) sullivanBlue else Color.White
                    )
                ) {
                    Row(
                        modifier = Modifier.padding(16.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = when(categoria) {
                                "MASA" -> "⚖️"
                                "LONGITUD" -> "📏"
                                "TEMPERATURA" -> "🌡️"
                                else -> "📊"
                            },
                            style = MaterialTheme.typography.headlineMedium
                        )
                        
                        Spacer(modifier = Modifier.width(16.dp))
                        
                        Text(
                            text = categoria,
                            fontWeight = FontWeight.Bold,
                            color = if (selectedCategoria == categoria) Color.White else Color.Black
                        )
                    }
                }
            }
            
            if (selectedCategoria.isNotEmpty()) {
                Spacer(modifier = Modifier.height(16.dp))
                
                Text(
                    "Tipo de conversión:",
                    fontWeight = FontWeight.SemiBold,
                    color = sullivanBlue
                )
                
                Spacer(modifier = Modifier.height(8.dp))
                
                conversiones[selectedCategoria]?.forEach { (tipo, nombre) ->
                    FilterChip(
                        selected = selectedTipo == tipo,
                        onClick = { selectedTipo = tipo },
                        label = { Text(nombre) },
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 4.dp),
                        colors = FilterChipDefaults.filterChipColors(
                            selectedContainerColor = lightBlue,
                            selectedLabelColor = Color.White
                        )
                    )
                }
                
                if (selectedTipo.isNotEmpty()) {
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    OutlinedTextField(
                        value = valor,
                        onValueChange = { valor = it },
                        label = { Text("Valor a convertir") },
                        modifier = Modifier.fillMaxWidth(),
                        colors = OutlinedTextFieldDefaults.colors(
                            focusedBorderColor = sullivanBlue,
                            focusedLabelColor = sullivanBlue
                        ),
                        shape = RoundedCornerShape(12.dp)
                    )
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    
                    Button(
                        onClick = {
                            valor.toDoubleOrNull()?.let {
                                viewModel.convertir(selectedTipo, it, selectedCategoria)
                            }
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(56.dp),
                        enabled = !uiState.isLoading && valor.isNotEmpty(),
                        colors = ButtonDefaults.buttonColors(
                            containerColor = sullivanBlue,
                            contentColor = Color.White
                        ),
                        shape = RoundedCornerShape(12.dp)
                    ) {
                        if (uiState.isLoading) {
                            CircularProgressIndicator(
                                modifier = Modifier.size(24.dp),
                                color = Color.White
                            )
                        } else {
                            Text("✨ Convertir", fontWeight = FontWeight.Bold)
                        }
                    }
                }
            }
            
            if (uiState.resultado.isNotEmpty()) {
                Spacer(modifier = Modifier.height(24.dp))
                
                Card(
                    colors = CardDefaults.cardColors(
                        containerColor = Color(0xFF4CAF50)
                    ),
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(16.dp)
                ) {
                    Column(modifier = Modifier.padding(20.dp)) {
                        Text(
                            "✅ Resultado",
                            fontWeight = FontWeight.Bold,
                            color = Color.White,
                            style = MaterialTheme.typography.titleLarge
                        )
                        
                        Spacer(modifier = Modifier.height(12.dp))
                        
                        Text(
                            uiState.resultado,
                            style = MaterialTheme.typography.headlineMedium,
                            fontWeight = FontWeight.Bold,
                            color = Color.White
                        )
                    }
                }
            }
            
            if (uiState.error.isNotEmpty()) {
                Spacer(modifier = Modifier.height(16.dp))
                
                Card(
                    colors = CardDefaults.cardColors(
                        containerColor = Color(0xFFFFEBEE)
                    ),
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(12.dp)
                ) {
                    Text(
                        text = "❌ ${uiState.error}",
                        modifier = Modifier.padding(16.dp),
                        color = Color(0xFFC62828),
                        fontWeight = FontWeight.SemiBold,
                        textAlign = androidx.compose.ui.text.style.TextAlign.Center
                    )
                }
            }
            }
        }
    }
}
