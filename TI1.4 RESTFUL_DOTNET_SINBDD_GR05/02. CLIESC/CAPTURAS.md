# 📸 Capturas de Pantalla (Descripción Visual)

## 🔐 Ventana de Login

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║         Sistema de Conversión de Unidades                ║
║                   Iniciar Sesión                          ║
║                                                           ║
║   Usuario:      [MONSTER                      ]          ║
║                                                           ║
║   Contraseña:   [*********                    ]          ║
║                                                           ║
║                                                           ║
║       ┌─────────────────┐   ┌─────────────────┐         ║
║       │ Iniciar Sesión  │   │     Salir       │         ║
║       └─────────────────┘   └─────────────────┘         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

### Características:
- ✅ Campos de texto para usuario y contraseña
- ✅ Contraseña oculta con asteriscos
- ✅ Botones con colores distintivos
- ✅ Ventana centrada en la pantalla
- ✅ Validación en tiempo real

---

## 🖥️ Ventana Principal

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║  🔄 Sistema de Conversión de Unidades                      👤 MONSTER        ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  ┌─────────────────────────┐  ┌──────────────────────────────────────────┐  ║
║  │ 📝 Datos de Conversión  │  │ 📋 Lista de Conversiones                 │  ║
║  ├─────────────────────────┤  ├──────────────────────────────────────────┤  ║
║  │                         │  │ ID | Tipo  | Origen | Destino | Factor  │  ║
║  │ ID: [1          ]       │  │ ══════════════════════════════════════   │  ║
║  │                         │  │ 1  | Long. | metros | km      | 0.001   │  ║
║  │ Tipo de Conversión:     │  │ 2  | Peso  | gramos | kg      | 0.001   │  ║
║  │ [Longitud       ]       │  │ 3  | Temp. | C      | F       | 1.8     │  ║
║  │                         │  │ 4  | Vol.  | litros | ml      | 1000    │  ║
║  │ Unidad Origen:          │  │ 5  | Dist. | millas | km      | 1.609   │  ║
║  │ [metros         ]       │  │                                          │  ║
║  │                         │  │                                          │  ║
║  │ Unidad Destino:         │  │                                          │  ║
║  │ [kilómetros     ]       │  │                                          │  ║
║  │                         │  │                                          │  ║
║  │ Factor de Conversión:   │  │                                          │  ║
║  │ [0.001          ]       │  │                                          │  ║
║  │                         │  │                                          │  ║
║  │ Descripción:            │  │                                          │  ║
║  │ ┌─────────────────────┐ │  │                                          │  ║
║  │ │Conversión de metros │ │  │                                          │  ║
║  │ │a kilómetros...      │ │  │                                          │  ║
║  │ │                     │ │  │                                          │  ║
║  │ └─────────────────────┘ │  │                                          │  ║
║  │                         │  │                                          │  ║
║  │  ┌──────┐ ┌──────┐     │  └──────────────────────────────────────────┘  ║
║  │  │Crear │ │Updt. │     │                                                 ║
║  │  └──────┘ └──────┘     │                                                 ║
║  └─────────────────────────┘                                                 ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║  🔄 Refrescar    🗑️ Eliminar    ✅ Listo              🚪 Cerrar Sesión      ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Características:
- ✅ Layout de dos columnas (Formulario | Lista)
- ✅ Tabla interactiva con todas las conversiones
- ✅ Formulario completo con validación
- ✅ Barra de estado en tiempo real
- ✅ Colores distintivos para cada acción
- ✅ Usuario visible en la barra superior

---

## 📊 Estados de la Aplicación

### ✅ Estado: Exitoso
```
Estado: ✅ Conversión creada exitosamente
```

### ❌ Estado: Error
```
Estado: ❌ Error: No se pudo conectar con el servidor
```

### ℹ️ Estado: Información
```
Estado: ℹ️ Cargando conversiones...
```

### ⚠️ Estado: Advertencia
```
Estado: ⚠️ Por favor complete todos los campos
```

---

## 🎨 Esquema de Colores

| Elemento | Color | Uso |
|----------|-------|-----|
| **Header** | Azul (#2196F3) | Barra superior |
| **Crear** | Verde (#4CAF50) | Acción positiva |
| **Actualizar** | Naranja (#FF9800) | Modificación |
| **Eliminar** | Rojo (#f44336) | Acción destructiva |
| **Refrescar** | Azul (#2196F3) | Recarga de datos |
| **Limpiar** | Gris (#9E9E9E) | Reset de formulario |
| **Salir** | Gris oscuro (#607D8B) | Cierre |

---

## 💡 Diálogos y Mensajes

### Mensaje de Confirmación (Eliminar)
```
╔═══════════════════════════════════╗
║   Confirmar Eliminación           ║
╟───────────────────────────────────╢
║                                   ║
║  ¿Está seguro de eliminar la     ║
║  conversión: 'Longitud'?          ║
║                                   ║
║     ┌────┐         ┌────┐        ║
║     │ Sí │         │ No │        ║
║     └────┘         └────┘        ║
╚═══════════════════════════════════╝
```

### Mensaje de Error (Campos vacíos)
```
╔═══════════════════════════════════╗
║   Campo requerido                 ║
╟───────────────────────────────────╢
║                                   ║
║  Por favor, ingrese el tipo de   ║
║  conversión                       ║
║                                   ║
║           ┌────────┐              ║
║           │   OK   │              ║
║           └────────┘              ║
╚═══════════════════════════════════╝
```

### Mensaje de Éxito (Crear)
```
╔═══════════════════════════════════╗
║   Éxito                           ║
╟───────────────────────────────────╢
║                                   ║
║  La conversión se creó           ║
║  correctamente                    ║
║                                   ║
║           ┌────────┐              ║
║           │   OK   │              ║
║           └────────┘              ║
╚═══════════════════════════════════╝
```

### Mensaje de Bienvenida (Login)
```
╔═══════════════════════════════════╗
║   Login Exitoso                   ║
╟───────────────────────────────────╢
║                                   ║
║  ¡Bienvenido MONSTER!             ║
║                                   ║
║           ┌────────┐              ║
║           │   OK   │              ║
║           └────────┘              ║
╚═══════════════════════════════════╝
```

---

## 🎬 Flujo Visual de Uso

### 1️⃣ Crear una nueva conversión
```
Abrir app → Login → Llenar formulario → Clic "Crear" → Ver en lista
```

### 2️⃣ Actualizar una conversión
```
Seleccionar en lista → Editar campos → Clic "Actualizar" → Ver cambios
```

### 3️⃣ Eliminar una conversión
```
Seleccionar en lista → Clic "Eliminar" → Confirmar → Lista actualizada
```

### 4️⃣ Refrescar datos
```
Clic "Refrescar" → Consulta API → Lista actualizada
```

---

## 📱 Responsividad

- ✅ Ventana redimensionable
- ✅ Scrollbars automáticos en la tabla
- ✅ Adaptación del contenido
- ✅ Centrado automático
- ✅ Tamaños mínimos respetados

---

## 🎯 Experiencia de Usuario

### Interacciones destacadas:
- **Tecla Enter**: Navega entre campos y ejecuta login
- **Selección en tabla**: Carga automáticamente el formulario
- **Doble clic**: (Futuro) Abrir detalle
- **Colores semánticos**: Verde = OK, Rojo = Peligro, Azul = Info
- **Mensajes claros**: Estados visibles en todo momento
- **Confirmaciones**: Antes de acciones destructivas

---

¡La interfaz es intuitiva y profesional! 🎨✨
