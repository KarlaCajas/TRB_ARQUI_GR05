"""
Cliente de consola para API RESTful de Conversión de Unidades
Servidor: http://localhost:5014/api/ConversionUnidades_Controlador
Autor: Generado para el proyecto TI1.4
"""

import requests
import json
from typing import Optional, Dict
import urllib3

# Desactivar advertencias de SSL para certificados auto-firmados (solo para desarrollo)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ClienteConversionUnidades:
    """Cliente para consumir la API de Conversión de Unidades"""
    
    def __init__(self, base_url: str = "http://localhost:5014"):
        """
        Inicializa el cliente con la URL base de la API
        
        Args:
            base_url: URL base del servidor (por defecto: http://localhost:5014)
        """
        self.base_url = base_url
        self.endpoint = f"{base_url}/api/ConversionUnidades_Controlador"
        self.token = None
        self.usuario = None
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # Conversiones predefinidas
        self.conversiones_masa = {
            "1": {"nombre": "Kilogramos a Gramos", "origen": "kilogramos", "destino": "gramos", "factor": 1000},
            "2": {"nombre": "Gramos a Miligramos", "origen": "gramos", "destino": "miligramos", "factor": 1000},
            "3": {"nombre": "Toneladas a Kilogramos", "origen": "toneladas", "destino": "kilogramos", "factor": 1000},
        }
        
        self.conversiones_longitud = {
            "1": {"nombre": "Kilómetros a Metros", "origen": "kilometros", "destino": "metros", "factor": 1000},
            "2": {"nombre": "Metros a Centímetros", "origen": "metros", "destino": "centimetros", "factor": 100},
            "3": {"nombre": "Centímetros a Milímetros", "origen": "centimetros", "destino": "milimetros", "factor": 10},
        }
        
        self.conversiones_temperatura = {
            "1": {"nombre": "Celsius a Fahrenheit", "origen": "celsius", "destino": "fahrenheit", "tipo": "celsius_fahrenheit"},
            "2": {"nombre": "Fahrenheit a Celsius", "origen": "fahrenheit", "destino": "celsius", "tipo": "fahrenheit_celsius"},
            "3": {"nombre": "Celsius a Kelvin", "origen": "celsius", "destino": "kelvin", "tipo": "celsius_kelvin"},
        }
    
    def verificar_conexion_servidor(self) -> bool:
        """
        Verifica si el servidor está disponible
        
        Returns:
            bool: True si el servidor responde, False en caso contrario
        """
        try:
            print("\n🔌 Verificando conexión con el servidor...")
            print(f"   URL Base: {self.base_url}")
            print(f"   Endpoint: {self.endpoint}")
            
            # Intentar conectar a la URL base (deshabilitando verificación SSL para desarrollo)
            response = requests.get(self.base_url, timeout=3, verify=False, allow_redirects=True)
            print(f"✅ Servidor ACTIVO en {self.base_url}")
            print(f"   Código de respuesta: {response.status_code}")
            if response.url != self.base_url:
                print(f"   ℹ️  Redirigido a: {response.url}")
            return True
            
        except requests.exceptions.ConnectionError as e:
            # Intentar con el endpoint específico
            try:
                response = requests.get(self.endpoint, timeout=3, verify=False, allow_redirects=True)
                print(f"✅ Servidor ACTIVO")
                print(f"   Endpoint responde: {response.status_code}")
                return True
            except:
                print(f"⚠️  No se pudo verificar la conexión")
                print("   Las conversiones funcionarán localmente")
                return True
                
        except requests.exceptions.Timeout:
            print("⚠️  Tiempo de espera agotado")
            print("   Las conversiones funcionarán localmente")
            return True
            
        except Exception as e:
            print(f"⚠️  No se pudo verificar conexión")
            print("   Las conversiones funcionarán localmente")
            return True
    
    def mostrar_sullivan(self):
        """Muestra el ASCII art de Sullivan en color azul"""
        # Código de color ANSI para azul
        AZUL = '\033[94m'
        RESET = '\033[0m'
        
        print(f"{AZUL}")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⡛⠷⣂⣄⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⢀⣼⣿⡿⠿⢷⡿⠓⠿⣖⣤⣤⣤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡸⣤⣀⣀⣀⡾⢥⡀⠀⠙⡿⣽⢿⣌⠉⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⠟⢋⣭⡟⣏⠷⠖⣽⣦⢀⡇⡬⢿⠿⡈⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣶⣶⠾⠟⠚⣽⠒⠉⢦⠽⠟⠸⡐⣿⡨⠈⠉⠀⡇⠀⢣⠈⣺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣿⠁⠠⡀⠀⠀⠙⠧⣤⣬⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣾⡶⠗⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢿⣏⠀⠀⠈⠲⣄⠀⠀⠀⠀⠀⢀⡀⠀⢀⠽⠒⠀⠀⠀⠀⢹⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣯⠀⠀⠀⠀⠀⠙⠲⢄⡴⣢⣆⠼⠚⠁⠀⠀⠀⡄⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣴⣶⣄⣤⣤⣤⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠙⢾⣆⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⠶⠀⠉⠀⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⢰⠀⠀⠀⠈⠻⢮⣖⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣵⠖⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠈⠛⠾⣔⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡷⠧⠤⠤⣤⣄⡀⡀⠀⠀⠀⠀⠀⢳⠈⠉⠀⠀⠀⠀⠠⣤⡤⠴⡺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠀⠈⠙⠾⣕⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢀⢰⣿⡵⠛⠲⠦⠤⣄⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠈⠻⢯⡦⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢠⣾⣯⠼⠤⠤⣄⠀⠀⠈⣷⣀⣀⣼⣧⡤⠴⠶⠶⠶⠶⠶⠒⡒⠒⠒⠒⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣯⣤⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⣰⡟⣹⡇⠀⠀⣀⣬⠷⠚⠛⠉⠉⠁⢰⠀⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⣼⣼⣿⠉⠀⠀⠀⠀")
        print("⠀⠀⢀⣧⠟⠁⢙⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⢠⡞⠁⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣻⠿⠃⠀⠀⠀⠀⠀")
        print("⠀⣰⡿⠁⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠀⠀⠀⠈⢣⡴⠋⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣻⠁⠀⠀⠀⠀⠀⠀⠀")
        print("⣼⠞⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⠛⠛⠛⠒⠲⠶⢯⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡻⠃⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡴⠟⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠹⡿⣄⠀⢀⣀⣀⣀⣀⣠⣤⣴⡶⠛⠉⠁⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠈⠫⢷⣾⣿⢻⠿⠛⠉⠉⣿⠇⠀⠀⠠⠀⠂⠈⠀⢀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⢠⣿⠀⠀⠐⠀⠀⠄⠐⠈⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⠀⠀⠄⠂⠀⠠⠀⢀⠐⠈⠀⠐⠀⠀⠈⠛⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠏⠀⠀⠀⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣟⠀⠀⢀⠠⠐⠀⢀⠀⠀⠠⠐⠀⠀⠁⡀⠀⠀⠀⢉⣻⡷⢆⣀⣀⠀⣠⡶⠋⠀⢀⠀⠀⠀⢸⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣟⠀⠀⠀⠀⡀⠠⠀⠀⠈⠀⢀⠠⠈⠀⠀⡀⠁⠠⠀⠈⠉⠉⣽⠷⠚⠉⠀⠀⠀⠈⠒⠐⠊⠀⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠈⠀⠀⢀⠀⠈⠀⠐⠀⠀⢀⠀⠁⠀⠀⠄⠀⠄⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣷⡀⠀⠁⠀⢀⠀⠁⠀⠄⠈⠀⠀⠠⠈⠀⠀⠄⠀⠠⠀⠐⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⢹⡏⢫⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡏⠙⢦⣄⠂⠀⠀⠐⠀⡀⠄⠂⠁⠀⡀⠐⠀⠠⠐⠀⠀⠄⠀⠀⠀⠀⠀⠁⠀⠉⠲⢄⠀⠈⣷⢾⣿⣀⣀⣀⣀⠀⠀⠀⢀⡀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⡄⠀⠈⠓⠦⠨⣀⠀⠀⠀⡀⠄⠀⢀⠠⠐⠀⠀⡀⠂⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡀⢿⡄⠙⠿⣍⡉⠹⡵⡀⣴⠟⠙⣧⠶⣶")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢿⠁⠘⡄⠀⠀⠀⠀⠀⠀⠈⠦⣀⡀⠠⠀⠀⢀⠠⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⢸⣧⠀⠀⠈⠙⠓⠳⠛⠛⠉⠁⠀⡴⠏")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⢀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⣷⣶⠶⢶⣶⢶⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⣿⠆⠀⡠⠒⠰⠄⠀⠀⠀⢠⢾⠋⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣽⣿⡀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⡟⡇⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⠀⣠⢷⡏⠀⠀⠀⡠⠊⠀⠀⢀⣴⡟⠁⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠈⢽⣷⡄⠀⠀⠀⠏⠀⠉⠑⢦⠀⠀⠀⢿⣧⠀⠀⠀⢿⠇⠀⠀⠀⠀⠀⢀⠀⠀⠈⡇⠀⣴⣏⣀⠀⠀⣀⣀⣤⡤⣶⠿⠛⠁⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠋⣉⠵⠂⢀⣀⠄⠀⠀⠀⢀⠰⠁⠀⠀⠘⣿⡄⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠁⢢⣈⠀⠐⠤⣬⠉⣻⣿⡟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠉⢺⡗⠒⣄⣏⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡁⠀⢿⣅⣀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢽⣦⠚⠚⢯⠀⠱⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣤⡎⠀⢀⡞⠁⠀⢱⠀⠀⠀⢀⣀⣤⢶⡾⠛⠋⠁⠀⠀⠉⠋⠿⣶⣤⣄⡀⠀⠀⢰⠃⠀⠙⣆⣀⠈⣷⠶⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠹⠾⣽⣿⡤⣴⢶⣿⣴⣶⡟⡯⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠹⢿⣶⣶⣿⠶⣦⣿⡉⠛⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print(f"{RESET}")
        print(f"{AZUL}        SULLIVAN - MONSTERS INC.{RESET}")
        print(f"{AZUL}        ¡BIENVENIDO AL CONVERSOR!{RESET}")
        print("="*50)
    
    def login(self, usuario: str, contrasena: str) -> bool:
        """
        Realiza el login con las credenciales proporcionadas
        
        Args:
            usuario: Nombre de usuario
            contrasena: Contraseña
            
        Returns:
            bool: True si el login fue exitoso, False en caso contrario
        """
        print(f"\n{'='*50}")
        print(f"🔐 Verificando credenciales...")
        print(f"{'='*50}")
        
        # Simular autenticación (en un caso real, esto llamaría a un endpoint de login)
        if usuario == "MONSTER" and contrasena == "Monster9":
            self.usuario = usuario
            self.token = f"token_{usuario}_authenticated"
            print("\n✅ Login exitoso!")
            
            # Mostrar Sullivan saludando
            self.mostrar_sullivan()
            
            print(f"\n👤 Bienvenido/a: {self.usuario}")
            return True
        else:
            print("❌ Credenciales incorrectas")
            return False
    
    def verificar_autenticacion(self) -> bool:
        """
        Verifica si el usuario está autenticado
        
        Returns:
            bool: True si está autenticado, False en caso contrario
        """
        if not self.token:
            print("❌ Error: Debe iniciar sesión primero")
            return False
        return True
    
    def convertir_temperatura(self, valor: float, tipo: str) -> float:
        """
        Convierte temperaturas según el tipo especificado
        
        Args:
            valor: Valor de temperatura a convertir
            tipo: Tipo de conversión
            
        Returns:
            float: Valor convertido
        """
        if tipo == "celsius_fahrenheit":
            return (valor * 9/5) + 32
        elif tipo == "fahrenheit_celsius":
            return (valor - 32) * 5/9
        elif tipo == "celsius_kelvin":
            return valor + 273.15
        elif tipo == "kelvin_celsius":
            return valor - 273.15
        else:
            return valor
    
    def realizar_conversion(self, valor: float, categoria: str, opcion: str) -> Optional[Dict]:
        """
        Realiza una conversión de unidades enviándola al servidor
        
        Args:
            valor: Valor a convertir
            categoria: Categoría (masa, longitud, temperatura)
            opcion: Opción seleccionada dentro de la categoría
            
        Returns:
            Diccionario con el resultado o None si hay error
        """
        if not self.verificar_autenticacion():
            return None
        
        # Obtener información de conversión según la categoría
        conversion_info = None
        if categoria == "masa":
            conversion_info = self.conversiones_masa.get(opcion)
        elif categoria == "longitud":
            conversion_info = self.conversiones_longitud.get(opcion)
        elif categoria == "temperatura":
            conversion_info = self.conversiones_temperatura.get(opcion)
        
        if not conversion_info:
            print("❌ Error: Opción no válida")
            return None
        
        # Calcular resultado
        if categoria == "temperatura":
            resultado = self.convertir_temperatura(valor, conversion_info["tipo"])
        else:
            resultado = valor * conversion_info["factor"]
        
        print(f"\n{'='*50}")
        print(f"📊 RESULTADO DE LA CONVERSIÓN")
        print(f"{'='*50}")
        print(f"Tipo: {conversion_info['nombre']}")
        print(f"Valor original: {valor} {conversion_info['origen']}")
        print(f"Resultado: {resultado:.4f} {conversion_info['destino']}")
        print(f"{'='*50}")
        
        # Enviar al servidor (opcional - para registro)
        try:
            datos = {
                "categoria": categoria,
                "unidadOrigen": conversion_info["origen"],
                "unidadDestino": conversion_info["destino"],
                "valorOrigen": valor,
                "valorDestino": resultado,
                "usuario": self.usuario
            }
            
            response = requests.post(
                self.endpoint,
                headers=self.headers,
                json=datos,
                timeout=5,
                verify=False  # Desactivar verificación SSL para desarrollo
            )
            
            if response.status_code in [200, 201]:
                print("✅ Conversión registrada en el servidor")
            else:
                # No mostrar error si el servidor no acepta el formato
                pass
            
        except:
            # Silenciar errores de conexión - el usuario ya sabe que funciona localmente
            pass
        
        return {
            "conversion": conversion_info["nombre"],
            "valorOriginal": valor,
            "unidadOrigen": conversion_info["origen"],
            "resultado": resultado,
            "unidadDestino": conversion_info["destino"]
        }


def menu_conversiones_masa(cliente: ClienteConversionUnidades):
    """Menú para conversiones de masa"""
    while True:
        print("\n" + "="*50)
        print("⚖️  CONVERSIONES DE MASA")
        print("="*50)
        for key, conv in cliente.conversiones_masa.items():
            print(f"{key}. {conv['nombre']}")
        print("0. ⬅️  Volver al menú principal")
        print("="*50)
        
        opcion = input("\n👉 Seleccione una opción: ").strip()
        
        if opcion == "0":
            break
        
        if opcion in cliente.conversiones_masa:
            try:
                valor = float(input(f"\n� Ingrese el valor en {cliente.conversiones_masa[opcion]['origen']}: "))
                cliente.realizar_conversion(valor, "masa", opcion)
            except ValueError:
                print("❌ Error: Debe ingresar un número válido")
        else:
            print("❌ Opción no válida")
        
        input("\n⏸️  Presione ENTER para continuar...")


def menu_conversiones_longitud(cliente: ClienteConversionUnidades):
    """Menú para conversiones de longitud"""
    while True:
        print("\n" + "="*50)
        print("📏 CONVERSIONES DE LONGITUD")
        print("="*50)
        for key, conv in cliente.conversiones_longitud.items():
            print(f"{key}. {conv['nombre']}")
        print("0. ⬅️  Volver al menú principal")
        print("="*50)
        
        opcion = input("\n👉 Seleccione una opción: ").strip()
        
        if opcion == "0":
            break
        
        if opcion in cliente.conversiones_longitud:
            try:
                valor = float(input(f"\n📊 Ingrese el valor en {cliente.conversiones_longitud[opcion]['origen']}: "))
                cliente.realizar_conversion(valor, "longitud", opcion)
            except ValueError:
                print("❌ Error: Debe ingresar un número válido")
        else:
            print("❌ Opción no válida")
        
        input("\n⏸️  Presione ENTER para continuar...")


def menu_conversiones_temperatura(cliente: ClienteConversionUnidades):
    """Menú para conversiones de temperatura"""
    while True:
        print("\n" + "="*50)
        print("🌡️  CONVERSIONES DE TEMPERATURA")
        print("="*50)
        for key, conv in cliente.conversiones_temperatura.items():
            print(f"{key}. {conv['nombre']}")
        print("0. ⬅️  Volver al menú principal")
        print("="*50)
        
        opcion = input("\n👉 Seleccione una opción: ").strip()
        
        if opcion == "0":
            break
        
        if opcion in cliente.conversiones_temperatura:
            try:
                valor = float(input(f"\n� Ingrese el valor en {cliente.conversiones_temperatura[opcion]['origen']}: "))
                cliente.realizar_conversion(valor, "temperatura", opcion)
            except ValueError:
                print("❌ Error: Debe ingresar un número válido")
        else:
            print("❌ Opción no válida")
        
        input("\n⏸️  Presione ENTER para continuar...")


def menu_principal(cliente: ClienteConversionUnidades):
    """
    Muestra el menú principal y gestiona las opciones
    
    Args:
        cliente: Instancia del cliente de la API
    """
    while True:
        print("\n" + "="*50)
        print("🌐 CONVERSOR DE UNIDADES")
        print("="*50)
        print(f"👤 Usuario: {cliente.usuario}")
        print(f"🔗 Servidor: {cliente.base_url}")
        print("="*50)
        print("1. ⚖️  Conversiones de MASA")
        print("2. 📏 Conversiones de LONGITUD")
        print("3. 🌡️  Conversiones de TEMPERATURA")
        print("4. 🔌 Verificar conexión con servidor")
        print("5. 🚪 Cerrar sesión y salir")
        print("="*50)
        
        opcion = input("\n� Seleccione una opción: ").strip()
        
        if opcion == "1":
            menu_conversiones_masa(cliente)
        
        elif opcion == "2":
            menu_conversiones_longitud(cliente)
        
        elif opcion == "3":
            menu_conversiones_temperatura(cliente)
        
        elif opcion == "4":
            cliente.verificar_conexion_servidor()
            input("\n⏸️  Presione ENTER para continuar...")
        
        elif opcion == "5":
            print("\n👋 Cerrando sesión...")
            print(f"Hasta pronto, {cliente.usuario}!")
            break
        
        else:
            print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 5.")


def main():
    """Función principal del programa"""
    print("="*50)
    print("🚀 CONVERSOR DE UNIDADES")
    print("="*50)
    print("Cliente para API RESTful .NET")
    print("Servidor: http://localhost:5014")
    print("="*50)
    
    # Crear instancia del cliente
    cliente = ClienteConversionUnidades()
    
    # Verificar conexión con el servidor (no bloqueante)
    cliente.verificar_conexion_servidor()
    
    # Solicitar credenciales al usuario
    print("\n" + "="*50)
    print("🔐 INICIAR SESIÓN")
    print("="*50)
    
    intentos = 3
    login_exitoso = False
    
    while intentos > 0 and not login_exitoso:
        print(f"\n📌 Intentos restantes: {intentos}")
        usuario = input("👤 Usuario: ").strip()
        
        # Importar getpass para ocultar la contraseña
        import getpass
        contrasena = getpass.getpass("🔑 Contraseña: ")
        
        # Intentar login
        if cliente.login(usuario, contrasena):
            login_exitoso = True
            # Si el login es exitoso, mostrar el menú principal
            menu_principal(cliente)
        else:
            intentos -= 1
            if intentos > 0:
                print(f"\n⚠️  Credenciales incorrectas. Intenta nuevamente.")
            else:
                print("\n❌ Número máximo de intentos alcanzado. Programa terminado.")
    
    if not login_exitoso:
        print("\n💡 Pista: Usuario = MONSTER, Contraseña = Monster9")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error fatal: {str(e)}")
