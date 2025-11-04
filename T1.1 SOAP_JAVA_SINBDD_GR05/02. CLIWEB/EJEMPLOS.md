# 📚 Ejemplos de Uso - Sistema de Conversión

## Ejemplos Prácticos de Conversiones

### ⚖️ Ejemplos de Conversión de Masa

#### Ejemplo 1: Convertir Kilogramos a Gramos
```
Entrada:
- Tipo de conversión: Kilogramos a Gramos
- Valor: 5

Resultado:
- Valor Original: 5 kg
- Valor Convertido: 5000.0000 g
- Fórmula: 5 kg × 1000 = 5000.0000 g
```

#### Ejemplo 2: Convertir Libras a Kilogramos
```
Entrada:
- Tipo de conversión: Libras a Kilogramos
- Valor: 150

Resultado:
- Valor Original: 150 lb
- Valor Convertido: 68.0388 kg
- Fórmula: 150 lb × 0.453592 = 68.0388 kg
```

#### Ejemplo 3: Convertir Gramos a Onzas
```
Entrada:
- Tipo de conversión: Gramos a Onzas
- Valor: 500

Resultado:
- Valor Original: 500 g
- Valor Convertido: 17.6370 oz
- Fórmula: 500 g × 0.035274 = 17.6370 oz
```

---

### 📏 Ejemplos de Conversión de Longitud

#### Ejemplo 1: Convertir Metros a Centímetros
```
Entrada:
- Tipo de conversión: Metros a Centímetros
- Valor: 2.5

Resultado:
- Valor Original: 2.5 m
- Valor Convertido: 250.0000 cm
- Fórmula: 2.5 m × 100 = 250.0000 cm
```

#### Ejemplo 2: Convertir Pies a Metros
```
Entrada:
- Tipo de conversión: Pies a Metros
- Valor: 10

Resultado:
- Valor Original: 10 ft
- Valor Convertido: 3.0480 m
- Fórmula: 10 ft × 0.3048 = 3.0480 m
```

#### Ejemplo 3: Convertir Kilómetros a Metros
```
Entrada:
- Tipo de conversión: Kilómetros a Metros
- Valor: 5.5

Resultado:
- Valor Original: 5.5 km
- Valor Convertido: 5500.0000 m
- Fórmula: 5.5 km × 1000 = 5500.0000 m
```

#### Ejemplo 4: Convertir Pulgadas a Centímetros
```
Entrada:
- Tipo de conversión: Pulgadas a Centímetros
- Valor: 12

Resultado:
- Valor Original: 12 in
- Valor Convertido: 30.4800 cm
- Fórmula: 12 in × 2.54 = 30.4800 cm
```

---

### 🌡️ Ejemplos de Conversión de Temperatura

#### Ejemplo 1: Convertir Celsius a Fahrenheit
```
Entrada:
- Tipo de conversión: Celsius a Fahrenheit
- Valor: 25

Resultado:
- Valor Original: 25 °C
- Valor Convertido: 77.00 °F
- Fórmula: (25 × 9/5) + 32 = 77.00 °F
```

#### Ejemplo 2: Convertir Fahrenheit a Celsius
```
Entrada:
- Tipo de conversión: Fahrenheit a Celsius
- Valor: 100

Resultado:
- Valor Original: 100 °F
- Valor Convertido: 37.78 °C
- Fórmula: (100 - 32) × 5/9 = 37.78 °C
```

#### Ejemplo 3: Convertir Celsius a Kelvin
```
Entrada:
- Tipo de conversión: Celsius a Kelvin
- Valor: 0

Resultado:
- Valor Original: 0 °C
- Valor Convertido: 273.15 K
- Fórmula: 0 + 273.15 = 273.15 K
```

#### Ejemplo 4: Convertir Kelvin a Fahrenheit
```
Entrada:
- Tipo de conversión: Kelvin a Fahrenheit
- Valor: 300

Resultado:
- Valor Original: 300 K
- Valor Convertido: 80.33 °F
- Fórmula: (300 - 273.15) × 9/5 + 32 = 80.33 °F
```

---

## 🎯 Casos de Uso Comunes

### En Cocina
- **Recetas Internacionales**: Convertir onzas a gramos
  - Ejemplo: 8 oz de harina = 226.796 g

### En Construcción
- **Mediciones**: Convertir pies a metros
  - Ejemplo: Habitación de 12 ft = 3.6576 m

### En Ciencia
- **Experimentos**: Convertir Celsius a Kelvin
  - Ejemplo: Temperatura ambiente 20°C = 293.15 K

### En Viajes
- **Equipaje**: Convertir libras a kilogramos
  - Ejemplo: Maleta de 50 lb = 22.6796 kg

### En Clima
- **Pronósticos**: Convertir Fahrenheit a Celsius
  - Ejemplo: 75°F = 23.89°C

---

## 💡 Consejos de Uso

1. **Números Decimales**: Use punto (.) como separador decimal
   - Correcto: `10.5`
   - Incorrecto: `10,5`

2. **Precisión**: Los resultados muestran hasta 4 decimales para masa/longitud y 2 para temperatura

3. **Valores Negativos**: Permitidos especialmente en temperaturas
   - Ejemplo: -40°C = -40°F (coinciden en este punto)

4. **Números Grandes**: El sistema maneja valores grandes correctamente
   - Ejemplo: 1000000 g = 1000 kg

---

## 🔄 Flujo de Trabajo Típico

1. **Acceder al Dashboard** después del login
2. **Seleccionar la categoría** apropiada (Masa, Longitud o Temperatura)
3. **Elegir la conversión específica** del menú
4. **Ingresar el valor numérico**
5. **Hacer clic en Convertir**
6. **Revisar el resultado** con todas las unidades mostradas
7. **Realizar otra conversión** o volver al dashboard

---

## ✅ Validaciones Automáticas

- ✔️ **Entrada numérica**: Solo acepta números válidos
- ✔️ **Tipo de conversión**: Debe seleccionar una opción válida
- ✔️ **Cálculos precisos**: Usa factores de conversión estándar
- ✔️ **Formato de salida**: Siempre muestra las unidades correctas
