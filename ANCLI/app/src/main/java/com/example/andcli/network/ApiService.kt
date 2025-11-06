package com.example.andcli.network

import com.example.andcli.data.ConversionRequest
import com.example.andcli.data.ConversionResponse
import com.example.andcli.data.LoginRequest
import retrofit2.Response
import retrofit2.http.*

interface ApiService {
    
    @POST("api/login")
    @FormUrlEncoded
    suspend fun login(
        @Field("username") username: String,
        @Field("password") password: String
    ): Response<LoginResponse>
    
    @POST("api/convertir")
    @FormUrlEncoded
    suspend fun convertir(
        @Field("tipo_conversion") tipoConversion: String,
        @Field("valor") valor: Double
    ): Response<ConversionResponse>
    
    @GET("dashboard")
    suspend fun getDashboard(): Response<String>
}

data class LoginResponse(
    val success: Boolean,
    val message: String,
    val usuario: String?
)
