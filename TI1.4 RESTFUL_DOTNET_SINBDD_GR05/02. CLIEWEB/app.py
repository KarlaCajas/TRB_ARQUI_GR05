from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import requests
from functools import wraps

app = Flask(__name__)
app.secret_key = 'monster_secret_key_2025'

# Configuración del servidor .NET
API_BASE_URL = 'http://localhost:5014/api/ConversionUnidades_Controlador'

# Credenciales quemadas
USUARIO_VALIDO = 'MONSTER'
PASSWORD_VALIDO = 'Monster9'

# Decorador para verificar login
def login_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Debe iniciar sesión primero', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Ruta principal - redirige al login y limpia sesión
@app.route('/')
def index():
    # Siempre limpiar la sesión al inicio
    session.clear()
    return redirect(url_for('login'))

# Ruta de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        
        if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
            session['usuario'] = usuario
            flash('¡Bienvenido MONSTER!', 'success')
            return redirect(url_for('menu'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html')

# Ruta de Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('login'))

# Ruta para limpiar sesión (útil para debugging)
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect(url_for('login'))

# Menú principal de conversiones
@app.route('/menu')
@login_requerido
def menu():
    return render_template('menu.html', usuario=session.get('usuario'))

# Conversión de Masa
@app.route('/conversion/masa', methods=['GET', 'POST'])
@login_requerido
def conversion_masa():
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            valor = float(request.form.get('valor'))
            tipo_conversion = request.form.get('tipo_conversion')
            
            # Mapeo de conversiones específicas
            conversiones = {
                'kg-g': ('kilogramo', 'gramo', 'g'),
                'g-mg': ('gramo', 'miligramo', 'mg'),
                't-kg': ('tonelada', 'kilogramo', 'kg')
            }
            
            if tipo_conversion not in conversiones:
                error = "Tipo de conversión no válido"
                flash(error, 'danger')
            else:
                de_unidad, a_unidad, simbolo = conversiones[tipo_conversion]
                
                # Llamada al API .NET
                params = {
                    'valor': valor,
                    'unidadOrigen': de_unidad,
                    'unidadDestino': a_unidad
                }
                
                response = requests.get(API_BASE_URL, params=params, verify=False, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    resultado = {
                        'resultado': f"{data['resultado']} {simbolo}",
                        'valorOriginal': valor,
                        'unidadOrigen': de_unidad,
                        'valorConvertido': data['resultado'],
                        'unidadDestino': a_unidad
                    }
                    flash('Conversión realizada exitosamente', 'success')
                else:
                    error = f"Error del servidor: {response.status_code} - {response.text}"
                    flash(error, 'danger')
                
        except requests.exceptions.RequestException as e:
            error = f"Error de conexión: {str(e)}"
            flash(error, 'danger')
        except ValueError:
            error = "Por favor ingrese un valor numérico válido"
            flash(error, 'danger')
        except Exception as e:
            error = f"Error: {str(e)}"
            flash(error, 'danger')
    
    return render_template('conversion_masa.html', resultado=resultado, error=error)

# Conversión de Longitud
@app.route('/conversion/longitud', methods=['GET', 'POST'])
@login_requerido
def conversion_longitud():
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            valor = float(request.form.get('valor'))
            tipo_conversion = request.form.get('tipo_conversion')
            
            # Mapeo de conversiones específicas
            conversiones = {
                'km-m': ('kilometro', 'metro', 'm'),
                'm-cm': ('metro', 'centimetro', 'cm'),
                'cm-mm': ('centimetro', 'milimetro', 'mm')
            }
            
            if tipo_conversion not in conversiones:
                error = "Tipo de conversión no válido"
                flash(error, 'danger')
            else:
                de_unidad, a_unidad, simbolo = conversiones[tipo_conversion]
                
                # Llamada al API .NET
                params = {
                    'valor': valor,
                    'unidadOrigen': de_unidad,
                    'unidadDestino': a_unidad
                }
                
                response = requests.get(API_BASE_URL, params=params, verify=False, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    resultado = {
                        'resultado': f"{data['resultado']} {simbolo}",
                        'valorOriginal': valor,
                        'unidadOrigen': de_unidad,
                        'valorConvertido': data['resultado'],
                        'unidadDestino': a_unidad
                    }
                    flash('Conversión realizada exitosamente', 'success')
                else:
                    error = f"Error del servidor: {response.status_code} - {response.text}"
                    flash(error, 'danger')
                
        except requests.exceptions.RequestException as e:
            error = f"Error de conexión: {str(e)}"
            flash(error, 'danger')
        except ValueError:
            error = "Por favor ingrese un valor numérico válido"
            flash(error, 'danger')
        except Exception as e:
            error = f"Error: {str(e)}"
            flash(error, 'danger')
    
    return render_template('conversion_longitud.html', resultado=resultado, error=error)

# Conversión de Temperatura
@app.route('/conversion/temperatura', methods=['GET', 'POST'])
@login_requerido
def conversion_temperatura():
    resultado = None
    error = None
    
    if request.method == 'POST':
        try:
            valor = float(request.form.get('valor'))
            tipo_conversion = request.form.get('tipo_conversion')
            
            # Mapeo de conversiones específicas
            conversiones = {
                'c-f': ('celsius', 'fahrenheit', '°F'),
                'f-c': ('fahrenheit', 'celsius', '°C'),
                'c-k': ('celsius', 'kelvin', 'K')
            }
            
            if tipo_conversion not in conversiones:
                error = "Tipo de conversión no válido"
                flash(error, 'danger')
            else:
                de_unidad, a_unidad, simbolo = conversiones[tipo_conversion]
                
                # Llamada al API .NET
                params = {
                    'valor': valor,
                    'unidadOrigen': de_unidad,
                    'unidadDestino': a_unidad
                }
                
                response = requests.get(API_BASE_URL, params=params, verify=False, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    resultado = {
                        'resultado': f"{data['resultado']} {simbolo}",
                        'valorOriginal': valor,
                        'unidadOrigen': de_unidad,
                        'valorConvertido': data['resultado'],
                        'unidadDestino': a_unidad
                    }
                    flash('Conversión realizada exitosamente', 'success')
                else:
                    error = f"Error del servidor: {response.status_code} - {response.text}"
                    flash(error, 'danger')
                
        except requests.exceptions.RequestException as e:
            error = f"Error de conexión: {str(e)}"
            flash(error, 'danger')
        except ValueError:
            error = "Por favor ingrese un valor numérico válido"
            flash(error, 'danger')
        except Exception as e:
            error = f"Error: {str(e)}"
            flash(error, 'danger')
    
    return render_template('conversion_temperatura.html', resultado=resultado, error=error)

# Verificar conexión con el servidor
@app.route('/verificar_servidor')
@login_requerido
def verificar_servidor():
    try:
        response = requests.get(API_BASE_URL.replace('/api/ConversionUnidades_Controlador', ''), verify=False, timeout=5)
        return jsonify({
            'estado': 'conectado',
            'codigo': response.status_code,
            'mensaje': 'Servidor .NET activo',
            'url': API_BASE_URL.replace('/api/ConversionUnidades_Controlador', '')
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'estado': 'desconectado',
            'mensaje': f'Error: {str(e)}',
            'url': API_BASE_URL.replace('/api/ConversionUnidades_Controlador', '')
        }), 500

if __name__ == '__main__':
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    app.run(debug=True, port=3000)
