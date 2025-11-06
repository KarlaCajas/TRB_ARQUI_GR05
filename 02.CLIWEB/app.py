"""
Cliente Web SOAP en Python/Flask para consumir el servicio .NET
Autor: Sistema
Fecha: 2025-11-03
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from zeep import Client
from zeep.transports import Transport
from requests import Session as RequestsSession
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'monsters_university_secret_key_2025'  # Clave secreta para sesiones

# Configuración
WSDL_URL = "http://localhost:63393/Service.svc?wsdl"
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"

# Cliente SOAP global
soap_client = None

def init_soap_client():
    """Inicializa el cliente SOAP"""
    global soap_client
    try:
        session = RequestsSession()
        session.verify = False
        transport = Transport(session=session)
        soap_client = Client(WSDL_URL, transport=transport)
        return True
    except Exception as e:
        print(f"Error al conectar con el servicio SOAP: {e}")
        return False

# Decorador para proteger rutas que requieren login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Debes iniciar sesión para acceder a esta página', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Página de inicio - redirige al login o al dashboard"""
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        usuario = request.form.get('username', '').strip()
        contrasena = request.form.get('password', '')
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            session['usuario'] = usuario
            flash(f'¡Bienvenido, {usuario}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.pop('usuario', None)
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('login'))

# ============= API ENDPOINTS PARA ANDROID =============

@app.route('/api/login', methods=['POST'])
def api_login():
    """API endpoint para login desde Android"""
    try:
        # Intentar obtener datos de JSON o formulario
        if request.is_json:
            data = request.get_json()
            username = data.get('username', '').strip()
            password = data.get('password', '')
        else:
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '')
        
        if username == USUARIO_VALIDO and password == CONTRASENA_VALIDA:
            session['usuario'] = username
            return jsonify({
                'success': True,
                'message': f'¡Bienvenido, {username}!',
                'usuario': username
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Credenciales incorrectas'
            }), 401
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

@app.route('/api/convertir', methods=['POST'])
def api_convertir():
    """API endpoint para conversiones desde Android"""
    if 'usuario' not in session:
        return jsonify({
            'success': False,
            'message': 'No autorizado. Inicia sesión primero.'
        }), 401
    
    try:
        # Intentar obtener datos de JSON o formulario
        if request.is_json:
            data = request.get_json()
            tipo_conversion = data.get('tipo_conversion')
            valor = float(data.get('valor'))
        else:
            tipo_conversion = request.form.get('tipo_conversion')
            valor = float(request.form.get('valor'))
        
        resultado = None
        unidad_origen = ""
        unidad_destino = ""
        
        # Conversiones de Temperatura
        if tipo_conversion == 'celsius_fahrenheit':
            resultado = soap_client.service.CelsiusToFahrenheit(valor)
            unidad_origen = "°C"
            unidad_destino = "°F"
        elif tipo_conversion == 'fahrenheit_celsius':
            resultado = soap_client.service.FahrenheitToCelsius(valor)
            unidad_origen = "°F"
            unidad_destino = "°C"
        elif tipo_conversion == 'celsius_kelvin':
            resultado = soap_client.service.CelsiusToKelvin(valor)
            unidad_origen = "°C"
            unidad_destino = "K"
        
        # Conversiones de Masa
        elif tipo_conversion == 'kg_lb':
            resultado = soap_client.service.KilogramsToPounds(valor)
            unidad_origen = "kg"
            unidad_destino = "lb"
        elif tipo_conversion == 'lb_kg':
            resultado = soap_client.service.PoundsToKilograms(valor)
            unidad_origen = "lb"
            unidad_destino = "kg"
        elif tipo_conversion == 'kg_oz':
            resultado = soap_client.service.KilogramsToOunces(valor)
            unidad_origen = "kg"
            unidad_destino = "oz"
        
        # Conversiones de Longitud
        elif tipo_conversion == 'm_ft':
            resultado = soap_client.service.MetersToFeet(valor)
            unidad_origen = "m"
            unidad_destino = "ft"
        elif tipo_conversion == 'ft_m':
            resultado = soap_client.service.FeetToMeters(valor)
            unidad_origen = "ft"
            unidad_destino = "m"
        elif tipo_conversion == 'km_mi':
            resultado = soap_client.service.KilometersToMiles(valor)
            unidad_origen = "km"
            unidad_destino = "mi"
        else:
            return jsonify({
                'success': False,
                'message': 'Tipo de conversión no válido'
            }), 400
        
        return jsonify({
            'success': True,
            'resultado': resultado,
            'unidad_origen': unidad_origen,
            'unidad_destino': unidad_destino,
            'valor_original': valor,
            'mensaje': f'{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}'
        }), 200
        
    except ValueError:
        return jsonify({
            'success': False,
            'message': 'Valor numérico inválido'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error en la conversión: {str(e)}'
        }), 500

# ============= FIN API ENDPOINTS =============

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard principal con las opciones de conversión"""
    return render_template('dashboard.html', usuario=session.get('usuario'))

@app.route('/convertir', methods=['POST'])
@login_required
def convertir():
    """Realiza la conversión según el tipo seleccionado"""
    try:
        tipo_conversion = request.form.get('tipo_conversion')
        valor = float(request.form.get('valor'))
        
        resultado = None
        mensaje = ""
        unidad_origen = ""
        unidad_destino = ""
        
        # Conversiones de Temperatura
        if tipo_conversion == 'celsius_fahrenheit':
            resultado = soap_client.service.CelsiusToFahrenheit(valor)
            unidad_origen = "°C"
            unidad_destino = "°F"
        
        elif tipo_conversion == 'fahrenheit_celsius':
            resultado = soap_client.service.FahrenheitToCelsius(valor)
            unidad_origen = "°F"
            unidad_destino = "°C"
        
        elif tipo_conversion == 'celsius_kelvin':
            resultado = soap_client.service.CelsiusToKelvin(valor)
            unidad_origen = "°C"
            unidad_destino = "K"
        
        # Conversiones de Masa
        elif tipo_conversion == 'kg_lb':
            resultado = soap_client.service.KilogramsToPounds(valor)
            unidad_origen = "kg"
            unidad_destino = "lb"
        
        elif tipo_conversion == 'lb_kg':
            resultado = soap_client.service.PoundsToKilograms(valor)
            unidad_origen = "lb"
            unidad_destino = "kg"
        
        elif tipo_conversion == 'kg_oz':
            resultado = soap_client.service.KilogramsToOunces(valor)
            unidad_origen = "kg"
            unidad_destino = "oz"
        
        # Conversiones de Longitud
        elif tipo_conversion == 'm_ft':
            resultado = soap_client.service.MetersToFeet(valor)
            unidad_origen = "m"
            unidad_destino = "ft"
        
        elif tipo_conversion == 'ft_m':
            resultado = soap_client.service.FeetToMeters(valor)
            unidad_origen = "ft"
            unidad_destino = "m"
        
        elif tipo_conversion == 'km_mi':
            resultado = soap_client.service.KilometersToMiles(valor)
            unidad_origen = "km"
            unidad_destino = "mi"
        
        # Crear mensaje de resultado
        mensaje = f"{valor} {unidad_origen} = {resultado:.4f} {unidad_destino}"
        
        # Retornar a la página de resultado
        return render_template('resultado.html', 
                             usuario=session.get('usuario'),
                             valor_original=valor,
                             unidad_origen=unidad_origen,
                             resultado=resultado,
                             unidad_destino=unidad_destino,
                             mensaje=mensaje)
        
    except ValueError:
        flash('Error: Ingresa un valor numérico válido', 'error')
    except Exception as e:
        flash(f'Error al realizar la conversión: {str(e)}', 'error')
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    print("\n" + "="*60)
    print(" INICIANDO CLIENTE WEB SOAP ".center(60))
    print("="*60 + "\n")
    
    if init_soap_client():
        print("✓ Conexión establecida con el servicio SOAP")
        print(f"✓ WSDL: {WSDL_URL}")
        print("\n✓ Servidor web iniciando en http://localhost:5000")
        print("="*60 + "\n")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("✗ No se pudo conectar con el servicio SOAP")
        print("✗ Verifica que el servidor .NET esté ejecutándose")
