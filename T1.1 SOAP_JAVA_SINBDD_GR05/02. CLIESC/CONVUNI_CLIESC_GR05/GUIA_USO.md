# 🎯 GUÍA DE USO - Cliente SOAP Conversor de Unidades

## 📖 Índice
1. [Instalación](#instalación)
2. [Inicio de la Aplicación](#inicio-de-la-aplicación)
3. [Pantalla de Login](#pantalla-de-login)
4. [Ventana Principal](#ventana-principal)
5. [Realizar Conversiones](#realizar-conversiones)
6. [Solución de Problemas](#solución-de-problemas)

---

## 🔧 Instalación

### Opción 1: Instalación Automática (Recomendada)
1. Haz doble clic en `instalar.bat`
2. Espera a que se instalen las dependencias
3. Presiona cualquier tecla para cerrar

### Opción 2: Instalación Manual
```powershell
# Abre PowerShell en la carpeta del proyecto
pip install zeep
```

---

## 🚀 Inicio de la Aplicación

### Opción 1: Ejecutar con script
1. Asegúrate de que el servicio SOAP esté ejecutándose en:
   ```
   http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
   ```
2. Haz doble clic en `ejecutar.bat`

### Opción 2: Ejecutar manualmente
```powershell
python cliente_soap.py
```

---

## 🔐 Pantalla de Login

### Descripción
Al iniciar la aplicación, verás una ventana de login elegante con:
- Campo de Usuario
- Campo de Contraseña (oculta con asteriscos)
- Botón "INGRESAR"

### Credenciales
```
Usuario:    MONSTER
Contraseña: Monster9
```

### Características
- ✅ Validación de campos vacíos
- ✅ Verificación de credenciales locales
- ✅ Autenticación con el servicio SOAP
- ✅ Presiona Enter para login rápido
- ✅ Mensajes de error claros

### Errores Comunes
- **"Por favor ingrese usuario y contraseña"**: Completa ambos campos
- **"Usuario o contraseña incorrectos"**: Verifica las credenciales
- **"No se pudo conectar al servicio SOAP"**: Verifica que el servidor esté activo

---

## 🏠 Ventana Principal

### Descripción
Después del login exitoso, se abre la ventana principal con tres pestañas:

### 🌡️ Pestaña: Temperatura
Conversiones disponibles:
1. **Celsius → Fahrenheit**
2. **Fahrenheit → Celsius**
3. **Celsius → Kelvin**

### ⚖️ Pestaña: Masa
Conversiones disponibles:
1. **Toneladas → Kilogramos**
2. **Kilogramos → Gramos**
3. **Gramos → Miligramos**

### 📏 Pestaña: Longitud
Conversiones disponibles:
1. **Kilómetros → Metros**
2. **Metros → Centímetros**
3. **Centímetros → Milímetros**

---

## 🔄 Realizar Conversiones

### Pasos:
1. **Selecciona la pestaña** de la categoría deseada
2. **Ingresa el valor** numérico en el campo de entrada
3. **Presiona "➜ Convertir"** o la tecla Enter
4. **El resultado** aparecerá automáticamente a la derecha

### Ejemplos de Uso:

#### Ejemplo 1: Convertir 100°C a Fahrenheit
```
1. Ve a la pestaña "🌡️ Temperatura"
2. En "Celsius a Fahrenheit", ingresa: 100
3. Presiona "Convertir"
4. Resultado: 212.0 °F
```

#### Ejemplo 2: Convertir 5 km a Metros
```
1. Ve a la pestaña "📏 Longitud"
2. En "Kilómetros a Metros", ingresa: 5
3. Presiona "Convertir"
4. Resultado: 5000.0 m
```

#### Ejemplo 3: Convertir 2.5 kg a Gramos
```
1. Ve a la pestaña "⚖️ Masa"
2. En "Kilogramos a Gramos", ingresa: 2.5
3. Presiona "Convertir"
4. Resultado: 2500.0 g
```

### ✨ Características
- ✅ Interfaz intuitiva y moderna
- ✅ Conversión en tiempo real
- ✅ Soporte para números decimales
- ✅ Atajo de teclado (Enter)
- ✅ Mensajes de error descriptivos
- ✅ Resultados destacados en verde

---

## 🐛 Solución de Problemas

### Problema 1: "No se pudo conectar al servicio SOAP"
**Causa**: El servidor SOAP no está ejecutándose

**Solución**:
1. Verifica que el servidor Java esté activo
2. Accede a: http://localhost:8080/ConUni_Soap_Java_GR05/CONUNI?wsdl
3. Si no carga, inicia el servidor SOAP

### Problema 2: "ModuleNotFoundError: No module named 'zeep'"
**Causa**: La librería zeep no está instalada

**Solución**:
```powershell
pip install zeep
```

### Problema 3: "Error en conversión"
**Causa**: Formato de entrada incorrecto

**Solución**:
- Verifica que ingresaste un número válido
- Usa punto (.) para decimales, no coma (,)
- Ejemplos válidos: 10, 10.5, -5, 0.25

### Problema 4: La ventana se abre y cierra inmediatamente
**Causa**: Error de Python o dependencias

**Solución**:
1. Abre PowerShell en la carpeta del proyecto
2. Ejecuta: `python cliente_soap.py`
3. Lee el mensaje de error
4. Instala dependencias faltantes

### Problema 5: "tkinter no disponible" (En Linux)
**Causa**: Tkinter no está instalado en el sistema

**Solución** (Linux):
```bash
sudo apt-get install python3-tk
```

---

## 📝 Validaciones de Entrada

### Números Aceptados:
- ✅ Enteros: `10`, `100`, `1000`
- ✅ Decimales: `10.5`, `3.14`, `0.5`
- ✅ Negativos: `-10`, `-5.5`
- ✅ Cero: `0`

### Números NO Aceptados:
- ❌ Texto: `abc`, `diez`
- ❌ Símbolos: `@`, `#`, `$`
- ❌ Coma decimal: `10,5` (usar punto: `10.5`)
- ❌ Espacios: ` 10 `, `1 0`

---

## 🎨 Características de la Interfaz

### Diseño Moderno:
- 🎨 Colores profesionales y legibles
- 📱 Interfaz responsive y adaptable
- 🖱️ Botones con efectos hover
- ⌨️ Atajos de teclado intuitivos
- 📊 Organización por pestañas
- ✨ Iconos visuales para cada categoría

### Accesibilidad:
- Fuentes grandes y legibles
- Contraste adecuado de colores
- Mensajes de error claros
- Feedback visual inmediato

---

## 📞 Soporte

### Grupo: GR05
### Proyecto: Cliente SOAP - Conversor de Unidades
### Tecnologías: Python 3, Tkinter, Zeep

---

## 🎓 Casos de Uso Académicos

### Demostración 1: Conversiones de Temperatura
```
Input: 0°C  → Output: 32°F
Input: 100°C → Output: 212°F
Input: 0°C → Output: 273.15K
```

### Demostración 2: Conversiones de Masa
```
Input: 1 tonelada → Output: 1000 kg
Input: 1 kg → Output: 1000 g
Input: 1 g → Output: 1000 mg
```

### Demostración 3: Conversiones de Longitud
```
Input: 1 km → Output: 1000 m
Input: 1 m → Output: 100 cm
Input: 1 cm → Output: 10 mm
```

---

## ✅ Checklist de Verificación

Antes de presentar o demostrar:
- [ ] Servidor SOAP ejecutándose
- [ ] Dependencias instaladas (zeep)
- [ ] Python 3.7+ instalado
- [ ] Credenciales correctas (MONSTER / Monster9)
- [ ] Prueba de cada tipo de conversión
- [ ] Verificación de manejo de errores

---

## 🏆 Ventajas de la Implementación

1. **Interfaz Gráfica Profesional**
   - No requiere conocimientos técnicos para usar
   - Diseño intuitivo y moderno

2. **Seguridad**
   - Sistema de login con credenciales
   - Validación en cliente y servidor

3. **Organización**
   - Conversiones agrupadas por categoría
   - Navegación por pestañas

4. **Manejo de Errores**
   - Mensajes claros y descriptivos
   - Validación de entrada robusta

5. **Facilidad de Uso**
   - Scripts de instalación automática
   - Documentación completa
   - Atajos de teclado

---

**¡Disfruta usando el Cliente SOAP Conversor de Unidades GR05! 🚀**
