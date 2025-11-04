# 📸 Instrucciones para agregar la imagen del login

## Pasos para configurar la imagen circular en el login:

### 1. Guardar la imagen
- Guarda la imagen del monstruo azul (Monster) en la carpeta del proyecto
- Nombre del archivo: `logo_login.png`
- Ruta completa: `c:\Arquitectura G5\TI1.1 SOAP_JAVA_SINBDD_GR05\02. CLIESC\CONVUNI_CLIESC_GR05\logo_login.png`

### 2. Instalar dependencias
Ejecuta uno de estos comandos:

```powershell
# Opción 1: Usar el script de instalación
.\instalar.bat

# Opción 2: Instalar manualmente
pip install Pillow
```

### 3. Ejecutar la aplicación
```powershell
python cliente_soap.py
```

## ✨ Características de la imagen:
- ✅ Tamaño circular automático (150x150 px)
- ✅ Se muestra en la parte superior del login
- ✅ Bordes suavizados profesionales
- ✅ Si no encuentra la imagen, el login funciona normalmente

## 🎨 Puedes usar cualquier imagen:
Solo asegúrate de:
1. Que sea formato PNG, JPG, o JPEG
2. Que el nombre sea `logo_login.png`
3. Que esté en la misma carpeta que `cliente_soap.py`

## 📝 Nota:
Si quieres usar un nombre diferente o ubicación diferente para la imagen, 
modifica esta línea en `cliente_soap.py` (línea ~185):

```python
ruta_imagen = os.path.join(os.path.dirname(__file__), "logo_login.png")
```

Cambia `"logo_login.png"` por el nombre que prefieras.
