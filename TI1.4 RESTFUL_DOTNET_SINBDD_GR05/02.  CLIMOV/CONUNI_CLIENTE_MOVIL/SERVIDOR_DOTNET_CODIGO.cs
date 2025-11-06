// ConversionUnidades_Controlador.cs
// Copia este código en tu proyecto .NET

using Microsoft.AspNetCore.Mvc;

namespace TuProyecto.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ConversionUnidades_Controlador : ControllerBase
    {
        [HttpPost]
        public IActionResult ConvertirUnidades([FromBody] ConversionRequest request)
        {
            try
            {
                if (request == null)
                {
                    return BadRequest(new ConversionResponse
                    {
                        Resultado = 0,
                        Mensaje = "Request inválido",
                        Exito = false
                    });
                }

                double resultado = 0;
                bool conversionValida = false;

                // Conversiones de Temperatura
                if (request.TipoConversion == "Temperatura")
                {
                    if (request.UnidadOrigen == "Celsius" && request.UnidadDestino == "Fahrenheit")
                    {
                        resultado = (request.Valor * 9.0 / 5.0) + 32;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Fahrenheit" && request.UnidadDestino == "Celsius")
                    {
                        resultado = (request.Valor - 32) * 5.0 / 9.0;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Celsius" && request.UnidadDestino == "Kelvin")
                    {
                        resultado = request.Valor + 273.15;
                        conversionValida = true;
                    }
                }
                // Conversiones de Masa
                else if (request.TipoConversion == "Masa")
                {
                    if (request.UnidadOrigen == "Kilogramos" && request.UnidadDestino == "Gramos")
                    {
                        resultado = request.Valor * 1000;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Gramos" && request.UnidadDestino == "Miligramos")
                    {
                        resultado = request.Valor * 1000;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Toneladas" && request.UnidadDestino == "Kilogramos")
                    {
                        resultado = request.Valor * 1000;
                        conversionValida = true;
                    }
                }
                // Conversiones de Longitud
                else if (request.TipoConversion == "Longitud")
                {
                    if (request.UnidadOrigen == "Kilómetros" && request.UnidadDestino == "Metros")
                    {
                        resultado = request.Valor * 1000;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Metros" && request.UnidadDestino == "Centímetros")
                    {
                        resultado = request.Valor * 100;
                        conversionValida = true;
                    }
                    else if (request.UnidadOrigen == "Centímetros" && request.UnidadDestino == "Milímetros")
                    {
                        resultado = request.Valor * 10;
                        conversionValida = true;
                    }
                }

                if (!conversionValida)
                {
                    return BadRequest(new ConversionResponse
                    {
                        Resultado = 0,
                        Mensaje = $"Conversión no soportada: {request.UnidadOrigen} a {request.UnidadDestino}",
                        Exito = false
                    });
                }

                return Ok(new ConversionResponse
                {
                    Resultado = resultado,
                    Mensaje = "Conversión exitosa",
                    Exito = true
                });
            }
            catch (Exception ex)
            {
                return StatusCode(500, new ConversionResponse
                {
                    Resultado = 0,
                    Mensaje = $"Error en el servidor: {ex.Message}",
                    Exito = false
                });
            }
        }

        [HttpGet]
        public IActionResult TestConnection()
        {
            return Ok(new { 
                mensaje = "API de Conversión de Unidades funcionando correctamente",
                fecha = DateTime.Now 
            });
        }
    }

    public class ConversionRequest
    {
        public string TipoConversion { get; set; } = string.Empty;
        public string UnidadOrigen { get; set; } = string.Empty;
        public string UnidadDestino { get; set; } = string.Empty;
        public double Valor { get; set; }
    }

    public class ConversionResponse
    {
        public double Resultado { get; set; }
        public string Mensaje { get; set; } = string.Empty;
        public bool Exito { get; set; }
    }
}
