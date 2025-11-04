# 🚀 INICIO RÁPIDO - Conversor de Unidades

## ⚡ Pasos para Ejecutar

### 1️⃣ Instalar Dependencias
```powershell
pip install -r requirements.txt
```

### 2️⃣ Asegurarse de que el Servidor .NET esté Corriendo
Tu servidor debe estar ejecutándose en: `http://localhost:5014`

### 3️⃣ Ejecutar el Cliente
```powershell
python cliente_api.py
```

## 🔑 Credenciales
- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## 📱 Navegación del Menú

### Menú Principal
```
1. ⚖️  Conversiones de MASA
2. 📏 Conversiones de LONGITUD
3. 🌡️  Conversiones de TEMPERATURA
4. 🔌 Verificar conexión con servidor
5. 🚪 Cerrar sesión y salir
```

### Ejemplo de Uso: Convertir 100 Kilogramos a Libras

1. Ejecuta `python cliente_api.py`
2. Inicia sesión automáticamente (credenciales quemadas)
3. Selecciona opción `1` (Conversiones de MASA)
4. Selecciona opción `4` (Kilogramos a Libras)
5. Ingresa `100` cuando te pida el valor
6. ¡Listo! Verás el resultado: `220.4620 libras`

### Ejemplo: Convertir 25 Celsius a Fahrenheit

1. Selecciona opción `3` (Conversiones de TEMPERATURA)
2. Selecciona opción `1` (Celsius a Fahrenheit)
3. Ingresa `25`
4. Resultado: `77.0000 fahrenheit`

## 🔧 Conversiones Disponibles

### ⚖️ MASA
1. Kilogramos → Gramos
2. Gramos → Miligramos
3. Toneladas → Kilogramos

### 📏 LONGITUD
1. Kilómetros → Metros
2. Metros → Centímetros
3. Centímetros → Milímetros

### 🌡️ TEMPERATURA
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Celsius → Kelvin

## ⚠️ Notas Importantes

- ✅ El cliente **funciona sin servidor** (conversiones se hacen localmente)
- ✅ El servidor solo se usa para **registrar** las conversiones
- ✅ Si el servidor no está disponible, el programa preguntará si deseas continuar
- ✅ Puedes usar `Ctrl+C` en cualquier momento para salir

## 🐛 Problemas Comunes

### No encuentra el módulo 'requests'
```powershell
pip install requests
```

### El servidor no está disponible
- Verifica que el servidor .NET esté corriendo
- Confirma el puerto 5014
- Puedes continuar sin servidor (opción en el inicio)

### Error de sintaxis al ejecutar
- Asegúrate de usar Python 3.7+
- Verifica: `python --version`

## 📞 Verificar Conexión

Usa la opción `4` del menú principal para verificar si el servidor está disponible en cualquier momento.

---

¡Disfruta convirtiendo unidades! 🎉
