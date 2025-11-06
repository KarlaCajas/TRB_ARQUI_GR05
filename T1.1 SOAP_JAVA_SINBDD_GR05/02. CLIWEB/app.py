from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para sesiones

# Credenciales quemadas
USUARIO_VALIDO = "MONSTER"
CONTRASENA_VALIDA = "Monster9"

# Diccionario de conversiones de unidades - SOLO LAS ESPECIFICADAS
CONVERSIONES_TEMPERATURA = {
    'c_a_f': {'unidad_origen': '°C', 'unidad_destino': '°F', 'nombre': 'Celsius a Fahrenheit'},
    'f_a_c': {'unidad_origen': '°F', 'unidad_destino': '°C', 'nombre': 'Fahrenheit a Celsius'},
    'c_a_k': {'unidad_origen': '°C', 'unidad_destino': 'K', 'nombre': 'Celsius a Kelvin'}
}

CONVERSIONES_MASA = {
    'kg_a_g': {'factor': 1000, 'unidad_origen': 'kg', 'unidad_destino': 'g', 'nombre': 'Kilogramos a Gramos'},
    'g_a_mg': {'factor': 1000, 'unidad_origen': 'g', 'unidad_destino': 'mg', 'nombre': 'Gramos a Miligramos'},
    't_a_kg': {'factor': 1000, 'unidad_origen': 't', 'unidad_destino': 'kg', 'nombre': 'Toneladas a Kilogramos'}
}

CONVERSIONES_LONGITUD = {
    'km_a_m': {'factor': 1000, 'unidad_origen': 'km', 'unidad_destino': 'm', 'nombre': 'Kilómetros a Metros'},
    'm_a_cm': {'factor': 100, 'unidad_origen': 'm', 'unidad_destino': 'cm', 'nombre': 'Metros a Centímetros'},
    'cm_a_mm': {'factor': 10, 'unidad_origen': 'cm', 'unidad_destino': 'mm', 'nombre': 'Centímetros a Milímetros'}
}

def convertir_masa(valor, tipo_conversion):
    """Convierte unidades de masa"""
    if tipo_conversion in CONVERSIONES_MASA:
        conv = CONVERSIONES_MASA[tipo_conversion]
        resultado = valor * conv['factor']
        return {
            'valor_original': valor,
            'unidad_original': conv['unidad_origen'],
            'valor_convertido': round(resultado, 4),
            'unidad_convertida': conv['unidad_destino'],
            'formula': f"{valor} {conv['unidad_origen']} × {conv['factor']} = {resultado:.4f} {conv['unidad_destino']}"
        }
    return None

def convertir_longitud(valor, tipo_conversion):
    """Convierte unidades de longitud"""
    if tipo_conversion in CONVERSIONES_LONGITUD:
        conv = CONVERSIONES_LONGITUD[tipo_conversion]
        resultado = valor * conv['factor']
        return {
            'valor_original': valor,
            'unidad_original': conv['unidad_origen'],
            'valor_convertido': round(resultado, 4),
            'unidad_convertida': conv['unidad_destino'],
            'formula': f"{valor} {conv['unidad_origen']} × {conv['factor']} = {resultado:.4f} {conv['unidad_destino']}"
        }
    return None

def convertir_temperatura(valor, tipo_conversion):
    """Convierte unidades de temperatura"""
    if tipo_conversion not in CONVERSIONES_TEMPERATURA:
        return None
    
    conv = CONVERSIONES_TEMPERATURA[tipo_conversion]
    
    # Fórmulas de conversión de temperatura
    if tipo_conversion == 'c_a_f':
        resultado = (valor * 9/5) + 32
        formula = f"({valor} × 9/5) + 32 = {resultado:.4f} {conv['unidad_destino']}"
    elif tipo_conversion == 'c_a_k':
        resultado = valor + 273.15
        formula = f"{valor} + 273.15 = {resultado:.4f} {conv['unidad_destino']}"
    elif tipo_conversion == 'f_a_c':
        resultado = (valor - 32) * 5/9
        formula = f"({valor} - 32) × 5/9 = {resultado:.4f} {conv['unidad_destino']}"
    else:
        return None
    
    return {
        'valor_original': valor,
        'unidad_original': conv['unidad_origen'],
        'valor_convertido': round(resultado, 4),
        'unidad_convertida': conv['unidad_destino'],
        'formula': formula
    }


@app.route('/')
def index():
    """Página principal - redirige según el estado de autenticación"""
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login"""
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        contrasena = request.form.get('contrasena', '').strip()
        
        # Validar credenciales
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            session['usuario'] = usuario
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    """Panel principal después del login"""
    if 'usuario' not in session:
        flash('Debe iniciar sesión primero', 'warning')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', 
                         usuario=session['usuario'],
                         conversiones_masa=CONVERSIONES_MASA,
                         conversiones_longitud=CONVERSIONES_LONGITUD,
                         conversiones_temperatura=CONVERSIONES_TEMPERATURA)


@app.route('/convertir/<categoria>', methods=['GET', 'POST'])
def convertir(categoria):
    """Página de conversión de unidades"""
    if 'usuario' not in session:
        flash('Debe iniciar sesión primero', 'warning')
        return redirect(url_for('login'))
    
    resultado = None
    error = None
    conversiones = {}
    titulo = ""
    
    # Determinar la categoría
    if categoria == 'masa':
        conversiones = CONVERSIONES_MASA
        titulo = "Conversión de Masa"
    elif categoria == 'longitud':
        conversiones = CONVERSIONES_LONGITUD
        titulo = "Conversión de Longitud"
    elif categoria == 'temperatura':
        conversiones = CONVERSIONES_TEMPERATURA
        titulo = "Conversión de Temperatura"
    else:
        flash('Categoría de conversión no válida', 'error')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        try:
            valor = float(request.form.get('valor', 0))
            tipo_conversion = request.form.get('tipo_conversion', '')
            
            # Realizar la conversión según la categoría
            if categoria == 'masa':
                resultado = convertir_masa(valor, tipo_conversion)
            elif categoria == 'longitud':
                resultado = convertir_longitud(valor, tipo_conversion)
            elif categoria == 'temperatura':
                resultado = convertir_temperatura(valor, tipo_conversion)
            
            if resultado is None:
                error = "Tipo de conversión no válido"
                
        except ValueError:
            error = "Por favor ingrese un valor numérico válido"
        except Exception as e:
            error = f"Error al realizar la conversión: {e}"
    
    return render_template('convertir.html',
                         categoria=categoria,
                         titulo=titulo,
                         conversiones=conversiones,
                         resultado=resultado,
                         error=error)


@app.route('/logout')
def logout():
    """Cerrar sesión"""
    session.pop('usuario', None)
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
