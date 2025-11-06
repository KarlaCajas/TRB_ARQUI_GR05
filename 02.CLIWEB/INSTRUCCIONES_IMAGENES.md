# Instrucciones para las Imágenes del Cliente Web

## 📸 Imágenes Necesarias

Coloca las siguientes imágenes en la carpeta `02.CLIWEB/static/images/`:

### 1. **login-solivan.jpeg**
- Imagen circular de Sullivan de Monsters University
- Para el login
- Ruta completa: `c:\ARQUITECTURA\TI1.2 SOAP_DOTNET_SINBDD_GRO#5\02.CLIWEB\static\images\login-solivan.jpeg`

### 2. **Monsters_university_6.jpg** 
- Imagen de fondo con los monstruos de Monsters University
- Para el dashboard
- Ruta completa: `c:\ARQUITECTURA\TI1.2 SOAP_DOTNET_SINBDD_GRO#5\02.CLIWEB\static\images\Monsters_university_6.jpg`

## 📂 Estructura de Carpetas

```
02.CLIWEB/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   └── images/          ← COLOCA LAS IMÁGENES AQUÍ
│       ├── login-solivan.jpeg
│       └── Monsters_university_6.jpg
└── templates/
    ├── base.html
    ├── login.html
    └── dashboard.html
```

## ✅ Si No Colocas las Imágenes

El sistema funcionará igual:
- **Login**: Mostrará un círculo azul con emoji 🎓 como placeholder
- **Dashboard**: Mostrará fondo blanco/gris

## 🚀 Ejecutar el Cliente Web

```powershell
cd "c:\ARQUITECTURA\TI1.2 SOAP_DOTNET_SINBDD_GRO#5\02.CLIWEB"
python app.py
```

Luego abre: http://localhost:5000

## 🔐 Credenciales de Acceso (Quemadas en el código)

- **Usuario**: `MONSTER`
- **Contraseña**: `Monster9`

**IMPORTANTE**: Los campos en el formulario son:
- Campo "username" → Ingresar: MONSTER
- Campo "password" → Ingresar: Monster9

## ⚠️ Solución de Problemas

### No puedo iniciar sesión
- Verifica que estés usando exactamente: **MONSTER** (todo en mayúsculas)
- Contraseña: **Monster9** (M mayúscula, resto minúsculas, termina en 9)
- Los campos del formulario se corrigieron para usar `username` y `password`

### Las imágenes no se muestran
- Coloca las imágenes en `static/images/` con los nombres exactos
- Reinicia el servidor Flask después de agregar las imágenes
- Verifica que los nombres de archivo respeten mayúsculas/minúsculas
