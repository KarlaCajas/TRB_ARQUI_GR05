"""
Cliente API REST para Conversión de Unidades
"""
import requests
from typing import List, Dict, Optional
import json
import urllib3

# Deshabilitar advertencias SSL para desarrollo local con certificados auto-firmados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIClient:
    """Cliente para comunicarse con la API REST de Conversión de Unidades"""
    
    def __init__(self, base_url: str = "http://localhost:5014/api/ConversionUnidades_Controlador"):
        self.base_url = base_url
        self.timeout = 10
        self.verify_ssl = False  # Deshabilitar verificación SSL para desarrollo local
        
    def _handle_response(self, response: requests.Response) -> Dict:
        """Maneja la respuesta de la API"""
        try:
            response.raise_for_status()
            return {
                "success": True,
                "data": response.json() if response.text else None,
                "message": "Operación exitosa"
            }
        except requests.exceptions.HTTPError as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error HTTP {response.status_code}: {str(e)}"
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "data": None,
                "message": "Error de conexión: No se pudo conectar con el servidor"
            }
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "data": None,
                "message": "Error: Tiempo de espera agotado"
            }
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error inesperado: {str(e)}"
            }
    
    def obtener_todas(self) -> Dict:
        """Obtiene todas las conversiones de unidades (GET)"""
        try:
            response = requests.get(self.base_url, timeout=self.timeout, verify=self.verify_ssl)
            return self._handle_response(response)
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error al obtener conversiones: {str(e)}"
            }
    
    def obtener_por_id(self, id_conversion: int) -> Dict:
        """Obtiene una conversión específica por ID (GET)"""
        try:
            url = f"{self.base_url}/{id_conversion}"
            response = requests.get(url, timeout=self.timeout, verify=self.verify_ssl)
            return self._handle_response(response)
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error al obtener conversión: {str(e)}"
            }
    
    def crear_conversion(self, datos: Dict) -> Dict:
        """Crea una nueva conversión de unidades (POST)"""
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                self.base_url,
                json=datos,
                headers=headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            return self._handle_response(response)
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error al crear conversión: {str(e)}"
            }
    
    def actualizar_conversion(self, id_conversion: int, datos: Dict) -> Dict:
        """Actualiza una conversión existente (PUT)"""
        try:
            url = f"{self.base_url}/{id_conversion}"
            headers = {"Content-Type": "application/json"}
            response = requests.put(
                url,
                json=datos,
                headers=headers,
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            return self._handle_response(response)
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error al actualizar conversión: {str(e)}"
            }
    
    def eliminar_conversion(self, id_conversion: int) -> Dict:
        """Elimina una conversión (DELETE)"""
        try:
            url = f"{self.base_url}/{id_conversion}"
            response = requests.delete(url, timeout=self.timeout, verify=self.verify_ssl)
            return self._handle_response(response)
        except Exception as e:
            return {
                "success": False,
                "data": None,
                "message": f"Error al eliminar conversión: {str(e)}"
            }
    
    def verificar_conexion(self) -> bool:
        """Verifica si el servidor está disponible"""
        try:
            response = requests.get(self.base_url, timeout=5, verify=self.verify_ssl)
            # Si recibimos cualquier respuesta del servidor (200, 400, 404, 405, etc.)
            # significa que está disponible y escuchando peticiones
            return True
        except:
            return False
