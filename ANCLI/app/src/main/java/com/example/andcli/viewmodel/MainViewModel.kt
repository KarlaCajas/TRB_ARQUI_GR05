package com.example.andcli.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.andcli.network.RetrofitClient
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

data class ConversionState(
    val isLoading: Boolean = false,
    val isLoggedIn: Boolean = false,
    val resultado: String = "",
    val error: String = "",
    val categoria: String = "",
    val tipoConversion: String = ""
)

class MainViewModel : ViewModel() {
    
    private val _uiState = MutableStateFlow(ConversionState())
    val uiState: StateFlow<ConversionState> = _uiState
    
    private val apiService = RetrofitClient.apiService
    
    fun login(username: String, password: String) {
        viewModelScope.launch {
            _uiState.value = _uiState.value.copy(isLoading = true, error = "")
            try {
                val response = apiService.login(username, password)
                if (response.isSuccessful && response.body()?.success == true) {
                    _uiState.value = _uiState.value.copy(
                        isLoggedIn = true,
                        isLoading = false,
                        error = ""
                    )
                } else {
                    val message = response.body()?.message ?: "Credenciales incorrectas"
                    _uiState.value = _uiState.value.copy(
                        isLoading = false,
                        error = message
                    )
                }
            } catch (e: Exception) {
                _uiState.value = _uiState.value.copy(
                    isLoading = false,
                    error = "Error de conexión: ${e.message}"
                )
            }
        }
    }
    
    fun convertir(tipoConversion: String, valor: Double, categoria: String) {
        viewModelScope.launch {
            _uiState.value = _uiState.value.copy(isLoading = true, error = "")
            try {
                val response = apiService.convertir(tipoConversion, valor)
                if (response.isSuccessful && response.body()?.success == true) {
                    val data = response.body()!!
                    val resultadoTexto = "${data.resultado} ${data.unidad_destino}"
                    
                    _uiState.value = _uiState.value.copy(
                        isLoading = false,
                        resultado = resultadoTexto,
                        error = "",
                        categoria = categoria,
                        tipoConversion = tipoConversion
                    )
                } else {
                    val message = response.body()?.mensaje ?: "Error en la conversión"
                    _uiState.value = _uiState.value.copy(
                        isLoading = false,
                        error = message
                    )
                }
            } catch (e: Exception) {
                _uiState.value = _uiState.value.copy(
                    isLoading = false,
                    error = "Error de conexión: ${e.message}"
                )
            }
        }
    }
    
    private fun extraerResultadoDeHtml(html: String): String {
        // Ya no es necesario, ahora recibimos JSON
        return "Conversión realizada"
    }
    
    fun clearResult() {
        _uiState.value = _uiState.value.copy(resultado = "", error = "")
    }
    
    fun logout() {
        _uiState.value = ConversionState()
    }
}
