package com.example.andcli.data

data class LoginRequest(
    val username: String,
    val password: String
)

data class ConversionRequest(
    val tipo_conversion: String,
    val valor: Double,
    val categoria: String
)

data class ConversionResponse(
    val success: Boolean,
    val resultado: Double,
    val unidad_origen: String,
    val unidad_destino: String,
    val valor_original: Double,
    val mensaje: String
)

data class ErrorResponse(
    val success: Boolean,
    val error: String,
    val message: String
)
