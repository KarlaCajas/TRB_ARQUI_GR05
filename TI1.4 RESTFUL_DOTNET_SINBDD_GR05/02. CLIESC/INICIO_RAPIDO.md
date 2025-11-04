# 🚀 Inicio Rápido - Calculadora de Conversión de Unidades

## ▶️ Para ejecutar la aplicación:

### 1. (Opcional) Inicia el servidor REST .NET
Si deseas guardar las conversiones en el servidor:
```
El servidor debe estar disponible en: http://localhost:5014/api/ConversionUnidades_Controlador
```

**Nota:** La aplicación funciona perfectamente SIN servidor (modo offline)

### 2. Instala las dependencias (solo la primera vez)
```powershell
pip install -r requirements.txt
```

### 3. Ejecuta la aplicación
```powershell
python app.py
```

O haz doble clic en: `ejecutar.bat`

## 🔐 Credenciales de Login

- **Usuario:** `MONSTER`
- **Contraseña:** `Monster9`

## 🔄 Conversiones Disponibles

### 🌡️ TEMPERATURA
- **Celsius a Fahrenheit** (C → F)
- **Fahrenheit a Celsius** (F → C)
- **Celsius a Kelvin** (C → K)

### ⚖️ MASA
- **Kilogramos a Gramos** (kg → g)
- **Gramos a Miligramos** (g → mg)
- **Toneladas a Kilogramos** (t → kg)

### 📏 LONGITUD
- **Kilómetros a Metros** (km → m)
- **Metros a Centímetros** (m → cm)
- **Centímetros a Milímetros** (cm → mm)

### 📏 LONGITUD
- **Kilómetros a Metros** (km → m)
- **Metros a Centímetros** (m → cm)
- **Centímetros a Milímetros** (cm → mm)

## 🎯 Cómo Usar

1. **Inicia sesión** con las credenciales
2. **Selecciona** una categoría (Temperatura, Masa o Longitud)
3. **Elige** el tipo de conversión específica
4. **Ingresa** el valor a convertir
5. **Presiona** el botón "CONVERTIR" o Enter
6. **¡Listo!** El resultado aparece con sus unidades

## 💡 Ejemplo de Uso

```
1. Categoría: Temperatura
2. Conversión: Celsius a Fahrenheit
3. Valor: 25
4. Resultado: 25 °C = 77.00 °F
```

## 📝 Características

- ✅ Calculadora simple y directa
- ✅ Resultados con 2 decimales
- ✅ Todos los resultados incluyen unidades
- ✅ Botón "Limpiar" para reiniciar
- ✅ Presiona Enter para convertir rápidamente
- ✅ Validación de campos
- ✅ **Conexión con servidor REST .NET** (opcional)
- ✅ **Guardado automático** de conversiones en el servidor
- ✅ **Modo offline** si el servidor no está disponible
- ✅ **Botón "Cerrar Sesión"** para volver al login
- ✅ **Confirmación** antes de salir

## 🌐 Modos de Funcionamiento

### Con Servidor (Online):
- ✅ Las conversiones se guardan automáticamente
- ✅ Indicador: "✅ Conectado al servidor"
- ✅ Cada conversión crea un registro en la base de datos

### Sin Servidor (Offline):
- ✅ Las conversiones funcionan normalmente
- ✅ Indicador: "⚠️ Servidor no disponible (modo offline)"
- ✅ No se guardan en el servidor (solo cálculo local)

## 🚪 Navegación

### Cerrar Sesión:
1. Clic en "🚪 Cerrar Sesión"
2. Confirma la acción
3. Vuelve automáticamente al login
4. Puedes ingresar nuevamente

### Salir de la Aplicación:
1. Clic en la X de la ventana
2. Confirma "¿Desea salir?"
3. La aplicación se cierra completamente

## 📁 Archivos principales

- `app.py` - Ejecutar para iniciar la aplicación completa
- `login_window.py` - Ventana de login
- `main_window.py` - Calculadora de conversiones
- `api_client.py` - Cliente para conectar con servidor REST
- `FLUJO_NAVEGACION.md` - Documentación del flujo completo

## ✨ Sin necesidad obligatoria de servidor REST

Esta aplicación funciona de dos formas:
1. **Con servidor:** Guarda conversiones en el servidor REST .NET
2. **Sin servidor:** Funciona como calculadora local offline

¡Listo para usar! 🎉
