using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using ConUni_Rest_Dotnet_GR05.ec.edu.monster.modelo;

namespace ConUni_Rest_Dotnet_GR05.ec.edu.monster.controlador
{
    [Route("api/[controller]")]
    [ApiController]
    public class ConversionUnidades_Controlador : ControllerBase
    {
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        public ActionResult<ConversionUnidades> Convertir(double valor, string? unidadOrigen, string? unidadDestino)
        {
            // Validación de entrada
            if (string.IsNullOrWhiteSpace(unidadOrigen) || string.IsNullOrWhiteSpace(unidadDestino))
            {
                return BadRequest("Las unidades de origen y destino son requeridas.");
            }

            try
            {
                var conversion = new ConversionUnidades
                {
                    Valor = valor,
                    UnidadOrigen = unidadOrigen,
                    UnidadDestino = unidadDestino
                };

                // Normalizar unidades a formato estándar (case-insensitive)
                string origen = unidadOrigen.Trim().ToLower();
                string destino = unidadDestino.Trim().ToLower();

                // Conversión de temperatura
                if (origen == "celsius" && destino == "fahrenheit")
                {
                    conversion.Resultado = (conversion.Valor * 9 / 5) + 32;  // Celsius a Fahrenheit
                }
                else if (origen == "fahrenheit" && destino == "celsius")
                {
                    conversion.Resultado = (conversion.Valor - 32) * 5 / 9;  // Fahrenheit a Celsius
                }
                else if (origen == "celsius" && destino == "kelvin")
                {
                    conversion.Resultado = conversion.Valor + 273.15;  // Celsius a Kelvin
                }
                else if (origen == "kelvin" && destino == "celsius")
                {
                    conversion.Resultado = conversion.Valor - 273.15;  // Kelvin a Celsius
                }
                else if (origen == "fahrenheit" && destino == "kelvin")
                {
                    conversion.Resultado = (conversion.Valor - 32) * 5 / 9 + 273.15;  // Fahrenheit a Kelvin
                }
                else if (origen == "kelvin" && destino == "fahrenheit")
                {
                    conversion.Resultado = (conversion.Valor - 273.15) * 9 / 5 + 32;  // Kelvin a Fahrenheit
                }

                // Conversión de masa
                else if (origen == "kilogramo" && destino == "gramo")
                {
                    conversion.Resultado = conversion.Valor * 1000;  // Kilogramo a Gramo
                }
                else if (origen == "gramo" && destino == "kilogramo")
                {
                    conversion.Resultado = conversion.Valor / 1000;  // Gramo a Kilogramo
                }
                else if (origen == "gramo" && destino == "miligramo")
                {
                    conversion.Resultado = conversion.Valor * 1000;  // Gramo a Miligramo
                }
                else if (origen == "miligramo" && destino == "gramo")
                {
                    conversion.Resultado = conversion.Valor / 1000;  // Miligramo a Gramo
                }
                else if (origen == "tonelada" && destino == "kilogramo")
                {
                    conversion.Resultado = conversion.Valor * 1000;  // Tonelada a Kilogramo
                }
                else if (origen == "kilogramo" && destino == "tonelada")
                {
                    conversion.Resultado = conversion.Valor / 1000;  // Kilogramo a Tonelada
                }

                // Conversión de longitud
                else if (origen == "kilometro" && destino == "metro")
                {
                    conversion.Resultado = conversion.Valor * 1000;  // Kilómetro a Metro
                }
                else if (origen == "metro" && destino == "kilometro")
                {
                    conversion.Resultado = conversion.Valor / 1000;  // Metro a Kilómetro
                }
                else if (origen == "metro" && destino == "centimetro")
                {
                    conversion.Resultado = conversion.Valor * 100;  // Metro a Centímetro
                }
                else if (origen == "centimetro" && destino == "metro")
                {
                    conversion.Resultado = conversion.Valor / 100;  // Centímetro a Metro
                }
                else if (origen == "centimetro" && destino == "milimetro")
                {
                    conversion.Resultado = conversion.Valor * 10;  // Centímetro a Milímetro
                }
                else if (origen == "milimetro" && destino == "centimetro")
                {
                    conversion.Resultado = conversion.Valor / 10;  // Milímetro a Centímetro
                }

                else
                {
                    return BadRequest($"Las unidades especificadas no son válidas o la conversión de '{unidadOrigen}' a '{unidadDestino}' no está soportada.");
                }

                return Ok(conversion);  // Regresamos el objeto de la conversión
            }
            catch (Exception ex)
            {
                return StatusCode(StatusCodes.Status500InternalServerError, 
                    $"Error al procesar la conversión: {ex.Message}");
            }
        }
    }
}

