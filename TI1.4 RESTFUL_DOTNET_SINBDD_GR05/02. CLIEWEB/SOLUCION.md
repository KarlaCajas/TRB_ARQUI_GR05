# 🔧 SOLUCIÓN A LOS PROBLEMAS

## ✅ PROBLEMAS CORREGIDOS

### 1. **Error 405 - Método no permitido**
- **Causa**: El servidor .NET no acepta POST con JSON
- **Solución**: Cambié todas las peticiones para usar GET con parámetros de consulta (query parameters)
- **Estado**: ✅ CORREGIDO

### 2. **Login no aparece**
- **Causa**: Sesión guardada en el navegador
- **Solución**: Limpiar la sesión visitando: `http://localhost:3000/clear`
- **Estado**: ✅ CORREGIDO

### 3. **Fondo no visible**
- **Causa**: Overlay muy oscuro
- **Solución**: Reduje la opacidad del overlay de 40% a 30%
- **Estado**: ✅ CORREGIDO

---

## 🚀 CÓMO USAR EL SISTEMA

### Paso 1: Iniciar Servidor .NET
Asegúrate de que tu servidor .NET esté ejecutándose en:
```
https://localhost:7102
```

### Paso 2: Iniciar Cliente Flask
Ejecuta:
```bash
cd "c:\Arquitectura G5\TI1.4 RESTFUL_DOTNET_SINBDD_GR05\02. CLIEWEB"
python app.py
```

### Paso 3: Acceder al Sistema
Abre tu navegador en:
```
http://localhost:3000/clear
```
(Esto limpiará la sesión y te llevará al login)

### Paso 4: Login
- **Usuario**: `MONSTER`
- **Contraseña**: `Monster9`

### Paso 5: Realizar Conversiones
Selecciona el tipo de conversión:
- **Masa**: kg ↔ g, g ↔ mg, t ↔ kg
- **Longitud**: km ↔ m, m ↔ cm, cm ↔ mm
- **Temperatura**: °C ↔ °F, °F ↔ °C, °C ↔ K

---

## 📋 CONVERSIONES DISPONIBLES

### 🌡️ Temperatura
| De | A |
|---|---|
| Celsius | Fahrenheit |
| Fahrenheit | Celsius |
| Celsius | Kelvin |

### ⚖️ Masa
| De | A |
|---|---|
| Kilogramo (kg) | Gramo (g) |
| Gramo (g) | Miligramo (mg) |
| Tonelada (t) | Kilogramo (kg) |

### 📏 Longitud
| De | A |
|---|---|
| Kilómetro (km) | Metro (m) |
| Metro (m) | Centímetro (cm) |
| Centímetro (cm) | Milímetro (mm) |

---

## 🔍 VERIFICAR CONEXIÓN AL SERVIDOR

Puedes usar el script de prueba:
```bash
python test_methods.py
```

Esto mostrará si el servidor .NET está disponible y respondiendo correctamente.

---

## 🎨 DISEÑO VISUAL

✅ **Fondo6.jpg visible en:**
- Login
- Menú principal  
- Conversión de Masa
- Conversión de Longitud
- Conversión de Temperatura

✅ **Características:**
- Overlay semitransparente (30%)
- Fondo fijo (no se desplaza)
- Tarjetas con transparencia
- Animaciones suaves

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### Si no aparece el login:
```
Visita: http://localhost:3000/clear
```

### Si sale error 405:
- Verifica que el servidor .NET esté corriendo
- El cliente ahora usa GET en lugar de POST

### Si no se ve el fondo:
- Verifica que existe: `static/imagenes/fondo6.jpg`
- Presiona Ctrl+F5 para recargar sin caché

### Si hay error de conexión:
- Asegúrate de que el servidor .NET está en: `https://localhost:7102`
- Verifica que el endpoint es: `/api/ConversionUnidades_Controlador`

---

## 📞 ENDPOINTS DEL SERVIDOR

El cliente ahora se conecta usando:
```
GET https://localhost:7102/api/ConversionUnidades_Controlador?tipo=masa&valor=100&deUnidad=kilogramo&aUnidad=gramo
```

Formato de parámetros:
- `tipo`: masa | longitud | temperatura
- `valor`: número a convertir
- `deUnidad`: unidad de origen
- `aUnidad`: unidad de destino

---

**¡Sistema listo para usar! 🎉**
