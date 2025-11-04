# 🔄 Flujo de Navegación y Características

## 🚪 Flujo de Navegación Completo

```
┌─────────────────────────────────────────────────────────────┐
│                    INICIO DE APLICACIÓN                      │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
        ┌─────────────────┐
        │  VENTANA LOGIN  │
        │  MONSTER        │
        │  Monster9       │
        └────────┬────────┘
                 │
          Login exitoso?
                 │
        ┌────────┴────────┐
        │ NO              │ SÍ
        ▼                 ▼
   ┌────────┐      ┌──────────────────┐
   │ SALIR  │      │   CALCULADORA    │
   └────────┘      │   (Main Window)  │
                   └────────┬─────────┘
                            │
                    ┌───────┴────────┐
                    │                │
                    ▼                ▼
            ┌───────────────┐  ┌────────────┐
            │ CERRAR SESIÓN │  │   SALIR    │
            │  (Logout)     │  │  (Cerrar)  │
            └───────┬───────┘  └─────┬──────┘
                    │                 │
                    ▼                 ▼
            ┌───────────────┐  ┌─────────┐
            │  VOLVER A     │  │  SALIR  │
            │    LOGIN      │  │   APP   │
            └───────────────┘  └─────────┘
```

## ✨ Características Implementadas

### 🔐 Sistema de Login
- **Usuario hardcodeado:** `MONSTER`
- **Contraseña hardcodeada:** `Monster9`
- **Validación:** Campos vacíos y credenciales incorrectas
- **Navegación:** Login exitoso → Calculadora

### 🔄 Calculadora de Conversiones
- **9 tipos de conversiones** en 3 categorías
- **Cálculo instantáneo** de conversiones
- **Resultados con unidades** incluidas
- **Conexión al servidor REST** para guardar conversiones
- **Modo offline** si el servidor no está disponible

### 🌐 Integración con API REST
- **Verificación automática** de conexión al servidor
- **Guardado automático** de cada conversión realizada
- **Indicador de estado** de conexión
- **Manejo de errores** si el servidor no responde
- **Modo offline** funcional sin servidor

### 🚪 Cerrar Sesión
- **Botón "Cerrar Sesión"** en la calculadora
- **Confirmación** antes de cerrar sesión
- **Vuelve al login** automáticamente
- **Permite cambiar de usuario** sin cerrar la app

### ❌ Salir de la Aplicación
- **Botón X** en la ventana (cerrar completamente)
- **Confirmación** antes de salir
- **Cierra la aplicación** completamente

## 📊 Estados de Conexión

### ✅ Servidor Disponible
```
Estado: ✅ Conectado al servidor
- Las conversiones se guardan automáticamente
- Cada conversión crea un registro en el servidor
```

### ⚠️ Servidor No Disponible
```
Estado: ⚠️ Servidor no disponible (modo offline)
- Las conversiones funcionan normalmente
- NO se guardan en el servidor
- Modo calculadora local
```

### ✅ Guardado Exitoso
```
Estado: ✅ Guardado en servidor
- La conversión se guardó correctamente
- El registro está disponible en el servidor
```

### ⚠️ Error al Guardar
```
Estado: ⚠️ No se pudo guardar
- La conversión se calculó correctamente
- NO se guardó en el servidor (error temporal)
```

## 🎯 Casos de Uso

### Caso 1: Uso Normal con Servidor
```
1. Usuario inicia la aplicación
2. Login con MONSTER / Monster9
3. Ve "✅ Conectado al servidor"
4. Selecciona: Temperatura → Celsius a Fahrenheit
5. Ingresa: 25
6. Presiona: CONVERTIR
7. Ve resultado: 25 °C = 77.00 °F
8. Ve: "✅ Guardado en servidor"
9. Conversión guardada en la base de datos
```

### Caso 2: Uso sin Servidor (Offline)
```
1. Usuario inicia la aplicación
2. Login con MONSTER / Monster9
3. Ve "⚠️ Servidor no disponible (modo offline)"
4. Selecciona: Masa → Kilogramos a Gramos
5. Ingresa: 2.5
6. Presiona: CONVERTIR
7. Ve resultado: 2.5 kg = 2500.00 g
8. Estado permanece en "⚠️ Servidor no disponible"
9. Conversión NO se guarda (modo local)
```

### Caso 3: Cerrar Sesión y Volver
```
1. Usuario está en la calculadora
2. Clic en "🚪 Cerrar Sesión"
3. Confirma: "¿Desea cerrar la sesión de MONSTER?"
4. Vuelve automáticamente al login
5. Puede ingresar nuevamente con las credenciales
6. Regresa a la calculadora
```

### Caso 4: Salir de la Aplicación
```
1. Usuario está en la calculadora
2. Clic en la X de la ventana
3. Confirma: "¿Desea salir de la aplicación?"
4. La aplicación se cierra completamente
```

## 📝 Datos Guardados en el Servidor

Cada conversión realizada guarda en el servidor:

```json
{
  "tipoConversion": "Temperatura - Celsius a Fahrenheit",
  "unidadOrigen": "Fahrenheit",
  "unidadDestino": "",
  "factorConversion": 2.8,
  "descripcion": "Conversión realizada por MONSTER: 25 °C = 77.00 °F"
}
```

### Campos:
- **tipoConversion:** Categoría y tipo de conversión
- **unidadOrigen:** Unidad de entrada
- **unidadDestino:** Unidad de salida
- **factorConversion:** Factor calculado
- **descripcion:** Texto completo con usuario y resultado

## 🔧 Configuración de API

### URL del Servidor
```
http://localhost:5014/api/ConversionUnidades_Controlador
```

### Cambiar URL
Editar `api_client.py`:
```python
class APIClient:
    def __init__(self, base_url: str = "TU_URL_AQUI"):
        self.base_url = base_url
```

## ⚡ Atajos de Teclado

| Tecla | Acción |
|-------|--------|
| **Enter** | Convertir (después de ingresar valor) |
| **Tab** | Navegar entre campos |
| **Esc** | (No implementado) |

## 🎨 Colores de Estado

| Color | Significado |
|-------|-------------|
| 🟢 Verde | Conexión exitosa / Guardado OK |
| 🟠 Naranja | Advertencia / Modo offline |
| 🔴 Rojo | Error |
| 🔵 Azul | Información |

## 💡 Recomendaciones

### Para Uso con Servidor:
1. ✅ Asegúrate de que el servidor .NET esté ejecutándose
2. ✅ Verifica que la URL sea correcta
3. ✅ Revisa el firewall si hay problemas de conexión

### Para Uso sin Servidor:
1. ✅ La aplicación funciona perfectamente offline
2. ✅ Todas las conversiones se calculan localmente
3. ✅ No necesitas el servidor para usar la calculadora

### Para Cambiar de Usuario:
1. ✅ Usa el botón "Cerrar Sesión"
2. ✅ Vuelve al login automáticamente
3. ✅ Ingresa con otras credenciales si lo deseas

---

¡La aplicación ahora tiene flujo completo de navegación! 🎉
