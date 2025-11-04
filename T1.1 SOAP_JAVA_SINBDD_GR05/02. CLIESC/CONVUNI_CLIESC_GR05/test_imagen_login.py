"""
Script de prueba para verificar la imagen circular en el login
"""
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import os

def crear_imagen_circular(ruta_imagen, tamano=150):
    """Crea una imagen circular desde un archivo"""
    try:
        # Verificar si existe el archivo
        if not os.path.exists(ruta_imagen):
            print(f"❌ No se encontró la imagen: {ruta_imagen}")
            return None
        
        print(f"✓ Imagen encontrada: {ruta_imagen}")
        
        # Abrir y redimensionar imagen
        img = Image.open(ruta_imagen)
        print(f"✓ Dimensiones originales: {img.size}")
        
        img = img.resize((tamano, tamano), Image.Resampling.LANCZOS)
        print(f"✓ Redimensionada a: {img.size}")
        
        # Crear máscara circular
        mascara = Image.new('L', (tamano, tamano), 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0, tamano, tamano), fill=255)
        print("✓ Máscara circular creada")
        
        # Aplicar máscara
        img_circular = Image.new('RGBA', (tamano, tamano))
        img_circular.paste(img, (0, 0))
        img_circular.putalpha(mascara)
        print("✓ Máscara aplicada")
        
        # Convertir a PhotoImage
        photo = ImageTk.PhotoImage(img_circular)
        print("✓ Convertida a PhotoImage")
        
        return photo
    except Exception as e:
        print(f"❌ Error al cargar imagen: {e}")
        return None

# Crear ventana de prueba
print("\n" + "="*50)
print("PRUEBA DE IMAGEN CIRCULAR - LOGIN")
print("="*50 + "\n")

root = tk.Tk()
root.title("Prueba - Imagen Circular Login")
root.geometry("400x500")
root.configure(bg='#f0f0f0')

# Centrar ventana
root.update_idletasks()
width = 400
height = 500
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Frame principal
main_frame = tk.Frame(root, bg='#f0f0f0')
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Cargar imagen
ruta_imagen = os.path.join(os.path.dirname(__file__), "logo_login.png")
imagen_circular = crear_imagen_circular(ruta_imagen, 150)

if imagen_circular:
    print("\n✅ ÉXITO: La imagen se cargó correctamente\n")
    
    # Mostrar imagen
    label_imagen = tk.Label(
        main_frame,
        image=imagen_circular,
        bg='#f0f0f0',
        borderwidth=0
    )
    label_imagen.pack(pady=(0, 20))
    
    # Mantener referencia
    label_imagen.image = imagen_circular
else:
    print("\n❌ ERROR: No se pudo cargar la imagen\n")
    
    # Mostrar mensaje de error
    error_label = tk.Label(
        main_frame,
        text="❌ No se pudo cargar la imagen",
        font=("Arial", 12),
        bg='#f0f0f0',
        fg='red'
    )
    error_label.pack(pady=(0, 20))

# Título
titulo = tk.Label(
    main_frame, 
    text="🔐 SISTEMA DE LOGIN", 
    font=("Arial", 16, "bold"),
    bg='#f0f0f0',
    fg='#333333'
)
titulo.pack(pady=(0, 10))

# Subtítulo
subtitulo = tk.Label(
    main_frame,
    text="Cliente SOAP - Conversor de Unidades",
    font=("Arial", 10),
    bg='#f0f0f0',
    fg='#666666'
)
subtitulo.pack(pady=(0, 20))

# Mensaje de prueba
mensaje = tk.Label(
    main_frame,
    text="Esta es una vista previa del login\ncon la imagen circular",
    font=("Arial", 9),
    bg='#f0f0f0',
    fg='#999999',
    justify='center'
)
mensaje.pack(pady=20)

# Botón cerrar
btn_cerrar = tk.Button(
    main_frame,
    text="Cerrar Prueba",
    font=("Arial", 10, "bold"),
    bg='#2196F3',
    fg='white',
    cursor='hand2',
    relief=tk.FLAT,
    padx=20,
    pady=10,
    command=root.destroy
)
btn_cerrar.pack(pady=20)

print("="*50)
print("Mostrando ventana de prueba...")
print("Cierra la ventana cuando termines de verificar")
print("="*50 + "\n")

root.mainloop()
